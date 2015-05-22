import urllib
import urllib2

####################
## CONFIGURATIONS ##
####################
API_DOMAIN = 'http://localhost:8000/'


class BaseTool(object):

    def to_JSON(self, response):
        return json.loads(response)


class User(BaseTool):

    USER_API_URL = 'accounts/'

    def __init__(self, *args, **kwargs):
        # User token
        self.token = None

        return super(User, self).__init__(*args, **kwargs)

    def create_user(self):
        # ask for username
        username = raw_input("Username: ")
        # ask for password
        password = raw_input("Password: ")

        url = "%s%s" % (API_DOMAIN, self.USER_API_URL)
        data = urllib.urlencode({'username': username, 'password': password})

        response = urllib2.urlopen(url=url, data=data)

        return response.read()

    def login_user(self):
        try:
            # ask for username
            username = raw_input("Username: ")
            # ask for password
            password = raw_input("Password: ")

            url = "%s%s%s" % (API_DOMAIN, self.USER_API_URL, 'authenticate')
            data = urllib.urlencode({'username': username, 'password':password})
            response = self.to_JSON(urllib2.urlopen(url=url, data=data).read())

            # record token
            self.token = response['token']

            return True

        except Exception as e:
            return False




if __name__ == "__main__":

    user = User()
    is_authenticated = user.login_user()

    if is_authenticated:
        print "1 - Create new message"
        print "2 - View message"
        print "3 - User list"
        choice = ra_input("Pick an action: ")

        if choice == "1":
            print "create message"
        if choice == "2":
            print "view message"
        if choice == "3":
            print "user_list"