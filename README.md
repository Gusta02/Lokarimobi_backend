# Lokar Backend (FastAPI)

Backend do sistema Lokar, responsável por gerenciar imóveis, leads, usuários, consentimento LGPD e integração com o portal público.

---

## 🚀 Tecnologias

* **Framework:** FastAPI
* **Banco de dados:** PostgreSQL
* **ORM:** SQLAlchemy
* **Autenticação:** JWT + Roles Middleware (Admin / Corretor)
* **Tarefas assíncronas:** Celery / FastAPI Background Tasks
* **Envio de e-mail:** SendGrid / Mailgun / AWS SES

---

## 🏗 Estrutura do Projeto

```
app/
├── main.py           # Inicializacao do FastAPI
├── models.py         # Modelos SQLAlchemy
├── schemas.py        # Schemas Pydantic
├── database.py       # Conexao com PostgreSQL
├── routers/
│   ├── auth.py       # Login / registro / JWT
│   ├── users.py      # CRUD usuarios e permissoes
│   ├── imoveis.py    # CRUD imoveis
│   ├── leads.py      # Gestao de leads
│   └── consent.py    # Registro e verificacao de consentimento LGPD
└── utils/
    ├── email.py      # Envio de e-mails e notificacoes
    └── background.py # Tasks assincronas
```

---

## ⚡ Funcionalidades Principais

* Cadastro e gerenciamento de **usuários** (Admin / Corretor)
* Cadastro e publicação de **imóveis**
* **Leads automáticos** do portal, com registro de interesse
* **Consentimento LGPD** via e-mail/WhatsApp antes de liberar leads para o CRM
* Dashboard interno para corretores e imobiliárias
* Relatórios de leads, imóveis e consentimento

---

## 💻 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/lokar-backend.git
cd lokar-backend
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv env
source env/bin/activate    # Linux/macOS
env\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure variáveis de ambiente (exemplo `.env`):

```
DATABASE_URL=postgresql://user:password@localhost:5432/lokar
SECRET_KEY=uma_chave_secreta
EMAIL_API_KEY=sua_chave_sendgrid
```

---

## 🚀 Executando o Backend

```bash
uvicorn app.main:app --reload
```

* O backend estará disponível em `http://localhost:8000`
* Documentação interativa Swagger: `http://localhost:8000/docs`

---

## 📦 Endpoints Principais

| Endpoint      | Método              | Descrição                                    |
| ------------- | ------------------- | -------------------------------------------- |
| `/auth/login` | POST                | Login de usuário                             |
| `/users/`     | GET/POST/PUT/DELETE | CRUD de usuários                             |
| `/imoveis/`   | GET/POST/PUT/DELETE | CRUD de imóveis                              |
| `/leads/`     | GET/POST            | Leads gerados pelo portal                    |
| `/consent/`   | POST/GET            | Registro e verificação de consentimento LGPD |

---

## 🔒 Consentimento LGPD

* Leads do portal só aparecem no CRM do corretor **após consentimento**
* Histórico de leads e consentimentos é mantido para auditoria
* Emails e mensagens são enviados automaticamente usando tasks assíncronas

---

## 🤝 Contribuição

* Fork este repositório
* Crie uma branch feature/nova-funcionalidade
* Envie Pull Requests com descrição detalhada
* Mantenha testes atualizados

---

## 📜 Licença

Este projeto está sob a licença MIT.
