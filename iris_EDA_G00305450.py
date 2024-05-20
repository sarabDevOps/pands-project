# Author - Sarabjeet Kumar
# Programming and Scripting project 
# version : 1



from ucimlrepo import fetch_ucirepo
import pandas as pd
import seaborn as sns # heat maps pair plot
import matplotlib.pyplot as plt
import os

# Set the Matplotlib backend to 'Agg' to prevent display
plt.switch_backend('Agg')

# Define the directory to save output files
output_directory = 'C:/Users/sarab/Desktop/sarabProject/output_files1/'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Fetch dataset
iris = fetch_ucirepo(id=53)

data = iris.data

print("**iris.data", iris.data)

# Data (as pandas dataframes)
X = iris.data.features
y = iris.data.targets

# Metadata
print("*****")
print("*****iris.metadata:", iris.metadata)
print("*****")

# Variable information
print("iris.variables:", iris.variables)

# Create a DataFrame using the features and targets data
df = pd.DataFrame(data['features'], columns=data['headers'])
df['class'] = data['targets']

# Exclude the 'class' column from the DataFrame before computing summary statistics
numeric_df = df.drop(columns=['class'])

# Compute summary statistics using describe()
summary_stats = numeric_df.describe()

# Define the path to the text file where you want to save the summary
summary_file_path = output_directory + 'summary_statistics.txt'

# Write summary statistics to the text file
with open(summary_file_path, 'w') as file:
    # Iterate over each variable
    for column in numeric_df.columns:
        file.write(f"Summary for variable: {column}\n")
        file.write("===================================\n")
        file.write(f"Count: {summary_stats[column]['count']}\n")
        file.write(f"Mean: {summary_stats[column]['mean']}\n")
        file.write(f"Standard Deviation: {summary_stats[column]['std']}\n")
        file.write(f"Minimum: {summary_stats[column]['min']}\n")
        file.write(f"25th Percentile: {summary_stats[column]['25%']}\n")
        file.write(f"Median (50th Percentile): {summary_stats[column]['50%']}\n")
        file.write(f"75th Percentile: {summary_stats[column]['75%']}\n")
        file.write(f"Maximum: {summary_stats[column]['max']}\n\n")

print(f"Variable summary saved to '{summary_file_path}'")



# Create histograms for each numeric variable and save them as PNG files
for column in numeric_df.columns:
    # Create a histogram
    plt.figure(figsize=(8, 6))
    plt.hist(numeric_df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    
    # Save the histogram as a PNG file
    plt.savefig(output_directory + f'{column}_histogram.png')
    
    # Close the plot to free memory
    plt.close()

print(f"Histograms saved to '{output_directory}'")

# Create scatter plots for each pair of numeric variables and save them as PNG files
pairplot = sns.pairplot(numeric_df)
pairplot.savefig(output_directory + 'scatter_plots.png')

print(f"Scatter plots saved to '{output_directory}'")

# Heatmap for correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

# Save the heatmap as a PNG file
heatmap_path = output_directory + 'correlation_matrix.png'
plt.savefig(heatmap_path)

# Close the heatmap plot
plt.close()

print(f"Correlation matrix saved to '{heatmap_path}'")
