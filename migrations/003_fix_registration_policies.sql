-- Drop all existing policies
drop policy if exists "Enable insert for authenticated users only" on registrations;
drop policy if exists "Enable insert for all users" on registrations;
drop policy if exists "Enable read access for authenticated users" on registrations;

-- Temporarily disable RLS to test if that's the issue
alter table registrations disable row level security;

-- Create a completely open policy
create policy "Enable all access"
on registrations
for all
using (true)
with check (true); 