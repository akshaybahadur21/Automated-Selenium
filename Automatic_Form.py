from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time

fire_path=r"C:\Users\akshaybahadur21\Desktop\PythonCode\Chromedriver.exe"
driver=webdriver.Chrome(fire_path)
driver.get("<URL>")

for x in range (0,50):
	time.sleep(2)
	driver.find_element_by_xpath("""//*[@title="Select position"]""").click()
	driver.find_element_by_xpath("""//*[contains(text(),'ML Developer')]""").click()

	name=driver.find_element_by_xpath("""//*[@placeholder='First name']""")
	name.send_keys("Akshay")
	sname=driver.find_element_by_xpath("""//*[@placeholder='Last name']""")
	sname.send_keys("Bahadur")
	email=driver.find_element_by_xpath("""//*[@placeholder='Email address']""")
	email.send_keys("<SOME EMAIL>")
	phone=driver.find_element_by_xpath("""//*[@placeholder='Mobile no.']""")
	phone.send_keys("<PHONE NUMBER>")
	curr=driver.find_element_by_xpath("""//*[@placeholder='Current Company / Organisation']""")
	curr.send_keys("Netcracker Technology")

	driver.find_element_by_xpath("""//*[@title="Your Experience"]""").click()
	driver.find_element_by_xpath("""//*[contains(text(),'Fresher/Intern')]""").click()

	git=driver.find_element_by_xpath("""//*[@placeholder='Links to you online work/portfolio.']""")  
	git.send_keys("https://github.com/akshaybahadur21")

	git=driver.find_element_by_xpath("""//*[@placeholder='How did you hear about Decimal Point?']""")  
	git.send_keys("College")

# driver.find_element_by_xpath("""//*[@id="decimal_opening"]/div/div[2]/div[2]/div/form/div/div[8]/div/div/input""").click()
# driver.find_element_by_css_selector('input[type="file"]').send_keys("C:\\Users\\akshaybahadur21\\Desktop\\ms\\Akshay_Bahadur_latest_CV.pdf")

	driver.find_element_by_xpath("""//*[@id="decimal_opening"]/div/div[2]/div[2]/div/form/div/div[8]/div/div/input""").send_keys("C:\\Users\\akshaybahadur21\\Desktop\\ms\\Akshay_Bahadur_CV_final.pdf")
	


