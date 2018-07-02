class League():

    root_url = "http://league.aicai.com"
    def __init__(self,url,name):
        self.name = name
        self.url = url

    def getUrl(self):
        return self.root_url + self.url
