lista_compras = ['laranja', 'cerveja', 'miojo', 'carvão', 'picanha']
while True:
  item = input("|*| digite um item para pegar da lista de compras: ")
  if item in lista_compras:
    print(f"|*| {item} está na lista de compras!")
    break
  else:
    print(f"|*| {item} não está na lista de compras!")
  