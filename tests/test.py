### Import packages, variables and test data ###

import pandas as pd
import numpy as np
from data_analyser import metrics_calculator as mc
ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)
for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()
# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()
# dates for twitter tweets
dates = twitter_df['Date'].to_list()
# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

items = [39660.0,
         36024.0,
         32127.0,
         39488.0,
         18422.0,
         23532.0,
         8842.0,
         37416.0,
         16156.0,
         18730.0,
         19261.0,
         25275.0]

### FUNCTION 1: Metric Dictionary ###

assert mc.dictionary_of_metrics(items) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'variance': 108160153.17,
                                   'standard deviation': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}, 'incorrect'

### FUNCTION 2: Five Number Summary ###

assert mc.five_num_summary(gauteng) == {'max': 39660.0,
                           'median': 24403.5,
                           'min': 8842.0,
                           'q1': 18422.5,
                           'q3': 36024.5}, 'incorrect'

### FUNCTION 3: Date Parser ###

assert mc.date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'
assert mc.date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20'], 'incorrect'

### FUNCTION 4: Hashtag & Municipality Extractor ###

assert mc.extract_municipality_hashtags(twitter_df.copy()).loc[4, "hashtags"] == ['#eskomfreestate', '#mediastatement'], 'incorrect'
assert mc.extract_municipality_hashtags(twitter_df.copy()).loc[5, "municipality"] == "Johannesburg", 'incorrect'

### FUNCTION 5: Number Of Tweets Per Day ###

assert mc.number_of_tweets_per_day(twitter_df.copy()).iloc[0] == 18, 'incorrect'
assert mc.number_of_tweets_per_day(twitter_df.copy()).iloc[1] == 11, 'incorrect'

### FUNCTION 6: Word Splitter ###

assert mc.word_splitter(twitter_df.copy()).loc[0, "Split Tweets"] == ['@bongadlulane', 'please', 'send', 'an', 'email', 'to','mediadesk@eskom.co.za'], 'incorrect'


### FUNCTION 7: Stop Word Remover ###

assert mc.stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za'], 'incorrect'
assert mc.stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit'], 'incorrect'
