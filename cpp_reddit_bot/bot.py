from dotenv import load_dotenv
import os
import praw

load_dotenv()

reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent='testscript by /u/cppbot',
                     username='cppbot')

print("Reddit configured")
