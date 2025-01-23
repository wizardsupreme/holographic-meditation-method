import { createClient } from '@supabase/supabase-js';

export const getSupabaseClient = () => {
  if (typeof window === 'undefined') return null;
  
  const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  
  if (!supabaseUrl || !supabaseKey) return null;
  
  return createClient(supabaseUrl, supabaseKey);
};

// src/utils/supabase.ts
export const eventService = {
  async getEvents() {
    const supabase = getSupabaseClient();
    if (!supabase) return [];
    const { data, error } = await supabase
      .from('events')
      .select('*');
    if (error) return [];
    return data;
  }
};