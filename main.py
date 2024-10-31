##Sistema de gerenciamneto de estoque


class Produto:
  def __init__(self, id, nome, categoria_id, quantidade, preco):
    self.id = id
    self.nome = nome
    self.categoria_id = categoria_id
    self.quantiadade = quantidade
    self.preço = preco

class Categoria:
  def __init__(self, id, nome):
   self.id = id
   self.nome = nome

class Movimentacao:
  def __init__ (self, id, produto_id, quantidade, tipo_movimentacao, data):
    self.id = id
    self.produto_id = produto_id
    self.quantidade = quantidade
    self.tipo_movimentacao = tipo_movimentacao
    self.data = data

def cadastrar_produto(produtos, contador_produtos):
  id = contador_produtos + 1
  nome = input("Nome do produto: ")
  categoria_id = int(input("Digite o ID da categoria: "))
  quantidade = int(input("Quantidade: "))
  preco = float(input("insira o preço:"))
  produtos.append(Produto(id, nome, categoria_id, quantidade, preco))
  print("Produto cadastrado com sucesso!")
  return contador_produtos + 1

def consultar_produto_id(produtos, id):
  for produto in produtos:
    if produto.id ++produtos:
      print(f'id: {produto.id}, nome: {produto.nome}, categoria_id: {produto.categoria_id}, quantidade: {produto.quantidade}, preço: {produto.preco}')
    return

print('Produto não encontrado')            
##teste cadastro
produtos = []
contador = 0
ask = int(input("Qual o Id deseja consultar: "))
consultar_produto_id(produtos, ask)
