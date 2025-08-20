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
lokar_backend/
├── main.py                   # Main geral, importa rotas de todos os serviços e inicializa o sistema
├── services/                 # Cada serviço é autônomo e contém tudo que precisa
│   ├── auth_service/
│   │   ├── main.py           # Inicializa o serviço
│   │   ├── models.py         # Models SQLAlchemy específicos do auth
│   │   ├── schemas.py        # Schemas Pydantic
│   │   └── routers/          # Routers modulares
│   │       └── auth.py
│   │
│   ├── users_service/
│   │   ├── main.py
│   │   ├── models.py         # Usuários, roles
│   │   ├── schemas.py
│   │   └── routers/
│   │       ├── users.py
│   │       ├── roles.py
│   │       └── profile.py
│   │
│   ├── imoveis_service/
│   │   ├── main.py
│   │   ├── models.py         # Imóveis, fotos
│   │   ├── schemas.py
│   │   └── routers/
│   │       ├── imoveis.py
│   │       └── fotos.py
│   │
│   ├── leads_service/
│   │   ├── main.py
│   │   ├── models.py         # Leads, interesses
│   │   ├── schemas.py
│   │   └── routers/
│   │       ├── leads.py
│   │       └── interesses.py
│   │
│   └── consent_service/
│       ├── main.py
│       ├── models.py         # Consentimentos LGPD
│       ├── schemas.py
│       └── routers/
│           └── consent.py
│
├── gateway/                  # API Gateway ou main do portal
│   ├── main.py               # Recebe requests externos, roteia para serviços
│   ├── routers/
│   │   ├── auth_gateway.py
│   │   ├── users_gateway.py
│   │   ├── imoveis_gateway.py
│   │   ├── leads_gateway.py
│   │   └── consent_gateway.py
│   └── utils.py              # JWT central, autenticação, logging
│
├── commons/                  # Utils compartilhados entre serviços
│   ├── email.py              # Envio de e-mails
│   ├── background.py         # Tasks assíncronas
│   ├── security.py           # Hashing, JWT, roles middleware
│   └── helpers.py            # Funções utilitárias gerais
│
├── config/                   # Configurações gerais
│   ├── settings.py           # Variáveis de ambiente
│   └── logging_config.py     # Configuração de logs
│
├── logs/                     # Logs do sistema
│   ├── logs_test.log
│   └── system.log
│
├── tests/                    # Testes unitários e scripts isolados
│   └── scripts.py
│
├── migrations/               # Alembic migrations para versionamento do banco
│
├── docker/                   # Dockerfiles e configs de cada serviço
│
├── requirements.txt
└── README.md

```

---
## Diagrama de Arquitetura – Lokar Backend
```css
                        ┌───────────────────────┐
                        │     Frontend React    │
                        │  (Portal Lokar / App)│
                        └─────────┬─────────────┘
                                  │ HTTP Requests
                                  │
                                  ▼
                        ┌───────────────────────┐
                        │      API Gateway       │
                        │   (gateway/main.py)   │
                        │ - Autenticação JWT    │
                        │ - Verificação LGPD    │
                        │ - Logging central     │
                        │ - CORS / Middlewares  │
                        └─────┬─────┬─────┬─────┘
                              │     │     │
             ┌────────────────┘     │     └────────────────┐
             ▼                      ▼                      ▼
   ┌─────────────────┐      ┌─────────────────┐     ┌─────────────────┐
   │ auth_service     │      │ users_service    │     │ imoveis_service │
   │ - main.py        │      │ - main.py        │     │ - main.py       │
   │ - models.py      │      │ - models.py      │     │ - models.py     │
   │ - schemas.py     │      │ - schemas.py     │     │ - schemas.py    │
   │ - routers/auth.py│      │ - routers/users/ │     │ - routers/      │
   └─────────────────┘      └─────────────────┘     └─────────────────┘
             │                      │                      │
             ▼                      ▼                      ▼
   ┌─────────────────┐      ┌─────────────────┐     ┌─────────────────┐
   │ leads_service    │      │ consent_service  │     │ commons          │
   │ - main.py        │      │ - main.py        │     │ - email.py       │
   │ - models.py      │      │ - models.py      │     │ - background.py  │
   │ - schemas.py     │      │ - schemas.py     │     │ - helpers.py     │
   │ - routers/       │      │ - routers/       │     │ - security.py    │
   └─────────────────┘      └─────────────────┘     └─────────────────┘
             │                      │
             └─────────┬────────────┘
                       │
                       ▼
                ┌─────────────┐
                │ PostgreSQL  │
                │ (Cada serviço│
                │ pode ter seu│
                │  schema)    │
                └─────────────┘
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
