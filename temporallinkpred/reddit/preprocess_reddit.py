import pandas as pd
import torch
df = pd.read_csv("edges.csv", skiprows=1, header=None)
ef = torch.load('edge_features.pt')
# nf = torch.load('node_features.pt')
# ef = ef.to(torch.uint8)
# nf = nf.to(torch.uint8)
breakpoint()

df = df[[1, 2, 3]] 
ef_df = pd.DataFrame(ef.numpy())
merged_df = pd.concat([df.reset_index(drop=True), ef_df], axis=1)
merged_df.to_csv('reddit_edgelist.csv', index=False)
# nf_df = pd.DataFrame(nf.numpy())
# nf_df.to_csv('node_features.csv', index=False)
breakpoint()