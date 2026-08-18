from class_test import Website
from class_test import User
from secret import secret

#currently Chrome is the only option
chrome = Website("https://portal.nm911.org/", "Chrome")
user_me_nm911 = User(secret.username, secret.password)

chrome.login_nm911(user_me_nm911)
chrome.upload_nm911("C:/Users/GIS/Desktop/thing/GIS_upload.zip")

# time.sleep(5)
# driver.close()