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
cursor.execute ('SELECT * FROM "ZillowMWData";')
# Fetch result
df_mw = DataFrame(cursor.fetchall())
df_mw.columns = ['ZIP', 'State', 'City', 'Metro', 'CountyName', 'ValueDate','HomeValue']

df_updated_mw = df_mw.drop(['ZIP', 'State', 'City', 'Metro'], axis=1)
# df_updated = df.drop(['HomeValue'])
# df.drop(['Metro'], axis=1)
# print(df_updated)

county_name_mw = df_updated_mw['CountyName']


df_onehotmw = df_updated_mw.select_dtypes(exclude=['number']) \
                .apply(LabelEncoder().fit_transform) \
                .join(df_updated_mw.select_dtypes(include=['number']))

county_encoded_mw = df_onehotmw['CountyName']

county_merged_mw = pd.concat([county_name_mw, county_encoded_mw], axis=1)

# dropped = county_merged.reset_index(drop=True, inplace=True)

county_merged_mw.columns = ['CountyName', 'CountyCode']
county_merged_mw = county_merged_mw.set_index(['CountyName'])
county_dict_mw = county_merged_mw.to_dict()

print(county_dict_mw['CountyCode'])
# print(df_onehotmw)

y = df_onehotmw['HomeValue'].values.reshape(-1, 1)
X = df_onehotmw[['CountyName', 'ValueDate']]

Xscaler = StandardScaler()
Xscaler = Xscaler.fit(X)
Xscaled = Xscaler.transform(X)

yscaler = StandardScaler()
yscaler = yscaler.fit(y)
yscaled = yscaler.transform(y)

X_train, X_test, y_train, y_test = train_test_split(Xscaled, yscaled, test_size=0.33)


lin_regmw = LinearRegression()
lin_regmw.fit(X_train, y_train)
pickle.dump(lin_regmw, open('zillowmw-ml.pkl','wb'))

score = lin_regmw.score(X_train, y_train)
predict = lin_regmw.predict(X)
print(f"Score = {score}")