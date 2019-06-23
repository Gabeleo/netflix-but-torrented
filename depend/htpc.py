from selenium import webdriver
from selenium.webdriver.firefox.options import Options


"""Selenium web driver"""
infohash = None

# @staticmethod
def create(url, query):
    options = Options()
    options.add_argument('-headless')

    driver = webdriver.Firefox(options=options, executable_path="C:/Users/Gabe/geckodriver/geckodriver.exe")
    driver.get(url)

    search(driver, query)
    play(get_search_results(driver))

    driver.quit()


def search(driver, query):
    """Executes a search query with the pirate bay search bar"""
    search_elem = driver.find_element_by_xpath('/html/body/div/form/p[1]/input') #input form
    search_elem.send_keys(query)
    driver.find_element_by_xpath('/html/body/div/form/p[3]/input[1]').click() #search button


def get_search_results(driver):
    res_input = '1080'

    #html table of sorts
    tbody = driver.find_element_by_css_selector('#searchResult > tbody:nth-child(2)')

    tbody.find_elements_by_xpath('./tr')
    title = driver.find_element_by_xpath('//*[@class="detLink"]').get_attribute("title")

    if title.find(res_input) >= 0:
        magnet_link = driver.find_element_by_xpath(
            '//*[@title="Download this torrent using magnet"]').get_attribute("href")

        return magnet_link


def play(search_results):
    torrent = 'https://instant.io/'
    global infohash
    infohash = torrent + "#" + search_results
