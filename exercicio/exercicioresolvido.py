from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa(ABC):
    """
        Define a classe Pessoa
        - recebe: nome e telefone
    """
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome.title()
        self.telefone = telefone

    # encapsula o atributo nome para que ele
    # não seja alterado diretamente
    @property
    def nome(self):
        return self.__nome
    
  
    @abstractmethod 
    def get_info(self):
        pass

class Autor(Pessoa):
    """
        Define a classe Autor
        - recebe: nome
    """
    def __init__(self, nome: str):
        # usa None para o valor do telefone do autor
        super().__init__(nome, None)

    # usaria o método __str__ aqui para retornar os valores
    def get_info(self): 
        return f"Autor: {self.nome}"
    
    def __str__(self) -> str:
        return f'{self.nome}'

class Usuario(Pessoa):
    """
        Define a classe Usuário
        - recebe: nome e telefone
    """
    def __init__(self, nome: str, telefone: str):
        super().__init__(nome, telefone)

    # usaria o método __str__ aqui para retornar os valore.
    # dessa forma preciso chamar um novo método pra ter o 
    # retorno da string formatada, com __str__ posso retornar 
    # uma string chamando diretamente do objeto.
    def get_info(self):
        return f"Usuário: {self.nome}, Telefone: {self.telefone}"

class Livro:
    def __init__(self, titulo, editora, autores, generos):
        self.titulo = titulo
        self.editora = editora
        self.autores = autores  # Lista de objetos Autor
        self.generos = generos  # Lista de gêneros
        self._exemplares = []  # Lista de objetos Exemplar
    
    def adicionar_exemplar(self, exemplar):
        self._exemplares.append(exemplar)

    def remover_exemplar(self):
        if self._exemplares:
            return self._exemplares.pop(0)
        return None

    @property
    def exemplares_disponiveis(self):
        """Retorna o número de exemplares disponíveis para empréstimo."""
        return len(self._exemplares)
    
    def __str__(self) -> str:
        return f'{self.titulo}, {self.autores}, {self.editora} - {self.exemplares_disponiveis}'

class Exemplar:
    def __init__(self, livro):
        self.livro = livro
        self.estado = "disponível"

    def emprestar(self):
        self.estado = "emprestado"

    def devolver(self):
        self.estado = "disponível"

class Emprestimo:
    def __init__(self, usuario, exemplar, max_renovacoes=0):
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
        self.renovacoes = 0
        self.max_renovacoes = max_renovacoes
        self.estado = "emprestado"

    def devolver(self):
        self.data_devolucao = datetime.now()
        self.estado = "devolvido"
        self.exemplar.devolver()

    def renovar(self):
        if self.renovacoes < self.max_renovacoes:
            self.renovacoes += 1
            self.data_emprestimo = datetime.now()
        else:
            print("Número máximo de renovações atingido.")

autor1 = Autor("J.K. Rowling")

livro1 = Livro("Harry Potter e a Pedra Filosofal", "Rocco", [autor1], ["Fantasia", "Aventura"])

exemplar1 = Exemplar(livro1)
livro1.adicionar_exemplar(exemplar1)

usuario1 = Usuario("João da Silva", "1111-2222")

emprestimo1 = Emprestimo(usuario1, exemplar1, max_renovacoes=2)
exemplar1.emprestar()

emprestimo1.devolver()

print(f"Usuário: {emprestimo1.usuario.nome}")
print(f"Livro: {emprestimo1.exemplar.livro.titulo}")
print(f"Data de Empréstimo: {emprestimo1.data_emprestimo}")
print(f"Data de Devolução: {emprestimo1.data_devolucao}")
print(f"Estado do Empréstimo: {emprestimo1.estado}")

print(f"Exemplares disponíveis de '{livro1.titulo}': {livro1.exemplares_disponiveis}")
