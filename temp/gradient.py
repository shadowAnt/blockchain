# -*- coding: UTF-8 -*-
import numpy as np
import random

#梯度下降计算
def gradient(w,Y_i,X_i,j):
	#转置
	X_i=X_i.reshape(1,X_i.shape[0])
	# 注意np array must use dot or matmul,not *
	part=np.matmul(X_i,w)-Y_i

	return part[0][0]*X_i[0][j]

#随机梯度下降
def random_gradient(X_st,Y_st,X_to,w):
	#设置步数和学习速率
	step=2000
	alpha=0.01
	print("begin random_gradient")

	for s in range(step):
		for j in range(len(w)):
			#随机挑选随机梯度下降的i
			temp_random=random.randint(0,len(X_st)-1)
			#更新w
			w[j]=w[j]-alpha*gradient(w,Y_st[temp_random],X_to[temp_random],j)
		#打印loss
		if s % 100==0:
			print("random_gradient loss function:")
			print(np.sum(np.square(np.matmul(X_to,w)-Y_st)))

#全量梯度下降
def all_gradient(X_st,Y_st,X_to,w):
	#设置步数和学习速率
	step=2000
	alpha=0.01
	print("begin all_gradient")

	for s in range(step):
		for j in range(len(w)):
			#随机挑选随机梯度下降的i
			for k in range(len(X_st)):
				#更新w
				w[j] = w[j] - alpha * gradient(w, Y_st[k], X_to[k], j)
		#打印loss
		if s % 100==0:
			print("all_gradient loss function:")
			print(np.sum(np.square(np.matmul(X_to, w) - Y_st)))

#批量梯度
def batch_gradient(X_st,Y_st,X_to,w):
	#设置步数和学习速率
	step = 2000
	alpha = 0.01
	batch_size = 10
	
	print("begin batch_gradient")

	for s in range(step):
		for j in range(len(w)):
			#随机挑选随机梯度下降的i
			Batch=np.random.randint(0, len(X_st), (1, batch_size))
			for o in range(batch_size):
				#更新w
				w[j]=w[j]-alpha*gradient(w, Y_st[Batch[0][o]], X_to[Batch[0][o]], j)
		#打印loss
		if s % 100==0:
			print("batch_gradient loss function:")
			print(np.sum(np.square(np.matmul(X_to,w)-Y_st)))
#动量梯度
def mome_gradient(X_st,Y_st,X_to,w):
	#设置步数和学习速率
	step = 2000
	alpha = 0.01
	batch_size = 10
	before = np.zeros(len(w))
	gamma = 0.03
	print("begin mome_gradient")
	for s in range(step):
		for j in range(len(w)):
			#随机挑选随机梯度下降的i
			Batch=np.random.randint(0,len(X_st),(1,batch_size))
			for o in range(batch_size):
				#更新w,用动量梯度下降
				w[j]=w[j]-alpha*gradient(w,Y_st[Batch[0][o]],X_to[Batch[0][o]],j)-gamma*before[j]
				before[j]=gradient(w,Y_st[Batch[0][o]],X_to[Batch[0][o]],j)
		#打印loss
		if s % 100==0:
			print("mome_gradient loss function:")
			print(np.sum(np.square(np.matmul(X_to,w)-Y_st)))

#初始化实验数据部分
#dim为维度，num为数据个数
dim=6
num=10

#随机生成数据X_st和标签Y_st
X_st = np.random.rand(num, dim-1)
Y_st = np.random.randint(0, 2, (num, 1))
print(X_st)
print(Y_st)
#连接X_st和Y_st
X_to=np.concatenate((Y_st,X_st), axis=1)

w=np.random.rand(dim,1)
#测试
# random_gradient(X_st,Y_st,X_to,w)
# all_gradient(X_st,Y_st,X_to,w)
# batch_gradient(X_st,Y_st,X_to,w)
# mome_gradient(X_st,Y_st,X_to,w)

#print(w.shape)
#print(X_to.shape)
#print(X_to*w)