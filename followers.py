import tweepy

print('Starting...')

# Aquí se deben poner las credenciales de la cuenta
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

myusername = api.me().screen_name
file_name = "last_seen_id.txt"

def follow_users():
    search = ('minimalist', 'painting')
    number_of_tweets = 100
    for tweet in tweepy.Cursor(api.search, search).items(number_of_tweets):
        try:
            api.create_favorite(tweet.id)
            print('@' + tweet.user.screen_name, tweet.text, 'marked as favorite')
            api.create_friendship(screen_name=tweet.user.screen_name)
            print('now following @' + tweet.user.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def stop_following():
    for id in api.friends_ids(myusername):
        api.destroy_friendship(id)
        print('not following ', str(api.get_user(id)))


def unlike_tweets():
    for tweet in tweepy.Cursor(api.favorites, id=api.get_user(myusername).id_str).items():
        api.destroy_favorite(tweet.id)


# follow_users()
# stop_following()
# unlike_tweets()
