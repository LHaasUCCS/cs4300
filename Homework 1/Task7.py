import pandas as pd

# pandas is very useful for making well organized data frames
# create a DataFrame 
data = {
    'Patient Name': ['John Doe', 'Jane Smith', 'Robert Brown', 'Emily White', 'Michael Green'],
    'Age': [45, 52, 30, 67, 39],
    'Diagnosis': ['Diabetes', 'Hypertension', 'Asthma', 'Heart Disease', 'Cancer'],
    'Treatment': ['Insulin', 'Beta-blockers', 'Inhaler', 'Surgery', 'Chemotherapy']
}

# load data into a pandas Df
df = pd.DataFrame(data)

# filter by age greater than 50 
filtered_df = df[df['Age'] > 50]

# sort the data by age
sorted_df = df.sort_values(by='Age')

# mean of patient age
average_age = df['Age'].mean()

# Print results
print("Filtered DataFrame (Age > 50):")
print(filtered_df)
print("\nSorted DataFrame by Age:")
print(sorted_df)
print(f"\nAverage Age: {average_age}")

def test_DF():
    assert df['Age'].mean() == 46.6
    assert df["Patient Name"][1] == "Jane Smith" 
