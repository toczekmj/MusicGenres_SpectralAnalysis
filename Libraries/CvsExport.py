import pandas as pd


def export_data_to_csv(x_values: int, y_values: int, genre: str, path: str, define_genre_by_filename: bool,  index=False):
    data_dict = {
        "x_values": x_values,
        "y_values": y_values
    }

    if ".csv" not in path.lower():
        path = path + ".csv"

    if define_genre_by_filename:
        path = path.split('/')

    pd.DataFrame(data_dict).to_csv(path, index=index)
