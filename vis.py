import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_visualization(file_path):
    df = pd.read_csv(file_path)
    sns.pairplot(df)
    plt.savefig('vis.png')
    print("Visualization created.")
    # Call next script
    import subprocess
    subprocess.run(['python3', 'model.py', file_path])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vis.py <file_path>")
    else:
        create_visualization(sys.argv[1])