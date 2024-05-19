# pands-project
## The project is made for as a part of college work - Module -> Programming and Scripting  

### Project Overview
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

├── iris_EDA_G00305450.py
├── output_files1/
│   ├── summary_statistics.txt
│   ├── sepal_length_histogram.png
│   ├── sepal_width_histogram.png
│   ├── petal_length_histogram.png
│   ├── petal_width_histogram.png
│   ├── scatter_plots.png
├── README.md
└── requirements.txt







