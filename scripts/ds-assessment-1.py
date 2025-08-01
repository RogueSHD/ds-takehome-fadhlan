
#libraries that we needed to import in order to make this a success 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

# 1. Load data from what I have generated in the generatecsv.py file using the dataset with features: `user_id`, `last_login_days_ago`, `num_purchases`, `avg_purchase_value`, and a binary target `churned`.
df = pd.read_csv(r'C:\Users\Fadhlan\Desktop\data-takehome-fadhlan\data\churn_dataset.csv')

# 2. Drop column that we are not using which are user_id and churn but churn we need to use it for target variable purposes and it should not be listed in our features
X = df.drop(['user_id', 'churned'], axis=1)
y = df['churned']

# 3. Feature scaling (important for logistic regression) Why? because transforming your numeric features so they’re on a similar scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#almost theree...

# 4. Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# 5. from here we willl train our logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Make predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

# 7. lastly, evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))
print(classification_report(y_test, y_pred))
