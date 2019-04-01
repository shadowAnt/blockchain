# coding: utf-8
'''
@author: TC
@file: zp.py
@time: 2019/3/31 23:38
'''

import numpy as np


batch_size=12 #数据集大小
num_feature=5 #特征值大小
x=np.random.randn(batch_size,num_feature)#随机生成自变量
y=np.random.randint(2,size=(batch_size,1))#随机生成因变量
w=np.random.randn(5,1)#随机生成权值

for index in range(4):#四批计算
    x_s=np.arange(15).reshape(3,5)
    x_s[0]=x[index*3+0]
    x_s[1] = x[index * 3 + 1]
    x_s[2] = x[index * 3 + 1]
    y_s=np.dot(x_s,w)#自变量与权值做卷积
    a_s=y_s-y[index*3:index*3+3]#卷积和与因变量值做差
    loss=np.mean(np.square(a_s))#损失函数
    print('loss_s_%d:'%index,loss)
    gradient_a_s = 2 * a_s  # 损失函数求导后取绝对值
    gradient_w_s = np.dot(x_s.T, gradient_a_s)  # 梯度下降
    print("gradient_a_s_%d="%index, gradient_a_s)
    print("gradient_w_s_%d="%index, gradient_w_s)
    print("gradient_a_s_%d.shape="%index, gradient_a_s.shape)
    print("gradient_w_s_%d.shape="%index, gradient_w_s.shape)


