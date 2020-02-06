### FUNCTION 1: Metric Dictionary ###

### FUNCTION 2: Five Number Summary ###

### FUNCTION 3: Date Parser ###

### FUNCTION 4: Hashtag & Municipality Extractor ###

def extract_municipality_hashtags(df):
    """
    This function takes in a pandas dataframe of tweets and
    extracts municipalities from a dictionary of municipalities.
    Hashtags are also extracted and returned as a list.
    Municipalities and hashtags are added as new columns and
    the modified dataframe is returned.
    """
    new_data = df
    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}
    municipalities_list = []
    hashtags_list = []
    for row in new_data['Tweets']:
        row = row.replace(":","")
        #Extract municipalities
        municipalities = []
        [municipalities.append(municipality_dict[word]) for word in row.split() if word in municipality_dict]
        municipalities_list.append(municipalities)
        #Extract hashtags
        hashtags = []
        [hashtags.append(word.lower()) for word in row.split() if word[0] == ("#")]
        hashtags_list.append(hashtags)
    #Add municipality column
    new_data['municipality'] = municipalities_list
    new_data['municipality'] = new_data['municipality'].apply(lambda entry: np.nan if (type(entry) == list and len(entry) == 0) else entry)
    new_data['municipality'] = new_data['municipality'].apply(lambda entry: ''.join(entry) if (type(entry) == list and len(entry) == 1) else entry)
    #Add hashtags column
    new_data['hashtags'] = hashtags_list
    new_data['hashtags'] = new_data['hashtags'].apply(lambda entry: np.nan if (type(entry) == list and len(entry) == 0) else entry)
    return new_data

### FUNCTION 5: Number Of Tweets Per Day ###

### FUNCTION 6: Word Splitter ###

### FUNCTION 7: Stop Word Remover ###
