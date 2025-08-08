#!/bin/bash

echo "=== Sistema de Help Desk TI ==="
echo "Iniciando sistema localmente..."
echo ""

# Função para limpar processos
cleanup() {
    echo ""
    echo "Parando serviços..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null
    fi
    exit 0
}

# Configurar trap para limpar ao sair
trap cleanup SIGINT SIGTERM

# Verificar se PostgreSQL está rodando
echo "Verificando PostgreSQL..."
if ! pg_isready -h localhost -p 5432 2>/dev/null; then
    echo "PostgreSQL não está rodando. Por favor, inicie o PostgreSQL primeiro."
    echo "Você pode usar Docker: docker run --name postgres -e POSTGRES_PASSWORD=helpdesk_pass -e POSTGRES_USER=helpdesk_user -e POSTGRES_DB=helpdesk_db -p 5432:5432 -d postgres:15-alpine"
    exit 1
fi

echo "PostgreSQL está rodando ✓"

# Configurar backend
echo ""
echo "Configurando backend..."
cd backend

# Instalar dependências do Python
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

echo "Ativando ambiente virtual e instalando dependências..."
source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1

# Inicializar banco de dados
echo "Inicializando banco de dados..."
python -c "from app.db.init_db import create_tables, init_db; from app.db.database import SessionLocal; create_tables(); db = SessionLocal(); init_db(db); db.close(); print('Banco inicializado com sucesso!')"

# Iniciar backend
echo "Iniciando backend na porta 8000..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload > backend.log 2>&1 &
BACKEND_PID=$!

cd ..

# Configurar frontend
echo ""
echo "Configurando frontend..."
cd frontend

# Instalar dependências do Node.js
echo "Instalando dependências do frontend..."
npm install > /dev/null 2>&1

# Iniciar frontend
echo "Iniciando frontend na porta 3000..."
BROWSER=none npm start > frontend.log 2>&1 &
FRONTEND_PID=$!

cd ..

echo ""
echo "=== Sistema iniciado com sucesso! ==="
echo ""
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 Documentação API: http://localhost:8000/docs"
echo ""
echo "Credenciais de teste:"
echo "👑 Admin: admin@helpdesk.com / admin123"
echo "🔧 Técnico: tecnico@helpdesk.com / tecnico123"
echo "👤 Usuário: usuario@helpdesk.com / usuario123"
echo ""
echo "Pressione Ctrl+C para parar o sistema"
echo ""

# Aguardar
wait