from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape, len(train_labels), train_labels)
print(test_images.shape,  len(test_labels),  test_labels) 
