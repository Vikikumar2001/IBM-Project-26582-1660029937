# -*- coding: utf-8 -*-
"""Assignment_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JpBI4eKO-fe3Gh5kMbVrVxDZCfQYKAZD
"""

from google.colab import drive
drive.mount('/content/gdrive')

from google.colab import files
uploaded = files.upload()

"""**2. Load the dataset into the tool**"""

import pandas as pd
import io
import numpy as np

a = pd.read_csv(io.BytesIO(uploaded['abalone.csv']))

a.head()

"""3.**Perform Below Visualizations.
∙ Univariate Analysis
∙ Bi-Variate Analysis
∙ Multi-Variate Analysis**

**Univariate Analysis**
"""

import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import matplotlib.pyplot as plt

cols = 3
rows = 3
num_cols = a.select_dtypes(exclude='object').columns
fig = plt.figure( figsize=(cols*5, rows*5))
for i, col in enumerate(num_cols):
    
    ax=fig.add_subplot(rows,cols,i+1)
    
    sns.histplot(x = a[col], ax = ax)
    
fig.tight_layout()  
plt.show()

sns.boxenplot(x=a["Shell weight"])

"""**Bi-Variate Analysis**"""

plt.scatter(a.Height,a.Length)
plt.xlabel('Height')
plt.ylabel('Length')

"""**Multi-Variate Analysis**"""

sns.scatterplot(a['Height'], a['Shucked weight'], hue = a['Shell weight'])

"""
**4. Perform descriptive statistics on the dataset.**"""

a.mean()

a.median()

a.mode()

"""
**5. Check for Missing values and deal with them.**"""

a.isnull().sum()

"""There is no missing values

6.**Find the outliers and replace them outliers**
"""

a['Shell weight'] = np.where(a['Shell weight'] > 325, 140, a['Shell weight'])
a.describe()

"""7. **Check for Categorical columns and perform encoding.**"""

from sklearn.compose import make_column_selector as selector

categorical_columns_selector = selector(dtype_include=object)
categorical_columns = categorical_columns_selector(a)
categorical_columns

data_categorical = a[categorical_columns]
data_categorical.head()

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

a['Sex']= label_encoder.fit_transform(a['Sex'])
a['Sex'].unique()

"""8. **Split the data into dependent and independent variables.**"""

x=a.iloc[:,:-1]
x.head()

y=a.iloc[:,-1]
y.head()

""". 9. **Scale the independent variables**"""

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x=scaler.fit_transform(x)

a_scaled =a.copy()
col_names = ['Shucked weight', 'Whole weight']
features = a_scaled[col_names]
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
a_scaled[col_names] = scaler.fit_transform(features.values)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(5, 10))

a_scaled[col_names] = scaler.fit_transform(features.values)
a_scaled

"""10.**Split the data into training and testing**

"""

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33)

x_train.shape

x_test.shape

"""11. **Build the Model**

"""

from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor()

"""12. **Train the Model**"""

reg.fit(x_train,y_train)

"""**13. Test the Model**"""

y_pred=reg.predict(x_test)

print(y_pred)

"""**14. Measure the performance using Metrics.**"""

from sklearn.metrics import mean_squared_error
import math
print(math.sqrt(mean_squared_error(y_test,y_pred)))