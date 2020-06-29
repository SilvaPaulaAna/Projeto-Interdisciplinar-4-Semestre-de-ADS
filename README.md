
# DJango_(Python)_ProjetoWeb-PI
* Desenvolvimento do PI/Fatec 1º semestre de 2020, aplicação do frameWork DJango com uso da linguagem Python.
* Inicialização do diretório por **Ana Paula Dutra**

## ================== Membros
	Ana P. D. Silva
	Ramon T. Goncalves
	Sidnei P. Souza

## Definições do "banco de dados":
	Banco utilizado: POSTGRE
	Nome do banco: ebbusiness

### Como iniciar esta apliação
	1 - Instalar Python
	2 - Instalar Django através do PIP (Pyhton Installer Packages)
	3 - Instalar extensões auxiliares
		3.1 - Crispy (https://django-crispy-forms.readthedocs.io/en/latest/install.html)
		3.2 - Modal-Forms (https://pypi.org/project/django-bootstrap-modal-forms/)
		3.3 - PsychoPG2 (https://pypi.org/project/psycopg2/)
	4 - Instalar PostGre (Banco de dados: https://www.postgresql.org/download/)
	5 - Executar comandos para criar as tabelas
		5.1 - MAKEMIGRATIONS - Cria as tabelas
		5.2 - MIGRATE - Transfere os dados para banco


## ----- Conteúdo do diretório -----

### ================== RAIZ
	[folder] Ebbusiness
	[folder] EbbusinessApp
		[file] db.sqlite3
		[file] manage.py
		[file] README.md -------- Este arquivo de apresentação
			 
### ================== EbbusinessApp
	[folder] __pyCache__  	(Arquivos auto-compilados de execução do servidor DJANGO)
	* Estes arquivos definem as variáveis de nome do projeto e pasta principal,
	* Caso a pasta principal seja renomada o servidor não será carregado, consequentemente suas páginas não exibidas

	[folder] templates		(Pasta onde ficam os arquivos HTML e CSS)
		[file] __init__.py
		[file] asgi.py
		[file] settings.py
		[file] urls.py (Configura os endereços WEB/HTML)
		[file] wsgi.py
		[file] manage.py (executa as funções do DJANGO com comando "python manage.py COMANDO")


