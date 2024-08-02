# 使用dataSet
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

train_data = datasets.FashionMNIST(
    "./",
    train=True,
    download=True,
    transform=ToTensor()
)

train_dataloader = DataLoader(train_data, batch_size=64, shuffle=True)

# 遍历 数据
for x, y in train_dataloader:
    # Shape of X[N, C, H, W]: torch.Size([64, 1, 28, 28])
    print(x.shape)
    # Shape of y: torch.Size([64]) torch.int64
    print(y.dtype)
