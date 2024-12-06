valor_total = 0

print("Sorveteria Gelatto")
print("bem-vindo ao sistema de vendas de sorvetes!")
tipo_sorvete = input("|*| Entre com o tipo do sorvete! [casquinha/cascão/cestinha]:\n")
sabor_sorvete = input("|*| Entre com o sabor do sorvete [morango/creme/chocolate]:\n")
cobertura_sorvete = input("|*| Entre com a cobertura do sorvete [caramelo/morango/chocolate]:\n")

if tipo_sorvete == "casquinha":
  valor_total += 1.00
elif tipo_sorvete == "cascao":
  valor_total += 2.50
elif tipo_sorvete == "cestinha":
  valor_total += 4.00
else:
  print("|*| Tipo de sorvete inválido!")

if cobertura_sorvete == "caramelo" or cobertura_sorvete == "morango" or cobertura_sorvete == "chocolate":
  valor_total += 1.50
  print("|*| Pedido pronto!! (๑•̀ㅂ•́)و✧")
  print(f"|*| O valor total do seu pedido é: R$ {valor_total:.2f}")
elif cobertura_sorvete == "sem cobertura":
  valor_total += 0.00
  print("|*| Pedido pronto!! (๑•̀ㅂ•́)و✧")
  print(f"|*| O valor total do seu pedido é: R$ {valor_total:.2f}")
else:
  print("|*| Cobertura inválida!")
  print("|*| Não foi possível realizar seu pedido!! ( ﾟдﾟ)つ NãOo")
  
