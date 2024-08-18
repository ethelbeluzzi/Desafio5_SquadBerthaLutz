# 💻 Bootcamp Back-end Python & Django da WoMakersCode 👩‍💻

Bem-vindo ao repositório dos exercícios do Desafio 5 da Semana 04 do Bootcamp Back-end Python e Django do Squad Bertha Lutz.

## Integrantes: 👩‍💻

- **Ethel Panitsa Beluzzi**  
  Responsável pela criação do modelo base.

- **Hyngrid Souza e Silva**  
  Revisão geral e melhoria das explicações no README.

- **Karine Yasmin dos Santos Ribeiro**  
  Revisão e melhoria do código, com foco no conceito de classe abstrata, além de uma explicação breve do seu uso no código.

- **Larissa Vital Caetano Pereira**  
  Revisão e melhoria do código, com foco no conceito de propriedade, além de uma explicação breve do seu uso no código.

- **Louise Silva Ferreira**  
  Revisão e melhoria do código, com foco no conceito de classe, além de uma explicação breve do seu uso no código.

- **Marina Caponera Silva**  
  Revisão e melhoria do código, com foco no conceito de encapsulamento, além de uma explicação breve do seu uso no código.

- **Natália do Nascimento da Costa**  
  Revisão geral do código e realização de testes completos.

- **Sofia Nakamaru**  
  Revisão e melhoria do código, com foco no conceito de herança, além de uma explicação breve do seu uso no código.

---

## 🧩 Descrição do Desafio

Este projeto faz parte do Desafio 5 da Semana 04 do Bootcamp Back-end Python e Django, com o objetivo de construir um sistema de gerenciamento de biblioteca utilizando conceitos fundamentais de programação orientada a objetos (POO) em Python. O sistema permite a interação entre autores, usuários, livros e o processo de empréstimo, seguindo um design modular e organizado.

---

## 🔍 Explorando o Conceito de Classe

Os conceitos de classe aparecem em nosso sistema de gerenciamento de biblioteca de maneira fundamental, organizando as informações e funcionalidades em componentes bem definidos e modularizados. Cada classe representa um elemento essencial da biblioteca, facilitando a interação entre autores, usuários, livros e o processo de empréstimo.

### 📚 Classe `Pessoa` - A Base Abstrata para Autores e Usuários

Uma classe abstrata em programação orientada a objetos é uma classe que não pode ser instanciada diretamente e serve como um modelo para outras classes. Seu propósito é fornecer uma base comum para um grupo de subclasses, garantindo que elas implementem certos métodos e atributos. Classes abstratas são uma maneira de definir uma interface que outras classes devem seguir, ajudando a promover um design mais organizado e modular.

#### Atributos:
- **`nome`**: Nome da pessoa, armazenado de forma privada para garantir encapsulamento.

#### Métodos:
- **`__str__()`**: Um método abstrato que deve ser implementado pelas subclasses para fornecer detalhes específicos.

### ✒️ Classe `Autor` - Representando Criadores de Conteúdo

A classe `Autor` herda de `Pessoa` e se especializa em representar os autores dos livros da biblioteca. Além das informações pessoais herdadas, `Autor` pode listar os livros que escreveu, integrando-se diretamente ao acervo da biblioteca.

#### Atributos:
- Herdados da classe `Pessoa`.

#### Métodos:
- **`__str__()`**: Retorna uma string com os detalhes do autor.
- **`listar_livros(livros)`**: Gera uma lista dos títulos de livros associados a este autor.

### 👥 Classe `Usuario` - Pessoas que Usam a Biblioteca

A classe `Usuario` também herda de `Pessoa`, mas é focada nos leitores que utilizam a biblioteca. Esta classe gerencia os empréstimos feitos pelo usuário, permitindo que eles acessem e controlem suas atividades na biblioteca.

#### Atributos:
- **`nome`**: Nome do usuário.
- **`telefone`**: Telefone do usuário.
- **`nacionalidade`**: Nacionalidade do usuário.
- **`email`**: Email do usuário.
- **`emprestimos`**: Lista de empréstimos associados ao usuário.
- **`reservas`**: Lista de reservas feitas pelo usuário.
- **`numero_cadastro`**: Número de cadastro único, gerado automaticamente ao criar o usuário, facilitando o gerenciamento e identificação de usuários.

#### Métodos:
- **`__str__()`**: Retorna uma string com os detalhes do usuário.
- **`adicionar_emprestimo(emprestimo)`**: Adiciona um novo empréstimo ao histórico do usuário.
- **`listar_emprestimos()`**: Retorna uma lista de livros emprestados pelo usuário, com as respectivas datas de devolução.
- **`listar_reservas()`**: Retorna uma lista de livros reservados pelo usuário.

### 📖 Classe `Livro` - A Essência do Acervo

A classe `Livro` representa os livros disponíveis na biblioteca. Com atributos que vão desde o título até o ISBN, essa classe é a chave para organizar e gerenciar o acervo de maneira eficiente.

#### Atributos:
- **`titulo`**: Título do livro.
- **`editora`**: Nome da editora.
- **`autores`**: Lista de objetos `Autor`.
- **`generos`**: Lista de gêneros literários.
- **`isbn`**: Número ISBN (opcional).
- **`ano_publicacao`**: Ano de publicação (opcional).
- **`sinopse`**: Breve descrição do livro (opcional).
- **`_exemplares`**: Lista de objetos `Exemplar` disponíveis.
- **`lingua`**: Língua em que o livro está escrito.
- **`num_paginas`**: Número de páginas do livro.

