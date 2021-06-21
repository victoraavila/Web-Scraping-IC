import gecko_config

from selenium import webdriver

# 1. Configuring Firefox automation with Selenium
driver = webdriver.Firefox()

# 2. Getting HTML content from the URL
url = "http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
driver.get(url)

# 3. Closing modal-content banner as soon as possible
banner_closing_available = False
while banner_closing_available == False:
    try:
        driver.find_element_by_xpath(
            '''/html/body/div[5]/div/div[2]/div/div/div/div/div[1]/button/span'''
        ).click()
        banner_closing_available = True
    except Exception as e:
        pass
