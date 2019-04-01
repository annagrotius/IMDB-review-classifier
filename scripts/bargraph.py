# -*- coding: utf-8 -*-
"""
Creates different visualizations from the data in the csv file aggregated_stats.csv.
All images saved in the folder [visualizations/].
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def make_bargraph(bar_values, x_vals, title = None, image_name = None, xlabel = None, ylabel = None):
    # Create x-axis
    ax = np.arange(len(x_vals))
    plt.xticks(ax, x_vals)
    # plot the bars
    i = 0
    for vals in bar_values:
        plt.bar(ax+i, vals[1:], width=0.5, label= vals[0])
        i+=0.20

    # Create y-axis
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # title
    plt.title(title)
    # legend
    plt.legend()
    plt.savefig(image_name)
    plt.close()

    return


# Run the function
    
if not os.path.exists('../visualizations'):
    os.mkdir("../visualizations")
    
with open("../stats_files/aggregated_stats.csv", "r", encoding = "utf-8") as infile:
    data = infile.read()
    rows = data.split("\n")  
 
# get the values for the graphs
stats = []   
for row in rows:
    cols = row.split(',')
    stats.append(cols)
    
pos_values = stats[1] 
neg_values = stats[2]
  
# define variables and then make a bargraph of the punctuation stats  
punct = ["period (.)", "exclamation (!)", "question (?)"]
punct_vals = []
pos_punct = [pos_values[0], float(pos_values[7]), float(pos_values[8]), float(pos_values[9])]
neg_punct = [neg_values[0], float(neg_values[7]), float(neg_values[8]), float(neg_values[9])]
punct_vals.append(pos_punct)
punct_vals.append(neg_punct)
 
make_bargraph(punct_vals, punct, xlabel = "punctuation", title = "Number of Punctuation Marks", \
              image_name = "../visualizations/avg_punct.png", ylabel = "average amount")


# define variables and then make a bargraph of the punctuation stats  
words = ["Adjectives", "Verbs", "Nouns"]
word_vals = []
pos_words = [pos_values[0], float(pos_values[4]), float(pos_values[5]), float(pos_values[6])]
neg_words = [neg_values[0], float(neg_values[4]), float(neg_values[5]), float(neg_values[6])]
word_vals.append(pos_words)
word_vals.append(neg_words)

make_bargraph(word_vals, words, ylabel = "average amount", title = "Average Amount of Words and POS-words",\
              image_name = "../visualizations/avg_words.png" )