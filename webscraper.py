import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


searched_error = str(input('paste here your error:'))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://stackoverflow.com')

search = driver.find_element_by_name('q')
search.send_keys(searched_error)
search.send_keys(Keys.RETURN)


result_links = driver.find_elements_by_css_selector("[class='question-hyperlink']")
for link in result_links:
    link.send_keys(Keys.CONTROL + 't', Keys.RETURN)


# driver.quit()