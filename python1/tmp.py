f#%%
import pandas as pd

#%%
df_dis = pd.read_csv('dis_23.csv')
# %%
# %%
df_strs = pd.read_csv('stress_cable.csv')
# %%
df_strs.head()
# %%
df_all = pd.concat([df_dis,df_strs],axis=1)
# %%
d