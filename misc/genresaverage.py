import os

import numpy as np
import pandas as pd
from glob import glob


def process_genre_folder(genre_folder):
    # Get all CSV files in the genre folder
    csv_files = glob(os.path.join(genre_folder, '*.csv'))

    if not csv_files:
        print(f"No CSV files found in {genre_folder}")
        return

    # Initialize a list to store dataframes
    y_values_list = []
    x_values_list = []

    for file in csv_files:
        df = pd.read_csv(file)
        y_values_list.append(df['y_values'])
        x_values_list.append(df['x_values'])

    y_values_df = pd.DataFrame(y_values_list)
    x_values_df = pd.DataFrame(x_values_list)

    y_values_mean = y_values_df.mean(axis=0)
    x_values_mean = x_values_df.mean(axis=0)

    result_df = pd.DataFrame({'x_values': x_values_mean, 'y_values': y_values_mean})

    output_dir = 'averaged_csvs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the result DataFrame to a new CSV file
    output_file = os.path.join(output_dir, f"{os.path.basename(genre_folder)}_averaged.csv")
    result_df.to_csv(output_file, index=False)
    print(f"Saved averaged CSV for {genre_folder} to {output_file}")


def process_all_genres(base_dir):
    # Get all genre folders
    genre_folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and f.endswith('CSV')]

    for genre_folder in genre_folders:
        process_genre_folder(os.path.join(base_dir, genre_folder))

# this is a script which gets average from one of the music genres
# it operates on already created CSV files, not on the .mp3 files
if __name__ == "__main__":
    base_directory = ''  # Replace with the path to your base directory
    process_all_genres(base_directory)
