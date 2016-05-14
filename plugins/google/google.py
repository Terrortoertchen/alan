from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


try:
  browser = webdriver.Firefox()
except:
  print ":speak:I couldn't find firefox. Try installing it."

browser.get("http://www.google.com")

print ":speak: Opening google."

def get_text(prompt):
  print ":speak:{}".format(prompt)
  print ":listen:"
  text = raw_input()
  return text

def action(action_name):
  global page_location
  if action_name == "click":
    text = get_text("What is the link?")
    links = browser.find_elements_by_partial_link_text('{}'.format(text))
    if len(links) == 0:
      links = browser.find_elements_by_partial_link_text('{}'.format(text.title()))
    try:
      links[0].click()
    except:
      print ":speak:Can't open the link."

  elif action_name == "search":
    text = get_text("Ready")
    elem = browser.find_element_by_name('q')  # Find the search box
    elem.clear()
    elem.send_keys('{}'.format(text) + Keys.RETURN)

  elif action_name == "back":
    browser.execute_script("window.history.go(-1)")

  elif action_name == "top":
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  elif action_name == "down":
    browser.execute_script("window.scrollBy(0, 400);")




while True:
  do_action = raw_input()
  if do_action == "exit":
    exit(0)
  else:
    action(do_action)