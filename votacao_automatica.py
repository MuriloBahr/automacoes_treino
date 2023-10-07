from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import os

def terminal_clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def jungkook_voting_kpop():
        count = 0
        random_number = random.randint(10, 13)
        driver = webdriver.Edge()
        driver.get("https://www.mtvema.com/pt-br/vota/best-kpop/")
        print('Indo para o Jungkook (MELHOR KPOP DO ANO)')
        sleep(10)
        while count < 100:
            try:
                button = driver.find_element("xpath", "//div/section/div/div[3]/div/section[11]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/button")
                button.click()
                driver.execute_script("arguments[0].style.border = '2px solid red';", button)
                print(f"Botão clicado {count}x")
                count += 1
            except:
                print('Botão Nao Encontrado')
            sleep(random_number)
            terminal_clean()
    
def jungkook_voting_music():
    count = 0
    driver = webdriver.Edge()
    random_number = random.randint(10, 13)
    driver.get("https://www.mtvema.com/pt-br/vota/best-song/")
    print('Indo para o Jungkook (MELHOR MUSICA)')
    sleep(10)
    while count < 100:
        try:
            button = driver.find_element("xpath", "//div/section/div/div[3]/div/section[2]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/button")
            button.click()
            driver.execute_script("arguments[0].style.border = '2px solid red';", button)
            print(f"Botão clicado {count}x")
            count += 1
        except:
            print('Botão Nao Encontrado')
        sleep(random_number)
        terminal_clean()
    
def matue_voting():
    driver = webdriver.Edge()
    driver.get("https://www.mtvema.com/pt-br/vota/best-brasilian-act/")     
    random_number = random.randint(10, 13)
    count = 0
    sleep(10)
    while count < 100:
        try:
            button = driver.find_element("xpath", "//div/section/div/div[3]/div/section[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[5]/button")
            button.click()
            driver.execute_script("arguments[0].style.border = '2px solid red';", button)
            print(f"Botão clicado {count}x")
            count += 1
        except:
            print("Botão não encontrado")
        sleep(random_number)
        terminal_clean()
    
def main():
    count = 0
    while count < 2:
        matue_voting ()
        jungkook_voting_kpop()
        jungkook_voting_music()
        count += 1

if __name__ == "__main__":
    main()