from add_file import insert_file
from retrieve_file import filter_retrival
import keyboard

print("WELCOME TO JESSICA'S SCHOOL LIBRARY")
while(True):
    print("Choose what you want to do:\n")

    choice = input("0 -> insert a new file \n1 -> Get documents\n")

    file_path = "../Database/database.csv"
    list_path = "../Database/list_options.csv"

    if choice == '0':
        insert_file(file_path, list_path)
    elif choice == '1':
        filter_retrival(file_path, list_path)
    elif choice == 'x':
        print("Quitting, The Library is at your service")
        break
    else:
        print("Choice not available, choose between 0 and 1 or x to exit the library")

    print("*********************************************************************\n")