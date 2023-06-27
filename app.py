import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Data_csv = pd.read_csv("data/train.csv")
Data_tf = tf.constant(Data_csv.values,dtype=float)
x_Data_raw= Data_tf[: ,3:-1]
y_Data_raw = Data_tf[: ,-1]
y_Data = tf.expand_dims(y_Data_raw, 0)
# paramenters for dividing up the dataset
train_r= 0.8
val_r = 0.1
test_r =0.1
dataset_size = len(x_Data_raw)

# actually divising the dataset
X_train = x_Data_raw 


print(y_Data_raw[5])
