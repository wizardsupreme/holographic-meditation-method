// src/components/EventList.tsx
import React, { useState, useEffect } from 'react';
import { getSupabaseClient } from '../utils/supabase';
import { EventCard } from './EventCard';
import type { Event } from '../@types/meditation';

const EventList: React.FC = () => {
  const [events, setEvents] = useState<Event[]>([]);

  useEffect(() => {
    const supabase = getSupabaseClient();
    if (!supabase) return;

    async function fetchEvents() {
      const { data, error } = await supabase
        .from('events')
        .select('*')
        .order('date', { ascending: true });

      if (!error) {
        setEvents(data || []);
      }
    }

    fetchEvents();
  }, []);

  return (
    <div className="event-list">
      {events.length === 0 ? (
        <p>No events scheduled</p>
      ) : (
        events.map(event => (
          <EventCard key={event.id} event={event} />
        ))
      )}
    </div>
  );
};

export default EventList;