import bs4

try:
    arquivoDeExemplo = open('scraping/cte.html', 'r', encoding='utf-8')
    objSoup = bs4.BeautifulSoup(arquivoDeExemplo, features="lxml")

    table = objSoup.find('table', {'id': 'standard_table'})
    print(table)
    rows = table.tbody.find_all('tr')
    print(rows)
    for row in rows:
        columns = row.find_all('td')
        primeira_coluna = columns[0].get_text()
        ultima_coluna = columns[-1].get_text()
        print(f"coluna: {primeira_coluna}, descricao: {ultima_coluna}")

except Exception as exc:
    print("Houve um erro: %s" % (exc))