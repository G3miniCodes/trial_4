import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(df):
    train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df['Churn'])
    return {'train': train, 'test': test}
