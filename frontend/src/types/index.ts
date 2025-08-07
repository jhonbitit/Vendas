export interface User {
  id: number;
  email: string;
  full_name: string;
  role: 'user' | 'technician' | 'admin';
  department?: string;
  phone?: string;
  is_active: boolean;
  created_at: string;
  updated_at?: string;
}

export interface Category {
  id: number;
  name: string;
  description?: string;
  color: string;
  is_active: boolean;
  created_at: string;
}

export interface Ticket {
  id: number;
  title: string;
  description: string;
  status: 'open' | 'in_progress' | 'waiting_user' | 'resolved' | 'closed';
  priority: 'low' | 'medium' | 'high' | 'urgent';
  creator_id: number;
  assignee_id?: number;
  category_id: number;
  created_at: string;
  updated_at?: string;
  resolved_at?: string;
  closed_at?: string;
  creator: User;
  assignee?: User;
  category: Category;
  comments: TicketComment[];
}

export interface TicketComment {
  id: number;
  content: string;
  is_internal: boolean;
  ticket_id: number;
  author_id: number;
  author: User;
  created_at: string;
  updated_at?: string;
}

export interface CreateTicket {
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high' | 'urgent';
  category_id: number;
}

export interface UpdateTicket {
  title?: string;
  description?: string;
  status?: 'open' | 'in_progress' | 'waiting_user' | 'resolved' | 'closed';
  priority?: 'low' | 'medium' | 'high' | 'urgent';
  assignee_id?: number;
  category_id?: number;
}

export interface CreateTicketComment {
  content: string;
  is_internal?: boolean;
}

export interface LoginData {
  username: string;
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface TicketStats {
  total: number;
  open: number;
  in_progress: number;
  resolved: number;
  closed: number;
}