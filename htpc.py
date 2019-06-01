from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

class Driver(object):
    def __init__(self, url):
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        driver.get(url)

        self.search(driver)
        self.get_search_results(driver)
        self.play(driver, self.get_search_results(driver))
        self.__str__(self.play(get_search_results(driver)))
        
    def search(self, driver):
        movie_input = input('Search for Movies: ')

        search_elem = driver.find_element_by_xpath('/html/body/div/form/p[1]/input')
        search_elem.send_keys(movie_input)
        driver.find_element_by_xpath('/html/body/div/form/p[3]/input[1]').click()

    def get_search_results(self, driver):
        res_input = '1080'

        tbody = driver.find_element_by_css_selector('#searchResult > tbody:nth-child(2)')

        for row in tbody.find_elements_by_xpath('./tr'):
            title = driver.find_element_by_xpath('//*[@class="detLink"]').get_attribute("title")

            if title.find(res_input) > -1:
                magnet_link = driver.find_element_by_xpath(
                    '//*[@title="Download this torrent using magnet"]').get_attribute("href")

                return magnet_link

    def play(self, driver, get_search_results):
        torrent = 'https://instant.io/'
        result = get_search_results

        infohash = torrent + "#" + result
        print(infohash)
        return infohash

        def __str__(self, play):
            infohash = play
            return infohash


#if __name__ == '__main__':
    #Driver('https://thepiratebay.org/')
