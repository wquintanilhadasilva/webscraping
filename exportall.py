import os
from bs4 import BeautifulSoup

output_file = "output.csv"
directory = "~/output/public/tables"

with open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write("tabela;coluna;descricao\n")
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f_in:
                soup = BeautifulSoup(f_in, "html.parser")
                table = soup.find('table', {'id': 'standard_table'})
                rows = table.tbody.find_all('tr')
                for row in rows:
                    if row.parent.name == 'tbody':
                        columns = row.find_all('td')
                        primeira_coluna = columns[0].get_text()
                        ultima_coluna = columns[-1].get_text()
                        ultima_coluna = ultima_coluna.replace('\n', '')
                        ultima_coluna = ultima_coluna.replace(';', ',')
                        if filename == 'nfe.html' and primeira_coluna == 'finalidade_nfe':
                            print(f"coluna: {primeira_coluna}, descricao: {ultima_coluna}")
                        f_out.write(f"{filename.replace('.html', '')};{primeira_coluna};{ultima_coluna}\n")