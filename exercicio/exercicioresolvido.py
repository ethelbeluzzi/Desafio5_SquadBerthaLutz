from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Pessoa(ABC):
    def __init__(self, nome, telefone, email=None, endereco=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def exibir_info_completa(self):
        info = f"Nome: {self.nome}, Telefone: {self.telefone}"
        if self.email:
            info += f", Email: {self.email}"
        if self.endereco:
            info += f", Endereço: {self.endereco}"
        return info

    @abstractmethod
    def get_info(self):
        pass

class Autor(Pessoa):
    def get_info(self):
        return f"Autor: {self.nome}, Telefone: {self.telefone}"

    def listar_livros(self, livros):
        return [livro.titulo for livro in livros if self in livro.autores]

class Usuario(Pessoa):
    def __init__(self, nome, telefone, email=None, endereco=None):
        super().__init__(nome, telefone, email, endereco)
        self.emprestimos = []

    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        return [f"{emp.exemplar.livro.titulo} (Devolução: {emp.data_devolucao})" for emp in self.emprestimos]

    def get_info(self):
        return f"Usuário: {self.nome}, Telefone: {self.telefone}"

class Livro:
    def __init__(self, titulo, editora, autores, generos, isbn=None, ano_publicacao=None, sinopse=None):
        self.titulo = titulo
        self.editora = editora
        self.autores = autores  # Lista de objetos Autor
        self.generos = generos  # Lista de gêneros
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.sinopse = sinopse
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
        return len([ex for ex in self._exemplares if ex.estado == "disponível"])

class Exemplar:
    def __init__(self, livro):
        self.livro = livro
        self.estado = "disponível"

    def emprestar(self):
        self.estado = "emprestado"

    def devolver(self):
        self.estado = "disponível"

class Emprestimo:
    def __init__(self, usuario, exemplar, max_renovacoes=0, duracao_emprestimo=14):
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = datetime.now()
        self.data_devolucao_prevista = self.data_emprestimo + timedelta(days=duracao_emprestimo)
        self.data_devolucao = None
        self.renovacoes = 0
        self.max_renovacoes = max_renovacoes
        self.estado = "emprestado"
        usuario.adicionar_emprestimo(self)

    def devolver(self):
        self.data_devolucao = datetime.now()
        self.estado = "devolvido"
        self.exemplar.devolver()

    def renovar(self):
        if self.renovacoes < self.max_renovacoes:
            self.renovacoes += 1
            self.data_emprestimo = datetime.now()
            self.data_devolucao_prevista = self.data_emprestimo + timedelta(days=14)
        else:
            print("Número máximo de renovações atingido.")

    def esta_atrasado(self):
        return datetime.now() > self.data_devolucao_prevista and self.estado == "emprestado"

# ---- Testes ----

# Criando instâncias de autor e livro
autor1 = Autor("J.K. Rowling", "1234-5678", email="jk@example.com")
livro1 = Livro("Harry Potter e a Pedra Filosofal", "Rocco", [autor1], ["Fantasia", "Aventura"], isbn="978-3-16-148410-0", ano_publicacao=1997, sinopse="Um menino descobre que é um bruxo.")

# Adicionando exemplares ao livro
exemplar1 = Exemplar(livro1)
exemplar2 = Exemplar(livro1)
livro1.adicionar_exemplar(exemplar1)
livro1.adicionar_exemplar(exemplar2)

# Criando um usuário
usuario1 = Usuario("João da Silva", "1111-2222", email="joao@example.com")

# Realizando um empréstimo
emprestimo1 = Emprestimo(usuario1, exemplar1, max_renovacoes=2)
exemplar1.emprestar()

# Exibindo informações
print(f"Informações do Autor: {autor1.get_info()}")
print(f"Livros do Autor: {autor1.listar_livros([livro1])}")

print(f"Informações do Usuário: {usuario1.get_info()}")
print(f"Empréstimos do Usuário: {usuario1.listar_emprestimos()}")

print(f"Exemplares disponíveis de '{livro1.titulo}': {livro1.exemplares_disponiveis}")

# Testando renovação e devolução
emprestimo1.renovar()
print(f"Data de Empréstimo após renovação: {emprestimo1.data_emprestimo}")
print(f"Data de Devolução Prevista após renovação: {emprestimo1.data_devolucao_prevista}")

emprestimo1.devolver()
print(f"Estado do Empréstimo após devolução: {emprestimo1.estado}")
print(f"Exemplares disponíveis de '{livro1.titulo}' após devolução: {livro1.exemplares_disponiveis}")

# Testando atraso de empréstimos
emprestimo2 = Emprestimo(usuario1, exemplar2, max_renovacoes=1, duracao_emprestimo=1)  # Empréstimo de 1 dia
exemplar2.emprestar()

# Simulando um atraso (aumentando artificialmente a data de empréstimo)
emprestimo2.data_emprestimo -= timedelta(days=2)
emprestimo2.data_devolucao_prevista = emprestimo2.data_emprestimo + timedelta(days=1)

print(f"O empréstimo 2 está atrasado? {emprestimo2.esta_atrasado()}")
