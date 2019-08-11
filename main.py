import os
import requests
import time
import xlwt
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
load_dotenv()

def outputXlsx(lista1, lista2):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("PesquisaPreco1")
 
    sheet1.write(0, 0, "Nome")
    sheet1.write(0, 1, "Preço")
    col = 1
    for item in lista1:
        sheet1.write(col, 0, item)
        sheet1.write(col, 1, lista2[col-1])
        col += 1
    book.save("planilha.xls")

def procurarClassesHtml(domhtml, classehtml):
    lista = list()
    elementos = domhtml.find_elements_by_class_name(classehtml)
    for item in elementos:
        lista.append(item.text)
    return lista

def encontrarProximaPagina(currentPage):
    page = requests.get(currentPage)
    soup = BeautifulSoup(page.content, 'html.parser')
    nextpagelinks = soup.find_all(class_='neemu-pagination-next')
    fullurl = os.getenv('BASE_URL') + str(nextpagelinks[0].select('a')[0].get('href'))
    return fullurl


def main():
    #faz o primeiro request
    driver = webdriver.Firefox()
    driver.get(os.getenv('URL_REQUEST'))
    proxima = encontrarProximaPagina(os.getenv('URL_REQUEST'))
    nomes = list()
    precos = list()
    for i in range(int(os.getenv('NUMERO_PAGINAS'))):
        nomes.extend(procurarClassesHtml(driver, 'nm-product-name'))
        precos.extend(procurarClassesHtml(driver, 'nm-price-value'))
        proxima = encontrarProximaPagina(proxima)
        driver.get(proxima)

    outputXlsx(nomes, precos)
    
if __name__ == "__main__":
    main()