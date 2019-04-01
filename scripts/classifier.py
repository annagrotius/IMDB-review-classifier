# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:09:05 2019

@author: annag
"""
import csv
from utils import create_csv
import os

def get_features_from_csv(filepath):
    """
    Opens a csv file and reads its contents with DictReader. Output a list of 
    dictionaries where each dictionary is a row from the csv file.
    """
    entries = []
    with open(filepath) as infile:
        reader = csv.DictReader(infile, delimiter = ',')
        for entry in reader:
            entries.append(entry)
            
    return entries


def get_model_values(entries):
    """
    Input is a list of dictionaries.
    Outputs 2 dictionaries with values that serve
    as the classifier model.
    """
    pos_model = dict()
    neg_model = dict()
    for entry in entries:
        if entry['label'] == 'P':
            # re-assign each dict value to be an int or float (originally a string)
            pos_model['review_length'] = float(entry['review_length'])
            pos_model['avg_word_length'] = float(entry['avg_word_length'])
            pos_model['char_length'] = float(entry['char_length'])
        else:
            neg_model['review_length'] = float(entry['review_length'])
            neg_model['avg_word_length'] = float(entry['avg_word_length'])
            neg_model['char_length'] = float(entry['char_length'])

    return(pos_model, neg_model)
    

def get_file_values(entries):
    """
    Input is a list of dictionaries which contain data from a csv file.
    Output is a list of dictionaries with the same data but now in form that is 
    easy to manipulate (Returns a dict type rather than OrderedDict type). 
    """
    all_file_values = []
    for values in entries:
        file_values = dict()
        file_values['file'] = values['file']
        file_values['label'] = values['label']
        file_values['review_length'] = float(values['review_length'])
        file_values['avg_word_length'] = float(values['avg_word_length'])
        file_values['char_length'] = float(values['char_length'])
        all_file_values.append(file_values)
    
    return(all_file_values)
    

def get_dist_from_model(model, file_values):
    """
    For each file, gets its distance from the positive and negative model.
    Input is the model values and the file's dictionary of values.
    Output is the distance.
    """
    # gets model values
    feat1model = model['review_length']
    feat2model = model['avg_word_length']
    feat3model = model['char_length']
    # weights for classfication formula
    weights = [1,1,1]
    # gets file values
    feat1test = file_values['review_length']
    feat2test = file_values['avg_word_length']
    feat3test = file_values['char_length']  
    # distance classification formula
    distance = abs(feat1model - feat1test) * weights[0] \
            + abs(feat2model - feat2test) * weights[1] + abs(feat3model - feat3test) * weights[2]

    return(distance)
    
    
def get_classification(neg_dist, pos_dist):
    """
    Input is the file's distance from the negative and positive models.
    Ouput is a string that says whether its classification is positive or negative.
    """
    classification = min(neg_dist, pos_dist)
    if classification == neg_dist:
        result = "N"
    else:
        result = "P"
        
    return result


def determine_accuracy(csv_accuracy_file):
    """Reads in the predictions from a csv file and determines their accuracy."""
    prediction_entries = []
    with open(csv_accuracy_file, "r") as accuracy_file:
        reader = csv.DictReader(accuracy_file, delimiter=',')
        for row in reader:
            row['file'] = row['file']
            row['label'] = row['label']
            row['prediction'] = row['prediction']
            prediction_entries.append(row)

    files_classified = 0
    classified_correct = 0
    for prediction_dict in prediction_entries:
        files_classified += 1
        if prediction_dict["label"] == prediction_dict["prediction"]:
            classified_correct += 1
    accuracy = (classified_correct/files_classified)*100
    
    return files_classified, classified_correct, accuracy

    
def main():
    
    if not os.path.exists('../predictions'):
        os.mkdir("../predictions")
        
    aggregate_data = get_features_from_csv("../stats_files/aggregated_stats.csv")
    run_train_files = get_features_from_csv("../stats_files/train_stats.csv")
    run_valid_files = get_features_from_csv("../stats_files/valid_stats.csv")
    run_test_files = get_features_from_csv("../stats_files/test_stats.csv")
    
    pos_model, neg_model = get_model_values(aggregate_data)
    train_values = get_file_values(run_train_files)
    valid_values = get_file_values(run_valid_files)
    test_values = get_file_values(run_test_files)
    
    train_outputs = []
    for file in train_values:
        pos_dist = get_dist_from_model(pos_model, file)
        neg_dist = get_dist_from_model(neg_model, file)
        classification = get_classification(neg_dist, pos_dist)
        
        file_output = dict()
        file_output['file'] = file['file']
        file_output['label'] = file['label']
        file_output['prediction'] = classification
        train_outputs.append(file_output)
    
    create_csv(train_outputs, "../predictions/train_data_predictions.csv")
    amount_files_tested, classified_correct, accuracy = determine_accuracy("../predictions/train_data_predictions.csv")
    print("Number of files processed:", amount_files_tested)
    print("Number classified correct:", classified_correct)
    print(f"Accuracy: {round(accuracy,2)}%")
    
    valid_outputs = []
    for file in valid_values:
        pos_dist = get_dist_from_model(pos_model, file)
        neg_dist = get_dist_from_model(neg_model, file)
        classification = get_classification(neg_dist, pos_dist)
        
        file_output = dict()
        file_output['file'] = file['file']
        file_output['label'] = file['label']
        file_output['prediction'] = classification
        valid_outputs.append(file_output)
    
    create_csv(valid_outputs, "../predictions/validation_data_predictions.csv")
    amount_files_tested, classified_correct, accuracy = determine_accuracy("../predictions/validation_data_predictions.csv")
    print("Number of files processed:", amount_files_tested)
    print("Number classified correct:", classified_correct)
    print(f"Accuracy: {round(accuracy,2)}%")

    test_outputs = []
    for file in test_values:
        pos_dist = get_dist_from_model(pos_model, file)
        neg_dist = get_dist_from_model(neg_model, file)
        classification = get_classification(neg_dist, pos_dist)
        
        file_output = dict()
        file_output['file'] = file['file']
        file_output['label'] = file['label']
        file_output['prediction'] = classification
        test_outputs.append(file_output)
    
    create_csv(test_outputs, "../predictions/test_data_predictions.csv")    
    amount_files_tested, classified_correct, accuracy = determine_accuracy("../predictions/test_data_predictions.csv")
    print("Number of files processed:", amount_files_tested)
    print("Number classified correct:", classified_correct)
    print(f"Accuracy: {round(accuracy,2)}%")
    
        
    
if __name__ == '__main__':
    main()


