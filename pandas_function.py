import pandas as pd
import numpy as np

# Creating DataFrames
print("Creating DataFrames:")
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, 6, 7, 8],
    'C': ['foo', 'bar', 'baz', 'qux'],
    'D': pd.date_range('20230101', periods=4)
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Basic Information
print("\nBasic Information:")
print("Data types:\n", df.dtypes)
print("Summary:\n", df.describe())
print("Info:")
df.info()

# Accessing Data
print("\nAccessing Data:")
print("Column A:\n", df['A'])
print("First two rows:\n", df.head(2))
print("Last two rows:\n", df.tail(2))

# Indexing and Selection
print("\nIndexing and Selection:")
print("Selecting by label (iloc):\n", df.iloc[1, 1])  # Row 1, Column 1
print("Selecting by position (loc):\n", df.loc[1, 'B'])  # Row 1, Column 'B'
print("Boolean indexing:\n", df[df['A'] > 1])

# Handling Missing Data
print("\nHandling Missing Data:")
df_filled = df.fillna(0)
print("Fill NaNs with 0:\n", df_filled)
df_dropped = df.dropna()
print("Drop rows with NaNs:\n", df_dropped)

# Adding and Dropping Columns
print("\nAdding and Dropping Columns:")
df['E'] = df['A'] * 2
print("New column 'E' added:\n", df)
df_dropped_col = df.drop(columns=['E'])
print("Column 'E' dropped:\n", df_dropped_col)

# Sorting
print("\nSorting:")
df_sorted = df.sort_values(by='B', ascending=False)
print("Sorted by column 'B':\n", df_sorted)

# Applying Functions
print("\nApplying Functions:")
print("Applying lambda to 'A':\n", df['A'].apply(lambda x: x * 2))
print("Applying np.sum to all columns:\n", df.apply(np.sum))

# Aggregations
print("\nAggregations:")
print("Mean of each column:\n", df.mean(numeric_only=True))
print("Sum of each column:\n", df.sum(numeric_only=True))
print("Minimum of each column:\n", df.min(numeric_only=True))

# Grouping
print("\nGrouping:")
df_grouped = df.groupby('C').sum()
print("Grouped by 'C':\n", df_grouped)

# Merging DataFrames
print("\nMerging DataFrames:")
data2 = {
    'A': [2, 3, 4, 5],
    'F': [10, 11, 12, 13]
}
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df, df2, on='A', how='outer')
print("Merged DataFrames:\n", merged_df)

# Pivoting
print("\nPivoting:")
pivot_data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [30, 40, 35, 45]
}
pivot_df = pd.DataFrame(pivot_data)
pivoted = pivot_df.pivot(index='Date', columns='City', values='Temperature')
print("Pivoted DataFrame:\n", pivoted)

# Concatenating DataFrames
print("\nConcatenating DataFrames:")
df3 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df4 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
concat_df = pd.concat([df3, df4], axis=0)
print("Concatenated DataFrames:\n", concat_df)

# Window Functions (Rolling, Expanding)
print("\nWindow Functions:")
df['Rolling Mean'] = df['B'].rolling(window=2).mean()
print("Rolling mean of 'B' (window=2):\n", df)

# Date-Time Functions
print("\nDate-Time Functions:")
df['Day'] = df['D'].dt.day
df['Month'] = df['D'].dt.month
df['Year'] = df['D'].dt.year
print("Date-based columns (Day, Month, Year):\n", df)

# Renaming Columns
print("\nRenaming Columns:")
df_renamed = df.rename(columns={'A': 'Alpha', 'B': 'Beta'})
print("Renamed Columns:\n", df_renamed)

# DataFrame to NumPy Array
print("\nDataFrame to NumPy Array:")
array = df.to_numpy()
print("Converted to NumPy Array:\n", array)

# Basic Plotting (Requires matplotlib)
print("\nBasic Plotting:")
df['B'].plot(kind='line', title='Column B Line Plot')

# Memory Usage
print("\nMemory Usage:")
print("Memory usage of DataFrame:\n", df.memory_usage())

# Duplicates
print("\nHandling Duplicates:")
data_with_duplicates = {'A': [1, 1, 2, 2], 'B': [3, 3, 4, 5]}
df_duplicates = pd.DataFrame(data_with_duplicates)
print("Original DataFrame with Duplicates:\n", df_duplicates)
print("Dropped duplicates:\n", df_duplicates.drop_duplicates())
