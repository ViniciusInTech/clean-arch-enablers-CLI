# CAE(Clean arch enablers)

O CAE foi concebido como uma ferramenta valiosa para desenvolvedores, simplificando e acelerando o processo de criação de projetos que adotam a Clean Architecture.
Através de comandos simples no terminal, o CAE permite a criação de estruturas de projetos padronizadas de acordo com suas necessidades específicas.
Além disso, viabiliza a criação ágil de casos de uso e a atualização de dependências entre as camadas do projeto.



## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Instalação

### Status da Instalação Atual (Windows)

Atualmente, o CAE não oferece um instalador simplificado, o que é parte de nossos planos futuros. Isso se deve às melhorias e mudanças constantes em andamento. Uma versão mais intuitiva está em desenvolvimento, planejada para concluir ajustes na identidade visual, sintaxe e otimização do código.

### Planos para Outros Sistemas Operacionais

Estamos comprometidos em tornar o CAE compatível com outros sistemas operacionais. Estamos trabalhando em tornar o código mais flexível para possibilitar o uso em plataformas diferentes.

### Uso Atual no Windows

Para utilizar o CAE no Windows atualmente, é necessário baixar o código-fonte do CAE. Após isso, modifique o arquivo .bat para apontar para a localização do executável principal do CAE em seu computador e adicione o CAE como uma variável de ambiente.

### Uso e Adaptação

Posteriormente, ajuste o arquivo template .json para se adequar às suas necessidades específicas e utilize o CAE conforme desejado.

## Uso

Atualmente, o CAE oferece alguns comandos principais. O primeiro é utilizado para criar a estrutura completa do projeto e também para criar casos de uso.

### Comando para Criação de Projeto

A criação do projeto é realizada utilizando o seguinte comando:

```bash
cae new project nome_projeto com.example
```

Este comando é utilizado para criar projetos completos, utilizando templates que podem ser personalizados através da manipulação do arquivo .json.

### Comando para Criação de casos de usos

A criação dos casos de uso é realizada utilizando o seguinte comando:

```bash
cae new function nome_caso_de_uso
```

Este comando é utilizando para a criação dos casos de usos, lembrando que temos suporte para as seguintes function: fuc, suc, cuc e ruc.

## Licença

O CAE foi desenvolvido por Carlos Vinicius e Lucio. A utilização por terceiros é gratuita, com a única exigência de créditos aos desenvolvedores.

### Perfil no GitHub

- [Perfil de Carlos Vinicius](https://github.com/vinicius123131)
- [Perfil de Lucio](https://github.com/julucinho)

