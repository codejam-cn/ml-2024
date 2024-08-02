# 下载数据集并使用
import torch
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

train_data = datasets.FashionMNIST(
    "./",
    train=True,
    download=True,
    transform=ToTensor()
)

# train_data = datasets.FashionMNIST(
#     "./",
#     train=False,
#     download=True,
#     transform=ToTensor()
# )

print(train_data.__sizeof__())

figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(train_data), size=(1,)).item()
    img, label = train_data[sample_idx]
    plt.title(label)
    plt.imshow(img.squeeze())
    plt.show()
