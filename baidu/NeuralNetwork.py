import numpy as np


class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # 初始化权重
        self.i_nodes = input_nodes
        self.h_nodes = hidden_nodes
        self.o_nodes = output_nodes

        self.wih = np.random.normal(0.0, pow(self.h_nodes, -0.5), (self.h_nodes, self.i_nodes))
        self.who = np.random.normal(0.0, pow(self.o_nodes, -0.5), (self.o_nodes, self.h_nodes))

        self.lr = learning_rate  # 学习率
        self.activation_function = lambda x: 1 / (1 + np.exp(-x))  # 激活函数为sigmoid函数
        self.activation_function_derivative = lambda x: x * (1 - x)

    def train(self, inputs_list, targets_list):
        # 转换为数组
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        # 计算输入层到隐藏层的输出
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        # 计算隐藏层到输出层的输出
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        # 反向传播错误
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)

        # 更新权重
        self.who += self.lr * np.dot((output_errors * self.activation_function_derivative(final_outputs)),
                                     np.transpose(hidden_outputs))
        self.wih += self.lr * np.dot((hidden_errors * self.activation_function_derivative(hidden_outputs)),
                                     np.transpose(inputs))

    def query(self, input_list):
        # 转换为数组
        inputs = np.array(input_list, ndmin=2).T

        # 计算隐藏层的输出
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        # 计算输出层的输出
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


# 示例使用
input_nodes = 784  # MNIST数据集的输入节点数
hidden_nodes = 200  # 隐藏层节点数
output_nodes = 10  # 输出层节点数(对应于数字0-9)
learning_rate = 0.1

# 创建神经网络实例
nn = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# 假设这是从MNIST数据集中获得的一个训练样本
# 输入是一个0-9的图像的像素值，目标是对应的数字
# 输入是一个784维的数组，目标是一个10维的数组，代表每个数字的可能性
inputs = [1.0, 0.5, ..., 0.9]  # 示例输入
targets = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]  # 示例目标输出，代表数字7

# 训