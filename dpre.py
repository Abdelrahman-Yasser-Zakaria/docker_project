import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def data_preprocessing(file_path):
    df = pd.read_csv(file_path)
    # Data Cleaning
    df = df.drop(['PassengerId', 'Name', 'Ticket','Cabin'], axis=1)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    # Data Transformation
    # Encode categorical variables using one-hot encoding
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'])
    df['Age_Disc'] = df['Age']
    # Scale numerical variables using MinMaxScaler
    scaler = MinMaxScaler()
    df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
    # Create new feature "FamilySize"
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    # Data Discretization
    # Discretize "Age" into 4 age groups
    bins = [0, 18, 30, 50, 80]
    labels = ['Child', 'Young Adult', 'Adult', 'Elderly']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

    df.to_csv('res_dpre.csv', index=False)
    print("Data preprocessing completed.")

    # Call next script
    import subprocess
    subprocess.run(['python3', 'eda.py', 'res_dpre.csv'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dpre.py <file_path>")
    else:
        data_preprocessing(sys.argv[1])