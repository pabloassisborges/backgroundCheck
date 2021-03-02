from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Configure Google Chrome instance
options = webdriver.ChromeOptions()

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugin-port=9222")
options.add_argument("--screen-size=1200x800")
options.add_argument("--disable-popup-blocking")
options.add_argument("test-type")


def element_to_info(element):
    bio = element.find_elements_by_css_selector('div.EntitySnippet-bio div')

    return {
        'nome': element.find_element_by_css_selector('a.EntitySnippet-anchor').text,
        'link': element.find_element_by_css_selector('a.EntitySnippet-anchor').get_attribute('href'),
        'processos': bio[0].text,
        'tribunais relevantes': bio[1].text,
        'parte mais citada': bio[2].text
    }


def create_browser():
    """Create an instance of google chrome browser."""
    return webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=options.to_capabilities())


chrome = create_browser()
chrome.implicitly_wait(1)

sleep(3)

chrome.get(f'https://www.jusbrasil.com.br/consulta-processual/busca?q={"Lucas Almeida Silva"}')

element = chrome.find_element_by_xpath('//*[@id="app-root"]/div/div/div[1]/div[2]/div[2]')
elements = element.find_elements_by_css_selector('div.EntitySnippet-item.EntitySnippet--expanded.EntitySnippet-topic')
result = list(map(element_to_info, elements))
# results = element.find_elements_by_css_selector('div.EntitySnippet-item EntitySnippet--expanded EntitySnippet-topic')
# info = list(map(element_to_info, results))
# elements = chrome.find_elements_by_css_selector('a.EntitySnippet-anchor')

chrome.quit()
