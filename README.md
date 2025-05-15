# Projeto WMS (Warehouse Management System)

Este projeto é um sistema de gerenciamento de armazéns (WMS) construído com **Flask**, **SQLAlchemy**, **Flask-Migrate** e **PostgreSQL**. Ele permite o controle de produtos com funcionalidades como cadastro, validade, rastreio e controle de estoque.

---

## 🧱 Tecnologias utilizadas

* Python 3.13
* Flask
* SQLAlchemy
* Flask-Migrate
* PostgreSQL

---

## 📁 Estrutura do Projeto

```
Projeto-WMS/
├── app/
│   ├── __init__.py       # Criação do app e inicialização do banco
│   ├── models.py         # Definição do modelo Produto
├── migrations/           # Arquivos de migração do banco (criado pelo Flask-Migrate)
├── README.md             # Este arquivo
├── requirements.txt      # Dependências do projeto
```

---

## 🧪 Como rodar o projeto localmente

### Pré-requisitos

* Python 3.13 instalado
* PostgreSQL instalado e rodando

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/projeto-wms.git
cd projeto-wms
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Certifique-se de ter um banco criado:

```bash
psql -U postgres
CREATE DATABASE wms_db;
CREATE USER dionis WITH PASSWORD '44718640';
GRANT ALL PRIVILEGES ON DATABASE wms_db TO dionis;
```

No arquivo `app/__init__.py`, a URI de conexão deve estar assim:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dionis:44718640@localhost/wms_db'
```

### 5. Inicialize o banco de dados

```bash
flask db init
flask db migrate -m "Criar tabela produtos"
flask db upgrade
```

---

## 📦 Modelo de Produto

```python
class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False)
    validade = db.Column(db.Date, nullable=True)
    quantidade = db.Column(db.Integer, default=0)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
```

---

## 💾 Comandos úteis

```bash
# Criar uma nova migração após modificar models.py
flask db migrate -m "mensagem"

# Aplicar a migração
flask db upgrade

# Ver estrutura das tabelas no banco
psql -U dionis -d wms_db
\d produtos
```

---

## ✅ Status do Projeto

🚧 Em desenvolvimento. Até agora temos:

* Modelo de produto
* Migrations com Alembic/Flask-Migrate
* Banco PostgreSQL funcionando

---

## 🧔 Autor

Dioni — [github.com/seu-usuario](https://github.com/DioniSouza)
