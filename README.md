# Lokar Web

Sistema de gestão imobiliária com suporte a CRM, leads, agendamento de visitas, controle de acessos, logs e sessões, construído em arquitetura de **microserviços** e banco de dados em modelo **Star Schema (Golden Layer)**.

---

## 🚀 Objetivo do Projeto
O **Lokar Web** tem como propósito fornecer uma solução escalável e segura para gestão de imóveis e relacionamento com leads, integrando:
- Cadastro e gerenciamento de imóveis.
- CRM para controle de leads e funil de vendas.
- Agendamento de visitas e acompanhamento de tarefas.
- Controle de sessões para maior segurança de acessos.
- Logs de auditoria para rastrear ações de usuários.
- Dashboards e relatórios baseados em modelo **Data Warehouse (Star Schema)**.

---

## 📐 Arquitetura
- **Backend:** Python (FastAPI/Django)
- **Frontend:** React (futuro)
- **Banco de Dados:** PostgreSQL (Docker)
- **Modelo de Dados:** Star Schema (Dimensões e Fatos)
- **Deploy:** Docker + Docker Compose
- **Autenticação:** JWT + Refresh Tokens
- **Estilo:** Microserviços independentes comunicando via API

---

## 📂 Estrutura de Pastas

```bash
lokar-web/
│── README.md                # Documentação principal
│── docker-compose.yml       # Orquestração de containers
│── .env                     # Variáveis de ambiente
│
├── services/                # Serviços (microserviços isolados)
│   ├── auth/                # Autenticação e controle de sessões
│   │   ├── app/
│   │   │   ├── routers/
│   │   │   ├── models/
│   │   │   ├── schemas/
│   │   │   ├── services/
│   │   │   ├── utils/
│   │   │   └── main.py
│   │   └── tests/
│   │
│   ├── users/               # Gestão de usuários e perfis
│   │   └── ...
│   │
│   ├── imobiliaria/         # Gestão de imobiliárias
│   │   └── ...
│   │
│   ├── imoveis/             # Cadastro e mídia de imóveis
│   │   └── ...
│   │
│   ├── crm/                 # Gestão de leads e pipeline
│   │   ├── app/
│   │   │   ├── routers/
│   │   │   ├── models/
│   │   │   ├── schemas/
│   │   │   ├── services/
│   │   │   └── main.py
│   │   └── tests/
│   │
│   ├── analytics/           # Logs, métricas e dashboards
│   │   └── ...
│   │
│   └── notifications/       # (Opcional) E-mail, SMS, Push
│       └── ...
│
├── db/                      # Banco de dados
│   ├── migrations/          # Scripts de versionamento
│   ├── schema.sql           # Estrutura inicial do Star Schema
│   └── seeds.sql            # Dados de exemplo
│
└── docs/                    # Documentação adicional
    ├── business-rules.md    # Regras de negócio detalhadas
    ├── api-docs.md          # Endpoints das APIs
    └── erd.png              # Diagrama do banco
```

## 📊 Modelo de Dados (Star Schema)

**Dimensões**:
- dim_usuario → Usuários do sistema
- dim_imobiliaria → Imobiliárias cadastradas
- dim_imovel → Imóveis cadastrados
- dim_lead → Leads no CRM
- dim_midia_imovel → Fotos e vídeos dos imóveis
- dim_sessao_usuario → Sessões ativas

**Fatos**:
- fact_log_usuario → Logs de ações de usuários
- fact_pipeline_lead → Avanço de leads no funil
- fact_agendamento_visita → Agendamentos de visitas
- fact_tarefa_crm → Tarefas associadas a leads/usuários

## 📜 Regras de Negócio

**Autenticação & Sessão**
- Apenas uma sessão ativa por usuário é permitida.
- Tentativa de login em dispositivo diferente encerra sessão anterior.
- Tokens JWT com refresh configurado.
- Controle de Logs
- Toda ação de CRUD gera um registro em fact_log_usuario.
- Logs armazenam: usuário, ação, entidade afetada, timestamp, IP e user-agent.

**CRM*
- Leads devem estar vinculados a uma imobiliária e a um responsável (usuário).
- Leads passam por estágios no pipeline: Novo → Contato → Proposta → Fechado (ganho/perdido).
- Cada lead pode ter múltiplas tarefas e agendamentos.
- Gestão de Imóveis
- Imóvel precisa estar vinculado a uma imobiliária.
- Cada imóvel pode ter múltiplas mídias (imagens/vídeos). 
- Histórico de acessos e visitas registrado em tabelas de fato.

**Dashboards & Analytics**
- Baseados no Golden Layer, agregando métricas de leads, visitas, imóveis e conversões.
- Possibilidade de exportação em CSV/PDF.

## 🛠️ Como Rodar Localmente
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/lokar-web.git
cd lokar-web

# Suba os containers
docker-compose up -d --build

# Acesse o serviço principal
http://localhost:8000/docs
```

