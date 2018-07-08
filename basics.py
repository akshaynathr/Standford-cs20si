#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 20:58:52 2017

@author: akshaynathr
"""

 import tensorflow as tf
 
 #constants
 # tf.constant(value, dtype=None, shape=None, name='Any name' , verify_shape = False)
 
 oneD_tensor = tf.constant([2,2], name ="vector")
 
 twoXtwo_tensor = tf.constant([[0,1],[2,2],[3,3]] , name = "twoByTwo_tensor")
 
 #zeros
 
 zero_matrix = tf.zeros([2,3], tf.int32) #==> [[0,0],[0,0],[0,0]]
 
 #input is not shape, but an actual matrix
 zero_matrix2 = tf.zeros_like([[0,1],[2,3],[3,3]]) #==> [[0,0],[0,0],[0,0]]
 
 #ones
 
 one_matrix = tf.ones([2,3], tf.int32) # ==> [[1,1],[1,1],[1,1]]
 
 one_matrix2 = tf.ones_like([[0,1],[2,3],[3,3]]) # ==> [[1,1],[1,1],[1,1]]
 
 # fills the input shape with given scalar
 fill_shape=tf.fill([2,3],8) # ==> [[8,8],[8,8],[8,8]]
 
 
 #create sequences
 ## create a sequence of num  evenly-spaced values are generated beginning at start . If num ​ 1, the values in the sequence increase by stop - start / num - 1, so that the last one is exactly stop

 tf.linspace(1,10,1,name='linespace',dtype='int')
 
 #create a range 
 
 tf.range(1,10,2) #=> [1,3,5,7,9]
 
 #limit =5
 tf.range(limit) #> [0,1,2,3,4,5]
 
 #Note : tensorflow sequences are not iterable
 #for _ in tf.range(5):  ==> error
 
 