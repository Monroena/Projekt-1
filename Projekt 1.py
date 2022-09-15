# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:35:34 2022

@author: Bruger
"""

# exercise 1.5.1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris csv data using the Pandas library
filename = 'C:/Users/Bruger/OneDrive - Danmarks Tekniske Universitet/Skrivebord/SAheart.data'
messy_data = pd.read_csv(filename, sep=',', header=0)

attributeNames = np.asarray(messy_data.columns)

#We remove row.names, as we already have an index to sort our data
del messy_data["row.names"]


#We replace Present with 1 and Absent to 0. We do this because we´re not interested in
# the datatype string
messy_data=messy_data.replace("Present",1)
messy_data=messy_data.replace("Absent",0)


data = np.array(messy_data, dtype=np.float64)

#X_c = data[:, :-1].copy()
#y_c = data[:, -1].copy()

summary=messy_data.describe()