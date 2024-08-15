# ---- Testes ----

from exercicio.exercicioresolvido import *

# Criando instâncias de autor, livro e funcionário
autor1 = Autor("J.K. Rowling", "1234-5678", email="jk@example.com")
livro1 = Livro("Harry Potter e a Pedra Filosofal", "Rocco", [autor1], ["Fantasia", "Aventura"], "Português", 223, isbn="978-3-16-148410-0", ano_publicacao=1997, sinopse="Um menino descobre que é um bruxo.")
funcionario1 = Funcionario("Ana Maria", "9999-8888", email="ana@example.com", cargo="Bibliotecária")

# Adicionando exemplares ao livro
exemplar1 = Exemplar(livro1)
exemplar2 = Exemplar(livro1)
livro1.adicionar_exemplar(exemplar1)
livro1.adicionar_exemplar(exemplar2)

# Criando usuários
usuario1 = Usuario("João da Silva", "1111-2222", email="joao@example.com")
usuario2 = Usuario("Maria Oliveira", "3333-4444", email="maria@example.com")

# Realizando um empréstimo
emprestimo1 = Emprestimo(usuario1, exemplar1, max_renovacoes=2)
exemplar1.emprestar()

# Exibindo informações
print(f"Informações do Autor: {autor1.get_info()}")
print(f"Livros do Autor: {autor1.listar_livros([livro1])}")

print(f"Informações do Usuário 1: {usuario1.get_info()}")
print(f"Empréstimos do Usuário 1: {usuario1.listar_emprestimos()}")

print(f"Informações do Usuário 2: {usuario2.get_info()}")

print(f"Exemplares disponíveis de '{livro1.titulo}': {livro1.exemplares_disponiveis}")

# Testando renovação e devolução
emprestimo1.renovar()
print(f"Data de Empréstimo após renovação: {emprestimo1.data_emprestimo}")
print(f"Data de Devolução Prevista após renovação: {emprestimo1.data_devolucao_prevista}")

emprestimo1.devolver()
print(f"Estado do Empréstimo após devolução: {emprestimo1.estado}")
print(f"Exemplares disponíveis de '{livro1.titulo}' após devolução: {livro1.exemplares_disponiveis}")

# Testando atraso de empréstimo
emprestimo2 = Emprestimo(usuario2, exemplar2, max_renovacoes=1, duracao_emprestimo=1)  # Empréstimo de 1 dia
exemplar2.emprestar()

# Simulando um atraso (aumentando artificialmente a data de empréstimo)
emprestimo2.data_emprestimo -= timedelta(days=2)
emprestimo2.data_devolucao_prevista = emprestimo2.data_emprestimo + timedelta(days=1)

print(f"O empréstimo 2 está atrasado? {emprestimo2.esta_atrasado()}")

# Calculando multa para o empréstimo atrasado
multa_emprestimo2 = Multa(emprestimo2)
print(f"Multa devida: R$ {multa_emprestimo2.calcular_multa():.2f}")

# Criando uma reserva para um livro que está emprestado
reserva1 = Reserva(usuario1, livro1)
print(f"Reservas do Usuário 1: {usuario1.listar_reservas()}")

# Registrando eventos no log
log = Log()
log.registrar_evento("Empréstimo realizado.")
log.registrar_evento("Livro devolvido.")
log.registrar_evento("Multa aplicada.")
log.registrar_evento(f"Usuário {usuario1.nome} fez uma reserva.")

print("Logs de eventos:")
print(log.exibir_logs())
