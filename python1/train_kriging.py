

#在使用kriging model前，输入数据需要分别进行归一化(normalization)。参考的公式为，
# x1_norm = (x1 - x1.min()) / (x1.max() - x1.min())

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

    ycol='23z'
    y=df[ycol].values
   
    return x, y 

#%%
#训练
path_train = './训练/训练数据集/' 
df_pred = pd.DataFrame()

train_pool = ['200','300','400','500','600','700','800']
#train_pool = ['200','300','400']

for data in train_pool:
    df_train = pd.read_csv(path_train+data+'训练dis.csv')
    # print(df_train.shape)
    x, y = normalization(df_train)
    #k = kriging(x[::40], y[::40])#隔40个取一个
    k = kriging(x, y)
    print(f'data={data}')
    %time   k.train()

    #df_pred[data] = [k.predict(xi) for xi in x_test]#简单的预测

    with open(f'./训练/循环训练结果/kriging_{data}.pkl','wb') as f:
        pkl.dump(k,f)
    del(k) 
df_pred.head()

#%%
#预测
#预测用数据
df_test = pd.read_csv(path_train+'700训练dis.csv')
x_test,y_test = normalization(df_test.sample(50))
df_pred['y_test']=y_test

with open('/home/kesci/work/models/kriging_700.pkl','rb') as f:
    k_trained = pkl.load(f)
%timeit y_pred = [k_trained.predict(xi) for xi in x_test]

#%%
from sklearn.metrics import r2_score
plt.figure()
for i, data in enumerate(train_pool):
    plt.subplot(2,4,1+i)
    x = df_pred['y_test']
    y = df_pred[data]
    plt.plot(x,y,'bd')
    plt.text(49,52,f'r2 = {r2_score(x,y)}',fontsize=10)
    plt.xlim([48,54])
    plt.ylim([48,54])
    plt.title(data)







# %%
