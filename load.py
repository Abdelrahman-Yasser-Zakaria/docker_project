import sys
import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df.to_csv('loaded_data.csv', index=False)
    print("Data loaded successfully.")
    # Call next script
    import subprocess
    subprocess.run(['python3', 'dpre.py', 'loaded_data.csv'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <file_path>")
    else:
        load_data(sys.argv[1])