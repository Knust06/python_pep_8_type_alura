# Projeto Python PEP 8 e Tipagem

Este repositório contém um projeto Python desenvolvido seguindo as boas práticas recomendadas pela PEP 8 e utilizando tipagem estática.

## Estrutura do Projeto

O projeto inclui vários módulos que gerenciam diferentes tipos de filas de processamento. Aqui está uma breve descrição dos principais arquivos:

- `constantes.py`: Contém as constantes usadas em todo o projeto.
- `fila_base.py`: Define a classe base para as filas.
- `fila_normal.py`: Implementa a fila de processamento normal.
- `fila_prioritaria.py`: Implementa a fila de processamento prioritário.
- `fabrica_fila.py`: Uma fábrica para criar instâncias de filas.
- `estatistica_resumida.py` e `estatistica_detalhada.py`: Módulos para gerar estatísticas das filas.
- `main.py`: Ponto de entrada do projeto que utiliza os módulos mencionados.

## Qualidade de Código

Para garantir a qualidade do código, o projeto utiliza a seguinte ferramenta:

### Flake8

Flake8 é usado para garantir que o código segue as diretrizes de estilo da PEP 8. A configuração do Flake8 pode ser encontrada no arquivo `tox.ini`, que define as regras específicas de estilo de código e os diretórios a serem verificados.
