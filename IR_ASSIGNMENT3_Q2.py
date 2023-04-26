#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

print("step 1")


# In[19]:


data = pd.read_csv("C:\\Users\\91783\\Desktop\\IR 2023\\assignment3\\practice folder\\soc-sign-bitcoinalpha.csv", header=None)
data.columns = ['source', 'target', 'rating', 'time']
print("step 2")


# In[25]:


list_edge = []
unique_sources = np.unique(data["source"])
list_edge = []

for source in unique_sources:
    tmp_df = data[data["source"] == source]
    tmp_edge_list = np.column_stack((tmp_df["source"], tmp_df["target"])).tolist()
    list_edge += tmp_edge_list
print("step 3")


# In[26]:


idx_list = {val: idx for idx, val in enumerate(np.unique(np.append(np.sort(data.source.unique()), np.sort(data.target.unique()))))}
                                               
adj_mat_dir = np.zeros((len(idx_list), len(idx_list)))
adj_mat_undir = np.zeros((len(idx_list), len(idx_list)))
print("step 4")


# In[27]:


for nodes in list_edge:
    adj_mat_dir[idx_list[nodes[0]], idx_list[nodes[1]]] = 1
    
    adj_mat_undir[idx_list[nodes[0]], idx_list[nodes[1]]] = 1
    adj_mat_undir[idx_list[nodes[1]], idx_list[nodes[0]]] = 1
print("step 5")


# In[28]:


G = nx.from_numpy_matrix(adj_mat_undir, create_using=nx.DiGraph)
page_rank = nx.pagerank(G)
hubs, authorities = nx.hits(G)
print("step 6")


# In[29]:


compare = pd.DataFrame({"Node": list(idx_list.keys()), "Node_id": list(idx_list.values()), "pageRank": list(page_rank.values()), "Hubs": list(hubs.values()), "Authorities": list(authorities.values())})
print(compare)
print("step 7")


# In[ ]:




