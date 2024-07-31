import csv
import pandas as pd


def filter_retrival(file_path, list_path):

    #getting the possible options available for
    df = pd.read_csv('../Database/list_options.csv', usecols=['Subject'])
    filtered_subjects = df['Subject'].dropna()
    de = pd.read_csv('../Database/list_options.csv', usecols=['School'])
    filtered_schools = de['School'].dropna()
    print("Choose what you want to do:\n")
    choice = int(input("0 -> filter by subject \n1 -> filter by school\n2-> filter by subject and school\n"))
    if choice == 0:
        subject = input(f"Select the subject among: {filtered_subjects.values}\n") #mettere il vettore tra cui scegliere e dare le opzioni in automatico
        school = False
        get_documents(subject, school, file_path)
    elif choice == 1:
        subject = False
        school = input(f"Select the school among: {filtered_schools.values}\n")
        get_documents(subject, school, file_path)
    elif choice == 2:
        subject = input(f"Select the subject among: {filtered_subjects.values}\n")
        school = input(f"Select the school among: {filtered_schools.values}\n")
        get_documents(subject, school, file_path)
    else:
        print("Choice not available, choose between 0, 1 and 2\n")




def get_documents(subject, school, file_path):

    if school is False:
        found = filter_subject(file_path, subject)
        if found is False:
            print(f"No file with {subject} found d\n")
    elif subject is False:
        found = filter_school(file_path, school)
        if found is False:
            print(f"No file with {school} found \n")
    else:
        found = filter_subject_school(file_path, subject, school)
        if found is False:
            print(f"No file with {subject} and {school} found\n")

def filter_subject(file_path, subject):
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == subject:
                print(row[0], row[1], row[2])
                found = True
        if not found:
            found = False
    return found



def filter_school(file_path, school):
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[3] == school:
                print(row[0], row[1], row[3])
                found = True
        if not found:
            found = False
    return found


def filter_subject_school(file_path, subject, school):
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[3] == school and row[2] == subject:
                print(row[0], row[1], row[2], row[3])
                found = True
        if not found:
            found = False
    return found