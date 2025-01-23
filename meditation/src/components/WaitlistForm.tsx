import React, { useState } from 'react';
import { eventService } from '../utils/supabase';
import type { WaitlistEntry } from '../@types/meditation';

interface WaitlistFormProps {
  type: WaitlistEntry['type'];
  onSuccess: () => void;
}

export const WaitlistForm: React.FC<WaitlistFormProps> = ({ type, onSuccess }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: ''
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await eventService.joinWaitlist({
        type,
        ...formData
      });
      onSuccess();
    } catch (error) {
      console.error('Waitlist join failed:', error);
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
      <button type="submit" className="button button--primary">
        Join Waitlist
      </button>
    </form>
  );
};
