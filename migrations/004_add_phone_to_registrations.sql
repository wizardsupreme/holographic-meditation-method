-- Up Migration
ALTER TABLE registrations
ADD COLUMN phone TEXT;

-- Down Migration
ALTER TABLE registrations
DROP COLUMN phone; 