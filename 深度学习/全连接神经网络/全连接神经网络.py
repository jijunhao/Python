import os
from keras.datasets import mnist
# 导入数据集合
(train_images, train_labels), (test_images, test_labels) = mnist.load_data((os.getcwd())+'/mnist.npz')

# 查看训练数据集内容
print(train_images.shape)
print(len(train_labels))
print(train_labels)

# 查看测试数据集内容
print(test_images.shape)
print(len(test_labels))
print(test_labels)

# 数据预处理-区间缩放
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# 数据预处理-One-Hot编码
from keras.utils import to_categorical
print(train_labels[:5])
train_labels = to_categorical(train_labels)
print(train_labels[:5])

print("--------------")

print(test_labels[:5])
test_labels = to_categorical(test_labels)
print(test_labels[:5])

# 全连接神经网络
from tensorflow.keras import models
from tensorflow.keras import layers
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(256, activation='relu'))
network.add(layers.Dense(10, activation='softmax'))

# 网络结构
network.summary()

# 指定损失函数、优化器、监控指标
network.compile(optimizer='rmsprop', loss='categorical_crossentropy',metrics=['accuracy'])

# 划分验证集
x_val = train_images[:10000]
partial_x_train = train_images[10000:]
y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]

# 设置检查点，以验证集上的损失值为标准保存当前最优参数模型
from tensorflow.keras.callbacks import ModelCheckpoint
checkpointer = ModelCheckpoint(filepath='MNIST.ValLoss.ModelAndWeights.hdf5', monitor='val_loss',
                               verbose=1, save_best_only=True, save_weights_only=False)

# 训练模型
history = network.fit(partial_x_train, partial_y_train, epochs=15,
                      batch_size=128,validation_data=(x_val, y_val),callbacks=[checkpointer])

# 查看测试集上的精度
test_loss, test_acc = network.evaluate(test_images, test_labels,verbose=0)
print('test_acc:', test_acc)

# 查看训练过程中记录的维度信息
history_dict = history.history
print(history_dict.keys())

# 绘制损失值在训练集和测试集上的结果
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Arial Unicode MS']  #显示中文

history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
epochs = range(1, len(loss_values) + 1)
plt.figure(dpi=120)

plt.plot(epochs, loss_values, 'b', label='Training loss',color='r')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss',color='g')
plt.title('train_loss and val_loss')

plt.xticks([x for x in range(1,16)],fontsize=8)
plt.xlabel('number of train')

plt.ylabel('loss value')
plt.grid()
plt.legend()
plt.show()


# 绘制精度值在训练集和测试集上的结果
plt.clf() #清空图像
acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.figure(dpi=120)

plt.plot(epochs, acc,  'b', label='Training loss',color='r')
plt.plot(epochs, val_acc, 'b', label='Validation loss',color='g')
plt.title('train acc and val acc')

plt.xticks([x for x in range(1,16)],fontsize=8)
plt.xlabel('train of number')
plt.ylabel('acc')
plt.grid()
plt.legend()
plt.show()