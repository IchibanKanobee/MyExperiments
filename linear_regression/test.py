from NN.Layer import Layer

layer = Layer("a", [100, 200])
print layer.name
print layer.shape

layer.set_data(5)
