import scipy.io
import json
import numpy as np

# Load the .mat file
mat_file = scipy.io.loadmat('ExampleData.mat')

# Function to convert data to a JSON-serializable format
def convert_data(value):
    if isinstance(value, np.ndarray):
        return value.tolist()  # Convert numpy arrays to lists
    elif isinstance(value, bytes):
        return value.decode('utf-8', errors='ignore')  # Decode bytes to string, ignoring errors
    return value

# Convert the .mat file dictionary to a JSON-compatible format
# Remove any metadata fields such as '__header__', '__version__', '__globals__'
mat_data = {key: convert_data(mat_file[key]) for key in mat_file if not key.startswith('__')}

# Save to a JSON file
with open('output_file.json', 'w') as json_file:
    json.dump(mat_data, json_file, indent=4)
