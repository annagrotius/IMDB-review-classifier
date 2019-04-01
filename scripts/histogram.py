# -*- coding: utf-8 -*-
"""
Creates a histogram.
"""
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import os

def create_histogram(filepath, key, label, title=None, image_name="no_name.png"):
    """Creates a histogram of with a kernel density estimation drawn.
    Positional args: filepath of a csv file, a label for the key of dictionary read in
    Kwargs: title for the histogram, image name for the graph image saved"""
    
    entries = list()
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=",")
        # convert value from string to a float
        for entry in reader:
            if entry["label"] == label:
                entry[key] = float(entry[key])
                entries.append(entry)

    length = list()
    for entry in entries:
        length.append(entry[key])

    sns.distplot(length, kde=True, axlabel="Length")
    plt.title(title)
    plt.savefig(image_name)
    plt.close()
    
    return

if not os.path.exists('../visualizations'):
    os.mkdir("../visualizations")
    
create_histogram("../stats_files/test_stats.csv", key ="char_length", label = "P",
                 title="Char Length Distribution - Positive Data", image_name="../visualizations/char_length-POSITIVE.png")
