#%%
import numpy
import pandas as pd
import matplotlib.pyplot as plt

# %%
#path=r"C:\Users\DL\Desktop\张拉整体梁温度不确定\DIM"
#df=pd.read_csv(path+'\dis_23.csv')
df=pd.read_csv('dis_23.csv')

df.describe()

plt.rcParams['figure.figsize'] = (18.0, 6.0) # 单位是inches








#温度对nod23挠度Z的影响
#%%
df.boxplot(column = '23z', by = ['A14','A23'])
plt.ylim([45, 55])#只调y轴
plt.show()

#%%
grouped = df.groupby(["A14", "A23"])
df2 = pd.DataFrame({col:vals['23z'] for col,vals in grouped})
meds = df2.median()
meds.sort_values(ascending=True,inplace=True)
df2 = df2[meds.index]
df2.boxplot()

# plt.xticks([''])
plt.ylim([45, 55])#只调y轴
plt.show()








#温度对nod23偏移Y的影响
#%%
df.boxplot(column = '23y', by = ['A14','A23'])
plt.ylim([45, 55])#只调y轴
plt.show()

#%%
grouped = df.groupby(["A14", "A23"])
df4 = pd.DataFrame({col:vals['23y'] for col,vals in grouped})
meds = df4.median()
meds.sort_values(ascending=True,inplace=True)
df4 = df4[meds.index]
df4.boxplot()

# plt.xticks([''])
plt.ylim([-35, -25])#只调y轴
plt.show()





#plt.axis([-5, 5, 0, 80])#调整四个值
#plt.xlim([-5, 5])#只调x轴
#plt.ylim([0, 80])#只调y轴
#plt.xlim(left=-5)#只调整x轴左侧
# %%
