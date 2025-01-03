from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, make_response
from supabase_py import create_client, Client # type: ignore
import os
from dotenv import load_dotenv # type: ignore
from datetime import datetime
from werkzeug.middleware.proxy_fix import ProxyFix

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Handle reverse proxy headers
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Disable Flask's default static file cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

# Verify Supabase connection at startup
try:
    # Test query to verify connection
    test_query = supabase.table('registrations').select("*").limit(1).execute()
    print("Supabase connection successful")
except Exception as e:
    print("Supabase connection error:", str(e))
    print("SUPABASE_URL:", os.getenv('SUPABASE_URL'))
    print("SUPABASE_KEY:", os.getenv('SUPABASE_KEY')[:10] + "...")  # Only print first 10 chars of key

def sanitize_form_data(form_data):
    """Clean and validate form data before storing"""
    allowed_fields = ['name', 'email', 'event_type', 'background', 'experience', 'notes']
    return {k: v.strip() for k, v in form_data.items() if k in allowed_fields and v}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lisbon-workshop')
def lisbon_workshop():
    return render_template('lisbon_workshop.html')

@app.route('/bali-retreat')
def bali_retreat():
    return render_template('bali_retreat.html')

@app.route('/success-stories')
def success_stories():
    return render_template('success_stories.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        data = sanitize_form_data(request.form.to_dict())
        
        # Validate required fields
        if not all(k in data for k in ['name', 'email', 'event_type']):
            raise ValueError("Missing required fields")
        
        # Add timestamp
        data['created_at'] = datetime.utcnow().isoformat()
        
        print("Attempting to insert data:", data)  # Debug print
        
        # Store registration in Supabase
        try:
            print("Supabase URL:", os.getenv('SUPABASE_URL'))
            print("Supabase key length:", len(os.getenv('SUPABASE_KEY')))
            result = supabase.table('registrations').insert(data).execute()
            print("Supabase response:", result)  # Debug print
        except Exception as supabase_error:
            print("Supabase error type:", type(supabase_error))
            print("Supabase error:", str(supabase_error))
            print("Supabase error details:", getattr(supabase_error, 'details', None))
            raise
        
        # Redirect to confirmation page
        return redirect(url_for('confirmation', event_type=data['event_type']))
        
    except Exception as e:
        print(f"Registration error: {str(e)}", flush=True)  # For debugging
        print(f"Error type: {type(e)}", flush=True)
        flash('Registration failed. Please try again.', 'error')
        return redirect(url_for('home'))

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/confirmation/<event_type>')
def confirmation(event_type):
    messages = {
        'bali_retreat': {
            'message': 'Your application for the Bali Immersion Retreat has been received. This exclusive retreat is limited to 12 participants, and we carefully review each application.',
            'return_url': '/bali-retreat'
        },
        'lisbon_workshop': {
            'message': 'Your application for the Lisbon Workshop has been received. We look forward to potentially welcoming you to this transformative experience.',
            'return_url': '/lisbon-workshop'
        },
        'general': {
            'message': 'Your application has been received. We\'ll review your information and contact you about the best program for your goals.',
            'return_url': '/apply'
        }
    }
    
    event_info = messages.get(event_type, messages['general'])
    return render_template('confirmation.html', 
                         message=event_info['message'],
                         return_url=event_info['return_url'])

@app.route('/test-favicon')
def test_favicon():
    return """
    <html>
        <head>
            <link rel="icon" type="image/x-icon" href="/static/favicon/favicon.ico">
        </head>
        <body>
            <h1>Favicon Test Page</h1>
        </body>
    </html>
    """

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'favicon'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.after_request
def add_header(response):
    """Add headers to disable caching for static files"""
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True) 