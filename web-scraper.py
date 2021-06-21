import gecko_config

from selenium import webdriver

# 1. Configuring Firefox automation with Selenium
driver = webdriver.Firefox()

# 2. Getting HTML content from the URL
url = "http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
driver.get(url)

# 3. Closing the modal-content banner as soon as possible
banner_closing_available = False
while banner_closing_available == False:
    try:
        driver.find_element_by_class_name("close").click()
        banner_closing_available = True
    except Exception as e:
        pass

# 4. Opening the page of the most recent Padrão TISS available
driver.find_element_by_class_name("alert-link").click()
  
# 5. Closing the second modal-content banner that shows up, also as soon as possible
banner_closing_available = False
while banner_closing_available == False:
    try:
        driver.find_element_by_class_name("close").click()
        banner_closing_available = True
    except Exception as e:
        pass

# 6. Clicking the button to open the Componente Organizacional file with Firefox
driver.find_element_by_xpath(
    "//div[@class='table-responsive']//table//tbody//tr[1]//td[3]//a"
    ).click()