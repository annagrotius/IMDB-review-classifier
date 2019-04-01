# -*- coding: utf-8 -*-
"""
Script that contains functions for extracting statistics of certain features and storing the data 
on a csv file. 
"""

import read_and_process as rp
from utils import combine_dirs
from utils import create_csv
import os    
            

def extract_pos(token_and_pos, part_of_speech="ADJ"):
    """
    Takes a list with tuples of (word, pos) as positional argument and returns a list of the words
    that are of a specific pos. Takes a keyword argument with a default "ADJ".
    """
    specific_pos_list = []
    for word, pos in token_and_pos:
        if pos == part_of_speech:
            specific_pos_list.append(word)
    
    return specific_pos_list


def get_review_length(tokens):
    """
    Calculates the length of tokens in a review. Takes a list of tokens as
    a positional argument.
    """
    total_length = len(tokens)
    
    return total_length


def get_punct_count(text, punct = "."):
    """
    Count the amount of a specified punctuation mark. 
    Arg: Text content of review file.
    Kwarg: punctuation mark to count.
    """
    punct_count = 0
    char_count = 0
    for char in text:
        char_count += 1
        if char == punct:
            punct_count += 1
    count_normalized = round((punct_count/char_count),3)
    
    return(count_normalized)


def get_avg_word_length(tokens):
    """
    Computes the average word length in a text.
    Takes a sequence of tokens as an argument.
    """
    total_tokens = len(tokens)
    token_lengths_sum = 0
    for token in tokens:
        word = token.text
        word_length = len(word)
        token_lengths_sum += word_length
    avg_word_length = round(token_lengths_sum/total_tokens,3)
    
    return(avg_word_length)
    

def get_goldlabel(filepath):
    """
    Determines gold label of file. Takes a filepath as argument.
    """
    if "pos" in filepath:
        return "P"
    else:
        return "N"
    
    
def count_characters(tokens):
    """
    Counts the number of characters in a review. 
    Takes a doc as input and returns an int. 
    """
    chars = 0
    tokens_text = tokens.text
    for char in tokens_text:
        chars += 1
    
    return chars
    

def get_ttr(tokens):
    """
    calculates the token-type ration in a review based on the 
    """
    types_in_review = set()
    tokens_in_review = []
    for token in tokens:
        if token.text.isalpha():
            types_in_review.add(token.text)
            tokens_in_review.append(token)
    ttr = round(len(types_in_review)/len(tokens_in_review), 3)
    
    return ttr

    
def extract_features(file):
    """
    Creates a dictionary to store the stats for one review file. Dictionary will be
    useful when writing stats data on a csv file. Takes a filepath as arg.
    """
    # get all the preprocessed data necessary for extracting features
    file_content, tokens, tokens_clean, lemma_and_pos = rp.preprocess(file)
    review_length = get_review_length(tokens)
    avg_word_length = get_avg_word_length(tokens)
    adjs_in_review = extract_pos(lemma_and_pos)
    char_length = count_characters(tokens)
    verbs_in_review = extract_pos(lemma_and_pos, part_of_speech="VERB")
    nouns_in_review = extract_pos(lemma_and_pos, part_of_speech="NOUN")
    periods = get_punct_count(file_content)
    exclamations = get_punct_count(file_content, punct = "!")
    questions = get_punct_count(file_content, punct = "?")
    ttr = get_ttr(tokens)
    # write the stats into a dictionary                        
    dictionary_with_stats = dict()
    dictionary_with_stats["file"] = os.path.basename(file)
    dictionary_with_stats["label"] = get_goldlabel(file)
    dictionary_with_stats["review_length"] = review_length
    dictionary_with_stats["avg_word_length"] = avg_word_length
    dictionary_with_stats["char_length"] = char_length
    # normalize pos word counts
    dictionary_with_stats["adjs"] = round(len(adjs_in_review)/review_length, 3)
    dictionary_with_stats["verbs"] = round(len(verbs_in_review)/review_length,3)
    dictionary_with_stats["nouns"] = round(len(nouns_in_review)/review_length,3)
    dictionary_with_stats["periods"] = periods
    dictionary_with_stats["exclamations"] = exclamations
    dictionary_with_stats["questions"] = questions
    dictionary_with_stats["ttr"] = ttr
    
    return(dictionary_with_stats)
    

