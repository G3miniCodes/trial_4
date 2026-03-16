import pandas as pd


def clean_data(df):
    # Convert character columns to factors (categorical)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')

    # Replace NA values in numeric columns with the mean of the column
    for col in df.select_dtypes(include=['number']).columns:
        df[col].fillna(df[col].mean(), inplace=True)

    # Filter out rows where the Churn column is NA
    df = df[df['Churn'].notna()]

    return df
