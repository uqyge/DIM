



######      如改上下限，归一化的数字要改！！！！！！





#%%
import numpy as np
from pyKriging.krige import kriging
import pandas as pd
import pickle as pkl

#%%
#path_matlab=r"C:\Users\DL\Desktop\张拉整体梁温度不确定\DIM"
#df1=pd.read_csv(path_matlab+'\dis_23.csv')
df1=pd.read_csv('dis_23.csv')

#%%
# 输入变量在传入前需要做归一化
# 测试数据在两个维度上上下限范围一致，所以直接计算。若不一致时需分维度计算

Acol=['A14','A23']
x11=(df1[Acol]-0.09)/0.01
Tcol=['Tup','Tmid','Tdown']
x12=df1[Tcol]/150
#公式     x1_norm = (x1 - x1.min()) / (x1.max() - x1.min()) 

x=pd.concat([x11, x12], axis=1).values

#%%
ycol='23z'
y=df1[ycol].values




#训练
#%%
%%time
k = kriging(x, y)
k.train()

with open('kriging_saved.pkl','wb') as f:
    pkl.dump(k,f) 







#%%
# 预测时同样需要做归一化处理









#%%
with open('kriging_saved.pkl','rb') as f:
    k_trained = pkl.load(f)

df_train = pd.read_csv('dis_23.csv')
input_Act_labels = ['A14','A23']
input_T_labels = ['Tup','Tmid','Tdown']
test_Act =  (df_train[input_Act_labels]-0.09)/0.01
test_T =  df_train[input_T_labels]/150

x_test=np.append(test_Act, test_T, axis=1)

#x_test = df_train[input_labels].values





#%%
%%time
k_pred = [k_trained.predict(x_) for x_ in x_test]







#误差
#%%
FEM_23z =  df_train['23z']

k_pred_mis=abs(k_pred-FEM_23z)

k_error=k_pred_mis/FEM_23z



mean_error=np.mean(k_error)

mean_error







