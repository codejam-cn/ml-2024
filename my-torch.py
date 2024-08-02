import torch
import numpy as np

# 直接从data得到Tenser
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
# print(x_data)

# 从 numPy Array得到Tenser
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
# print(x_np)

# from another Tenser
# x_ones = torch.ones_like(x_data)
# print(x_ones)

# x_rand = torch.rand_like(x_data, dtype=torch.float)
# print(x_rand)

# fours = torch.ones(4, 4)
#
# print(fours)
# print(fours[0])
# print(fours[:, 0])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

tenser = torch.tensor(arr)
print(tenser)

t_tenser = tenser.T
print(t_tenser)

value = tenser @ t_tenser
print(value)

sum_value = value.sum()
print(sum_value)
