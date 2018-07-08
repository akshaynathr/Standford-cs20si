import tensorflow as tf

#constants
# tf.constant(value, dtype=None, shape=None, name='Any name' , verify_shape = False)

oneD_tensor = tf.constant([2,2], name ="vector")

twoXtwo_tensor = tf.constant([[0,1],[2,2],[3,3]] , name = "2x2 tensor")

#zeros

zero_matrix = tf.zeros([2,3], tf.int32) #==> [[0,0],[0,0],[0,0]]

#input is not shape, but an actual matrix
zero_matrix2 = tf.zeros([[0,1],[2,3],[3,3]]) #==> [[0,0],[0,0],[0,0]]

#ones

one_matrix = tf.ones([2,3], tf.int32) # ==> [[1,1],[1,1],[1,1]]
one_matrix2 = tf.ones([[0,1],[2,3],[3,3]]) # ==> [[1,1],[1,1],[1,1]]


