import scipy.io
import pandas as pd

# Load the .mat file
mat_file = "water_dataset.mat"  # Replace with your file path
data = scipy.io.loadmat(mat_file)

# Inspect the keys to find the data of interest
print(data.keys())

# Extract the specific data structure (modify 'variable_name' as per your .mat file)
# Replace 'variable_name' with the key that contains your data
data_array = data['variable_name']

# Convert the data to a DataFrame (if it's 2D or similar structured)
df = pd.DataFrame(data_array)

# Save the DataFrame to a CSV file
csv_file = "output.csv"
df.to_csv(csv_file, index=False)
print(f"Data saved to {csv_file}")

