import random
from selenium import webdriver
import webdriver_manager

class Browser:
    def __init__(self):
        chrome_options = webdriver_manager.ChromeOptions()
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36"
        ]
        agent = user_agents[random.randint(0, len(user_agents) - 1)]
        chrome_options.add_argument("user-agent=" + agent)
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

    def __del__(self):
        self.driver.close()
        
    def execSearch(self, words):
        print("Metodo nao implementado...")
