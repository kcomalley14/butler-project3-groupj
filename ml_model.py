import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import psycopg2
import os
from sqlalchemy import create_engine
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression

DB_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DB_URL)
# Create a cursor to perform database operations
cursor = conn.cursor()
# Executing a SQL query
cursor.execute ('SELECT * FROM "ZillowINData";')
# Fetch result
df = DataFrame(cursor.fetchall())
df.columns = ['ZIP', 'State', 'City', 'Metro', 'CountyName', 'ValueDate','HomeValue']

df_updated = df.drop(['ZIP', 'State', 'City', 'Metro'], axis=1)
# df_updated = df.drop(['HomeValue'])
# df.drop(['Metro'], axis=1)
# print(df_updated)

county_name = df_updated['CountyName']


df_onehot = df_updated.select_dtypes(exclude=['number']) \
                .apply(LabelEncoder().fit_transform) \
                .join(df_updated.select_dtypes(include=['number']))

county_encoded = df_onehot['CountyName']

county_merged = pd.concat([county_name, county_encoded], axis=1)

# dropped = county_merged.reset_index(drop=True, inplace=True)

county_merged.columns = ['CountyName', 'CountyCode']
county_merged = county_merged.set_index(['CountyName'])
county_dict = county_merged.to_dict()

print(county_dict['CountyCode'])
# print(df_onehot)

y = df_onehot['HomeValue'].values.reshape(-1, 1)
X = df_onehot[['CountyName', 'ValueDate']]

Xscaler = StandardScaler()
Xscaler = Xscaler.fit(X)
Xscaled = Xscaler.transform(X)

yscaler = StandardScaler()
yscaler = yscaler.fit(y)
yscaled = yscaler.transform(y)

X_train, X_test, y_train, y_test = train_test_split(Xscaled, yscaled, test_size=0.33)


lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
pickle.dump(lin_reg, open('zillow-ml.pkl','wb'))

score = lin_reg.score(X_train, y_train)
predict = lin_reg.predict(X)
print(f"Score = {score}")