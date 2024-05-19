# pands-project
## The project is made for as a part of college work - Module -> Programming and Scripting  

### Project Overview

#### Iris Dataset Exploratory Data Analysis (EDA)
This repository contains Python code for performing Exploratory Data Analysis (EDA) on the Iris dataset. The analysis includes generating summary statistics, creating histograms, scatter plots, and a correlation heatmap for the numeric variables.


#### Dataset
The UCI Machine Learning Repository provides 150 samples of iris flowers with four features: sepal length, sepal width, petal length, and petal width. These samples make up the Iris dataset. One of the three species—Iris setosa, Iris versicolor, or Iris virginica—represents each sample.


#### Approach
The approach to the analysis is as follows:
1.	Data Fetching: The dataset is fetched using the ucimlrepo package.
2.	DataFrame Creation: The data is converted into a Pandas DataFrame.
3.	Summary Statistics: Basic summary statistics for each numeric variable are computed and saved to a text file. Provides an overview of the central tendency, dispersion, and shape of the dataset's distribution

4.	Histograms: Histograms are created for each numeric variable to visualize their distributions. Help in understanding the distribution and frequency of numeric variables.
5.	Scatter Plots: Scatter plots for each pair of numeric variables are generated to observe relationships. Useful for identifying potential relationships and correlations between pairs of variables.
6.	Correlation Heatmap: A heatmap of the correlation matrix is created to show correlations between variables.



#### Directory Structure

```
 ──> iris_EDA_G00305450.py
 ──> output_files1/
     ──> summary_statistics.txt
     ──> sepal_length_histogram.png
     ──> sepal_width_histogram.png
     ──> petal_length_histogram.png
     ──> petal_width_histogram.png
     ──> scatter_plots.png
──>README.md
──>requirements.txt
```

***iris_EDA_G00305450.py: Main script that performs the EDA.
 Output_files1/: Directory where the output files (summary statistics, histograms, scatter plots) are saved.***

 #### Results
1. Summary Statistics: Stored in output_files1/summary_statistics.txt.
2. Histograms: Stored as PNG files in output_files1/.
3. Scatter Plots: Stored as scatter_plots.png in output_files1/.
4. Correlation Heatmap: Stored as correlation_matrix.png in output_files1/.


#### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
Download and extract the zip folder here [pands-project](https://github.com/sarabDevOps/pands-project/archive/refs/heads/main.zip)

#### Prerequisites
VS Code . You can download here [VS Code](https://code.visualstudio.com/download)



#### Installing
Once you have downloaded the executable file click on it and it will automatic guide you for installation.

To run the code in this repository, you need to have Python 3.x and the following Python packages installed:

+ ucimlrepo

+ pandas

+ seaborn

+ matplotlib

+ You can install the required packages using pip:

+ pip install ucimlrepo pandas seaborn matplotlib



#### Deployment

File menu from VS Code ----> Hit the open ------>  select iris_EDA_G00305450 python file from file Explorer 

#### Built With
 Visual Studio Code ->  [VS Code](https://code.visualstudio.com/download)


#### Versioning

Version 1


#### Authors

[SarabDevOps](https://github.com/sarabDevOps)



## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/sarabDevOps/pands-project/blob/main/LICENSE) file for details














