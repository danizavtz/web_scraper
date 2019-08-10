import os
import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
from dotenv import load_dotenv
import xlwt
load_dotenv()


base_url = os.getenv('BASE_URL')

def output(filename, list1, list2, x, y, z):
    book = xlwt.Workbook()
    sh = book.add_sheet('lista')

    variables = [x, y, z]
    w_desc = 'id'
    x_desc = 'Nome'
    y_desc = 'preco'
    z_desc = 'descricao'
    desc = [w_desc, x_desc, y_desc, z_desc]

    col1_name = 'Stimulus Time'
    col2_name = 'Reaction Time'

    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    for n, v_desc, v in enumerate(zip(desc, variables)):
        sh.write(n, 0, v_desc)
        sh.write(n, 1, v)

    n+=1

    sh.write(n, 0, col1_name)
    sh.write(n, 1, col2_name)

    for m, e1 in enumerate(list1, n+1):
        sh.write(m, 0, e1)

    for m, e2 in enumerate(list2, n+1):
        sh.write(m, 1, e2)

    book.save(filename)

def procurarClassesNome(domhtml):
    domhtml.find_all(class="nm-product-name")

def procurarClassesPreco(domhtml):
    domhtml.find_all(class="nm-price-value")


def procurarIdProduto(domhtml):
    domhtml.find_all(class="nm-product-item  price-api-success")

def encontrarProximaPagina(domhtml):
    domhtml.find_all(class_='neemu-pagination-next')
    fullurl = baseurl.join(nextpagelinks[0].select('a')[0].get('href'))

    #inserir navegação para próxima página.

def chamarProximaPagina(fullurl):
    page = requests.get(fullurl)


def main():
    page = requests.get(URL_REQUEST)
    soup = BeautifulSoup(page.content, 'html.parser')

if __name__ == "__main__":
    main()