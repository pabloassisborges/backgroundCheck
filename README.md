# Background check
Integração de endpoints para checagem de background.

## Setup e instalação do projeto

Antes de instalar as dependências do projeto, recomenda-se criar um ambiente virtual para o projeto Python para que as mesmas sejam instaladas de forma local no projeto.

Windows:
```
python -m venv <nome do ambiente>
.\<nome do ambiente>\Scripts\activate
```

Linux\OS X:
```
python3 -m venv <nome do ambiente>
source source venv/bin/activate
```

Após a criação do ambiente virtual (opcional) é necessário também instalar um projeto chamado pipenv. Ele cria e gerencia dois arquivos chamado `Pipfile` e `Pipfile.lock` onde o segundo é responsável por assegurar que as versões das dependências a serem instaladas serão as especificadas pelo arquivo.

Windows:
```
python -m pip install pipenv
```

Linux\OS X:
```
python3 -m pip install pipenv
```

Por fim, para instalação das dependencias do projeto, basta utilizar o pipenv como instalador em vez do comando pip convencional:

Windows:
```
python -m pipenv -r Requirements.txt
```

Linux\OS X:
```
python3 -m pipenv -r Requirements.txt
```

Aguarde a instalação das dependências.

Para executar o projeto, existem 2 formas: execução direta ou via script. A execução direta vai pegar os valores defaul de configuração do servidor e basta apenas digitar `python server.py` para executar o projeto. O script carrega as variáveis de ambiente para o script principal e atribui valor a outras que o Flask utiliza por default. Para executar via script basta executar aquele que está em conformidade com o seu sistema operacional:

Windows:
```
serve.bat
```

Linux\OS X:
```
chmod u+x serve.sh
./serve.sh
```

A execução direta (`python server.py`) é para fins de debug, caso haja a necessidade de executar breakpoints marcados no código pela IDE.