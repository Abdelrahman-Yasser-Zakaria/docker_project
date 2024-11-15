import sys
import pandas as pd
from sklearn.cluster import KMeans

def kmeans_clustering(file_path):
    df = pd.read_csv(file_path)
    df=df.drop(["Survived","AgeGroup"],axis=1)
    kmeans = KMeans(n_clusters=3)
    df['cluster'] = kmeans.fit_predict(df)
    cluster_counts = df['cluster'].value_counts()
    with open('k.txt', 'w') as f:
        f.write(cluster_counts.to_string())
    print("K-means clustering completed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 model.py <file_path>")
    else:
        kmeans_clustering(sys.argv[1])