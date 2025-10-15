#!pip install pandas
import pandas as pd
# Load the dataset directly from the URL
file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv"
df = pd.read_csv(file_path)

# ✅ Print the number of columns in the dataset
print("Number of columns in the dataset:", df.shape[1])

# ✅ Identify the data types of each column
print("\nData types of each column:")
print(df.dtypes)

# ✅ Print the mean age of the survey participants
print("\nMean age of survey participants:", df['Age'].mean())

# Replace the age ranges with approximate numeric values (midpoints)
age_map = {
    "Under 18 years old": 17,
    "18-24 years old": 21,
    "25-34 years old": 29,
    "35-44 years old": 39,
    "45-54 years old": 49,
    "55-64 years old": 59,
    "65 years or older": 70,
    "Prefer not to say": None
}

# Map the age ranges to numeric values
df['Age_num'] = df['Age'].map(age_map)

# Calculate and print the mean of the numeric age values
mean_age = df['Age_num'].mean()
print("Estimated mean age of survey participants:", round(mean_age, 1))

# Load the dataset directly from the URL
file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv"
df = pd.read_csv(file_path)

# Display the first few rows
print(df.head())

exact_dup_mask = df.duplicated(keep=False)   # marks any row that has an identical twin (all columns)
num_exact_duplicates = exact_dup_mask.sum()
print(f"\nNumber of rows that have an exact duplicate (all columns equal): {num_exact_duplicates}")

if num_exact_duplicates:
    print("\nSample of exact duplicate rows:")
    print(df[exact_dup_mask].head(10))

    exact_dups = df.duplicated()
print("Exact duplicates:", exact_dups.sum())

# Check for duplicates based on key identifying fields
subset_cols = ["ResponseId", "Age", "Employment", "RemoteWork", "Country", "MainBranch"]
subset_cols = [c for c in subset_cols if c in df.columns]  # ensure they exist

subset_dups = df.duplicated(subset=subset_cols)
print("Duplicates based on subset:", subset_dups.sum())

# Remove duplicate rows (keep the first occurrence)
df_clean = df.drop_duplicates(subset=subset_cols, keep="first")

# Verify how many rows were removed
print("Removed:", df.shape[0] - df_clean.shape[0])

df_clean.to_csv("cleaned_survey_data.csv", index=False)
print("File 'cleaned_survey_data.csv' exported successfully.")
