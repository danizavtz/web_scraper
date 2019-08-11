# web_scraper

# Configuração
1. Criar virtualenv apontando para sua instância do python3
2. `virtualenv venv -p $(which python3)`
3. carregar o virtualenv
4. `source venv/bin/activate`
5. instalar as dependências contidas no requirements.txt
6. `pip install -r requirements.txt`
7. Ter instância do geckodriver para firefox instalada na máquina.(`https://github.com/mozilla/geckodriver/releases`). Baixar a ultima versão.
8. extrair o arquivo baixado para `/usr/bin`
9. Renomear o arquivo `dotenv-sample` para `.env`. Deve estar na raiz do projeto (mesmo diretório do main.py)
10. `python main.py`
11. ao final da execução deve ser criado um arquivo `planilha.xls`