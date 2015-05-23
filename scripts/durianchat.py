import os
import sys

import json
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
        return super(User, self).__init__(*args, **kwargs)

    def create_user(self):
        try:
            # ask for username
            username = raw_input("Username: ")
            # ask for password
            password = raw_input("Password: ")

            url = "%s%s" % (API_DOMAIN, self.USER_API_URL)
            data = urllib.urlencode({'username': username, 'password': password})

            response = self.to_JSON(urllib2.urlopen(url=url, data=data).read())

            if response.get('id'):
                print "The account has been successfully created!.\n"
                return True
            else:
                print "\n"
                print response
                print "\n"
                return False

        except Exception as e:
            print e
            print "There was an error when creating an account. please try again.\n"
            return False

    def login_user(self):
        try:
            # ask for username
            username = raw_input("Username: ")
            # ask for password
            password = raw_input("Password: ")

            url = "%s%s%s" % (API_DOMAIN, self.USER_API_URL, 'authenticate')
            data = urllib.urlencode({'username': username, 'password':password})
            response = self.to_JSON(urllib2.urlopen(url=url, data=data).read())

            return response['token']

        except Exception as e:
            return False

    def users_list(self):
        url = "%s%s" % (API_DOMAIN, self.USER_API_URL)
        headers = {'Authorization': 'Token %s' % self.token}
        request = urllib2.Request(url, None, headers)
        response = self.to_JSON(urllib2.urlopen(request).read())

        for user in response:
            print "%s : %s" % (user['username'], user['id'])

        return response

    def get_meinfo(self):
        try:
            url = "%s%s%s" % (API_DOMAIN, self.USER_API_URL, 'me')
            headers = {'Authorization': 'Token %s' % self.token}
            request = urllib2.Request(url, None, headers)
            response = self.to_JSON(urllib2.urlopen(request).read())

            return response
        except Exception as e:
            return False

    def get_userinfo(self, user_id):
        try:
            url = "%s%s%s" % (API_DOMAIN, self.USER_API_URL, user_id)
            headers = {'Authorization': 'Token %s' % self.token}
            request = urllib2.Request(url, None, headers)
            response = self.to_JSON(urllib2.urlopen(request).read())

            return response
        except Exception as e:
            return False



class Message(BaseTool):

    MESSAGE_API_URL = 'messages/'

    def __init__(self, *args, **kwargs):
        return super(Message, self).__init__(*args, **kwargs)

    def get_messages(self):
        url = "%s%s" % (API_DOMAIN, self.MESSAGE_API_URL)
        headers = {'Authorization': 'Token %s' % self.token}
        request = urllib2.Request(url, None, headers)
        response = self.to_JSON(urllib2.urlopen(request).read())

        for message in response:
            try:
                userinfo = self.get_userinfo(message['sender'])
                print "From: %s" % userinfo['username']
                print "Message: %s" % message['content']
                print "----------------------------------------------"
            except Exception as e:
                pass

        print "\n\n"
        raw_input('Press Enter to go back to MAIN MENU')
        os.system('clear')


    def create_message(self):
        try:
            # Sender is the logged in user
            sender = self.user['id']

            recipient = raw_input("Input Recipient\'s ID: ")
            content = raw_input("Type your message: ")

            url = "%s%s" % (API_DOMAIN, self.MESSAGE_API_URL)
            headers = {'Authorization': 'Token %s' % self.token}

            data = urllib.urlencode({'sender': sender, 'recipient': recipient, 'content': content})
            request = urllib2.Request(url, data, headers)
            response = self.to_JSON(urllib2.urlopen(request).read())

            os.system('clear')
            print "Message has been sent.\n"

        except Exception as e:
            os.system('clear')
            print "There's an error. Please try again.\n"


class Main(User, Message):

    def __init__(self, *args, **kwargs):
        self.token = None
        self.user = None
        return super(Main, self).__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        while True:
            print "1 - Login | 2 - Create new account | 3 - Quit\n\n"
            choice = raw_input("Pick an action: ")

            if choice == "1":
                # User login
                self.login()
                break;

            elif choice == "2":
                # create user
                is_created = self.create_user()
                if not is_created:
                    continue;
                else:
                    print "\nYou can now login using the account that you have created.\n"
                    self.login()
                    break;

            elif choice == "3":
                sys.exit("Thank you for using durianchat! bye. \n\n")



        # MAIN MENU
        self.main_menu()

    def login(self):
        while True:
            print "\nUSER LOGIN:"
            # login user
            token = self.login_user()

            if token:
                self.token = token
                user_info = self.get_meinfo()
                if user_info:
                    self.user = user_info
                    return True
                else:
                    print "There is an error. Please try again."
            else:
                print "Invalid username/password. please try again."

    def main_menu(self):
        os.system('clear')
        while True:
            print "1 - Create New Message | 2 - View Messages | 3 - Quit\n\n"
            choice = raw_input("Pick an action: ")
            if choice == "1":
                # Create new message
                os.system('clear')
                self.users_list()
                self.create_message()

            elif choice == "2":
                # View messages
                os.system('clear')
                self.get_messages()

            elif choice == "3":
                os.system('clear')
                sys.exit("Thank you for wasting your time! bye.\n\n")
            else:
                os.system('clear')
                print "Invalid choice. Please try again.\n"



if __name__ == "__main__":

    main = Main()
    main.run()