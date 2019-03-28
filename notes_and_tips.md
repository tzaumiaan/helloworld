# Some notes and tips about Python, Tensorflow, PyTorch, and so on...

## Tensorflow
- What's embedding layer?
  - Turn the one-hot input to an attribute vector with far less dimension
  - Only as the first layer of a NN model
  - Ref: [Deep Learning #4: Why You Need to Start Using Embedding Layers](
    https://towardsdatascience.com/deep-learning-4-embedding-layers-f9a02d55ac12)
  - Ref: [LSTM里Embedding Layer的作用是什么？](
    https://www.zhihu.com/question/45027109)
- What are the definitions an differences of static graph and dynamic graph?
  - Static: Graph is defined before session running, and remains static during session runtime
  - Dynamic: Graph can be changed during session runtime
  - Tensorflow uses static graph, and Tensorflow Fold supports dynamic graph
  - PyTorch supports dynamic graph in nature
- How to save and load a pre-trained model? What if we only apply partial values to a graph?
  - `TODO`
- What's the difference between `tf.Variable()` and `tf.get_variable()`?
  - `TODO`
- What's the purpose of `tf.transpose()`?
  - If `x` is 2D, `tf.transpose(x)` is equivalent to `np.transpose(x, axes=[1,0])`
  - If `x` has higher dimension, `tf.transpose(x, perm=[0,2,1])` means `np.transpose(x, axes=[0,2,1)`
- Is it OK to use `if` in graph? If no, what's the proper way?
  - `TODO`

## Numpy
- What's the difference between `np.concatenate()` and `np.stack()`?
  - `np.concatenate((arr0, arr1, ...), axis={0/1/2/...})` concatenates arrays along desired dimension,
    and all arrays have to align with other dimensions
  - `np.stack()` expands the dims of all inputs (a bit like `np.expand_dims`), and then concatenates,
    so all inputs have to have exactly same shapes
  - Ref: [Stackoverflow](https://stackoverflow.com/questions/33356442/)

## Python
- What's truthiness in Python?
  - `is` checks if two items belong to the same object, while `==` checks the values
  - `1==1.0` is true, while `1 is 1.0` is false
  - `a = 'a'` and `b = 'a'`, `a==b` is true, but `a is b` is false
  - Ref: [Truthiness in Python](https://www.udacity.com/wiki/cs258/truthiness-in-python)