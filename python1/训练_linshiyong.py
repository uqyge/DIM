
# %%
import sobol_seq
import numpy as np
import pandas as pd

# %%
Act=sobol_seq.i4_sobol_generate(2, 100)
Temp=sobol_seq.i4_sobol_generate(1, 125)

Act_T=sobol_seq.i4_sobol_generate(5, 400,skip=1000)

# %%
Act=0.01*Act+0.09
Temp=150*Temp

Act_T_1=0.01*Act_T[:,0:2]+0.07
Act_T_2=150*Act_T[:,2:5]

Act_T=np.append(Act_T_1, Act_T_2, axis=1)

# %%
#           plot FIG.3
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 5.0) # 单位是inches

plt.scatter(Act[:,0],Act[:,1])
#plt.savefig("C:/Users/DL/Desktop/出图/fig1/1.png",dpi=500,bbox_inches = 'tight')#解决图片不清晰，不完整的问题
#%%       存矩阵为csv
#path=r"C:\Users\DL\Desktop\张拉整体梁温度不确定\DIM"
#np.savetxt(path+"\inputACT.csv",Act,delimiter=',')
#np.savetxt(path+"\inputT.csv",Temp,delimiter=',')
#np.savetxt(path+"\inputACT_T.csv",Act_T,delimiter=',')
np.savetxt("inputACT.csv",Act,delimiter=',')
np.savetxt("inputT.csv",Temp,delimiter=',')
np.savetxt("inputACT_T.csv",Act_T,delimiter=',')





























#后面训练7-10的y z



#%%
import matplotlib.pyplot as plt
from pyKriging.krige import kriging
import pandas as pd
import pickle as pkl
import timeit

#%%
def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    return x



#训练
path_train = 'C:/Users/DL/Desktop/训练/200/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x = normalization(df_train)


def normalization(df):
    ycol='31'
    y=df[ycol].values
   
    return y 

df_train = pd.read_csv(path_train+'stress_cable.csv')
# print(df_train.shape)
y = normalization(df_train)


#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/200/200_stress_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 






def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    return x



#训练
path_train = 'C:/Users/DL/Desktop/训练/300/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x = normalization(df_train)


def normalization(df):
    ycol='31'
    y=df[ycol].values
   
    return y 

df_train = pd.read_csv(path_train+'stress_cable.csv')
# print(df_train.shape)
y = normalization(df_train)


#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/300/300_stress_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 






def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    return x



#训练
path_train = 'C:/Users/DL/Desktop/训练/400/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x = normalization(df_train)


def normalization(df):
    ycol='31'
    y=df[ycol].values
   
    return y 

df_train = pd.read_csv(path_train+'stress_cable.csv')
# print(df_train.shape)
y = normalization(df_train)


#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/400/400_stress_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 






def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    return x



#训练
path_train = 'C:/Users/DL/Desktop/训练/500/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x = normalization(df_train)


def normalization(df):
    ycol='31'
    y=df[ycol].values
   
    return y 

df_train = pd.read_csv(path_train+'stress_cable.csv')
# print(df_train.shape)
y = normalization(df_train)


#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/500/500_stress_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 






def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    return x



#训练
path_train = 'C:/Users/DL/Desktop/训练/600/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x = normalization(df_train)


def normalization(df):
    ycol='31'
    y=df[ycol].values
   
    return y 

df_train = pd.read_csv(path_train+'stress_cable.csv')
# print(df_train.shape)
y = normalization(df_train)


#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/600/600_stress_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 






def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    return x



#训练
path_train = 'C:/Users/DL/Desktop/训练/700/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x = normalization(df_train)


def normalization(df):
    ycol='31'
    y=df[ycol].values
   
    return y 

df_train = pd.read_csv(path_train+'stress_cable.csv')
# print(df_train.shape)
y = normalization(df_train)


#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/700/700_stress_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 






def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    return x



#训练
path_train = 'C:/Users/DL/Desktop/训练/800/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x = normalization(df_train)


def normalization(df):
    ycol='31'
    y=df[ycol].values
   
    return y 

df_train = pd.read_csv(path_train+'stress_cable.csv')
# print(df_train.shape)
y = normalization(df_train)


#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/800/800_stress_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 



































def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    ycol='23y'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/训练/200/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/200/200_y_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 










def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    ycol='23y'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/训练/300/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/300/300_y_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 











def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    ycol='23y'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/训练/400/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/400/400_y_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 





def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    ycol='23y'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/训练/500/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/500/500_y_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 





def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    ycol='23y'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/训练/600/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/600/600_y_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 






def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    ycol='23y'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/训练/700/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/700/700_y_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 











def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.09)/0.01
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    ycol='23y'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/训练/800/' 
df_pred = pd.DataFrame()

df_train = pd.read_csv(path_train+'dis_23.csv')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/训练/800/800_y_9to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 









#%%

def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.05)/0.05
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/100
    x=pd.concat([x11, x12], axis=1).values

    ycol='23z'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = './结果/0123/5-10/包含不收敛的点/' 
df_pred = pd.DataFrame()

df_train = pd.read_excel(path_train+'FEM_5-10_0-100_2000(收敛1000)包含不收敛的点.xlsx')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'./结果/0123/5-10/包含不收敛的点/z_5to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 













#%%
import matplotlib.pyplot as plt
from pyKriging.krige import kriging
import pandas as pd
import pickle as pkl
import timeit

# %%
def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.05)/0.05
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/150
    x=pd.concat([x11, x12], axis=1).values

    ycol='23z'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/DIM/python1/0326_1000/' 
df_pred = pd.DataFrame()

df_train = pd.read_excel(path_train+'dis_stress_5-10_150_1000.xlsx')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/DIM/python1/0326_1000/z_5to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k) 













#%%



def normalization(df):
    Acol=['A14','A23']
    x11=(df[Acol]-0.05)/0.05
    Tcol=['Tup','Tmid','Tdown']
    x12=df[Tcol]/100
    x=pd.concat([x11, x12], axis=1).values

    ycol='23y'
    y=df[ycol].values
   
    return x, y 


#训练
path_train = 'C:/Users/DL/Desktop/DIM/python1/0326_1000/' 
df_pred = pd.DataFrame()

df_train = pd.read_excel(path_train+'dis_stress_5-10_150_1000.xlsx')
# print(df_train.shape)
x, y = normalization(df_train)

#k = kriging(x[::40], y[::40])#隔40个取一个
k = kriging(x, y)

%time   k.train()

#df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

with open(f'C:/Users/DL/Desktop/DIM/python1/0326_1000/y_5to10_kriging.pkl','wb') as f:
        pkl.dump(k,f)
del(k)

# %%
