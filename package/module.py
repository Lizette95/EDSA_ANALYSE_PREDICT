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
            'variance': round(variance,2),
            'standard deviation': round(standard_dev,2),
            'min': round(min_val,2),
            'max': round(max_val,2)}

### FUNCTION 2: Five Number Summary ###

### FUNCTION 3: Date Parser ###
def dateparser(dates):
    date = [entry[0:10] for entry in dates]
    return date
### FUNCTION 4: Hashtag & Municipality Extractor ###

def extract_municipality_hashtags(df):
    """
    This function takes in a pandas dataframe of tweets and
    extracts municipalities using a dictionary of municipalities.
    Hashtags are also extracted and returned as a list.
    Municipalities and hashtags are added as new columns and
    the modified dataframe is returned.
    """
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
    for that day. The date colummn is set as the index of the new dataframe.
    """
    df['Dates'] = df.Date.str[0:10]
    count = df['Dates'].value_counts()
    df_count = pd.DataFrame(count)
    new_df = df_count.reset_index()
    new_df.columns = ['Date', 'Tweets']
    new_df = new_df.sort_values(by=['Date']).set_index('Date')
    return new_df

### FUNCTION 6: Word Splitter ###
def word_splitter(df):
    """
    Add docstring
    """
    df['Split Tweets'] = df['Tweets'].values.tolist()
    Split_tweets = df['Split Tweets']#.values.tolist()
    list_of_list = [[i.lower()] for i in Split_tweets]
    splitting_the_list_of_list = [item[0].split() for item in list_of_list]
    df['Split Tweets'] = splitting_the_list_of_list
    return df

### FUNCTION 7: Stop Word Remover ###
def stop_words_remover(df):
    """
    Add docstring
    """
    try:
        stop_w =  stop_words_dict
        df['Without Stop Words'] = df['Tweets'].values.tolist()
        Without_Stop_Words = df['Without Stop Words']
        list_of_lists = [[i.lower()] for i in Without_Stop_Words]
        Splitting_the_list_of_lists = [word[0].split() for word in list_of_lists]
        list_in_a_list = Splitting_the_list_of_lists
        list_without_stop_words = []
        for k in stop_w:
            Stop_Words = stop_w[k]
        for list1 in list_in_a_list:
            filteredtext = [t for t in list1 if t not in Stop_Words]
            list_without_stop_words.append(filteredtext)
        df['Without Stop Words'] = list_without_stop_words
        return df
    except TypeError:
        print('incorrect input you must input a dataframe')
