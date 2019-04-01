"""
utility functions for the system
"""

import csv
import os

def combine_dirs(dir1, dir2=None):
    """ 
    Takes directory(ies) as positional argument(s). Combines the files in the directories into a
    list of filepaths. These files can then be used for training or testing.
    """
    combined_dirs = []
    for file in os.listdir(dir1):
        filepath = os.path.join(dir1, file)
        combined_dirs.append(filepath)
    if dir2:
        for file in os.listdir(dir2):
            filepath = os.path.join(dir2, file)
            combined_dirs.append(filepath)

    return combined_dirs


def create_csv(list_of_dicts, filename):
    '''
    Creates a csv file. Takes a list of dictionaries as a positional argument. The values from the dictionary are
    used to fill in the rows of the file.
    '''
    with open(filename, "w", newline='') as datafile:
        header = list_of_dicts[0].keys()
        writer = csv.DictWriter(datafile, header)
        writer.writeheader()
        writer.writerows(list_of_dicts)
    
    return


def csv2dict(filepath):
    """ Takes a csv file and makes a list of dictionaries that can be used to manipulate the data in it."""
    entries = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f, delimiter=',')
        for entry in reader:
            # re-assign each dict value to be an int or float (originally a string)
            entry['review_length'] = int(entry['review_length'])
            entry['avg_word_length'] = float(entry['avg_word_length'])
            entry['char length'] = int(entry['char length'])
            entry['total_ADJS'] = float(entry['total_ADJS'])
            entry['total_VERBS'] = float(entry['total_VERBS'])
            entry['total_NOUNS'] = float(entry['total_NOUNS'])
            entry['. count'] = float(entry['. count'])
            entry['! count'] = float(entry['! count'])
            entry['? count'] = float(entry['? count'])  
            entry['TTR'] = float(entry['TTR'])
            entries.append(entry)
                                             
    return entries

