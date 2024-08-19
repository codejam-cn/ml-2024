import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    # 定义Net的初始化函数，这个函数定义了该神经网络的基本结构
    def __init__(self):
        super(Net, self).__init__()  # 对继承自父类的属性进行初始化 复制并使用Net的父类的初始化方法，即先运行nn.Module的初始化函数
        self.conv1 = nn.Conv2d(1, 6, 3)  # 输入1 输出6 卷积核是3*3 表示提取6个特征，得到6个feature map
        self.conv2 = nn.Conv2d(6, 16, 3)  # 输入6输出16
        # 全连接层定义了三层线性转换，16*6*6就是把这16个二维数组拍扁了后一维向量的size
        self.fc1 = nn.Linear(16 * 6 * 6, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
        # Linear有三个参数，分别是输入特征数，输出特征数以及是否使用偏置（默认为True）。
        # 默认情况下Linear会自动生成权重参数和偏置，所以在模型中不需要单独定义权重参数，
        # 并且Linear提供比原先自定义权重参数时使用的randn随机正太分布更好的参数初始化方法

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))  # 将x放入卷积层中 用激活函数relu激活  在2*2池化窗口进行最大池化
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)  # 经历第二个卷积层
        x = x.view(-1,
                   self.num_flat_features(x))  # 通过这个view()函数我们把二维数据变成了一维向量。 Convolution Layer和Fully Connected Layer的对接
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    ##使用num_flat_features函数计算张量x的总特征量
    def num_flat_features(self, x):
        size = x.size[1:]
        num_features = 1
        for s in size:
            num_features *= s  # 累乘
        return num_features


net = Net()
