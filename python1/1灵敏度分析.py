# %%
# ##############从此处开始   灵敏度分析
from SALib.analyze import sobol
from SALib.sample import saltelli
from SALib.test_functions import Ishigami
from SALib.util import read_param_file
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from pyKriging.krige import kriging
import pandas as pd
import pickle as pkl

#%%
problem = {
    'num_vars': 5,
    'names': ['A14', 'A23','Tup','Tmid','Tdown'],
    'bounds': [[0.09, 0.1],
               [0.09, 0.1],
               [0,150],
               [0,150],
               [0,150]]
}

inputs = saltelli.sample(problem, 10000,calc_second_order=False)

#%%       存矩阵为csv
#path=r"C:\Users\DL\Desktop\张拉整体梁温度不确定\DIM"
#np.savetxt(path+"\inputACT_T.csv",inputs,delimiter=',')

#np.savetxt("inputACT_T.csv",inputs,delimiter=',')

Act_T_1=(inputs[:,0:2]-0.05)/0.05
Act_T_2=inputs[:,2:5]/150

x_test=np.append(Act_T_1, Act_T_2, axis=1)





# %%a
with open(f'C:/Users/DL/Desktop/新出图/fig8/新的包含不收敛的训练/z_5to10_kriging.pkl','rb') as f:
    k_trained = pkl.load(f)

%time   k_pred = [k_trained.predict(x_) for x_ in x_test]

#np.savetxt(f"3D含不收敛z.csv",k_pred,delimiter=',')

z=np.array(k_pred)
Si_z = sobol.analyze(problem, z, calc_second_order=False, print_to_console=True)
print()
S1_z=Si_z['S1']
ST_z=Si_z['ST']




# %%a
with open(f'C:/Users/DL/Desktop/新出图/fig8/新的包含不收敛的训练/y_5to10_kriging.pkl','rb') as f:
    k_trained = pkl.load(f)

%time   k_pred = [k_trained.predict(x_) for x_ in x_test]

#np.savetxt(f"3D含不收敛z.csv",k_pred,delimiter=',')

z=np.array(k_pred)
Si_y = sobol.analyze(problem, z, calc_second_order=False, print_to_console=True)
print()
S1_y=Si_y['S1']
ST_y=Si_y['ST']













#%%
df1=pd.read_csv('dis_23.csv')

#算z灵敏度
zcol='23z'
z=df1[zcol].values

print(inputs.shape, z.shape[0])

#%%
Si_z = sobol.analyze(problem, z, calc_second_order=False, print_to_console=True)
print()
S1_z=Si_z['S1']
ST_z=Si_z['ST']








#算y灵敏度
#%%
ycol='23y'
y=df1[ycol].values

print(inputs.shape, y.shape[0])

#%%
Si_y = sobol.analyze(problem, y, calc_second_order=False, print_to_console=True)
print()
S1_y=Si_y['S1']
ST_y=Si_y['ST']









####### 此处开始   画灵敏度








#Z灵敏度
#%%
xedges = np.array([10,20,30,40,50,60])    #设置x轴取值
yedges = np.array([10,20,30])             #设置y轴取值

#设置X,Y对应点的值。即原始数据。
hist =np.array( [S1_z,ST_z]).T

#生成图表对象。
fig = plt.figure()
#生成子图对象，类型为3d
ax = fig.add_subplot(111,projection='3d')

#设置作图点的坐标
xpos, ypos = np.meshgrid(xedges[:-1]-2.5 , yedges[:-1]-2.5 )
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

#设置柱形图大小
dx =5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

#设置坐标轴标签
ax.set_xlabel('QOI')
ax.set_ylabel('S1ST')
ax.set_zlabel('sensitivity')

# x, y, z: array - like
# The coordinates of the anchor point of the bars.
# dx, dy, dz: scalar or array - like
# The width, depth, and height of the bars, respectively.
# minx = np.min(x)
# maxx = np.max(x + dx)
# miny = np.min(y)
# maxy = np.max(y + dy)
# minz = np.min(z)
# maxz = np.max(z + dz)
ax.bar3d(xpos, ypos, zpos, dx, dy, dz,color='b',zsort='average')
ax.set_zlim3d(0, 0.6)
plt.show()








#y灵敏度
#%%
xedges = np.array([10,20,30,40,50,60])    #设置x轴取值
yedges = np.array([10,20,30])             #设置y轴取值

#设置X,Y对应点的值。即原始数据。
hist =np.array( [S1_y,ST_y]).T

#生成图表对象。
fig = plt.figure()
#生成子图对象，类型为3d
ax = fig.add_subplot(111,projection='3d')

#设置作图点的坐标
xpos, ypos = np.meshgrid(xedges[:-1]-2.5 , yedges[:-1]-2.5 )
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

#设置柱形图大小
dx =5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

#设置坐标轴标签
ax.set_xlabel('QOI')
ax.set_ylabel('S1ST')
ax.set_zlabel('sensitivity')

# x, y, z: array - like
# The coordinates of the anchor point of the bars.
# dx, dy, dz: scalar or array - like
# The width, depth, and height of the bars, respectively.
# minx = np.min(x)
# maxx = np.max(x + dx)
# miny = np.min(y)
# maxy = np.max(y + dy)
# minz = np.min(z)
# maxz = np.max(z + dz)
ax.bar3d(xpos, ypos, zpos, dx, dy, dz,color='b',zsort='average')
ax.set_zlim3d(0, 0.6)
plt.show()

























# %%
#后面是sobol灵敏度分析例子




# %%
from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np

problem = {
  'num_vars': 3,
  'names': ['x1', 'x2', 'x3'],
  'bounds': [[-np.pi, np.pi]]*3
}

#%% Generate samples
param_values = saltelli.sample(problem, 1000)

#%% Run model (example)
Y = Ishigami.evaluate(param_values)

#%% Perform analysis
Si = sobol.analyze(problem, Y, print_to_console=True)
# Returns a dictionary with keys 'S1', 'S1_conf', 'ST', and 'ST_conf'
# (first and total-order indices with bootstrap confidence intervals)






