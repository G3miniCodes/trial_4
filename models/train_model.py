import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def train_model(train_data):
    X = train_data.drop(columns=['Churn'])
    y = train_data['Churn']

    model = RandomForestClassifier(n_estimators=200)
    model.fit(X, y)

    joblib.dump(model, 'models/churn_model.pkl')

    return model

if __name__ == "__main__":
    # Example usage
    train_data = pd.read_csv('path_to_train_data.csv')
    train_model(train_data)
