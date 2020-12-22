# Extract Twitter Data
Extract Tweets or Followers and Friends of users from Twitter

## extractTweetsGivenIds.py 
Uses the file sampleTweetIds.txt to read the tweet ids and extracts tweet object for the given tweet id.


## extractFriendsFollowers.py 
Uses the file sampleUserIds.txt to read the User ids and extracts followers for the given users.

Both the code files respect the Twitter API policy on number of queries made to the API.
The script makes queries using the API for the allowed number of queries and then halts for the required duration and starts quering again. 
