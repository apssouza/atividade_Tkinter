class Produtos:
    """
    Classe para criar objetos do tipo Produto.

    Atributos:
    nome (str): O nome do produto.
    preco (float): O preço do produto.
    marca (str): A marca do produto.
    """

    def __init__(self, nome, preco, marca):
        """
        Inicializa um objeto do tipo Produto.

        Args:
        nome (str): O nome do produto.
        preco (float): O preço do produto.
        marca (str): A marca do produto.
        """
        self.nome = nome
        self.preco = preco
        self.marca = marca

    def get_nome(self):
        '''
        Método get que retorna o nome do produto

        :return: Nome do produto
        '''
        return self.nome

    def get_preco(self):
        '''
        Método get que retorna o preço do produto

        :return: Preço do produto
        '''
        return self.preco

    def get_marca(self):
        '''
        Método get que retorna a marca do produto

        :return: Marca do produto
        '''
        return self.marca

    def set_nome(self, nome):
        '''
        Método set que define um novo nome para o produto

        nome: Novo nome para o produto
        '''
        self.nome = nome

    def set_preco(self, preco):
        '''
        Método set que define uma nova categoria para o produto

        preco: Novo preco para o produto
        '''
        self.preco = preco

    def set_marca(self, marca):
        '''
        Método set que define uma nova marca para o produto

        marca: Nova marca para o produto
        '''
        self.marca = marca


class Categoria(Produtos):
    """
    Classe para criar objetos do tipo Categoria, que herda atributos e métodos da classe Produto.

    Atributos:
    categoria (str): A categoria do produto.
    """

    def __init__(self, nome, preco, marca,categoria):
        """
        Inicializa um objeto do tipo Categoria.

        Args:
        nome (str): O nome do produto.
        preco (float): O preço do produto.
        marca (str): A marca do produto.
        categoria (str): A categoria do produto.
        """
        super().__init__(nome, preco, marca)
        self.categoria = categoria

    def get_categoria(self):
        '''
        Método get que retorna a categoria do produto

        :return: Categoria do produto
        '''
        return self.categoria

    def set_categoria(self,categoria):
        '''
        Método set que define uma nova categoria para o produto

        categoria: Nova categoria do produto
        '''
        self.categoria = categoria


