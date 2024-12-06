# Função para escolher o tipo de madeira
def escolha_tipo():
  madeiras  = {
    "PIN": "Tora de Pinho",
    "PER": "Tora de Peroba",
    "MOG": "Tora de Mogno",
    "IPE": "Tora de Ipê",
    "IMB": "Tora de Imbuia"
  }
  while True:
    # Pergunta o tipo de madeira e retorna o valor
    print("Digite o tipo de madeira que você deseja pedir:")
    for sigla, tipo in madeiras.items():
      print(f"{sigla} | {tipo}") # Retorna os tipos de madeiras
    tipo_escolhido = input(">> ").upper()
    if tipo_escolhido in madeiras:
      print(f"Você selecionou {madeiras[tipo_escolhido]}")
      if tipo_escolhido == "PIN":
        valor = 150.40
        return valor
      elif tipo_escolhido == "PER":
        valor = 170.20
        return valor
      elif tipo_escolhido == "MOG":
        valor = 190.90
        return valor
      elif tipo_escolhido == "IPE":
        valor = 210.10
        return valor
      elif tipo_escolhido == "IMB":
        valor = 220.70
        return valor
    else:
      print("Esse tipo de madeira não está disponível!") # Tratamento de erro

# Função para quantidade de toras e cálculo de desconto
def qtd_toras():
  while True:
    try:
      # Pergunta a quantidade e aplica desconto
        quantidade_escolhida = int(input("Digite a quantidade de toras(m³): "))
        if quantidade_escolhida < 100:
          return quantidade_escolhida, 0
        elif quantidade_escolhida >= 100 and quantidade_escolhida < 500:
          return quantidade_escolhida, 0.04
        elif quantidade_escolhida >= 500 and quantidade_escolhida < 1000:
          return quantidade_escolhida, 0.09
        elif quantidade_escolhida >= 1000 and quantidade_escolhida <= 2000:
          return quantidade_escolhida, 0.16
        else:
          print("Não aceitamos pedidos com essa quantidade de toras!")  
          # Tratamento de erro se o valor ultrapassa o limite
    except ValueError:
       print("Digite um valor válido para processeguir com o pedido!")  
       # Tratamento de erro se o valor não for um número

# Função para escolher o transporte
def transporte():
  transportes = {
    1: {"transporte": "Rodoviário ", "preco": 1000.00},
    2: {"transporte": "Ferroviário", "preco": 2000.00},
    3: {"transporte": "Hidroviário", "preco": 2500.00}
  }
  while True:
    # Pergunta o tipo de transporte e retorna o valor
    print("Digite o tipo de transporte que você deseja pedir:")
    for id, val in transportes.items():
      print(f"[{id}] {val['transporte']} | R$ {val['preco']}")
    try:
      transporte_escolhido = int(input(">> "))
      if transporte_escolhido in transportes:
        return transportes[transporte_escolhido]["preco"]
      else:
        print("Esse transporte não existe!") # Tratamento de erro 
    except ValueError:
      print("Digite um valor válido para processeguir com o pedido!") 
      # Tratamento de erro se o valor não for um número
      continue

def main():
  # Chama as funções e armazena os valores
  print('Bem-vindo à Madereira da Lenhadora Nicolle Ramos Batista!')
  print('Vamos começar o seu pedido!')
  tipoMadeira = escolha_tipo()
  qtdToras, desconto = qtd_toras() 
  transporte_preco = transporte() 

  total_pedido = ((tipoMadeira * qtdToras)*(1-desconto)) + transporte_preco
  print(f"O valor total do seu pedido é R$ {total_pedido:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
