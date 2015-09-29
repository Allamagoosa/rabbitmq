class TwitterBot(object):
    def __init__(self):
        pass
    def post_tweet(self, message):
        self.message = message
        print "post_tweet from class message= {0}".format(message)
        return "post tweet done"
    def search(self, q):
        self.q = q
        print "seach q"