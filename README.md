# IMDB-review-classifier
Python for Text Analysis final project

*This binary classifier for IMDB reviews is made by Anna de Groot and Simos Fousekis as a 
part of the final assignment for the course Python for Text Analysis, taught at the Vrije 
Universiteit Amsterdam in the [Humanities Research Master: Linguistics](http://masters.vu.nl/en/programmes/linguistics-research/index.aspx) (track [Human Language Technology](http://www.cltl.nl/teaching/human-language-technology/)).*

## Data
The dataset used is called the 'Large Movie Review Dataset' by Maas et al. (2011) and it can be downloaded
[here](http://ai.stanford.edu/~amaas/data/sentiment/). The data set was already split into negative 
movie review and positive movie review files, which are based on the rating score (from 1-10) that they 
were already given. The enitre data set contains 50,000 movie review text files-- 25,000 files for training and 25,000 for testing set. Each set has an equal number of positive and negative movie review files.

For our project, we use 2,500 of the training files (1,250 from negative training set, 1,250 from positive
training set) as a validation set. Please follow the following steps to prepare the data run the following the following line in 
your terminal to create a directory for the validation set. 

Before running the system, following the steps below to prepare the data. 

1. **Download the dataset** [here](http://ai.stanford.edu/~amaas/data/sentiment/) and save it in a folder called `data'. 
Place this folder in the folder where the rest of this project's files will be held. 

2. Since the original downloaded version of the dataset does not contain the training set, run the 
script *split_data.py* to organize the data, or copy and paste the following line into your terminal.

```
$ python split_data.py
```

Now there should be a folder in your working directory called `data/` with 3 top-level directories. The structure of the 
data should look like:

```
data/
  train/
    pos/
    neg/
test/
    pos/
    neg/
valid/
    pos_valid/
    neg_valid/
```   

## Necessary Python Libraries

In order to run this code, you will first need to download the packages/modules below.
Run the following lines in your terminal:

> Installing SpaCy and the necessary language model

```
$ conda install -c conda-forge spacy
```

```
$ python -m spacy download en
```


## Running the Code

After following the steps above, find the necessary files in the folder [scripts/] to run the system. A description of each script 
can be found at the top of each file. 

There are 2 options to run the system. Refer to the steps below.

#### Option 1

Run the script *main.py*. Optionally, copy and paste the following line into your terminal.
```
$ python main.py
```

#### Option 2

Run the scripts in the following order, either manually or copying and pasting the following lines into your 
terminal.

> run *feature_extraction.py*
```
$ python feature_extraction.py
```
While this script runs, a counter is printed to see how many files have been processed so far. 
After the script is done running, a new folder called [stats_file/] will exist and it will contain 4 csv files.

> run visual

> run *classifier.py*
```
$ python classifier.py
```
Once this script finishes, the amount of files processed, the files classified correctly, and the accuracy will be printed in your console or terminal. Additionally, a new folder called [predictions/] will exist in the current working directory where csv files that store the system's predictions can be found. 



