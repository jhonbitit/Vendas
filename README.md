# Sistema de Help Desk para TI

Este é um sistema completo de help desk para prestação de serviços de TI, desenvolvido com FastAPI (backend) e React (frontend).

## Funcionalidades

### Para Usuários
- Criar tickets de suporte
- Acompanhar status dos tickets
- Histórico de tickets
- Sistema de prioridades

### Para Técnicos/Administradores
- Dashboard de tickets
- Gerenciar tickets (atribuir, resolver, fechar)
- Sistema de categorias
- Relatórios e métricas
- Gerenciar usuários

## Tecnologias

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Frontend**: React + TypeScript + Tailwind CSS
- **Autenticação**: JWT
- **Banco de Dados**: PostgreSQL

## Estrutura do Projeto

```
/
├── backend/           # API FastAPI
├── frontend/          # Aplicação React
├── docker-compose.yml # Configuração Docker
└── README.md
```

## Como Executar

### Opção 1: Docker Compose (Recomendado)

1. Clone o repositório
2. Execute `docker-compose up` para subir o sistema completo
3. Aguarde alguns minutos para o build e inicialização
4. Acesse http://localhost:3000 para o frontend
5. API disponível em http://localhost:8000

### Opção 2: Execução Local

1. **Pré-requisitos:**
   - Python 3.11+
   - Node.js 18+
   - PostgreSQL 15+

2. **Iniciar PostgreSQL:**
   ```bash
   # Com Docker (mais fácil)
   docker run --name postgres -e POSTGRES_PASSWORD=helpdesk_pass -e POSTGRES_USER=helpdesk_user -e POSTGRES_DB=helpdesk_db -p 5432:5432 -d postgres:15-alpine
   
   # Ou configure PostgreSQL local com as credenciais em backend/.env
   ```

3. **Executar o sistema:**
   ```bash
   # No diretório raiz do projeto
   ./run_local.sh
   ```

4. **Acesso:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Documentação API: http://localhost:8000/docs

### Opção 3: Execução Manual

**Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -c "from app.db.init_db import create_tables, init_db; from app.db.database import SessionLocal; create_tables(); db = SessionLocal(); init_db(db); db.close()"
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

## Credenciais Padrão

- **Admin**: admin@helpdesk.com / admin123
- **Técnico**: tecnico@helpdesk.com / tecnico123
- **Usuário**: usuario@helpdesk.com / usuario123

## Status do Projeto

✅ **Concluído:**
- Arquitetura completa (Backend FastAPI + Frontend React)
- Sistema de autenticação JWT
- Modelos de dados (Usuários, Tickets, Categorias, Comentários)
- API RESTful completa com permissões
- Interface de usuário responsiva
- Dashboard com estatísticas
- Sistema de prioridades e status
- Containerização com Docker

🚧 **Em desenvolvimento:**
- Páginas de gerenciamento de tickets (lista, criação, edição)
- Páginas de administração (usuários, categorias)
- Sistema de notificações
- Relatórios avançados
- Upload de arquivos nos tickets

## Funcionalidades Implementadas

### Backend (FastAPI)
- ✅ Autenticação JWT
- ✅ CRUD completo para usuários, tickets, categorias
- ✅ Sistema de permissões por role
- ✅ Comentários em tickets (públicos e internos)
- ✅ Estatísticas e dashboard
- ✅ Documentação automática (Swagger/OpenAPI)

### Frontend (React + TypeScript)
- ✅ Interface moderna com Tailwind CSS
- ✅ Sistema de login/logout
- ✅ Dashboard com estatísticas
- ✅ Layout responsivo com sidebar
- ✅ Gestão de estado com Context API
- ✅ Notificações toast

### Banco de Dados
- ✅ PostgreSQL com SQLAlchemy
- ✅ Migrações automáticas
- ✅ Dados iniciais (usuários e categorias padrão)

## Arquitetura

```
Sistema Help Desk
├── Backend (FastAPI)
│   ├── API RESTful
│   ├── Autenticação JWT
│   ├── Validação Pydantic
│   └── PostgreSQL + SQLAlchemy
├── Frontend (React)
│   ├── TypeScript
│   ├── Tailwind CSS
│   ├── React Router
│   └── Axios
└── Banco de Dados
    ├── PostgreSQL
    └── Dados iniciais
```

## Estrutura de Permissões

| Funcionalidade | Usuário | Técnico | Admin |
|---|---|---|---|
| Criar tickets | ✅ | ✅ | ✅ |
| Ver próprios tickets | ✅ | ✅ | ✅ |
| Ver todos os tickets | ❌ | ✅ | ✅ |
| Atribuir tickets | ❌ | ✅ | ✅ |
| Gerenciar usuários | ❌ | ❌ | ✅ |
| Gerenciar categorias | ❌ | ❌ | ✅ |
| Comentários internos | ❌ | ✅ | ✅ |
| Estatísticas | ❌ | ✅ | ✅ |

## Contribuição

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
