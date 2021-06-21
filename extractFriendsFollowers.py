"""
Jayesh Choudhari
jayeshchoudhari.github.io
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


# get list of handles...
handlesFilePtr = open("./input/sampleUserIds.txt", "r")

allHandleIds = []
for line in handlesFilePtr:
    flds = line.strip().split()
    allHandleIds.append(flds[0].strip())

handlesFilePtr.close()

# user_id = '984456621417000960'

followersFilePtr = open("./output/extractedFollowers.txt", "w")

idNum = 0

# for user_id in allHandleIds[:2]:
for user_id in allHandleIds:
# for uid in range(len(allHandleIds)):

    # user_id = allHandleIds[uid]

    idNum += 1    
    print("working on user id {} -- {}".format(user_id, str(idNum)))

    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
        # c = tweepy.Cursor(api.followers_ids, id = 'RealDonaldTrump')
        # c = tweepy.Cursor(api.followers_ids, id = 'ladygaga')
        c = tweepy.Cursor(api.friends_ids, id = user_id, count=5000)
        print("type(c)=", type(c))
        ids = []
        lenPages = 0
        
        for page in c.pages():
            ids.append(page)
            lenPages += len(page)


        # ids here is a list of lists...
        # print ids
        print("Number of friends of {} = {} \n\n".format(user_id, str(lenPages)))

        writeStr = str(lenPages) + " " + user_id + " "
        for l in ids:
            writeStr += " ".join([str(fid) for fid in l]) + " "

        writeStr += "\n"    

        # print "ids[0]=", ids[0]
        # print "len(ids[0])=", len(ids[0])
        # print 5/0

        followersFilePtr.write(writeStr)
        followersFilePtr.flush()

        print("Done working on user id {} -- {}".format(user_id, str(idNum)))

    except tweepy.TweepError as e:
        print("tweepy.TweepError=", e.reason)
    except:
        e = sys.exc_info()[0]
        print ("Error: %s" % e)
    #print "error."
    

followersFilePtr.close()
