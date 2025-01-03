from flask import Flask, render_template, request, redirect, url_for, flash
from supabase_py import create_client, Client # type: ignore
import os
from dotenv import load_dotenv # type: ignore
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

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
        
        # Store registration in Supabase
        result = supabase.table('registrations').insert(data).execute()
        
        # Redirect to confirmation page
        return redirect(url_for('confirmation', event_type=data['event_type']))
        
    except Exception as e:
        print(f"Registration error: {str(e)}")  # For debugging
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

if __name__ == '__main__':
    app.run(debug=True) 