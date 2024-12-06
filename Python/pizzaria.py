# Iniciando o valor total do pedido como zero
valor_total_pedido = 0.00
pedidos = True

print("Bem-vindo à pizzaria da Nicolle Ramos Batista")
print("Cardápio -----------------------------------------")
print("| Tamanho | Pizza Salgada [PS] | Pizza Doce [PD] | ")
print("|    P    |     R$ 30,00       |     R$ 34,00    | ")
print("|    M    |     R$ 45,00       |     R$ 48,00    | ")
print("|    G    |     R$ 60,00       |     R$ 66,00    | ")
print("--------------------------------------------------")
print("Vamos iniciar seu pedido!")

# Loop principal para fazer os pedidos
while pedidos:
  # Solicitando o tipo de pizza
  tipo_pizza = input("Deseja uma Pizza Salgada ou Pizza Doce? [PS/PD]\n").upper()

  # Pizza Salgada
  if tipo_pizza == "PS":
    print("Você escolheu uma Pizza Salgada!")
     # Solicitando o tamanho da pizza
    tamanho_pizza = input("Qual o tamanho da sua fome? [G/M/P] \n").upper()

    # [PS] tamanhos
    if tamanho_pizza == "G":
      print("Você pediu uma Pizza Salgada Grande: R$ 60.00")
      valor_total_pedido += 60.00
    elif tamanho_pizza == "M":
      print("Você pediu uma Pizza Salgada Média: R$ 45.00")
      valor_total_pedido += 45.00
    elif tamanho_pizza == "P":
      print("Você pediu uma Pizza Salgada Pequena: R$ 30.00")
      valor_total_pedido += 30.00
    else:
      print("Tamanho de pizza inválido!Tente novamente.")
      continue

  # Pizza Doce
  else:
    if tipo_pizza == "PD":
      print("Você escolheu uma Pizza Doce!")
       # Solicitando o tamanho da pizza
      tamanho_pizza = input("Qual o tamanho da sua fome? [G/M/P] \n").upper()

      # [PD] tamanhos
      if tamanho_pizza == "G":
        print("Você pediu uma Pizza Doce Grande: R$ 66.00")
        valor_total_pedido += 66.00
      elif tamanho_pizza == "M":
        print("Você pediu uma Pizza Doce Média: R$ 48.00")
        valor_total_pedido += 48.00
      elif tamanho_pizza == "P":
        print("Você pediu uma Pizza Doce Pequena: R$ 34.00")
        valor_total_pedido += 34.00
      else:
        print("Tamanho de pizza inválido! Tente novamente.")
        continue

    else:
      print("Tipo de pizza inválido! Tente novamente.")
      continue

  # Solicitando se o cliente quer outra pizza
  pedidos = input("Deseja adicionar outro pedido? [S/N] \n").upper()
  if pedidos == "N":
    pedidos = False
    
# Exibindo o valor total do pedido ao final
print("Valor total do seu pedido: R$ %.2f" % valor_total_pedido)
