# encoding: utf-8
'''
@author: TC
@file: my.py
@time: 2019/3/21 14:00
'''
import numpy as np

# TODO 批量梯度下降
def batch_gradient(x, y):
    m = x.shape[0]
    x0 = np.ones((m, 1))
    input_data = np.hstack([x0, x_train])
    m, n = input_data.shape
    loop_max = 1000000
    epsilon = 1e-5
    np.random.seed(0)
    theta = np.random.randn(n, 1)
    alpha = 0.00001     # 学习率
    # 初始化误差，每个维度的theta都应该有一个误差，所以误差是一个6维。
    error = np.zeros((n, 1))  # 列向量
    diff = np.zeros((input_data.shape[1], 1))       # 偏导数
    count = 0
    while count < loop_max:
        count += 1
        sum_m = np.zeros((n, 1))
        for i in range(m):
            for j in range(n):
                # 计算每个维度的theta
                diff[j] = (input_data[i].dot(theta) - y_train[i]) * input_data[i, j]
            # 求每个维度的梯度的累加和
            sum_m = sum_m + diff
        # 利用这个累加和更新梯度
        theta = theta - alpha * sum_m
        if np.linalg.norm(theta - error) < epsilon:
            break
        else:
            error = theta
    print(theta.T[0])

#TODO 随机梯度下降
def random_gradient(x, y):
    m = x.shape[0]
    x0 = np.ones((m, 1))
    input_data = np.hstack([x0, x_train])
    m, n = input_data.shape
    #TODO 初始化阶段
    # 两个终止条件
    loop_max = 10000000
    epsilon = 1e-6
    # theta
    np.random.seed(0)
    theta = np.random.rand(n).T  # 随机生成n维1列的矩阵
    # 学习率
    alpha = 0.000001
    # 迭代误差
    error = np.zeros(n)
    # 初始化偏导数矩阵
    diff = np.zeros(n)
    # 循环次数
    count = 0
    # TODO 计算梯度
    while count < loop_max:
        count += 1
        for i in range(m):
            # 计算每个维度theta的梯度，并运用一个梯度去更新它
            diff = input_data[i].dot(theta) - y_train[i]
            theta = theta - alpha * diff * (input_data[i])
        if np.linalg.norm(theta - error) < epsilon:  # 判断theta与零向量的距离是否在阈值内，在一定范围内时停止迭代。
            break
        else:
            error = theta
    print(theta)

#TODO 小批量梯度下降
def minibatch_gradient(x, y):
    m = x.shape[0]
    x0 = np.ones((m, 1))
    input_data = np.hstack([x0, x_train])
    m, n = input_data.shape
    loop_max = 1000000
    epsilon = 1e-5
    alpha = 0.00001
    error = np.zeros((n, 1))  # 列向量
    diff = np.zeros((input_data.shape[1], 1))
    # 初始theta
    np.random.seed(0)  # 设置随机种子
    theta = np.random.randn(n, 1)  # 随机取一个1维列向量初始化theta
    count = 0
    # 设置小批量的样本数
    minibatch_size = 2
    while count < loop_max:
        count += 1
        sum_m = np.zeros((n, 1))
        for i in range(1, m, minibatch_size):
            for j in range(n):
                # 计算每个维度的theta
                diff[j] = (input_data[i].dot(theta) - y_train[i]) * input_data[i, j]
            sum_m = sum_m + diff
        theta = theta - alpha * (1.0 / minibatch_size) * sum_m
        if np.linalg.norm(theta - error) < epsilon:
            break
        else:
            error = theta
    print(theta.T[0])

#TODO 动量梯度下降
def mome_gradient(x, y):
    X_to = np.concatenate((y, x), axis=1)
    m = x.shape[0]
    x0 = np.ones((m, 1))
    input_data = np.hstack([x0, x_train])
    m, n = input_data.shape
    w = np.random.rand(n, 1)
    # 设置步数和学习速率
    step = 2000
    alpha = 0.01
    batch_size = 10
    before = np.zeros(n)
    gamma = 0.03
    for s in range(step):
        for j in range(n):
            #随机挑选随机梯度下降的i
            Batch=np.random.randint(0, len(x), (1, batch_size))
            for o in range(batch_size):
                #用动量梯度下降更新w
                w[j] = w[j] - alpha * gradient(w, y[Batch[0][o]], X_to[Batch[0][o]],j) - gamma * before[j]
                before[j] = gradient(w, y[Batch[0][o]], X_to[Batch[0][o]], j)
    print(w.T[0])

#梯度下降计算
def gradient(w, Y_i, X_i,j):
	#转置
	X_i = X_i.reshape(1, X_i.shape[0])
	part=np.matmul(X_i, w) - Y_i
	return part[0][0] * X_i[0][j]

#TODO 构造训练数据集
n = 6       #属性维度
m = 10      #样本容量
#随机生成训练数据x_train，(10 * 5)
x_train = np.random.rand(m, n-1)
y_train = np.random.randint(0, 2, (m, 1))
'''
构建一个num行1列的单位矩阵x0，然它和x_train组合，形成[x0, x1, x2, x3, x4, x5]，x0=1的数据形式，
可将y=t1*x1+t2*x2+t3*x3+t4*x4+t5*x5+b 写为 y=b*x0+t1*x1+t2*x2+t3*x3+t4*x4+t5*x5
即y=向量x_train乘向量theta，其中theta为[b, *, * , *, *, *]
'''

#TODO 测试阶段
batch_gradient(x_train, y_train)
random_gradient(x_train, y_train)
minibatch_gradient(x_train, y_train)
mome_gradient(x_train, y_train)