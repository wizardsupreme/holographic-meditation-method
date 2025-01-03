-- Update RLS policies for registrations table
drop policy if exists "Enable insert for authenticated users only" on registrations;

create policy "Enable insert for all users"
on registrations for insert
to anon
with check (true); 