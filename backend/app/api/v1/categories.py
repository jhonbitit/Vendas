from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, require_admin
from app.crud import category as crud_category
from app.db.database import get_db
from app.models.user import User
from app.schemas.category import Category as CategorySchema, CategoryCreate, CategoryUpdate

router = APIRouter()


@router.get("/", response_model=List[CategorySchema])
def read_categories(
    skip: int = 0,
    limit: int = 100,
    active_only: bool = True,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Listar categorias"""
    categories = crud_category.get_categories(db, skip=skip, limit=limit, active_only=active_only)
    return categories


@router.post("/", response_model=CategorySchema)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Criar nova categoria (apenas admin)"""
    db_category = crud_category.get_category_by_name(db, name=category.name)
    if db_category:
        raise HTTPException(
            status_code=400,
            detail="Category name already exists"
        )
    return crud_category.create_category(db=db, category=category)


@router.get("/{category_id}", response_model=CategorySchema)
def read_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Obter categoria específica"""
    db_category = crud_category.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.put("/{category_id}", response_model=CategorySchema)
def update_category(
    category_id: int,
    category_update: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Atualizar categoria (apenas admin)"""
    db_category = crud_category.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    # Verificar se o nome já existe em outra categoria
    if category_update.name:
        existing_category = crud_category.get_category_by_name(db, name=category_update.name)
        if existing_category and existing_category.id != category_id:
            raise HTTPException(
                status_code=400,
                detail="Category name already exists"
            )
    
    updated_category = crud_category.update_category(db, category_id, category_update)
    return updated_category


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """Desativar categoria (apenas admin)"""
    success = crud_category.delete_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deactivated successfully"}