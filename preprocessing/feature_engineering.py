import pandas as pd

def feature_engineering(df):
    df['tenure_group'] = pd.cut(df['tenure'], bins=[-1, 11, 23, float('inf')], labels=['new', 'mid', 'loyal'])
    df['tenure_group'] = df['tenure_group'].astype('category')
    return df
