# -*- coding: utf-8 -*-
"""
Runs the whole system on train, validation, and test data. 
"""
import os
from feature_extraction import create_stats_files
from feature_extraction import aggregate_stats
import classifier
import utils

# Read, process, extract features, and save to csv files stored in [stats_files/]

# combine all files into their respective directory
validation_filepaths = utils.combine_dirs("../data/valid/pos_valid", "../data/valid/neg_valid")
training_filepaths = utils.combine_dirs("../data/train/pos", "../data/train/neg")
testing_filepaths = utils.combine_dirs("../data/test/pos", "../data/test/neg")

# create directory to store csv files with stats, but first check if it already exists
if not os.path.exists('../stats_files'):
    os.mkdir('../stats_files')
    
# feature extraction and writing to csv 
create_stats_files(training_filepaths, "../stats_files/train_stats.csv")
create_stats_files(validation_filepaths, "../stats_files/valid_stats.csv")
create_stats_files(testing_filepaths, "../stats_files/test_stats.csv")
   
# create a csv file that stores the aggregated statistics from above
aggregated_stats = []
pos_avg_stats = aggregate_stats("../stats_files/valid_stats.csv")
neg_avg_stats = aggregate_stats("../stats_files/valid_stats.csv", label = "N")
aggregated_stats.append(pos_avg_stats)
aggregated_stats.append(neg_avg_stats)
utils.create_csv(aggregated_stats, "../stats_files/aggregated_stats.csv")

# Run classification on files. Predictions written on csv files and stored in [predictions/]
aggregate_data = classifier.get_features_from_csv("../stats_files/aggregated_stats.csv")
run_train_files = classifier.get_features_from("../stats_files/train_stats.csv")
run_valid_files = classifier.get_features_from_csv("../stats_files/valid_stats.csv")
run_test_files = classifier.get_features_from("../stats_files/test_stats.csv")
    
pos_model, neg_model = classifier.get_model_values(aggregate_data)
train_values = classifier.get_file_values(run_train_files)
valid_values = classifier.get_file_values(run_valid_files)
test_values = classifier.get_file_values(run_test_files)
    
    
class_outputs = []
for file in valid_values:
    pos_dist = classifier.get_dist_from_model(pos_model, file)
    neg_dist = classifier.get_dist_from_model(neg_model, file)
    classification = classifier.get_classification(neg_dist, pos_dist)
        
    file_output = dict()
    file_output['file'] = file['file']
    file_output['label'] = file['label']
    file_output['prediction'] = classification
    class_outputs.append(file_output)

# make new folder to hold csv files    
if not os.path.exists('../predictions'):
    os.mkdir("../predictions")
# create csv file to write the predictions
utils.create_csv(class_outputs, "../predictions/validation_data_predictions.csv")
    
amount_files_tested, classified_correct, accuracy = classifier.determine_accuracy("../predictions/validation_data_predictions.csv")
print("Number of files processed:", amount_files_tested)
print("Number classified correct:", classified_correct)
print(f"Accuracy: {round(accuracy,2)}%")