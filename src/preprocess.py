# preprocess.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Encode categorical variables
    label_encoder = LabelEncoder()
    df['salary'] = label_encoder.fit_transform(df['salary'])
    df['Department'] = label_encoder.fit_transform(df['Department'])

    # Define features and target variable
    X = df.drop('left', axis=1)
    y = df['left']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test
