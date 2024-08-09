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
    column_names = ['File Name', 'Path', 'Subject', 'School', 'Year']
    new_row_df = pd.DataFrame([attribute], columns=column_names)

    # Check if the file exists
    if not os.path.isfile(file_path):
        # Write the DataFrame with headers if the file does not exist
        new_row_df.to_csv(file_path, mode='w', header=True, index=False)
    else:
        # Append to the file without headers if it exists
        new_row_df.to_csv(file_path, mode='a', header=False, index=False)


    #2. UPDATE THE LIST OF OPTIONS POSSIBLE FOR SUBJECTS AND SCHOOLS


    options_saved(subject, school, list_path)

def options_saved(subject, school, list_path):


    # read specific columns of csv file
    df = pd.read_csv(list_path, usecols=['Subject'])
    out = df['Subject'].isin([subject]).any()
    print(out)
    if not out:
        new = True
    else:
        new = False

    df = pd.read_csv(list_path, usecols=['School'])
    out = df['School'].isin([school]).any()
    if not out:
        if new is False:
            dp = pd.DataFrame([[None, school]], columns=['Subject', 'School'])
            dp.to_csv(list_path, mode='a', header=False, index=False)
        else:
            dp = pd.DataFrame([[subject, school]], columns=['Subject', 'School'])
            dp.to_csv(list_path, mode='a', header=False, index=False)
