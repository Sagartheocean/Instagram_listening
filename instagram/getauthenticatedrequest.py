from instagram.client import InstagramAPI

access_token = "18128704314.08ac084.a9da4f6762de4a3bbdc457511599c111"
client_secret = "cb3e3c9061ab4b4fa603e9428f155780"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)

recent_media, next_ = api.user_recent_media(user_id="colgate", count=10)
for media in recent_media:
   print media.caption.text