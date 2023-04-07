from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.etf.com/etfanalytics/etf-finder')
driver.maximize_window()
botao_cookies = driver.find_element("xpath",'//*[@id="cookie-bar"]/p/a[2]')
botao_cookies.click()
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get('https://www.etf.com/etfanalytics/etf-finder') #etf.com tem todos os etfs do mundo inteiro, as 20h da uma bugada pq
# é atualização

time.sleep(5)
botao_100 = driver.find_element("xpath",
                               '/html/body/div[4]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/section[2]/div[1]/div/div[4]/button/label/span')
                               
driver.execute_script("arguments[0].click();", botao_100)

num_paginas = driver.find_element("xpath",'//*[@id="totalPages"]')
num_paginas = int(num_paginas.text.replace("of ",""))
num_paginas

lista_tabelas = []
elemento_tabela = driver.find_element("xpath",'//*[@id="finderTable"]')

for pagina in range(1, num_paginas + 1):
    html_tabela = elemento_tabela.get_attribute('outerHTML')
    tabela = pd.read_html(str(html_tabela))[0]
    lista_tabelas.append(tabela)
    botao_avancar = driver.find_element("xpath",'//*[@id="nextPage"]')
    botao_avancar.click()
    #time.sleep(2)  # adiciona uma pausa de 2 segundos para aguardar a página carregar completamente
    
tabela_cadastro_etfs = pd.concat(lista_tabelas)

tabela_cadastro_etfs

formulario_voltar = driver.find_element("xpath",'//*[@id="goToPage"]')
formulario_voltar.clear()
formulario_voltar.send_keys("1")
formulario_voltar.send_keys(u'\ue007')

performace = driver.find_element("xpath", '/html/body/div[4]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/ul/li[2]/span')
performace.click()



lista_tabelas = []
elemento_tabela = driver.find_element("xpath",'//*[@id="finderTable"]')

for pagina in range(1, num_paginas + 1):
    html_tabela = elemento_tabela.get_attribute('outerHTML')
    tabela = pd.read_html(str(html_tabela))[0]
    lista_tabelas.append(tabela)
    botao_avancar = driver.find_element("xpath",'//*[@id="nextPage"]')
    botao_avancar.click()
    #time.sleep(2)  # adiciona uma pausa de 2 segundos para aguardar a página carregar completamente
    
tabela_rentabilidade_etfs = pd.concat(lista_tabelas)

tabela_rentabilidade_etfs
driver.quit()
print(tabela_rentabilidade_etfs.columns)
tabela_cadastro_etfs = tabela_cadastro_etfs.set_index('Ticker')
tabela_rentabilidade_etfs = tabela_rentabilidade_etfs.set_index("Ticker")
tabela_rentabilidade_etfs = tabela_rentabilidade_etfs[['1 Year', '3 Years', '5 Years']]


tabela_rentabilidade_etfs
tabela_cadastro_etfs

base_dados_etfs = tabela_cadastro_etfs.join(tabela_rentabilidade_etfs, how = 'inner')
base_dados_etfs 

