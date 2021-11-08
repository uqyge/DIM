#%%
from re import X
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# %%
# df_for = pd.read_csv('./python1/dis_23_new_forward.csv',dtype=float)
# df_for = pd.read_csv('./python1/dis_23_new_forward.csv')
# df_for = pd.read_csv('./python1/dis_test.csv',keep_default_na=False)
df_for = pd.read_hdf('./act4.hdf5')
# %%
df_for.describe()
#%%
df_for.info()
# %%
df_good=df_for[df_for['ijk']==1]
df_good = df_good.astype('float')
df_good.info()

#%%
df_good['obj']=df_good['23z']/df_good['23y']
df_good

# %%
plt.scatter(df_good['23x'],df_good['23y'])
plt.plot(range(-170,30),np.zeros(200),'r-')
# %%
px.scatter_3d(df_good,x='23x',y='23y',z='23z',color='A1')

#%%
# cond=df_good['23y']>40
# %%
# df_select = df_good[cond][['A1','A2','A3','A4']]
# np.savetxt("inputACT_select.csv",df_select.values,delimiter=',')

#%%


#%%
df_stress = pd.read_csv('python1/stress_cable_forward.csv')
# %%
df_db = pd.concat([df_for,df_stress],axis=1)
# %%
df_db.to_hdf('act4.hdf5',key='noT')
# %%
a = pd.read_hdf('act4.hdf5')
# %%
a.to_parquet('act4.parquet')


# %%

# %%
plt.scatter(a['23x'],a['23y'])
# %%
df_good[['23x','23y']]
# %%
px.scatter(df_good,x='23x',y='23y')
# %%
df_for.to_csv('act4.csv',sep=',',encoding='utf')
#%%
test = pd.read_csv('act4.csv',converters = {u'code':str})
# %%
px.scatter(test,'23x','23y')
# %%
a=test[test['ijk']==1]
# %%
a=a.astype('float')
# %%
px.scatter(a,x='23x',y='23')

#%%
from sklearn.cluster import DBSCAN,KMeans
# %%
y = DBSCAN(eps=7).fit_predict(df_good[['23x','23y','23z']])
# y = KMeans(n_clusters=3).fit_predict(df_good['dis'].values.reshape(-1,1))
df_good['id']=y
sum(y==-1)

# dis=np.sqrt(np.square(df_good['23x'])+np.square(df_good['23y'])+np.square(df_good['23z']))
# df_good['dis']=dis


# %%
px.scatter_3d(df_good,x='23x',y='23y',z='23z',color = 'dis')
# %%
px.scatter_3d(df_good[df_good['id']!=-1],x='23x',y='23y',z='23z',color = 'id')
# %%
px.scatter_3d(df_good[df_good['id']==0],x='23x',y='23y',z='23z',color = 'id')

#%%


#%%

