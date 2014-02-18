import praw

current_user = praw.Reddit(user_agent='sub_bot')
print "PRAW instance created"

print "Login to the user you would like to migrate subscriptions from"
current_user.login()
print "User logged in, collecting subscribed subreddits"

subreddits = current_user.get_my_subreddits(limit=None)
print "Subreddits collected"


new_user = praw.Reddit(user_agent='sub_bot')
print "Please login to the new user"
new_user.login()

print "Subscribing to subreddits, this may take a few minutes..."
for sub in subreddits:
  new_user.get_subreddit(sub.display_name).subscribe()

print 'Subreddits succesfully migrated'