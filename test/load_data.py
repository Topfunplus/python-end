from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("x_train", x_train.shape)  # x_train (60000, 28, 28)  60000个样本 28*28的图片
print("y_train", y_train)


def reshape_data(x_train, x_test):
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    return x_train, x_test


(shaped_x, shaped_test_x) = reshape_data(x_test=x_test, x_train=x_train)
print("shaped_x", shaped_x)  # shaped_x (10000, 28, 28, 1) 10000个样本 28*28的图片
