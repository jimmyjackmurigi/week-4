import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load and preprocess data
df = pd.read_csv('data.csv')
df.dropna(axis=1, inplace=True)
X = df.drop(['diagnosis'], axis=1)
y = df['diagnosis'].apply(lambda x: 1 if x == 'M' else 0)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))