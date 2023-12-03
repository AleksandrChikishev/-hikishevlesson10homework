import pandas as pd

#Исходный код
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходный DataFrame:")
print(data.head())

# Преобразование в one-hot encoding без использования get_dummies
categories = pd.unique(data['whoAmI'])
one_hot = pd.DataFrame(0, columns=categories, index=data.index)
one_hot = one_hot.add(pd.get_dummies(data['whoAmI']))

# Объединение исходного DataFrame с one-hot encoding
data_one_hot = pd.concat([data, one_hot], axis=1)

print("\nDataFrame после преобразования в one-hot encoding:")
print(data_one_hot.head())
