import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("air_quality_sensor_readings.csv")

print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print((df == -200).sum())
df.replace(-200, np.nan, inplace=True)
print(df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)

print(df.isnull().sum())
numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')

plt.title("Correlation Matrix")
plt.show()

X = numeric_df.drop('CO(GT)', axis=1)
y = numeric_df['CO(GT)']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Linear Regression RMSE:", rmse)
print("Linear Regression R2:", r2)

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)

print("Random Forest RMSE:", rf_rmse)
print("Random Forest R2:", rf_r2)
print("\nModel Comparison")
print("----------------")
print("Linear Regression RMSE:", rmse)
print("Random Forest RMSE:", rf_rmse)
print("Linear Regression R2:", r2)
print("Random Forest R2:", rf_r2)

plt.figure(figsize=(8,5))
sns.histplot(df['CO(GT)'], bins=30)
plt.title("Distribution of CO Levels")
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df['NO2(GT)'], bins=30)
plt.title("Distribution of NO2 Levels")
plt.show()
plt.figure(figsize=(8,5))
sns.scatterplot(x='Temperature', y='CO(GT)', data=df)

plt.title("Temperature vs CO")
plt.show()
plt.figure(figsize=(8,5))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual CO")
plt.ylabel("Predicted CO")

plt.title("Actual vs Predicted CO")

plt.show()