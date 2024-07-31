import os
import pandas as pd

name_files = []
path_files = []
subjects = []
schools = []
years = []
def insert_file(file_path, list_path):

    print("Please enter the following elements:")
    print("Name file")
    name_file = input()
    print("Path of the file")
    path_file = input()
    print("Subject")
    subject = input()
    print("School")
    school = input()
    print("Year")
    year = input()

    #1. WRITING IN THE DATABASE

    attribute = [name_file, path_file, subject, school, year]

    # Convert the vector to a DataFrame
    # Assuming the CSV file should have headers: 'File Name', 'Path', 'Subject', 'School', 'Year'
    column_names = ['File Name', 'Path', 'Subject', 'School', 'Year']
    new_row_df = pd.DataFrame([attribute], columns=column_names)

    # Path to the CSV file
    csv_file = '../Database/database.csv'

    # Check if the file exists
    if not os.path.isfile(csv_file):
        # Write the DataFrame with headers if the file does not exist
        new_row_df.to_csv(csv_file, mode='w', header=True, index=False)
    else:
        # Append to the file without headers if it exists
        new_row_df.to_csv(csv_file, mode='a', header=False, index=False)


    #2. UPDATE THE LIST OF OPTIONS POSSIBLE FOR SUBJECTS AND SCHOOLS


    options_saved(subject, school)

def options_saved(subject, school):


    # read specific columns of csv file using Pandas
    df = pd.read_csv('../Database/list_options.csv', usecols=['Subject'])
    out = df['Subject'].isin([subject]).any()
    print(out)
    if not out:
        new = True
    else:
        new = False

    df = pd.read_csv('../Database/list_options.csv', usecols=['School'])
    out = df['School'].isin([school]).any()
    print(df['School'].values)
    print(out)
    if not out:
        if new is False:
            print("sono qui")
            dp = pd.DataFrame([[None, school]], columns=['Subject', 'School'])
            dp.to_csv('../Database/list_options.csv', mode='a', header=False, index=False)
        else:
            dp = pd.DataFrame([[subject, school]], columns=['Subject', 'School'])
            dp.to_csv('../Database/list_options.csv', mode='a', header=False, index=False)
