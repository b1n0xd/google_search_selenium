from search import *
import random

#construtor
class Google (Browser):
    def __init__(self):
        super().__init__();
        def execSearch(self, words):
            print("Esta pesquisando..." , words);
            pages = ["https://google.com/","https://google.com.br/","https://google.fr/","https://google.jp/"];
            page = pages[random.randint(0, len(pages) -1)];
            print("A pagina sera: " + page);
            