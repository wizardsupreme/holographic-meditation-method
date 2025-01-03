from flask import Flask, render_template, request, redirect, url_for, flash
from supabase_py import create_client, Client # type: ignore
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

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
        data = request.form.to_dict()
        # Store registration in Supabase
        result = supabase.table('registrations').insert(data).execute()
        flash('Registration successful! We will contact you soon.', 'success')
    except Exception as e:
        flash('Registration failed. Please try again.', 'error')
    
    return redirect(url_for('home'))

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) 