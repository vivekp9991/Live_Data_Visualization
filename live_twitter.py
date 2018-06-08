from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import json
import csv
#Variables that contains the user credentials to access Twitter API
access_token = "xxxx"
access_token_secret = "xxxx"
consumer_key = "xxxx"
consumer_secret = "xxxx"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):



    def on_status(self, status):
        self.get_tweet(status)

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

    def on_error(self, status):
      print (status)

    @staticmethod
    def get_tweet(tweet):
       # print "000000000000000000000000000000000000"
        if tweet.coordinates is not None:
            print ("yes comming...", tweet.coordinates)
            x, y = m(tweet.coordinates['coordinates'][0], tweet.coordinates['coordinates'][1])
            print (x, y)
            # print m(6117158.96328, 18969400.7768, inverse=True)
            try:
                m.plot(x, y, 'ro', markersize=2)
                plt.draw()

            except Exception as e:
               print (e)
        else:
            print  ("no dict... key found...")


if __name__ == '__main__':

    # Size of the map
    fig = plt.figure(figsize=(18, 4), dpi=250)

    # Set a title
    plt.title("Tweet's around the world")

    # Declare map projection, size and resolution
    m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='coral',lake_color='aqua')
    # draw parallels and meridians.
    m.drawparallels(np.arange(-90.,91.,30.))
    m.drawmeridians(np.arange(-180.,181.,60.))
    m.drawmapboundary(fill_color='aqua')

    plt.title("Twitter around the world")
#This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(locations=[-180, -90, 180, 90], async=True)
    plt.show()