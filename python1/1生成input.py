



######      如改上下限，cell 3 的数字要改！！！！！！





# %%
import sobol_seq
import numpy as np
import pandas as pd

# %%
Act=sobol_seq.i4_sobol_generate(2, 100,skip=0)
Temp=sobol_seq.i4_sobol_generate(1, 125)

Act_T=sobol_seq.i4_sobol_generate(5, 1000,skip=0)

Act_4=sobol_seq.i4_sobol_generate(4, 100_000,skip=0)
# Act_4=sobol_seq.i4_sobol_generate(4, 50,skip=0)
# %%
Act=0.01*Act+0.09
Temp=150*Temp

Act_T_1=0.05*Act_T[:,0:2]+0.05
Act_T_2=150*Act_T[:,2:5]

Act_T=np.append(Act_T_1, Act_T_2, axis=1)

Act_4 = 0.05+0.25*Act_4
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
np.savetxt("inputACT_4.csv",Act_4,delimiter=',')
#%%














#%%
#plt.rcParams['lines.linewidth'] = 2
#plt.rcParams['lines.linestyle'] = '--'
#plt.rcParams['figure.figsize'] = (12.0, 8.0) # 单位是inches
#plt.plot(x,y,color='r',label='exp1')
#plt.legend()