from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

#print(browser.title)
assert 'worked' in browser.title