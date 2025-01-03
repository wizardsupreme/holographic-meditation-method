# Database Structure

## Tables

### registrations

Stores all application submissions for workshops and retreats.

| Column | Type | Constraints | Description |
|----|----|----|----|
| id | bigint | PK, identity | Unique identifier |
| created_at | timestamp | not null | Timestamp of registration |
| name | text | not null | Applicant's full name |
| email | text | not null | Applicant's email |
| event_type | text | not null | Type of event ('bali_retreat', 'lisbon_workshop', 'general') |
| background | text | nullable | Applicant's professional background |
| experience | text | nullable | Previous meditation experience |
| notes | text | nullable | Additional notes or goals |
| status | text | default 'pending' | Application status |

### Indexes

* `registrations_email_idx`: Index on email for faster lookups
* `registrations_event_type_idx`: Index on event_type for filtering
* `registrations_created_at_idx`: Index on created_at for chronological queries

### Constraints

* `valid_event_type`: Ensures event_type is one of: 'bali_retreat', 'lisbon_workshop', 'general'

## Row Level Security (RLS)

The registrations table has RLS enabled with the following policies:

* Insert: Allowed for anonymous users (public access)
* Select: Allowed for authenticated users

## Future Considerations

Potential future additions:


1. Payment tracking table
2. User profiles table
3. Event schedules table
4. Testimonials table


