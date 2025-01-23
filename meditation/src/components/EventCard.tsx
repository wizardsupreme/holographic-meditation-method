// src/components/EventCard.tsx
import React from 'react';
import type { Event } from '../@types/meditation';

interface EventCardProps {
  event: Event;
}

export const EventCard: React.FC<EventCardProps> = ({ event }) => {
  return (
    <div className="card margin-bottom--lg">
      <div className="card__header">
        <h3>{event.title}</h3>
      </div>
      <div className="card__body">
        <p>{event.description}</p>
        <p>Date: {new Date(event.date).toLocaleDateString()}</p>
        <p>Location: {event.location}</p>
        {event.price && <p>Price: €{event.price}</p>}
      </div>
      <div className="card__footer">
        <button className="button button--primary">Register</button>
      </div>
    </div>
  );
};