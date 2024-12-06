print("Bem-vindo ao Sistema de Planos de Saúde")
print("desevolvido por Nicolle Ramos Batista!")

# Solicitação do valor base do plano e idade do cliente
valor_base = float(input("Informe o valor base do seu plano: R$ "))
idade_cliente = int(input("Informe a sua idade: "))

valor_mensal = 0.00
# Exibindo o valor mensal calculado
if idade_cliente >= 0 and idade_cliente < 19:
  valor_mensal = valor_base * (100/100)
elif idade_cliente >= 19 and idade_cliente < 29:
  valor_mensal = valor_base * (150/100)
elif idade_cliente >= 29 and idade_cliente < 39:
  valor_mensal = valor_base * (225/100)
elif idade_cliente >= 39 and idade_cliente < 49:
  valor_mensal = valor_base * (240/100)
elif idade_cliente >= 49 and idade_cliente < 59:
  valor_mensal = valor_base * (350/100)
elif idade_cliente >= 59:
  valor_mensal = valor_base * (600/100)
else:
  print("Idade inválida")

# Exibindo o valor mensal calculado
print("O valor mensal do seu plano é: R$ %.2f" % valor_mensal)
