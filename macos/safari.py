from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Safari
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from msedge.selenium_tools import Edge, EdgeOptions
import time
import os

###########################################################

#enter the link to the website you want to automate login.
website_link="http://10.122.1.76/guest/IIUM_Portal.php?cmd=login&mac=8c:7a:aa:ea:90:3a&essid=WiFi%40IIUM-MAHALLAH-5GHz&ip=10.122.25.154&apname=F10-L6-AP.05&vcname=instant-CA%3A50%3A56&switchip=securelogin.arubanetworks.com&url=http%3A%2F%2Fcaptive.apple.com%2F&_browser=1"

#enter your login username
username="2013794"

#enter your login password
password="K@nderi1206"

###########################################################

#enter the element for username input field
element_for_username="user"

#enter the element for password input field
element_for_password="password"

#enter the element for submit button
element_for_submit="ID_form13236db9_weblogin_submit"

###########################################################

# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]
# browser = webdriver.Chrome()	#uncomment this line,for chrome users
# driver = webdriver.Chrome(executable_path="")

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(executable_path="C:\\Workspace\\chromedriver_win32\\chromedriver.exe", options=options)
# browser = webdriver.Chrome(options=options)
browser.get((website_link))	

try:
	username_element = browser.find_element_by_name(element_for_username)
	username_element.send_keys(username)		
	password_element  = browser.find_element_by_name(element_for_password)
	password_element.send_keys(password)
	signInButton = browser.find_element(By.ID,element_for_submit)
	signInButton.click()
	
	#### to quit the browser uncomment the following lines ####
	# time.sleep(3)
	# browser.quit()
	# time.sleep(1)
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)
except Exception:
	#### This exception occurs if the element are not found in the webpage.
	print("Some error occured :(")

	# ### to quit the browser uncomment the following lines ####
	# browser.quit()
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)
	# os.system("pkill safaridriver")