#### Métodos:
- **`adicionar_exemplar(exemplar)`**: Adiciona um exemplar do livro ao acervo.
- **`remover_exemplar()`**: Remove um exemplar do acervo.
- **`exemplares_disponiveis()`**: Retorna o número de exemplares disponíveis para empréstimo.
- **`possui_exemplares_disponiveis()`**: Retorna `True` se houver pelo menos um exemplar disponível.

### 📚 Classe `Exemplar` - Gerenciando as Cópias Físicas

A classe `Exemplar` representa uma cópia física de um livro. Cada `Exemplar` tem um estado que indica se ele está disponível para empréstimo ou se está emprestado.

#### Atributos:
- **`livro`**: O objeto `Livro` ao qual o exemplar pertence.
- **`estado`**: Estado atual do exemplar (disponível ou emprestado).

#### Métodos:
- **`emprestar()`**: Marca o exemplar como emprestado.
- **`devolver()`**: Marca o exemplar como disponível.

### 🔄 Classe `Emprestimo` - Orquestrando o Ciclo de Empréstimos

A classe `Emprestimo` é a espinha dorsal do sistema de empréstimos, gerenciando todo o ciclo de vida de um empréstimo, desde a retirada do livro até a sua devolução ou renovação.

#### Atributos:
- **`usuario`**: O objeto `Usuario` que fez o empréstimo.
- **`exemplar`**: O objeto `Exemplar` que foi emprestado.
- **`data_emprestimo`**: Data em que o empréstimo foi feito.
- **`data_devolucao_prevista`**: Data prevista para a devolução.
- **`data_devolucao`**: Data real de devolução (se já devolvido).
- **`renovacoes`**: Número de vezes que o empréstimo foi renovado.
- **`max_renovacoes`**: Número máximo de renovações permitido.
- **`estado`**: Estado atual do empréstimo (emprestado ou devolvido).

#### Métodos:
- **`devolver()`**: Marca o empréstimo como devolvido e atualiza o estado do exemplar.
- **`renovar()`**: Renova o empréstimo, ajustando a data de devolução prevista.
- **`esta_atrasado()`**: Verifica se o empréstimo está atrasado.

### 🔄 Subclasses `EmprestimoDigital` e `EmprestimoFisico`

Essas subclasses diferenciam os diferentes comportamentos dos empréstimos. O método `tipo_emprestimo()` identifica e retorna o tipo (digital ou físico). `EmprestimoDigital` retorna "Empréstimo Digital" e `EmprestimoFisico` retorna "Empréstimo Físico". Este método permite diferenciar claramente os tipos de empréstimo, mantendo a lógica básica na classe base e implementando as especificidades nas subclasses.

### 📚 Classe `Multa` - Gerenciando Multas por Atraso

A classe `Multa` foi adicionada para calcular e gerenciar multas para empréstimos atrasados, proporcionando uma camada extra de controle sobre os empréstimos na biblioteca.

#### Métodos:
- **`calcular_multa()`**: Calcula o valor devido com base nos dias de atraso do empréstimo.

### 📚 Classe `Reserva` - Gerenciando Reservas de Livros

A classe `Reserva` foi adicionada para permitir que os usuários reservem livros quando todos os exemplares estiverem emprestados. Essa funcionalidade melhora o gerenciamento de disponibilidade e a experiência dos usuários

 da biblioteca.

#### Atributos:
- **`usuario`**: O objeto `Usuario` que fez a reserva.
- **`livro`**: O objeto `Livro` que foi reservado.
- **`data_reserva`**: Data em que a reserva foi feita.

### 📚 Classe `Log` - Registro de Eventos

A classe `Log` foi introduzida para registrar eventos importantes no sistema, como empréstimos, devoluções, aplicação de multas e reservas. Essa funcionalidade é útil para manter um histórico de atividades e auditoria.

#### Métodos:
- **`registrar_evento(evento)`**: Registra um novo evento no log.
- **`exibir_logs()`**: Exibe todos os eventos registrados.

---

## 🌟 Conclusão

Cada classe no nosso sistema foi projetada para representar aspectos importantes do gerenciamento de uma biblioteca, desde a gestão dos livros e autores até o controle dos empréstimos e das interações dos usuários. 

### 🧩 Conceitos

- **Classe Abstrata**: Utilizada para fornecer uma interface comum para as subclasses `Autor` e `Usuario`, garantindo que métodos como `__str__()` sejam implementados.
- **Herança**: Permite que `Autor` e `Usuario` herdem atributos e métodos da classe `Pessoa`, promovendo a reutilização de código.
- **Encapsulamento**: Protege os atributos, como `__nome` em `Pessoa`, impedindo alterações diretas e controlando o acesso por meio de propriedades.
- **Propriedade**: Usada para calcular e retornar dinamicamente o número de exemplares disponíveis na classe `Livro`, garantindo que os dados estejam sempre atualizados sem a necessidade de armazenamento redundante.

---

## 📅 Atualizações Recentes

- **15/08/2024**: 
  - Adicionada a classe `Multa` para gerenciar multas por atrasos.
  - Adicionadas as classes `Reserva` e `Log` para melhorar o gerenciamento de reservas e o registro de eventos.
  - Adição de novos atributos na classe `Livro` para fornecer mais informações detalhadas sobre o acervo, como `lingua` e `num_paginas`.
  - Melhorias na classe `Usuario`, com a adição do atributo `numero_cadastro`.

