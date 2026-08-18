from tools import Website, User
import time

######can be safely deleted upon download, just for testing purposes#########
try:
    import sys
    sys.path.append("E:/save/")
    from secret_module import secret_info
except:
    pass

#within the secret module, which is in the save folder, there is a secret class where we store our secret information: usernames and passwords
# class Secret_class():
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

# secret_info = Secret_class("some_username", "some_password")
#############################################################################

#we establish what website we want to log into for this instance and what browser we want to use. Currently Chrome is the only option
chrome = Website("https://portal.nm911.org/", "Chrome")

#Then, we import the username and password for this website. I have shown how to import this from a file that is outside our data structure,
# just give the absolute path to the system appended directory and follow the data structure. However, a local definition is also perfectly acceptable and
# honestly prefereable.
user_me_nm911 = User(secret_info.username, secret_info.password)

#We would do this pair of instructions for every different website we want to log into. The specification of _nm911 is important below as
# each website will have different methods for accessing their login, password, and submit fields/buttons


#we call our website object with the login to new mexico 911 function and pass it our user info.
chrome.login_nm911(user_me_nm911)
#then the absolute path to the zip file we want to upload.
chrome.upload_nm911("C:/Users/GIS/Desktop/thing/GIS_upload.zip")


#we would then wait for everything to upload- we don't want to have it on a set timer but in a "wait till this process finishes" check,
# but for testing purposes it's just a static timer.
time.sleep(1)
#after we have uploaded all we want to to the current page we must close the driver before trying to log in to another website.
chrome.logout()