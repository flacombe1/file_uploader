from tools import Website, User

######can be safely deleted upon download, just for testing purposes#########
try:
    import sys
    sys.path.append("E:/save/")
    from secret import secret
except:
    pass
###########

#currently Chrome is the only option
chrome = Website("https://portal.nm911.org/", "Chrome")
user_me_nm911 = User(secret.username, secret.password)

chrome.login_nm911(user_me_nm911)
chrome.upload_nm911("C:/Users/GIS/Desktop/thing/GIS_upload.zip")

# time.sleep(5)
# driver.close()