
# Guia de Configuração: Projeto Django + Next.js

### Estrutura do projeto

```bash
.
├── api                          # Backend Django
│   ├── config
│   ├── conftest.py
│   ├── core_apps
│   ├── manage.py
│   ├── pytest.ini
│   └── requirements.txt
|   └── ...
├── README.md
└── web                          # Frontend NextJS
    ├── components.json
    ├── next.config.mjs
    ├── package.json
    ├── package-lock.json
    ├── public
    ├── src
    └── tsconfig.json
```

### Rodar localmente

#### 1. Pré-requisitos

- Python 3.11+
- Node.js 20+ e npm
- Git

#### 1. Clonando o projeto

```bash
git clone https://github.com/FGA-GCES/trabalho-individual-2024-2.git
cd trabalho-individual-2024-2
```

#### 2. Configurando o backend (Django)

```bash
# Entre no diretório do backend
cd api

# Criar e ativar um ambiente virtual (Linux/MacOS)
python -m venv venv
source venv/bin/activate

# No Windows:
???

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

O backend estará rodando em `http://localhost:8000`

#### 3. Configurando o frontend (Next.js)

```bash
# Entre no diretório do frontend
cd web

# Instale as dependências
npm install

# Crie um arquivo .env.local baseado no exemplo
cp .env.example .env.local

# Inicie o servidor de desenvolvimento
npm run dev
```

O frontend estará rodando em `http://localhost:3000`
