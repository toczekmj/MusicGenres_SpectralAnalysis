import os
import pandas as pd


def convert_csv_files_to_custom_format(folder_path, output_file):
    all_data = []

    # traverse all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)

            # we assume that columns have names 'x_values' and 'y_values'
            x_values = df['x_values'].tolist()
            y_values = df['y_values'].tolist()

            # appends title at the beginning and music genre at the end of row
            if "JAZZ" in filename:
                row = [filename] + y_values + ["JAZZ"]
            elif "CLASSICAL" in filename:
                row = [filename] + y_values + ["CLASSICAL"]
            elif "POP" in filename:
                row = [filename] + y_values + ["POP"]
            elif "COUNTRY" in filename:
                row = [filename] + y_values + ["COUNTRY"]
            elif "HIPHOP" in filename:
                row = [filename] + y_values + ["HIPHOP"]
            elif "RAP" in filename:
                row = [filename] + y_values + ["RAP"]

            all_data.append(row)

    header = ["tytuły"] + x_values + ["gatunek_muzyczny"]

    # convert dataframe and write to file
    output_df = pd.DataFrame(all_data, columns=header)
    output_df.to_csv(output_file, index=False, header=True)


folder_path = "../FILES"
output_file = "../JAZZ_CLASSICAL_HIPHOP_COUNTRY_POP_RAP_merged.csv"
convert_csv_files_to_custom_format(folder_path, output_file)
