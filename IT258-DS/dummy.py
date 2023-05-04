import numpy as np
import matplotlib.pyplot as plt

# Generate example data
data = np.random.normal(10, 2, 1000)  # Normal distribution with mean 10 and standard deviation 2

# Plot histogram of data to visualize shape
plt.hist(data, bins=20)
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Calculate variance and standard deviation of data
variance = np.var(data)
std_dev = np.std(data)

print('Variance:', variance)
print('Standard Deviation:', std_dev)

# Perform one-way ANOVA on data to compare variation between groups and within groups
# Note: ANOVA requires data to be separated into groups
# For simplicity, we will split the data into two groups based on a threshold value
threshold = 11
group1 = data[data < threshold]
group2 = data[data >= threshold]

from scipy.stats import f_oneway

f_stat, p_val = f_oneway(group1, group2)

print('F-statistic:', f_stat)
print('P-value:', p_val)
