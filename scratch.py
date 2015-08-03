from urllib2 import Request, urlopen

class Trakt:
    def __init__(self):
        self.BASE_URI = "https://api.trakt.tv"
        self.USERNAME = "ThumbKiss" # Remove this
        self.PASSWORD = "moniarkoretmurni" # Remove this
        self.API_KEY = "38d92c129af4b81e25ba1be04e1f49afa65b17f7487be5696c051a8f8080025c" # Remove this

    def login(self):
        values = """
          {{
            "login": "{0}",
            "password": "{1}"
          }}
        """.format(self.USERNAME, self.PASSWORD)

        headers = {
          'Content-Type': 'application/json',
          'trakt-api-version': '2',
          'trakt-api-key': self.API_KEY
        }

        request = Request(self.BASE_URI + '/auth/login', data=values, headers=headers)
        response_body = urlopen(request).read()

        return response_body
