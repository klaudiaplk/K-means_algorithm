# K-means_algorithm

K-Means algorithm was tested only in Python3.6.

# Virtual environment
It is recommended to create virtual environment to install the appropriate python versions and libraries used in the program and described in the setup.py file. An example of creating a virtual environment:
```
path/to/python -m venv /path/to/new/virtual/environment
```

# Installation
```
git clone https://github.com/klaudiaplk/K-means_algorithm.git
cd K_means_algorithm
pip install -e .
```

# Usage
We can run the script using the command:
```
k_means_algorithm --input-file INPUT_FILE --output-dir OUTPUT_DIR --k-max K_MAX [--n-init N_INIT] [--max-iter MAX_ITER] [--method {elbow,silhouette}] [--plots {with,without}]
```
Parameters that are required and parameters that is optional to run the K-Means Algorithm:
```
--input-file -> [str] The path to the csv file containing the data to be clustered.
--output-dir -> [str] Path to the folder where the results of the K-Means algorithm will be saved.
--k-max -> [int] Max clusters to check for Elbow or Silhouette methods.
--n-init -> [int] Enter the number of initializations to perform K-Means algorithm. If nothing is entered, the default value is 10.
--max-iter -> [int] Enter a number of maximum iterations for each initialization of the k-means algorithm. If nothing is entered, the default value is 100.
--method -> choices=['elbow', 'silhouette'] Possibility to choose a method to determine the optimal K for K-Means Algorithm. You can choose between 'elbow' or 'silhouette'. If nothing is selected then the default will be selected 'elbow'.
--plots -> choices=['with', 'without'] Possibility to choose whether you want to draw plots or just save the results to a csv file. If nothing is selected then the default will be selected 'with'.
```
All application launch parameters are also available under the command:
```
k_means_algorithm -h
```

# Author
Palak Klaudia