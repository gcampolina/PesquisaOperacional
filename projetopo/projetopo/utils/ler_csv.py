import csv
import builtins

def ler_csv(dir):
  with builtins.open(dir,"r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)

    # Inicializa um dicionário para armazenar os dados
    #dados = {coluna: [] for coluna in leitor.fieldnames}
    dados =  []
    # Itera sobre cada linha e adiciona os dados às listas correspondentes
    for linha in leitor:
      linha_lida = []
      for coluna, valor in linha.items():
        try:
          linha_lida.append(float(valor))
        except:
          linha_lida.append(valor)
      dados.append(linha_lida)
  return dados