from utils.helpers import *
from utils.logger import *
from preprocessing.clean_data import *
from preprocessing.feature_engineering import *
from preprocessing.split_data import *
from models.train_model import *

def train_pipeline():

    log_message("Loading data")

    df = load_dataset("data/raw/telecom_churn.csv")

    log_message("Cleaning data")

    df = clean_data(df)

    df = feature_engineering(df)

    split = split_data(df)

    train = split['train']

    log_message("Training model")

    model = train_model(train)

    return model

if __name__ == "__main__":
    train_pipeline()
