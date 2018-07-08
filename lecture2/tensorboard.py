import tensorflow as tf

a = tf.constant(2,name = 'a')
b = tf.constant(4,name = 'b')

sum = tf.add(a,b,name='sum')


with tf.Session() as sess:
    writer  =tf.summary.FileWriter('./graph',sess.graph)
    print (sess.run(sum))


#close writer
writer.close()
