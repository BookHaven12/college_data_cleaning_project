
import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_students = 200
majors = ['Computer Science', 'Biology', 'Psychology', 'Economics', 'Sociology']
genders = ['Male', 'Female', 'Non-Binary', 'Prefer Not to Say']
states = ['CA', 'NY', 'TX', 'IL', 'WA']

# Generate mock data
df = pd.DataFrame({
    'student_id': [f"S{1000+i}" for i in range(n_students)],
    'first_name': np.random.choice(['Alex', 'Taylor', 'Jordan', 'Morgan', 'Casey'], n_students),
    'last_name': np.random.choice(['Smith', 'Johnson', 'Lee', 'Brown', 'Garcia'], n_students),
    'gender': np.random.choice(genders, n_students, p=[0.45, 0.45, 0.05, 0.05]),
    'age': np.random.randint(17, 26, n_students),
    'major': np.random.choice(majors, n_students),
    'gpa': np.round(np.random.normal(3.0, 0.4, n_students), 2),
    'credits_completed': np.random.randint(0, 130, n_students),
    'enrollment_date': pd.to_datetime(np.random.choice(pd.date_range('2019-08-01', '2023-08-01'), n_students)),
    'graduation_year': np.random.choice([2022, 2023, 2024, 2025, 2026, None], n_students, p=[0.15, 0.25, 0.3, 0.2, 0.05, 0.05]),
    'home_state': np.random.choice(states, n_students)
})

# Inject intentional data quality issues
df.loc[5, 'gpa'] = 4.8  # Invalid GPA
df.loc[10, 'major'] = 'Comp Sci'  # Inconsistent major
df.loc[20:25, 'graduation_year'] = None  # Missing years
df.loc[30, 'gender'] = 'femaale'  # Typo in gender
df.loc[40, 'credits_completed'] = -10  # Negative credit
df.loc[50, 'enrollment_date'] = pd.to_datetime('2022-09-01')
df.loc[50, 'graduation_year'] = 2020  # Illogical graduation before enrollment
df.loc[60, 'gender'] = 'F'
df.loc[70, 'gender'] = 'fem'
df.loc[80, 'major'] = 'computer sci'
df.loc[90, 'major'] = 'CS'

# Get the absolute path to the project root (one level up from this script)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure the 'data' directory exists at the project root
data_dir = os.path.join(project_root, "data")
os.makedirs(data_dir, exist_ok=True)

# Define the full path to the output CSV inside the 'data' folder
output_path = os.path.join(data_dir, "mock_college_students_with_issues.csv")

# Save the DataFrame to CSV
df.to_csv(output_path, index=False)
print(f"Mock dataset saved to: {output_path}")