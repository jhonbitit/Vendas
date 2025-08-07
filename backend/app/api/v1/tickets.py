from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, require_technician_or_admin
from app.crud import ticket as crud_ticket
from app.db.database import get_db
from app.models.user import User, UserRole
from app.models.ticket import TicketStatus
from app.schemas.ticket import (
    Ticket as TicketSchema, 
    TicketCreate, 
    TicketUpdate,
    TicketComment as TicketCommentSchema,
    TicketCommentCreate
)

router = APIRouter()


@router.get("/", response_model=List[TicketSchema])
def read_tickets(
    skip: int = 0,
    limit: int = 100,
    status: Optional[TicketStatus] = Query(None),
    creator_id: Optional[int] = Query(None),
    assignee_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Listar tickets"""
    # Usuários comuns só podem ver seus próprios tickets
    if current_user.role == UserRole.USER:
        creator_id = current_user.id
    
    tickets = crud_ticket.get_tickets(
        db, 
        skip=skip, 
        limit=limit, 
        status=status,
        creator_id=creator_id,
        assignee_id=assignee_id
    )
    return tickets


@router.post("/", response_model=TicketSchema)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Criar novo ticket"""
    return crud_ticket.create_ticket(db=db, ticket=ticket, creator_id=current_user.id)


@router.get("/{ticket_id}", response_model=TicketSchema)
def read_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Obter ticket específico"""
    db_ticket = crud_ticket.get_ticket(db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    # Usuários comuns só podem ver seus próprios tickets
    if current_user.role == UserRole.USER and db_ticket.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return db_ticket


@router.put("/{ticket_id}", response_model=TicketSchema)
def update_ticket(
    ticket_id: int,
    ticket_update: TicketUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Atualizar ticket"""
    db_ticket = crud_ticket.get_ticket(db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    # Verificar permissões
    if current_user.role == UserRole.USER:
        # Usuários só podem editar tickets próprios e apenas alguns campos
        if db_ticket.creator_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        
        # Limitar campos que usuário comum pode editar
        allowed_fields = {"title", "description", "priority", "category_id"}
        update_data = ticket_update.dict(exclude_unset=True)
        for field in update_data:
            if field not in allowed_fields:
                raise HTTPException(
                    status_code=403, 
                    detail=f"Users cannot modify field: {field}"
                )
    
    updated_ticket = crud_ticket.update_ticket(db, ticket_id, ticket_update)
    return updated_ticket


@router.post("/{ticket_id}/comments", response_model=TicketCommentSchema)
def create_ticket_comment(
    ticket_id: int,
    comment: TicketCommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Adicionar comentário ao ticket"""
    db_ticket = crud_ticket.get_ticket(db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    # Usuários comuns só podem comentar em seus próprios tickets
    if current_user.role == UserRole.USER and db_ticket.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    # Usuários comuns não podem criar comentários internos
    if current_user.role == UserRole.USER and comment.is_internal:
        comment.is_internal = False
    
    return crud_ticket.create_ticket_comment(
        db=db, 
        ticket_id=ticket_id, 
        comment=comment, 
        author_id=current_user.id
    )


@router.get("/{ticket_id}/comments", response_model=List[TicketCommentSchema])
def read_ticket_comments(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Obter comentários do ticket"""
    db_ticket = crud_ticket.get_ticket(db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    # Usuários comuns só podem ver comentários de seus próprios tickets
    if current_user.role == UserRole.USER and db_ticket.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    comments = crud_ticket.get_ticket_comments(db, ticket_id)
    
    # Filtrar comentários internos para usuários comuns
    if current_user.role == UserRole.USER:
        comments = [c for c in comments if not c.is_internal]
    
    return comments


@router.get("/stats/overview")
def get_tickets_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_technician_or_admin)
):
    """Obter estatísticas dos tickets (apenas técnicos e admins)"""
    return crud_ticket.get_tickets_stats(db)