from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'LE4zQRSrwCntbj6nRCCXyYsH7'
csecret = 'UVhoPayrcXhA2hxLT2pT64VYu2NiBwbeakGPT29MIu8NOIhDMl'
atoken = '1217287995654582272-a8sfnSdtZCaVjr7INa3BeZky16jcmr'
asecret = 'FuJNnNB8QfKRER7D2VsTReDuaSxHdcAzBkJY6EVJfIoGZ'

class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])