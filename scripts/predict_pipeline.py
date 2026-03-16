import pandas as pd
import joblib
from models.predict_model import predict_model
from evaluation.evaluate_model import evaluate_model
from preprocessing.clean_data import clean_data

def predict_pipeline():
    model = joblib.load("models/churn_model.pkl")
    df = pd.read_csv("data/raw/telecom_churn.csv")
    df = clean_data(df)
    predictions = predict_model(model, df)
    accuracy = evaluate_model(predictions, df["Churn"])
    return accuracy

if __name__ == "__main__":
    accuracy = predict_pipeline()
    print(f"Model accuracy: {accuracy}")
