import os
import os.path as osp
import pickle
import pandas as pd

def combine_pickle_files(directory_path, output_file):
    combined_df = pd.DataFrame()  # Initialize an empty DataFrame to store the merged data

    for file_name in os.listdir(directory_path):
        if file_name.endswith('feature.p'):
            file_path = osp.join(directory_path, file_name)
            with open(file_path, 'rb') as f:
                content = pickle.load(f)
                if isinstance(content, pd.DataFrame):
                    combined_df = pd.concat([combined_df, content], ignore_index=True)
    
    with open(output_file, 'wb') as out:
        pickle.dump(combined_df, out, protocol=pickle.HIGHEST_PROTOCOL)

# Example usage:
directory_path = '//wsl.localhost/Ubuntu/home/manasranjanprusti005/JAYESH_CHILLER'
output_file = './result.p'
combine_pickle_files(directory_path, output_file)