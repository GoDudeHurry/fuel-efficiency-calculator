import pandas as pd

def update_csv_sheet():
    pass

def get_csv_as_list_of_dict(path, filename):
    df = pd.read_csv(path + filename, sep=",")
    return df.to_dict("records")

def update_csv(data_list_as_dict, path, filename):
    df = pd.DataFrame(data_list_as_dict)
    df.to_csv(path + filename, index=False)


