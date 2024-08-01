import torch
import numpy as np

# 直接从data得到Tenser
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
#print(x_data)

# 从 numPy Array得到Tenser
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
#print(x_np)

# from another Tenser
x_ones = torch.ones_like(x_data)
print(x_ones)

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(x_rand)
