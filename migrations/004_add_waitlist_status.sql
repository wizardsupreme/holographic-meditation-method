-- Add waitlist status to registrations table
ALTER TABLE registrations 
ADD COLUMN IF NOT EXISTS waitlist_status text 
DEFAULT 'waiting'
CHECK (waitlist_status IN ('waiting', 'notified', 'registered', 'cancelled'));

-- Update existing records
UPDATE registrations 
SET waitlist_status = 'waiting' 
WHERE waitlist_status IS NULL; 