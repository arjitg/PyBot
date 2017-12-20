import praw
bot = praw.Reddit(user_agent='MySimpleBot v0.1',
                  client_id='abcdefGHIJKLO123--',
                  client_secret='12345678901abcdefgh-_',
                  username='demo_user',
                  password='demo_password')
subreddit = bot.subreddit('space')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'mars' in text.lower():
        # Generate a message
        message = "Why no love for Titan, u/{0} ?".format(author)

        comment.reply(message) # Send message
