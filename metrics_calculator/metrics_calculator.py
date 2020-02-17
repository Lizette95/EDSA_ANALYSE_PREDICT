import pandas as pd
import numpy as np

### FUNCTION 1: Metric Dictionary ###

def dictionary_of_metrics(items):
    """
    This function calculates metrics from Eskom data
    and outputs the metrics as a dictionary of a
    5 number summary i.e. mean, median, variance,
    standard deviation, minimum and maximum.
    """
    add_items = sum(items)
    items_len = len(items)
    #Mean
    mean = sum(items) / len(items)
    #Median
    sorted_items = sorted(items)
    index = (items_len - 1) // 2
    if (items_len %2 == 0):
        median = (sorted_items[index] + sorted_items[index + 1]) / 2.0
    else:
        median = sorted_items[index]
    #Variance
    i_minus_mean = []
    [i_minus_mean.append(i - float(mean)) for i in items]
    squared_i_minus_mean = [x ** 2 for x in i_minus_mean]
    variance = sum(squared_i_minus_mean) / (items_len - 1)
    #Standard deviation
    standard_dev = variance ** 0.5
    #Min
    min_val = items[0]
    for num in items:
        if min_val > num:
            min_val = num
    #Max
    max_val = items[0]
    for num in items:
        if max_val < num:
            max_val = num
#     #Test with numpy functions
#     mean = np.mean(items)
#     median = np.median(items)
#     variance = np.var(items,ddof=1)
#     standard_dev = np.std(items,ddof=1)
#     min_val = min(items)
#     max_val = max(items)
    #Result
    return {'mean': round(mean,2),
            'median': round(median,2),
            'var': round(variance,2),
            'std': round(standard_dev,2),
            'min': round(min_val,2),
            'max': round(max_val,2)}

### FUNCTION 2: Five Number Summary ###

def five_num_summary(items):
    """This function returns a dictonary of the five(5) number summary"""
    #maximum value
    max_value = np.max(np.array(items))
    #minimum value
    min_value = np.min(np.array(items))
    #median
    median = np.median(np.array(items))
    #Quartile1
    q1 = np.percentile(np.array(items), 25)
    #Quartile3
    q3 = np.percentile(np.array(items), 75)

    return {'min' : round(min_value, 2),
            'q1' : round(q1, 2),
            'median' : round(median, 2),
            'q3' : round(q3, 2),
            'max' : round(max_value, 2)}


### FUNCTION 3: Date Parser ###

def date_parser(dates):
    """Takes in a datetime and outputs date"""
    date = [entry[0:10] for entry in dates]
    return date

### FUNCTION 4: Hashtag & Municipality Extractor ###

def extract_municipality_hashtags(df):
    """
    This function takes in a pandas dataframe of tweets and
    extracts municipalities with a user-defined dictionary of municipalities.
    Hashtags are also extracted and returned as a list.
    Municipalities and hashtags are added as new columns and
    the modified dataframe is returned.
    """
    #Make new dataframe from df
    new_data = df
    municipalities_list = []
    hashtags_list = []
    for row in new_data['Tweets']:
        row = row.replace(":","")
        #Extract municipalities
        municipalities = []
        [municipalities.append(mun_dict[word]) for word in row.split() if word in mun_dict]
        municipalities_list.append(municipalities)
        #Extract hashtags
        hashtags = []
        [hashtags.append(word.lower()) for word in row.split() if word[0] == ("#")]
        hashtags_list.append(hashtags)
    #Add municipality column
    new_data['municipality'] = municipalities_list
    new_data['municipality'] = new_data['municipality'].apply(lambda entry: ''.join(entry) if (type(entry) == list and len(entry) != 0) else np.nan)
    #Add hashtags column
    new_data['hashtags'] = hashtags_list
    new_data['hashtags'] = new_data['hashtags'].apply(lambda entry: np.nan if (type(entry) == list and len(entry) == 0) else entry)
    #Return new dataframe
    return new_data

### FUNCTION 5: Number Of Tweets Per Day ###

def number_of_tweets_per_day(df):
    """
    This function takes in a pandas dataframe of tweets and
    returns a new dataframe, grouped by day, with the number of tweets
    for that day. The date column is set as the index of the new dataframe.
    """
    #Extract date
    df['Dates'] = df.Date.str[0:10]
    #Count number of tweets per day
    count = df['Dates'].value_counts()
    #Make new dataframe and set index
    df_count = pd.DataFrame(count)
    new_df = df_count.reset_index()
    new_df.columns = ['Date', 'Tweets']
    new_df = new_df.sort_values(by=['Date']).set_index('Date')
    #Return new dataframe
    return new_df

### FUNCTION 6: Word Splitter ###

def word_splitter(df):
    """
    Word Splitter is a function which splits the sentences
    in a dataframe's column into a list of the separate words.
    This function takes in a pandas dataframe as an input and
    returns the modified dataframe.
    """
    try:
        # We create a new column in the dataframe with the tweets and make it a list
        df['Split Tweets'] = df['Tweets'].values.tolist()
        # create a new valiable to contain the the list
        Split_tweets = df['Split Tweets']
        # We make sure that the words are lower case and make the list a of lists
        list_of_list = [[i.lower()] for i in Split_tweets]
        # We split the sentence into individual words in the list of lists
        splitting_the_list_of_list = [item[0].split() for item in list_of_list]
        # We put the list of lists into the dataframe column named Split Tweets
        df['Split Tweets'] = splitting_the_list_of_list
        # We return the whole modified dataframe
        return df
        # When a person inputs any other type other than a pandas dataframe they get a typeError
    except TypeError:
        print('incorrect input you must input a dataframe')

### FUNCTION 7: Stop Word Remover ###

def stop_words_remover(df):
    """
    Stop Words Remover is a function which removes english stop words from  tweets.
    This function takes in a pandas dataframe as an input and
    returns the modified dataframe.
    """
    try:
        # this variable take the dictionary of stop words
        stop_w =  stop_words_dict
        # We create a new column in the dataframe with the tweets and make it a list
        df['Without Stop Words'] = df['Tweets'].values.tolist()
        #  create a new valiable to contain the the list
        without_stop_words = df['Without Stop Words']
        # We make sure that the words are lower case and make the list a of lists
        list_of_lists = [[i.lower()] for i in without_stop_words]
        # We split the sentence into individual words in the list of lists
        splitting_the_list_of_lists = [word[0].split() for word in list_of_lists]
        # this variable has the list of lists of individual words of tweets
        list_in_a_list = splitting_the_list_of_lists
        # We create an empty list
        list_without_stop_words = []
        # We loop through the dictionary of stop words
        for k in stop_w:
            stop_words = stop_w[k]
        # We loop through the list of lists to compare with words in the dictionary
        for list1 in list_in_a_list:
            filteredtext = [t for t in list1 if t not in stop_words]
            list_without_stop_words.append(filteredtext)
        # We put the list of list into a pandas dataframe column named Without Stop Words
        df['Without Stop Words'] = list_without_stop_words
        # We return the whole modified dataframe
        return df
        # When a person inputs any other type other than a pandas dataframe they get a typeError
    except TypeError:
        print('incorrect input you must input a dataframe')
