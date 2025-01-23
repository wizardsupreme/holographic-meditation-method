import React, { useState } from 'react';
import { eventService } from '../utils/supabase';

interface RegistrationFormProps {
  eventId: string;
  onSuccess: () => void;
  onCancel: () => void;
}

export const RegistrationForm: React.FC<RegistrationFormProps> = ({ 
  eventId, 
  onSuccess, 
  onCancel 
}) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    whatsapp: '',
    meditationExperience: '',
    goals: ''
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await eventService.registerForEvent({
        eventId,
        ...formData
      });
      onSuccess();
    } catch (error) {
      console.error('Registration failed:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="margin-bottom--sm">
        <label>Name:</label>
        <input
          type="text"
          required
          value={formData.name}
          onChange={e => setFormData(prev => ({ ...prev, name: e.target.value }))}
        />
      </div>
      <div className="margin-bottom--sm">
        <label>Email:</label>
        <input
          type="email"
          required
          value={formData.email}
          onChange={e => setFormData(prev => ({ ...prev, email: e.target.value }))}
        />
      </div>
      <div className="margin-bottom--sm">
        <label>Phone:</label>
        <input
          type="tel"
          value={formData.phone}
          onChange={e => setFormData(prev => ({ ...prev, phone: e.target.value }))}
        />
      </div>
      <div className="margin-bottom--sm">
        <label>WhatsApp (if different):</label>
        <input
          type="tel"
          value={formData.whatsapp}
          onChange={e => setFormData(prev => ({ ...prev, whatsapp: e.target.value }))}
        />
      </div>
      <div className="margin-bottom--sm">
        <label>Meditation Experience:</label>
        <textarea
          value={formData.meditationExperience}
          onChange={e => setFormData(prev => ({ ...prev, meditationExperience: e.target.value }))}
        />
      </div>
      <div className="margin-bottom--sm">
        <label>Goals:</label>
        <textarea
          value={formData.goals}
          onChange={e => setFormData(prev => ({ ...prev, goals: e.target.value }))}
        />
      </div>
      <div>
        <button type="submit" className="button button--primary margin-right--sm">
          Register
        </button>
        <button type="button" className="button button--secondary" onClick={onCancel}>
          Cancel
        </button>
      </div>
    </form>
  );
};
