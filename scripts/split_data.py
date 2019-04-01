"""
This script prepares the data in order to run the system smoothly.
It creates the necessary directories and seperates the training data 
into positive and negative validation data sets.
"""

import glob 
import os

# create new directories for new data sets
for fp in ['../data/valid', '../data/valid/pos_valid', '../data/valid/neg_valid']:
    if not os.path.exists(fp):
        os.mkdir(fp)


def split_train_data(current_dir, new_dir):
    """
    Takes files from training data directory and puts it in validation data directory.
    Input parameters are string type.
    """
    for file in glob.glob(f'../data/train/{current_dir}/*.txt')[-1250:]:
        filename = os.path.basename(file)
        os.rename(file, f'../data/valid/{new_dir}/{filename}')
    return


# call the function and create a negative and positive validation set
split_train_data('pos', 'pos_valid')
split_train_data('neg', 'neg_valid')