from abc import ABC, abstractmethod
from datetime import datetime


class Pessoa(ABC):
    """
    Define a classe Pessoa
    - recebe: nome
    """

    # toda pessoa deve ter um nome
    def __init__(self, nome: str):
        self.__nome = nome.title()

    # encapsula o atributo nome para que ele
    # não seja alterado diretamente
    @property
    def nome(self):
        return self.__nome

    def __str__(self) -> str:
        return f"{self.nome}"


class Autor(Pessoa):
    """
    Define a classe Autor
    - recebe: nome
    """

    def __init__(self, nome: str):
        super().__init__(nome)

    def __str__(self) -> str:
        return f"Autor: {self.nome}"


class Usuario(Pessoa):
    """
    Define a classe Usuário
    - recebe: nome, telefone e nacionalidade
    """

    def __init__(self, nome: str, telefone: str, nacionalidade: str):
        super().__init__(nome)
        self.telefone = telefone
        self.__nacionalidade = nacionalidade

    @property
    def nacionalidade(self):
        return self.nacionalidade

    def __str__(self):
        return f"Nome: {self.nome}, Telefone {self.telephone}, Nacionalidade: {self.nacionalidade}"


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
    def quantidade_exemplares_disponiveis(self):
        """Retorna o número de exemplares disponíveis para empréstimo."""
        return sum(
            1 for exemplar in self._exemplares if exemplar.estado == "disponível"
        )

    def __str__(self) -> str:
        return f"{self.titulo}, {self.autores}, {self.editora} - {self.quantidade_exemplares_disponiveis}"

    @property
    def possui_exemplares_disponiveis(self):
        """Retorna True se houver pelo menos um exemplar disponível"""
        return self.quantidade_exemplares_disponiveis > 0


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

livro1 = Livro(
    "Harry Potter e a Pedra Filosofal", "Rocco", [autor1], ["Fantasia", "Aventura"]
)

# Adicionando exemplares
exemplar1 = Exemplar(livro1)
livro1.adicionar_exemplar(exemplar1)
exemplar2 = Exemplar(livro1)
livro1.adicionar_exemplar(exemplar2)
usuario1 = Usuario("João da Silva", "1111-2222", "Brasileiro")

emprestimo1 = Emprestimo(usuario1, exemplar1, max_renovacoes=2)
exemplar1.emprestar()
exemplar2.emprestar()

emprestimo1.devolver()

if livro1.possui_exemplares_disponiveis:
    print(f"Ainda há exemplares disponíveis de '{livro1.titulo}'")
else:
    print(f"Não há mais exemplares de '{livro1.titulo}'")

print(f"Usuário: {emprestimo1.usuario.nome}")
print(f"Livro: {emprestimo1.exemplar.livro.titulo}")
print(f"Data de Empréstimo: {emprestimo1.data_emprestimo}")
print(f"Data de Devolução: {emprestimo1.data_devolucao}")
print(f"Estado do Empréstimo: {emprestimo1.estado}")

# Verificando a quantidade de exemplares disponíveis
print(
    f"Exemplares disponíveis de '{livro1.titulo}': {livro1.quantidade_exemplares_disponiveis}"
)
