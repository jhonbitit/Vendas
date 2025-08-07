import axios from 'axios';
import type {
  User,
  Ticket,
  Category,
  CreateTicket,
  UpdateTicket,
  TicketComment,
  CreateTicketComment,
  LoginData,
  AuthResponse,
  TicketStats
} from '../types';

const API_BASE_URL = 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Interceptor para adicionar token de autenticação
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Interceptor para tratar erros de autenticação
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Auth
export const authAPI = {
  login: async (data: LoginData): Promise<AuthResponse> => {
    const formData = new FormData();
    formData.append('username', data.username);
    formData.append('password', data.password);
    
    const response = await api.post('/auth/login', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },
};

// Users
export const usersAPI = {
  getMe: async (): Promise<User> => {
    const response = await api.get('/users/me');
    return response.data;
  },

  updateMe: async (data: Partial<User>): Promise<User> => {
    const response = await api.put('/users/me', data);
    return response.data;
  },

  getUsers: async (): Promise<User[]> => {
    const response = await api.get('/users/');
    return response.data;
  },
};

// Categories
export const categoriesAPI = {
  getCategories: async (): Promise<Category[]> => {
    const response = await api.get('/categories/');
    return response.data;
  },

  createCategory: async (data: Omit<Category, 'id' | 'is_active' | 'created_at'>): Promise<Category> => {
    const response = await api.post('/categories/', data);
    return response.data;
  },

  updateCategory: async (id: number, data: Partial<Category>): Promise<Category> => {
    const response = await api.put(`/categories/${id}`, data);
    return response.data;
  },

  deleteCategory: async (id: number): Promise<void> => {
    await api.delete(`/categories/${id}`);
  },
};

// Tickets
export const ticketsAPI = {
  getTickets: async (params?: {
    status?: string;
    creator_id?: number;
    assignee_id?: number;
    skip?: number;
    limit?: number;
  }): Promise<Ticket[]> => {
    const response = await api.get('/tickets/', { params });
    return response.data;
  },

  getTicket: async (id: number): Promise<Ticket> => {
    const response = await api.get(`/tickets/${id}`);
    return response.data;
  },

  createTicket: async (data: CreateTicket): Promise<Ticket> => {
    const response = await api.post('/tickets/', data);
    return response.data;
  },

  updateTicket: async (id: number, data: UpdateTicket): Promise<Ticket> => {
    const response = await api.put(`/tickets/${id}`, data);
    return response.data;
  },

  getTicketComments: async (ticketId: number): Promise<TicketComment[]> => {
    const response = await api.get(`/tickets/${ticketId}/comments`);
    return response.data;
  },

  createTicketComment: async (ticketId: number, data: CreateTicketComment): Promise<TicketComment> => {
    const response = await api.post(`/tickets/${ticketId}/comments`, data);
    return response.data;
  },

  getTicketsStats: async (): Promise<TicketStats> => {
    const response = await api.get('/tickets/stats/overview');
    return response.data;
  },
};

export default api;