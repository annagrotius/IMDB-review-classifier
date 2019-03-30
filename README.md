# IMDB-review-classifier
Python for Text Analysis final project

*This binary classifier for IMDB reviews is made by Anna de Groot and Simos Fousekis as a 
part of the final assignment for the course Python for Text Analysis, taught at the Vrije 
Universiteit Amsterdam in the [Humanities Research Master: Linguistics](http://masters.vu.nl/en/programmes/linguistics-research/index.aspx) (track [Human Language Technology](http://www.cltl.nl/teaching/human-language-technology/)).*

data
where it is from
download from there
run the script to create train data

## Data
The dataset used is called the 'Large Movie Review Dataset' by Maas et al. (2011) and it can be downloaded
[here](http://ai.stanford.edu/~amaas/data/sentiment/). The data set was already split into negative 
movie review and positive movie review files, which are based on the rating score (from 1-10) they 
were given. The enitre data set contains 50,000 movie review text files-- 25,000 files for training and 25,000 for testing set. Each set has an equal number of positive
and negative movie review files.

For our project, we use 2,500 of the training files (1,250 from negative training set, 1,2500 from positive
training set) as a validation set. After downloading the data from the link above into the directory 
where the rest of this project's scripts are on your computer, run the following the following line in 
your terminal to create a directory for the validation set. 

Before running the system, following the steps below to prepare the data. 

1. **Download the dataset** [here](http://ai.stanford.edu/~amaas/data/sentiment/) and save it in a directory
on your computer called `IMDB-review-classifier` . 

2. Since the original downloaded version of the dataset does not contain the training set, run the following
script to organize the data. 

```python
python split_data.py
```

Now there should be a folder in your working directory called `data/` with 3 top-level directories. The structure of the 
data should look like:

```
data/
  train/
    pos/
    neg/
  valid/
    pos_valid/
    neg_valid/
  test/
    pos/
    neg/
```   

## Necessary Python Libraries

In order to run this code, you will first need to download the packages/modules below.
Run the following lines in your terminal:

>> Installing SpaCy and the necessary language model

```
$ conda install -c conda-forge spacy
```

```
$ python -m spacy download en
```

## Running the Code

Refer to the folder `scripts\` to run the system. 