def aggregate_stats(filepath, label = "P"):
    """
    Aggregates the data from a csv file by label (P or N). Returns a dict of the aggregated
    computed stats. 
    """
    # Open file and read its data. Make a list of data for each row
    # in the csv file (for each review file). 
    stats_data = []
    with open(filepath, "r", encoding = "utf-8") as stats_file:
        data = stats_file.read()
        rows = data.split("\n")   
    for row in rows:
        cols = row.split(',')
        stats_data.append(cols)
      
    # create list to store data file rows corresponding to the label desired
    data_to_aggregate = []
    # get the data of the desired label. Noticed the last list in stats data is empty, therefore
    # ending for loop before the last element.
    for file_stats in stats_data[:-1]: 
        if label == file_stats[1]:
            data_to_aggregate.append(file_stats)
    
    # create a dict for the values to aggregate
    aggregated_stats = {}
    aggregated_stats["label"] = label
    aggregated_stats["review_length"] = []
    aggregated_stats["avg_word_length"] = []
    aggregated_stats["char_length"] = []
    aggregated_stats["adjs"] = []
    aggregated_stats["verbs"] = []
    aggregated_stats["nouns"] = []
    aggregated_stats["periods"] = []
    aggregated_stats["exclamations"] = []
    aggregated_stats["questions"] = []
    aggregated_stats["ttr"] = []
    
    # add the respective data value to each dict key
    for data in data_to_aggregate:
        aggregated_stats["review_length"].append(int(data[2]))
        aggregated_stats["avg_word_length"].append(float(data[3]))
        aggregated_stats["char_length"].append(int(data[4]))
        aggregated_stats["adjs"].append(float(data[5]))
        aggregated_stats["verbs"].append(float(data[6]))
        aggregated_stats["nouns"].append(float(data[7]))
        aggregated_stats["periods"].append(float(data[8]))
        aggregated_stats["exclamations"].append(float(data[9]))
        aggregated_stats["questions"].append(float(data[10]))
        aggregated_stats["ttr"].append(float(data[11]))
    
    # Compute the average of all the values in the dictionary keys. Re-assign each key the average value.
    for key, value in aggregated_stats.items():
        # the first value of the dict is the label (A str type) so skip this
        if type(value) != str:
            key_list = value
            aggregated_stats[key] = round((sum(key_list)/len(key_list)), 3)
        
    return(aggregated_stats)        


def create_stats_files(filepaths, outfile):
    """
    Takes a list of filepaths as input. 
    Extract the statistics from the specified filepaths and writes them to a csv file.
    """
    training_instance_dicts = []
    i = 0
    for file in filepaths:
        instance_dict = extract_features(file)
        training_instance_dicts.append(instance_dict)
        i+=1
        print(i)
    create_csv(training_instance_dicts, outfile)    
    
    return
   
    
def main():
        
    validation_filepaths = combine_dirs("../data/train/pos", "../data/train/neg")
#    training_filepaths = combine_dirs("../data/valid/pos_valid", "../data/valid/neg_valid")
#    testing_filepaths = combine_dirs("../data/test/pos", "../data/test/neg")
    
    # create directory to store the csv files if one does not already exist
    if not os.path.exists('../stats_files'):
        os.mkdir('../stats_files')
    create_stats_files(validation_filepaths, "../stats_files/valid_stats.csv")
#    create_stats_files(training_filepaths, "../stats_files/train_stats.csv")
#    create_stats_files(testing_filepaths, "../stats_files/test_stats.csv")
    
    # get the aggregated statistics for positive and negative files. store these on a csv file.
    aggregated_stats = []
    pos_avg_stats = aggregate_stats("../stats_files/train_stats.csv")
    neg_avg_stats = aggregate_stats("../stats_files/train_stats.csv", label = "N")
    aggregated_stats.append(pos_avg_stats)
    aggregated_stats.append(neg_avg_stats)
    create_csv(aggregated_stats, "../stats_files/aggregated_stats.csv")
    
    
    
if __name__ == '__main__':
    main()