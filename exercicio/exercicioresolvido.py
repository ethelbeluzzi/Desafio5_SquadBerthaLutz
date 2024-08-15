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

class Funcionario(Pessoa):
    def __init__(self, nome, telefone, email=None, endereco=None, cargo=None):
        super().__init__(nome, telefone, email, endereco)
        self.cargo = cargo

    def get_info(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}"

class Usuario(Pessoa):
    contador_cadastro = 1  # Variável de classe para controle de número de cadastro

    def __init__(self, nome, telefone, email=None, endereco=None):
        super().__init__(nome, telefone, email, endereco)
        self.emprestimos = []
        self.reservas = []
        self.numero_cadastro = Usuario.contador_cadastro
        Usuario.contador_cadastro += 1  # Incrementa o número de cadastro para o próximo usuário

    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        return [f"{emp.exemplar.livro.titulo} (Devolução: {emp.data_devolucao})" for emp in self.emprestimos]

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

    def listar_reservas(self):
        return [f"Reserva: {reserva.livro.titulo}" for reserva in self.reservas]

    def get_info(self):
        return f"Usuário: {self.nome}, Telefone: {self.telefone}, Cadastro Nº: {self.numero_cadastro}"

class Livro:
    def __init__(self, titulo, editora, autores, generos, lingua, num_paginas, isbn=None, ano_publicacao=None, sinopse=None):
        self.titulo = titulo
        self.editora = editora
        self.autores = autores  # Lista de objetos Autor
        self.generos = generos  # Lista de gêneros
        self.lingua = lingua  # Língua do livro
        self.num_paginas = num_paginas  # Número de páginas do livro
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

class Reserva:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        usuario.adicionar_reserva(self)

class Multa:
    def __init__(self, emprestimo, valor_por_dia=1.0):
        self.emprestimo = emprestimo
        self.valor_por_dia = valor_por_dia

    def calcular_multa(self):
        if self.emprestimo.esta_atrasado():
            dias_atraso = (datetime.now() - self.emprestimo.data_devolucao_prevista).days
            return dias_atraso * self.valor_por_dia
        return 0.0

class Log:
    def __init__(self):
        self.eventos = []

    def registrar_evento(self, descricao):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.eventos.append(f"{timestamp} - {descricao}")

    def exibir_logs(self):
        return "\n".join(self.eventos)
