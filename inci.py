import pandas as pd

# Assuming 'chunk' is the chunk of data you want to save as CSV
# Convert the chunk to a DataFrame
df = pd.DataFrame(chunk)

# Save the DataFrame to a CSV file
df.to_csv('chunk_data.csv', index=False)
