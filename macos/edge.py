from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
from msedge.selenium_tools import Edge, EdgeOptions
import time
import os

###########################################################

#enter the link to the website you want to automate login.
website_link="http://10.122.1.76/guest/IIUM_Portal.php?cmd=login&mac=10:02:b5:6f:0e:c3&essid=WiFI%40IIUM-MAHALLAH-2.4GHz&ip=10.122.19.139&apname=F10-L6-AP.04&vcname=instant-CA%3A50%3A56&switchip=securelogin.arubanetworks.com&url=http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204&_browser=1"
#enter your login username
username="#######"
#enter your login password
password="********"

###########################################################

#enter the element for username input field
element_for_username="user"
#enter the element for password input field
element_for_password="password"
#enter the element for submit button
element_for_submit="ID_form13236db9_weblogin_submit"

###########################################################

#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
#browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]
#browser = webdriver.Chrome()	#uncomment this line,for chrome users
# driver = webdriver.Edge(executable_path="E:\\Downloads\\edgedriver_win64\\msedgedriver.exe")
# browser = webdriver.Edge(executable_path="C:\\Users\\nurai\\AppData\\Local\\Microsoft\\Edge SxS\\Application\\98.0.1091.0\\msedge.exe")

options = EdgeOptions()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("disable-gpu")
options.binary_location = "C:\\Users\\nurai\\AppData\\Local\\Microsoft\\Edge SxS\\Application\\98.0.1091.0\\msedge.exe"

webdriver_path = "C:\\Workspace\\edgedriver_win64\\msedgedriver.exe"

browser = Edge(options=options, executable_path=webdriver_path)

browser.get((website_link))	

try:
	username_element = browser.find_element_by_name(element_for_username)
	username_element.send_keys(username)		
	password_element  = browser.find_element_by_name(element_for_password)
	password_element.send_keys(password)
	# signInButton = browser.find_element_by_name(element_for_submit)
	signInButton = browser.find_element(By.ID,element_for_submit)
	signInButton.click()
	
	import os
	os.system("taskkill /f /im  msedgedriver.exe")

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
	# browserExe = "msedge.exe"
	# os.system("pkill "+browserExe)


