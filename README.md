# EDSA_ANALYSE_PREDICT
Building Functions to Calculate Metrics using Data

FUNCTION 1: Metric Dictionary

The function takes in a list of integers and returns a dictionary of the mean, median, variance, standard deviation, min and max. All answers are rounded to the second decimal.

FUNCTION 2: Five Number Summary

FUNCTION 3: Date Parser

The function takes a list of strings as input.
Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'.
The function returns a list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format.

FUNCTION 4: Hashtag & Municipality Extractor

This function takes in a pandas dataframe of tweets and
extracts municipalities with a user-defined dictionary of municipalities.
Hashtags are also extracted and returned as a list.
Municipalities and hashtags are added as new columns and
the modified dataframe is returned.

FUNCTION 5: Number Of Tweets Per Day

This function takes in a pandas dataframe of tweets and
returns a new dataframe, grouped by day, with the number of tweets
for that day. The date column is set as the index of the new dataframe.

FUNCTION 6: Word Splitter

Word Splitter is a function which splits the sentences
in a dataframe's column into a list of the separate words.
This function takes in a pandas dataframe as an input and
returns the modified dataframe.

FUNCTION 7: Stop Word Remover

Stop Words Remover is a function which removes english stop words from tweets.
This function takes in a pandas dataframe as an input and
returns the modified dataframe.
