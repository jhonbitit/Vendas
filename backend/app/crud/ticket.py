from sqlalchemy.orm import Session, joinedload
from app.models.ticket import Ticket, TicketStatus
from app.models.comment import TicketComment
from app.schemas.ticket import TicketCreate, TicketUpdate, TicketCommentCreate
from typing import Optional, List
from datetime import datetime


def get_ticket(db: Session, ticket_id: int) -> Optional[Ticket]:
    return db.query(Ticket).options(
        joinedload(Ticket.creator),
        joinedload(Ticket.assignee),
        joinedload(Ticket.category),
        joinedload(Ticket.comments).joinedload(TicketComment.author)
    ).filter(Ticket.id == ticket_id).first()


def get_tickets(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    status: Optional[TicketStatus] = None,
    creator_id: Optional[int] = None,
    assignee_id: Optional[int] = None
) -> List[Ticket]:
    query = db.query(Ticket).options(
        joinedload(Ticket.creator),
        joinedload(Ticket.assignee),
        joinedload(Ticket.category)
    )
    
    if status:
        query = query.filter(Ticket.status == status)
    if creator_id:
        query = query.filter(Ticket.creator_id == creator_id)
    if assignee_id:
        query = query.filter(Ticket.assignee_id == assignee_id)
    
    return query.offset(skip).limit(limit).all()


def create_ticket(db: Session, ticket: TicketCreate, creator_id: int) -> Ticket:
    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        category_id=ticket.category_id,
        creator_id=creator_id
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return get_ticket(db, db_ticket.id)


def update_ticket(db: Session, ticket_id: int, ticket_update: TicketUpdate) -> Optional[Ticket]:
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not db_ticket:
        return None
    
    update_data = ticket_update.dict(exclude_unset=True)
    
    # Atualizar timestamps específicos baseado no status
    if "status" in update_data:
        if update_data["status"] == TicketStatus.RESOLVED:
            update_data["resolved_at"] = datetime.utcnow()
        elif update_data["status"] == TicketStatus.CLOSED:
            update_data["closed_at"] = datetime.utcnow()
    
    for field, value in update_data.items():
        setattr(db_ticket, field, value)
    
    db.commit()
    db.refresh(db_ticket)
    return get_ticket(db, ticket_id)


def create_ticket_comment(
    db: Session, 
    ticket_id: int, 
    comment: TicketCommentCreate, 
    author_id: int
) -> TicketComment:
    db_comment = TicketComment(
        content=comment.content,
        is_internal=comment.is_internal,
        ticket_id=ticket_id,
        author_id=author_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_ticket_comments(db: Session, ticket_id: int) -> List[TicketComment]:
    return db.query(TicketComment).options(
        joinedload(TicketComment.author)
    ).filter(TicketComment.ticket_id == ticket_id).order_by(TicketComment.created_at).all()


def get_tickets_stats(db: Session) -> dict:
    """Obter estatísticas dos tickets"""
    total = db.query(Ticket).count()
    open_tickets = db.query(Ticket).filter(Ticket.status == TicketStatus.OPEN).count()
    in_progress = db.query(Ticket).filter(Ticket.status == TicketStatus.IN_PROGRESS).count()
    resolved = db.query(Ticket).filter(Ticket.status == TicketStatus.RESOLVED).count()
    closed = db.query(Ticket).filter(Ticket.status == TicketStatus.CLOSED).count()
    
    return {
        "total": total,
        "open": open_tickets,
        "in_progress": in_progress,
        "resolved": resolved,
        "closed": closed
    }