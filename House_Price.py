import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Housing.csv")
print(data.head())
print(data.info())
print(data.describe())
data_encoded = pd.get_dummies(data, drop_first=True)
data_encoded=data_encoded.astype(int)
print(data_encoded.head())
X = data_encoded.drop("price",axis=1)
y = data_encoded["price"]

x_train,x_test,y_train,y_test = train_test_split(X,  y, test_size =0.2, random_state = 42)
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print("r2_score" , r2_score(y_test,y_pred))
y_test_reset = y_test.reset_index(drop=True)
for i in range(109):
    print(f"{y_test_reset[i]} - - {y_pred[i]}")

residuals=y_test_reset-y_pred
plt.figure()
plt.scatter(range(len(y_test_reset)),y_test_reset,color ='red',marker='x')
plt.scatter(range(len(y_pred)),y_pred,color = 'blue', marker ='o')
plt.xlabel("actual target")
plt.ylabel("Predicted")
plt.title("Actual v/s predicted targets")
plt.grid()
plt.show()