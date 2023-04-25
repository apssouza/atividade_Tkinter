import tkinter as tk
from tkinter import messagebox
from Entidade import Produtos

# Criando a janela principal e definindo o tamanho
janela = tk.Tk()
janela.geometry("400x400")
janela.config(bg="lavender")

# Criando uma lista de produtos
lista_produtos =[]

#######################################################################################################

# Criando o botão para adicionar produtos
botao_adicionar = tk.Button(janela, text="Adicionar Produto")
def adicionar_produto():
    # Criando uma nova janela para adicionar um produto que aparece acima da janela principal (Toplevel)
    nova_janela = tk.Toplevel(janela)
    nova_janela.geometry("400x400")
    nova_janela.config(bg="lavender")
    nova_janela.title("Adicionar Produto")

    # Criando as entrada para as informações do produto
    nome_label = tk.Label(nova_janela, text="Nome")
    nome_label.pack()

    nome_entry = tk.Entry(nova_janela)
    nome_entry.pack()

    preco_label = tk.Label(nova_janela, text="Preço")
    preco_label.pack()

    preco_entry = tk.Entry(nova_janela)
    preco_entry.pack()

    marca_label = tk.Label(nova_janela, text="Marca")
    marca_label.pack()

    marca_entry = tk.Entry(nova_janela)
    marca_entry.pack()

    categoria_label = tk.Label(nova_janela, text="Categoria")
    categoria_label.pack()

    categoria_entry = tk.Entry(nova_janela)
    categoria_entry.pack()

    # Criando a função para adicionar o produto
    def adicionar():
        nome = nome_entry.get()
        preco = float(preco_entry.get())
        marca = marca_entry.get()
        categoria = categoria_entry.get()

        produto = Produtos.Categoria(nome, preco, marca, categoria)
        lista_produtos.append(produto)

        nova_janela.destroy()

    # Criando o botão "Adicionar"
    botao_adicionar = tk.Button(nova_janela, text="Adicionar", command=adicionar)
    botao_adicionar.pack()

# Adicionando a funcionalidade do botão
botao_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto,bg='LightBlue')
botao_adicionar.pack()

##############################################################################################################

# Criando o botão para remover produtos
botao_remover = tk.Button(janela, text="Remover Produto")

def remover_produto():
    # Criando uma nova janela para entrada de dados
    nova_janela = tk.Toplevel(janela)
    nova_janela.geometry("400x400")
    nova_janela.config(bg="lavender")
    nova_janela.title("Remover Produto")

    # Criando um label e entrada de texto para o nome do produto
    label_nome = tk.Label(nova_janela, text="Nome do produto:")
    label_nome.pack()
    entrada_nome = tk.Entry(nova_janela)
    entrada_nome.pack()

    # Função para remover o produto da lista
    def remover():
        nome_produto = entrada_nome.get()
        for produto in lista_produtos:
            if produto.get_nome() == nome_produto:
                lista_produtos.remove(produto)
                messagebox.showinfo("Remoção de produto", f"{nome_produto} foi removido com sucesso!")
                nova_janela.destroy()
            else:
                return
                messagebox.showerror("Erro", f"A remoção não foi concluída porque {nome_produto} não foi encontrado na lista.")

    # Cria o botão para remover o produto
    botao_remover = tk.Button(nova_janela, text="Remover Produto", command=remover,bg='LightBlue')
    botao_remover.pack()


##############################################################################################################

# Cria o botão para mostrar produtos
def mostrar_produtos():
    if len(lista_produtos) == 0:
        messagebox.showwarning("Lista de produtos", "A lista de produtos está vazia.")
    else:
        mensagem = "Lista de Produtos:\n\n"
        for produto in lista_produtos:
            mensagem += f"Nome: {produto.nome}\nPreço: R${produto.preco:.2f}\nMarca: {produto.marca}\nCategoria: {produto.categoria}\n\n"
        messagebox.showinfo("--- Lista de produtos ---", mensagem)

botao_mostrar = tk.Button(janela, text="Mostrar Produtos", command=mostrar_produtos, bg='LightBlue')
botao_mostrar.pack()

# Iniciando a janela principal
janela.mainloop()
