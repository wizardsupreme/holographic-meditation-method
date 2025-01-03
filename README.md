# Holographic Foundation Website

A Flask-based website for the Holographic Foundation, featuring meditation workshops and retreats.

## Project Structure

```
holographic-foundation/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   ├── meditation-bg.jpg
│   │   └── ...
│   └── favicon/
│       ├── favicon.ico
│       └── ...
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── lisbon_workshop.html
│   ├── bali_retreat.html
│   └── confirmation.html
├── migrations/
│   ├── 001_create_registrations_table.sql
│   ├── 002_update_registration_policies.sql
│   └── 003_fix_registration_policies.sql
├── scripts/
│   └── generate_favicon.py
├── app.py
├── requirements.txt
├── .env
└── .gitignore
```

## Local Development Setup


1. **Clone the repository**
   git clone \[repository-url\]
   cd holographic-foundation
2. **Create and activate a virtual environment**

   # On Windows

   python -m venv venv
   venv\\Scripts\\activate

   # On macOS/Linux

   python3 -m venv venv
   source venv/bin/activate
3. **Install dependencies**
   pip install -r requirements.txt
4. **Set up environment variables**
   * Copy .env.example to .env
   * Update the following variables in .env:
     FLASK_SECRET_KEY=your-secret-key-here
     SUPABASE_URL=your-supabase-url
     SUPABASE_KEY=your-supabase-key
5. **Create required directories and files**
   mkdir -p static/images
   mkdir -p static/css
6. **Add required images**
   * Add meditation-bg.jpg to static/images/ directory
7. **Run the application**
   python app.py

The site will be available at http://localhost:5000

## Supabase Setup


1. Create a new Supabase project
2. Create a 'registrations' table with the following columns:
   * id (int8) - primary key
   * created_at (timestamp with timezone)
   * name (text)
   * email (text)
   * event_type (text)
   * notes (text)

## Deployment


1. **Prepare for deployment**
   * Ensure all dependencies are in requirements.txt
   * Set up production environment variables
   * Configure your web server (e.g., Gunicorn)
2. **Deploy to your chosen platform**
   * Heroku
   * DigitalOcean
   * AWS
   * etc.
3. **Point your domain**
   * Update DNS settings to point to your deployed application
   * Configure SSL certificates

## Features

* Landing pages for workshops and retreats
* Registration system integrated with Supabase
* Responsive design using Bootstrap 5
* Flash messages for user feedback
* Silva Method meditation content
* Workshop pricing:
  * Lisbon Workshop: €350 per person
  * Bali Retreat: €5,000 per person

## Tech Stack

* Backend: Flask
* Frontend: Bootstrap 5
* Database: Supabase
* Deployment: Gunicorn

## Contributing


1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


