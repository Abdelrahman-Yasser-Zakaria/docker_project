import sys
import pandas as pd

def exploratory_data_analysis(file_path):
    df = pd.read_csv(file_path)
    # insight 1: Summary statistics
    summary_stats = df.describe()
    with open('eda-in-1.txt', 'w') as f:
        f.write("Summary Statistics:\n")
        f.write(summary_stats.to_string())

    # insight 2: Correlation matrix of numerical features
    correlation_matrix = df.drop("AgeGroup",axis=1).corr()
    with open('eda-in-2.txt', 'w') as f:
        f.write("Correlation Matrix:\n")
        f.write(correlation_matrix.to_string())

    # insight 3: Distribution of the 'Survived' column
    survived_distribution = df['Survived'].value_counts(normalize=True)
    with open('eda-in-3.txt', 'w') as f:
        f.write("Distribution of 'Survived' column:\n")
        f.write(survived_distribution.to_string())
    print("Exploratory data analysis completed.")
    
    # Call next script
    import subprocess
    subprocess.run(['python3', 'vis.py', file_path])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eda.py <file_path>")
    else:
        exploratory_data_analysis(sys.argv[1])