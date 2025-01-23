export interface Event {
  id: string;
  title: string;
  date: string;
  description: string;
  type: 'weekly' | 'workshop' | 'retreat';
  location: string;
  maxParticipants?: number;
  price?: number;
}

export interface Registration {
  id: string;
  eventId: string;
  name: string;
  email: string;
  phone?: string;
  whatsapp?: string;
  meditationExperience?: string;
  goals?: string;
  createdAt: string;
}

export interface WaitlistEntry {
  id: string;
  type: 'workshop' | 'retreat';
  name: string;
  email: string;
  phone?: string;
  createdAt: string;
}
