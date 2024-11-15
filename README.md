# Titanic Data Analysis and Clustering

This project performs data analysis and clustering on the Titanic dataset using a containerized environment. The steps include setting up a Docker container, creating Python scripts for data processing, exploratory data analysis, and visualization.

## Dataset

We use the Titanic dataset for this assignment. Download the dataset from [Kaggle](https://www.kaggle.com/c/titanic/data?select=train.csv).

## Steps

### 1. Create the Docker Environment

- **Base Image**: Use Ubuntu as the base image.
- **Virtual Environment**: Create a virtual environment called `venv`.
- **Install Libraries**: Install required libraries such as `numpy` and `pandas` in `venv`.
- **Directory Structure**: 
  - Create a directory `/home/doc-bd-al/` in the container.
  - Copy the dataset to this directory.
  - Set this directory as the working directory.
- **Startup Command**: Open a bash shell upon container startup.

### 2. Build and Run the Docker Container

- Build the Docker image:
  ```bash
  docker build -t big_data_assi1 .
  ```
- Run the Docker container:
  ```bash
  docker run -it big_data_assi1
  ```

### 3. Python Scripts

The project includes several Python scripts, each performing a specific task:

- **`load.py`**:
  - Loads the dataset and creates a new dataset `load_data.csv`.
  - Passes `load_data.csv` to `dpre.py` using the `subprocess` library.

- **`dpre.py`**:
  - Processes `load_data.csv` by cleaning, transforming, and discretizing the dataset.
  - Creates a new dataset `res_dpre.csv` and passes it to `eda.py`.

- **`eda.py`**:
  - Performs exploratory data analysis (EDA) on `res_dpre.csv`.
  - Generates summary statistics, a correlation matrix, and distributions for specific columns, saving each as a text file.
  - Calls `vis.py` for further processing.

- **`vis.py`**:
  - Creates visualizations for the dataset, specifically a pair plot of features, saving it as `vis.png`.
  - Passes the file to `model.py` for further processing.

- **`model.py`**:
  - Applies K-means clustering on the dataset.
  - Drops specific columns and assigns clusters to the data (3 clusters).
  - Saves the cluster counts in a text file `k.txt`.

### 4. Run Python Scripts and Final Script

- Execute the Python scripts in the container as per the dependency order described above.
- Run `final.sh` to copy output files from the container to the local machine in `bd-a1/service-result/` and stop the container.

## Output

The final outputs include:

- Processed datasets
- Summary statistics and correlation matrix text files
- Visualization image (`vis.png`)
- Cluster count text file (`k.txt`)