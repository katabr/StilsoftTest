# Определяет вспомогательные функции

class General():

    def __init__(self, browser, timeout=10):
        self.browser = browser
        #self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self)
