from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @abstractmethod
    def get_info(self):
        pass

class Autor(Pessoa):
    def get_info(self):
        return f"Autor: {self.nome}, Telefone: {self.telefone}"

class Usuario(Pessoa):
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
class EmprestimoDigital(Emprestimo):
        def tipo_emprestimo(self):
            return "Emprestimo Digital"
        
class EmprestimoFisico(Emprestimo):
        def tipo_emprestimo(self):
            return "Emprestimo Fisico"

autor1 = Autor("J.K. Rowling", "1234-5678")

livro1 = Livro("Harry Potter e a Pedra Filosofal", "Rocco", [autor1], ["Fantasia", "Aventura"])

exemplar1 = Exemplar(livro1)
livro1.adicionar_exemplar(exemplar1)

usuario1 = Usuario("João da Silva", "1111-2222")

emprestimo_fisico= EmprestimoFisico(usuario1, exemplar1, max_renovacoes=2)
exemplar1.emprestar()

emprestimo_fisico.devolver()

print(f"Tipo de Empréstimo: {emprestimo_fisico.tipo_emprestimo()}")
print(f"Usuário: {emprestimo_fisico.usuario.nome}")
print(f"Livro: {emprestimo_fisico.exemplar.livro.titulo}")
print(f"Data de Empréstimo: {emprestimo_fisico.data_emprestimo}")
print(f"Data de Devolução: {emprestimo_fisico.data_devolucao}")
print(f"Estado do Empréstimo: {emprestimo_fisico.estado}")
print(f"Exemplares disponíveis de '{livro1.titulo}': {livro1.exemplares_disponiveis}")
