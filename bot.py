import tweepy
import wget;

consumer_key = "enter here"
secret_key = "enter here"

key = "enter here"
secret = "enter here"


auth= tweepy.OAuthHandler(consumer_key, secret_key)
auth.set_access_token(key, secret)

api = tweepy.API(auth)



a = set()
"""
for tweet in public_tweets:
    print(tweet.text)
    f = open("tweets.txt","a")
    f.write(tweet.text)
    try:
       a.add(tweet.entities.get('media',[])[0]['media_url'])
    except:
        pass
"""

def retrieve(star,page):
    try:
        
       for tweet in tweepy.Cursor(api.user_timeline,id=star,page=page).items():
          f = open("tweets.txt","a")
          f.write(tweet.text)
       #print(tweet.text)
       
          try:
             
             wget.download(tweet.entities.get('media',[])[0]['media_url'])
          except:
             pass
        

       #download the images
       for x in a:
          wget.download(x)
       #api.update_status("Hello world!")
    except:
        print("Invalid username or the account is private.")



def main():
    while True:
       
        name = input("Welcome to Abhishek's Twitter scraper, enter the profile whose tweets and images you would like to scrape or q to quit: ")
        if(name=='q'):
            break
        page = input("Enter page")
        retrieve(name,page)


if __name__=="__main__":
    main()
