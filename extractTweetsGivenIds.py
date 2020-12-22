"""
"""
import sys
import tweepy
import time
from random import randint

from keys import keys #keep keys in separate file, keys.py

# consumer_key
# consumer_secret
# access_key
# access_secret

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_key']
ACCESS_TOKEN_SECRET = keys['access_secret']


setOfTweetIds = []

tweetIdFile = open("sampleTweetIds.txt", "r")
for line in tweetIdFile:
	setOfTweetIds.append(line.strip())
tweetIdFile.close()

tweetsOutputFile = open("extractedTweets.txt", "w")

# setOfTweetIds = [1039503262561517570, 1039274409528315904, 1039174695348854784, 1038550492513820672, 1039677499037372416, 1039559314590101505, 1039544201615171586, 1039537853125074946, 1038916252050354176, 1038876440262004736, 1038182678938431488, 1038136123875373057, 1037739757479055365, 1037737244273127425, 1037705822342668288, 1037705750926290945, 1037465429235716096, 1037436475774840832, 1039929895202250752, 1039929230681944065, 1039927561160196096, 1039926825999314944, 1039926767912460293]

writeHeader = "tweetId~~~~created_at~~~~userId~~~~full_text~~~~user_screen_name~~~~user_location~~~~user_description~~~~ users_followers_count~~~~users_friends_count~~~~user_created_at\n"

tweetsOutputFile.write(writeHeader)
tweetsOutputFile.flush()

totalCount = 0
successCount = 0

for tweetId in setOfTweetIds:

	try:
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

		tweetObj = api.get_status(tweetId, tweet_mode="extended")
		# print(tweetObj)

		reqdFlds = []
		tweetId = str(tweetId)
		tweetCreatedAt = tweetObj.created_at
		tweetUserId = tweetObj.user.id
		tweetText = tweetObj.full_text
		tweetUserName = tweetObj.user.name
		tweetUserScreenName = tweetObj.user.screen_name
		tweetUserLocation = tweetObj.user.location
		tweetUserDescription = tweetObj.user.description
		tweetUserFollowersCount = tweetObj.user.followers_count
		tweetUserFriendsCount = tweetObj.user.friends_count
		tweetUserCreatedAt = tweetObj.user.created_at

		reqdFlds = [tweetId, tweetCreatedAt, tweetUserId, tweetText, tweetUserName, tweetUserScreenName, tweetUserLocation, tweetUserDescription, tweetUserFollowersCount, tweetUserFriendsCount, tweetUserCreatedAt]
		# print(reqdFlds)

		writeStr = "~~~~".join([str(x) for x in reqdFlds]) + "\n"
		print(writeStr)
		tweetsOutputFile.write(writeStr)
		tweetsOutputFile.flush()

		successCount += 1

	except tweepy.TweepError as e:
		print("Tweepy.TweepError -- ", e.reason)

	except:
		e = sys.exc_info()[0]
		print("Error: %s" % e)

	totalCount += 1

	if totalCount % 10000 == 0 :
		print("Total Queries = ", totalCount, " Successful Queries = ", successCount)


tweetsOutputFile.close()