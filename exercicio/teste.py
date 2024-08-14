from exercicioresolvido import Autor, Usuario, Livro, Exemplar

# adicionando usuários e autores
usuario_teste = Usuario('Maria de Fátima', '48 99999 0000')
info_usuario_teste = usuario_teste.get_info()
print(info_usuario_teste)

autor_teste = Autor('Milton Santos')
info_autor_teste = autor_teste.get_info()
print(info_autor_teste)

# testa o encapsulamento do atributo nome
usuario_teste.__nome = 'José'
usuario_teste.telefone = '49 00000 9999'
info_usuario_teste = usuario_teste.get_info()
print(info_usuario_teste)

# iniciando um livro e testando disponibilidade
livro_teste = Livro('Por uma outra globalização', 'Record', autor_teste, ['geopolítica', 'ciências sociais'])

print(livro_teste)
livro_teste._exemplares = [4]

# adicionando exemplares
livro_teste.adicionar_exemplar(livro_teste)
livro_teste.adicionar_exemplar(livro_teste)
livro_teste.adicionar_exemplar(livro_teste)

# conferindo operação
print(livro_teste.generos, livro_teste)