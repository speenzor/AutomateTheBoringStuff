#! /usr/bin/env python3

#Chapter 11 Challenge - Command Line Emailer

#This takes your web email info for Gmail then opens a brower, logins to Gmail
#then composes an email with your recipient, subject, and body, then sends. This only
#works if two-factor authentication is turned off. You can see some commented out elements-
#those are where I had trouble finding an element that would work. You may run into the same problems
#and can easily try those that are commented out.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, time

print ('Please enter your Gmail username, then password, then the email recipient, then the subject line, then the email message, pressing enter after each input')

#username = sys.argv[1]
#password = sys.argv[2]
#to = sys.argv[3]
#subject = sys.argv[4]
#body = sys.argv[5]

username = input()
password = input()
to = input()
subject = input()
body = input()

browser = webdriver.Safari()
browser.get('https://www.google.com/gmail')
usernameElem= browser.find_element_by_id('identifierId')
usernameElem.send_keys(username)
nextButtonElem= browser.find_element_by_class_name('RveJvd snByac')
nextButtonElem.click()
time.sleep(2)
passwordElem= browser.find_element_by_name('password')
passwordElem.send_keys(password)
nextButtonElem= browser.find_element_by_class_name('RveJvd snByac')
nextButtonElem.click()
time.sleep(5)
composeButtonElem= browser.find_element_by_class_name('T-I J-J5-Ji T-I-KE L3')
composeButtonElem.click()
time.sleep(5)
#toElem= browser.find_element_by_id(':8e')
#toElem= browser.find_element_by_class_name('v0')
#toElem= browser.find_element_by_name('to')
#toElem= browser.find_element_by_class_name('wA')
#toElem= browser.find_element_by_id(':81')
toElem= browser.find_element_by_class_name('oj')
toElem.send_keys(to)
time.sleep(2)
subjectElem= browser.find_element_by_name('subjectbox')
subjectElem.send_keys(subject)
bodyElem= browser.find_element_by_class_name('Am Al editable LW-avf')
bodyElem.send_keys(body)
time.sleep(2)
#sendElem= browser.find_element_by_class_name('T-I J-J5-Ji ao0 T-I-atl L3 T-I-JW')
#sendElem= browser.find_element_by_id(':6n')
#sendElem= browser.find_element_by_class_name('J-J5-Ji')
sendElem= browser.find_element_by_id(':7n')
sendElem.click()
