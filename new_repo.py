import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from mylogins import *

mode = 0
repo_description = ""
path = "C:/Users/charl/Documents/Prog"
readme_text = "# New Project"
commit_msg = "First commit"

repo_name = sys.argv[1]
if len(sys.argv)>2:
	mode = sys.argv[2]
	if len(sys.argv)>3:
		repo_description = sys.argv[3]
		if len(sys.argv)>4:
			path = sys.argv[4]
			if len(sys.argv)>5:
				readme_text = sys.argv[5]
				if len(sys.argv)>6:
					commit_msg = sys.argv[6]

driver = webdriver.Firefox()
driver.get("http://github.com/new")

elem = driver.find_element_by_name("login")
elem.send_keys(usrname)
elem = driver.find_element_by_name("password")
elem.send_keys(passwrd)
elem.send_keys(Keys.RETURN)

time.sleep(5)

elem = driver.find_element_by_name("repository[name]")
elem.send_keys(repo_name)
elem = driver.find_element_by_name("repository[description]")
elem.send_keys(repo_description)
time.sleep(2)
elem = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
elem.click()

time.sleep(5)

elem = driver.find_element_by_id("empty-setup-clone-url")
repo_url = elem.get_attribute("value")

driver.close()

if mode == 0:
	os.chdir(path)
	os.system("mkdir "+repo_name)
	os.chdir(repo_name)
	time.sleep(1)
	os.system('echo '+readme_text+' >> README.md')
	time.sleep(2)
	
os.system('git init')
time.sleep(2)
os.system('git add .')
time.sleep(2)
os.system('git commit -m "'+commit_msg+'"')
time.sleep(3)
os.system('git remote add origin '+repo_url)
time.sleep(2)
os.system('git push -u origin master')