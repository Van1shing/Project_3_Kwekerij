from flask import Flask, render_template, send_from_directory, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for flash messages

# Routes for the main pages
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically handle the form data (e.g., send email, save to database)
        # For now, we'll just flash a success message
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/communities')
def communities():
    return render_template('communities.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

# Route for serving static files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/learn_more_blooming')
def learn_more_blooming():
    return render_template('learn_more_blooming.html')

@app.route('/learn_more_language_cafe')
def learn_more_language_cafe():
    return render_template('learn_more_language_cafe.html')

@app.route('/learn_more_generations')
def learn_more_generations():
    return render_template('learn_more_generations.html')

@app.route('/learn_more_companies')
def learn_more_companies():
    return render_template('learn_more_companies.html')

@app.route('/mentoring')
def mentoring():
    return render_template('mentoring.html')

if __name__ == '__main__':
    app.run(debug=True) 