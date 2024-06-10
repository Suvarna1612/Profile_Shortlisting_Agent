import streamlit as st
import pandas as pd

def main():
    st.title("Filter Your Candidates")

    # Assume the CSV file is in the current directory
    file_path = 'people_data.csv'
    df = pd.read_csv(file_path)
    st.write("Original Data", df)

    # Columns to exclude from filter options and display
    exclude_columns = ['name', 'email', 'phone_number', 'address','education','experience']

    # Allow user to select columns to filter, excluding specific columns
    columns = [col for col in df.columns if col not in exclude_columns and col not in ['age', 'skills']]
    filters = {}

    # Add a slider for selecting the age range
    min_age, max_age = int(df['age'].min()), int(df['age'].max())
    age_range = st.slider("Select age range", min_age, max_age, (min_age, max_age))

    # Add a slider for selecting the experience range
    min_exp, max_exp = int(df['experience'].min()), int(df['experience'].max())
    exp_range = st.slider("Select experience range (years)", min_exp, max_exp, (min_exp, max_exp))

    for column in columns:
        unique_values = df[column].unique().tolist()
        selected_values = st.multiselect(f"Select values for {column}", unique_values)
        if selected_values:
            filters[column] = selected_values

    # Multiselect for skills
    skills = ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'React', 'Node.js', 'Django', 'Flask']
    selected_skills = st.multiselect("Select skills", skills)

    # Radio button for selecting education level
    education_levels = ['High School', 'Bachelor Degree', 'Master Degree', 'Doctorate']
    selected_education = st.radio("Select education level", education_levels)

    # Apply filter conditions
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[(filtered_df['experience'] >= exp_range[0]) & (filtered_df['experience'] <= exp_range[1])]

    if filters:
        for column, selected_values in filters.items():
            filtered_df = filtered_df[filtered_df[column].isin(selected_values)]

    # Filter candidates by selected education level
    if selected_education == 'High School':
        filtered_df = filtered_df[filtered_df['education'].isin(['High School', 'Bachelor Degree', 'Master Degree', 'Doctorate'])]
    elif selected_education == 'Bachelor Degree':
        filtered_df = filtered_df[filtered_df['education'].isin(['Bachelor Degree', 'Master Degree', 'Doctorate'])]
    elif selected_education == 'Master Degree':
        filtered_df = filtered_df[filtered_df['education'].isin(['Master Degree', 'Doctorate'])]
    elif selected_education == 'Doctorate':
        filtered_df = filtered_df[filtered_df['education'] == 'Doctorate']

    # Filter candidates who have all selected skills
    if selected_skills:
        for skill in selected_skills:
            filtered_df = filtered_df[filtered_df['skills'].apply(lambda x: skill in x)]

    # Exclude specific columns from the final output
    #filtered_df = filtered_df.drop(columns=exclude_columns)
        
    st.write("Filtered Data", filtered_df)

    # Save the filtered DataFrame to a new CSV file
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download Filtered Data as CSV",
                       data=csv,
                       file_name="filtered_data.csv",
                       mime='text/csv')
    filtered_file_path = 'filtered_data.csv'
    filtered_df.to_csv(filtered_file_path, index=False)
    st.write(f"Filtered data saved to {filtered_file_path}")                   

if __name__ == "__main__":
    main()
