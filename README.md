# Documentação do Data Cleaner Service

Este serviço oferece recursos para executar a limpeza de dados com base em regras e ações de correção. Ele foi desenvolvido utilizando Python 3.10 e o framework Django 4.2. O serviço permite a manipulação de três entidades principais: Regra, Ação de Correção e Conjunto de Dados.

## Regra

A entidade Regra define critérios de validação que os dados devem atender. Cada regra possui um script que será executado para verificar se um dado específico está correto ou não.

## Ação de Correção

A entidade Ação de Correção define ações que podem ser aplicadas aos dados considerados incorretos. Cada ação de correção possui um script que será executado para corrigir o dado.

## Conjunto de Dados

A entidade Conjunto de Dados representa um conjunto de dados que serão submetidos à limpeza. Para realizar a limpeza, é necessário fornecer os dados, as regras que serão aplicadas e as ações de correção que serão executadas.

### Métodos

O Conjunto de Dados possui os seguintes métodos:

- `list()`: Retorna uma resposta de método não permitido para requisições GET.
- `retrieve()`: Retorna uma resposta de método não permitido para requisições GET de um objeto específico.
- `update()`: Retorna uma resposta de método não permitido para requisições PUT.
- `partial_update()`: Retorna uma resposta de método não permitido para requisições PATCH.
- `destroy()`: Retorna uma resposta de método não permitido para requisições DELETE.
- `create()`: Executa a limpeza dos dados fornecidos com base nas regras e ações de correção especificadas.

### Requisições

#### POST /conjuntosdedados/

Cria um novo conjunto de dados e executa a limpeza. O corpo da requisição deve conter os seguintes parâmetros:

- `dados`: Os dados a serem limpos.
- `regras`: URLs das regras que serão aplicadas.
- `acao_correcao`: URLs das ações de correção que serão executadas.

### Respostas

A resposta da requisição `POST /conjuntosdedados/` contém os seguintes campos:

- `correto`: Lista dos dados corretos após a limpeza.
- `errado`: Lista dos dados considerados errados após a limpeza.
- `corrigido`: Lista dos dados corrigidos após a limpeza.
- `nao_corrigido`: Lista dos dados não corrigidos após a limpeza.
- `dados`: Lista dos dados após a limpeza, incluindo os corretos, corrigidos e não corrigidos.

## ExecutarLimpeza

A classe `ExecutarLimpeza` é responsável por executar a lógica de limpeza dos dados. Ela possui métodos privados para aplicar as regras e ações de correção aos dados fornecidos.

## Requisitos de Instalação

Certifique-se de ter as seguintes bibliotecas instaladas no ambiente Python:

```
asgiref==3.6.0
autopep8==2.0.2
backports.zoneinfo==0.2.1


Django==4.2
djangorestframework==3.14.0
numpy==1.24.3
pandas==2.0.1
psycopg2==2.9.6
psycopg2-binary==2.9.6
pycodestyle==2.10.0
python-dateutil==2.8.2
python-decouple==3.8
pytz==2023.3
six==1.16.0
sqlparse==0.4.4
tomli==2.0.1
tzdata==2023.3
```

Você pode instalar as bibliotecas listadas acima usando o arquivo `requirements.txt`.
