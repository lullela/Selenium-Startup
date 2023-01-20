#Test Case
#------------------
# 1) Open Web Browser(Chrome,ff,edge)
# 2) Open Url https://opensource-demo.orangehrmlive.com/
# 3) Enter username (Admin)
# 4) Enter password (admin123)
# 5) Click on Login
# 6) Capture title of the home page. (Actual title)
# 7) Verify title of the page: OrangeHRM (expected)
# 8) Close browser

#Importing selenium module webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_var = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
#Making an object that is getting the chrome driver
driver = webdriver.Chrome(service=serv_var)
#Opening the website that we want with 'get'
driver.get("https://opensource-demo.orangehrmlive.com/")

#Making the browser wait until we find the elements
driver.implicitly_wait(15)

#Finding the element and performing an action
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.ID, "app").click()

#Creating variables for actual and expected title
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Test Passed")
else:
    print("Test Failed")