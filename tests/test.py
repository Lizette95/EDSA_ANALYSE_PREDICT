### before running the test we need the twitter_df dataframe to be run first ###
### FUNCTION 1: Metric Dictionary ###

from module import dictionary_of_metrics
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
assert dictionary_of_metrics(items) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'variance': 108160153.17,
                                   'standard deviation': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}, 'incorrect'

### FUNCTION 2: Five Number Summary ###

from module import five_num_summ
# Do some tests here

### FUNCTION 3: Date Parser ###

from module import date_parser
assert date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'
assert date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20'], 'incorrect'

### FUNCTION 4: Hashtag & Municipality Extractor ###

from module import extract_municipality_hashtags
assert extract_municipality_hashtags(twitter_df.copy()).loc[4, "hashtags"] == ['#eskomfreestate', '#mediastatement'], 'incorrect'
assert extract_municipality_hashtags(twitter_df.copy()).loc[5, "municipality"] == "Johannesburg", 'incorrect'

### FUNCTION 5: Number Of Tweets Per Day ###

from module import number_of_tweets_per_day
assert number_of_tweets_per_day(twitter_df.copy()).iloc[0] == 18, 'incorrect'
assert number_of_tweets_per_day(twitter_df.copy()).iloc[1] == 11, 'incorrect'

### FUNCTION 6: Word Splitter ###

from module import word_spliter
assert word_splitter(twitter_df.copy()).loc[0, "Split Tweets"] == ['@bongadlulane', 'please', 'send', 'an', 'email', 'to','mediadesk@eskom.co.za'], 'incorrect'


### FUNCTION 7: Stop Word Remover ###

from module import stop_words_http_remover
assert stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za'], 'incorrect'
assert stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit'], 'incorrect'
