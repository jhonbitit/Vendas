from sqlalchemy.orm import Session
from app.db.database import engine, Base
from app.models.user import User, UserRole
from app.models.category import Category
from app.core.security import get_password_hash


def create_tables():
    """Criar todas as tabelas"""
    Base.metadata.create_all(bind=engine)


def init_db(db: Session):
    """Inicializar banco de dados com dados padrão"""
    
    # Criar categorias padrão
    categories_data = [
        {"name": "Hardware", "description": "Problemas relacionados a hardware", "color": "#EF4444"},
        {"name": "Software", "description": "Problemas relacionados a software", "color": "#3B82F6"},
        {"name": "Rede", "description": "Problemas de conectividade e rede", "color": "#10B981"},
        {"name": "Email", "description": "Problemas com email e comunicação", "color": "#F59E0B"},
        {"name": "Acesso", "description": "Problemas de acesso e permissões", "color": "#8B5CF6"},
        {"name": "Outros", "description": "Outros problemas diversos", "color": "#6B7280"}
    ]
    
    for cat_data in categories_data:
        existing_category = db.query(Category).filter(Category.name == cat_data["name"]).first()
        if not existing_category:
            category = Category(**cat_data)
            db.add(category)
    
    # Criar usuários padrão
    users_data = [
        {
            "email": "admin@helpdesk.com",
            "full_name": "Administrador",
            "password": "admin123",
            "role": UserRole.ADMIN,
            "department": "TI"
        },
        {
            "email": "tecnico@helpdesk.com",
            "full_name": "Técnico de Suporte",
            "password": "tecnico123",
            "role": UserRole.TECHNICIAN,
            "department": "TI"
        },
        {
            "email": "usuario@helpdesk.com",
            "full_name": "Usuário Teste",
            "password": "usuario123",
            "role": UserRole.USER,
            "department": "Vendas"
        }
    ]
    
    for user_data in users_data:
        existing_user = db.query(User).filter(User.email == user_data["email"]).first()
        if not existing_user:
            hashed_password = get_password_hash(user_data["password"])
            user = User(
                email=user_data["email"],
                full_name=user_data["full_name"],
                hashed_password=hashed_password,
                role=user_data["role"],
                department=user_data["department"]
            )
            db.add(user)
    
    db.commit()


if __name__ == "__main__":
    from app.db.database import SessionLocal
    
    print("Criando tabelas...")
    create_tables()
    
    print("Inicializando dados...")
    db = SessionLocal()
    try:
        init_db(db)
        print("Banco de dados inicializado com sucesso!")
    finally:
        db.close()