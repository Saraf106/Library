import pandas as pd
def modify_path_file(file_path):

    name_file = input("Write the file you want to change the path of\n")
    new_path = input("Write the new path you saved your file\n")
    df = pd.read_csv(file_path)
    present = df['FileName'].isin([name_file]).any()
    if present:
        df.loc[df['FileName'] == name_file, ['Path']] = new_path

        df.to_csv(file_path, header=True, index=False)
        print("The change has been saved\n")
    else:
        print(f"No file present with name: {name_file}")


