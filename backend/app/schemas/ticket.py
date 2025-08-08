from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.models.ticket import TicketStatus, TicketPriority
from app.schemas.user import User
from app.schemas.category import Category


class TicketBase(BaseModel):
    title: str
    description: str
    priority: Optional[TicketPriority] = TicketPriority.MEDIUM
    category_id: int


class TicketCreate(TicketBase):
    pass


class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TicketStatus] = None
    priority: Optional[TicketPriority] = None
    assignee_id: Optional[int] = None
    category_id: Optional[int] = None


class TicketCommentBase(BaseModel):
    content: str
    is_internal: Optional[bool] = False


class TicketCommentCreate(TicketCommentBase):
    pass


class TicketComment(TicketCommentBase):
    id: int
    ticket_id: int
    author_id: int
    author: User
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class TicketInDB(TicketBase):
    id: int
    status: TicketStatus
    creator_id: int
    assignee_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Ticket(TicketInDB):
    creator: User
    assignee: Optional[User] = None
    category: Category
    comments: List[TicketComment] = []