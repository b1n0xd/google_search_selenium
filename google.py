from search import *
import random
from selenium.webdriver.common.keys import Keys

class Google(Browser):
    def __init__(self):
        super().__init__()
        
    def execSearch(self, words):
        print("Esta pesquisando...", words)
        pages = ["https://google.com/", "https://google.com.br/", "https://google.fr/", "https://google.jp/"]
        page = pages[random.randint(0, len(pages) - 1)]
        print("A pagina sera: " + page)
        
        self.driver.get(page)
        input_q = self.driver.find_element_by_xpath("//input[@name='q']")
        input_q.send_keys(words)
        input_q.send_keys(Keys.RETURN)
        buffer_links = []
        buffer_quadros = self.driver.find_elements_by_xpath("//div[@class='g' and div[1]/div[1]/a]")
        for i in range(len(buffer_quadros)):
            try:
                link = buffer_quadros[i].find_element_by_xpath("./div[1]/div[1]/a").get_attribute("href")
                buffer_links.append(link)
            except:
                print('Ignorando elementos dentro da DIV...')
        return buffer_links
