# Import the Twython Class
#https://stackabuse.com/accessing-the-twitter-api-with-python/   " for the future and live streaming tweets to synca nd
# below code also "
from twython import Twython
import pandas as pd
import json

# generate credentials into json file.
# credentials = {}
# credentials['CONSUMER_KEY'] = " "
# credentials['CONSUMER_SECRET'] = " "
# credentials['ACCESS_TOKEN'] = " "
# credentials['ACCESS_SECRET'] = " "

# with open("twitter_Credentials.json", "w") as file:
#     json.dump(credentials, file)

# Load credentials from json file
with open("twitter_Credentials.json", "r") as file:
    creds = json.load(file)
# Instantiate an object
python_tweets = Twython(creds["CONSUMER_KEY"], creds["CONSUMER_SECRET"])

# search tweets
search_terms = ['developing economy','technology poverty']

for query_term in search_terms:
    dict_ = {'id': [], 'screen_name': [], 'date': [], 'followers': [], 'listed': [], 'retweet': [],
             'inreplyto': [], 'friends_count': [], 'text': [], 'favorite_count': [], 'location': []}

    # Create our query
    query = {'q': f"{query_term}+and -filter:retweets",
             'count': 100,
             'lang': 'en',

             }
    for status in python_tweets.search(**query)['statuses']:
        dict_['id'].append(status['user']['id'])
        dict_['screen_name'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        dict_['followers'].append(status['user']['followers_count'])
        dict_['listed'].append(status['user']['listed_count'])
        dict_['retweet'].append(status['retweet_count'])
        dict_['inreplyto'].append(status['in_reply_to_screen_name'])
        dict_['friends_count'].append(status['user']['friends_count'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])
        dict_['location'].append(status['user']['location'])

    df = pd.DataFrame(dict_)
    df.sort_values(by='date',inplace=True, ascending=False)
    print(df)
    df.to_csv(f"{query_term}_tweets_csv.csv",index_label='index_numbers')