#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


df_anime=pd.read_csv('anime.csv')
df_rate=pd.read_csv('rating.csv')


# In[20]:


# Drop unkonw eposides
df_anime = df_anime[df_anime.episodes != 'Unknown']
df_anime = df_anime[~df_anime.rating.isna()]


# In[24]:


df_anime.episodes = df_anime.episodes.astype(int)


# In[25]:


df_anime.info()


# In[26]:


df_anime.head()


# In[27]:


print(df_anime.shape)


# ## Horizontal bar cahrt
# https://seaborn.pydata.org/generated/seaborn.countplot.html

# In[28]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")


# In[29]:


values = df_anime.type.value_counts()
values['TV']


# In[37]:



import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

values = df_anime.type.value_counts()

plt.figure(figsize=(16, 6))
ax = sns.countplot(y='type', data=df_anime, palette="muted")
ax.set(ylabel='Anime Types', xlabel='Number of animes')

for index, item in enumerate(ax.get_yticklabels()):
    ax.text(
        values[item.get_text()], 
        index, 
        values[item.get_text()], 
        color='black', 
        weight='light'
    )
    
ax.get_figure().savefig('./charts/anime_type_count.png')
plt.show()


# In[31]:


# Percentage of TV animes 
round(values['Movie']/sum(values.values), 2) * 100


# In[32]:


sns.set(style="whitegrid")

plt.figure(figsize=(16, 6))
ax = sns.boxplot(x="type", y="rating", data=df_anime, palette="Set3")
ax.set(ylabel='Anime Rating', xlabel='Type of animes')
ax.get_figure().savefig('./charts/boxplot_of_types_vs_rating.png')
plt.show()


# In[33]:


sns.set(style="whitegrid")

plt.figure(figsize=(16, 6))
ax = sns.violinplot(x="type", y="rating", data=df_anime, palette="Set3")
ax.set(ylabel='Anime Rating', xlabel='Type of animes')
ax.get_figure().savefig('./charts/violinplot_of_types_vs_rating.png')
plt.show()


# In[42]:


sns.set(style="whitegrid")

plt.figure(figsize=(16, 6))
ax = sns.jointplot(y="members", x="rating", data=df_anime, color='g', kind='reg')
ax.savefig('./charts/joinplot_members_vs_rating.png')
plt.show()


# In[43]:


sns.set(style="whitegrid")

plt.figure(figsize=(16, 6))
ax = sns.jointplot(x="rating", y="episodes", data=df_anime, kind='reg')
ax.savefig('./charts/joinplot_episodes_vs_rating.png')
plt.show()


# In[13]:





# In[14]:


df_anime


# In[45]:


df_anime[(df_anime.type == 'TV') & (df_anime.members > 1000)].sort_values(by=['rating'], ascending=False).head(10)


# In[47]:


list(df_anime[df_anime.name == 'Fullmetal Alchemist: Brotherhood']['genre'])


# Get dataframe info for the animes.

# In[4]:


df_anime.info()


# In[5]:


df_anime.isna().any()


# In[6]:


# Remove anime with unknow score
df_anime = df_anime[df_anime.episodes != 'Unknown']
df_anime.episodes = df_anime.episodes.astype(int)


# In[7]:


df_anime.describe()


# # Box plot for rating and members

# In[22]:


df_anime.head()


# In[ ]:


df.columns = df.columns.to_series().str.join('_')


# In[30]:


df_anime.pivot_table(
    values=['episodes','rating','members'], 
    index=['type'],
    aggfunc = {
        'episodes' : [max, min, np.mean],
        'rating' : [max, min, np.mean],
        'members' : [max, min, np.mean]
    }
)


# In[8]:


box_df = df_anime[['rating','members','episodes']]


# In[9]:


box_df.boxplot(column=['rating'])


# In[12]:


box_df['rating'].hist(bins=50)


# In[13]:


box_df.boxplot(column=['members'])


# In[15]:


box_df['members'].hist(bins=100)


# In[18]:


box_df['members'].quantile([.05, .25, .5, .75])


# In[19]:


box_df.boxplot(column=['episodes'])


# In[20]:


box_df['episodes'].hist(bins=50)


# In[21]:


box_df['episodes'].quantile([.05, .1,.25, .5, .75])


# In[ ]:




