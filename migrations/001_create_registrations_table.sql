-- Create registrations table
create table registrations (
    id bigint primary key generated always as identity,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    name text not null,
    email text not null,
    event_type text not null,
    background text,
    experience text,
    notes text,
    status text default 'pending',
    constraint valid_event_type check (event_type in ('bali_retreat', 'lisbon_workshop', 'general'))
);

-- Create indexes for better performance
create index registrations_email_idx on registrations(email);
create index registrations_event_type_idx on registrations(event_type);
create index registrations_created_at_idx on registrations(created_at desc);

-- Add RLS (Row Level Security) policies
alter table registrations enable row level security;

-- Create policy to allow inserts from authenticated users
create policy "Enable insert for authenticated users only"
on registrations for insert
to authenticated
with check (true);

-- Create policy to allow reading by authenticated users
create policy "Enable read access for authenticated users"
on registrations for select
to authenticated
using (true); 