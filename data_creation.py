import pandas as pd
from faker import Faker
import csv
fake = Faker()
def insert_fake_data_to_csv(num_records, file_name):
    skills_set = ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'React', 'Node.js', 'Django', 'Flask']
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'age', 'gender', 'email', 'phone_number', 'education', 'address', 'skills', 'experience', 'certifications'])
        for _ in range(num_records):
            name = fake.name()
            age = fake.random_int(min=18, max=80)
            gender = fake.random_element(elements=('Male', 'Female'))
            email = fake.email()
            phone_number = fake.phone_number()
            education = fake.random_element(elements=('High School', 'Bachelor Degree', 'Master Degree', 'Doctorate'))
            address = fake.address()
            skills = ', '.join(fake.random_elements(elements=skills_set, length=3, unique=True))  # Select 3 unique random skills
            experience = fake.random_element(elements=('0', '1', '2', '3', '4', '5'))
            certifications = fake.random_element(elements=('Yes', 'No'))  # Randomly select "Yes" or "No"
            writer.writerow([name, age, gender, email, phone_number, education, address, skills, experience, certifications])

# Create CSV file with fake data
file_name = 'people_data.csv'
insert_fake_data_to_csv(200, file_name)
pf = pd.read_csv('people_data.csv')
print(pf.head())
print(pf.info())