# -*- coding: utf-8 -*-
import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

# Load the MNIST dataset 加载MNIST数据集 手写体数字的图片数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape the data 重塑数据 数据预处理

# x_train.shape[0] 是样本数量 28是图片的长 28是图片的宽 1是图片的通道数
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# 输入的shape
input_shape = (28, 28, 1)

num_classes = 10

# Normalize the data 标准化数据 教材叫做归一化
x_train = x_train.astype("float32")  # 转换为32位浮点数 提高计算精度
x_test = x_test.astype("float32")
x_train /= 255  # 缩放到0-1之间
x_test /= 255

# Convert class vectors to binary class matrices   标签转换为独热编码
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# Create the model 创建简单的CNN模型
model = Sequential()
# Add the layers to the model 添加层到模型 使用relu激活函数
model.add(Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=input_shape))
# Add the pooling layer 添加池化层 使用最大池化
model.add(MaxPooling2D(pool_size=(2, 2)))
# Add the dropout layer 添加dropout层 防止过拟合
model.add(Dropout(0.25))
# Add the flatten layer 添加flatten层 将多维数据转换为一维数据 展平
model.add(Flatten())
# Add the dense layer 添加全连接层 使用relu激活函数
model.add(Dense(128, activation="relu"))
# Add the dropout layer 添加dropout层 防止过拟合
model.add(Dropout(0.5))
# Add the output layer 添加输出层 使用softmax激活函数
model.add(Dense(10, activation="softmax"))

# Compile the model 编译模型 使用Adadelta优化器
model.compile(
    loss=keras.losses.categorical_crossentropy,
    optimizer=keras.optimizers.Adadelta(),
    metrics=["accuracy"],
)

# Train the model 训练模型
model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=12,
    verbose=1,
    validation_data=(x_test, y_test),
)

# Evaluate the model 评估模型
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

# 测试模型
test_image = x_test[0]
plt.imshow(test_image.reshape(28, 28), cmap="gray")
plt.show()

# 1次处理一张图片 高度宽度为 28  通道数为 1
test_image = test_image.reshape(1, 28, 28, 1)
pred = model.predict(test_image)

# 获取pred数组中最大值的索引
print("Predicted digit:", np.argmax(pred))
