from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage for mess menu
menu_data = {
    'breakfast': '',
    'lunch': '',
    'snacks': '',
    'dinner': ''
}

# Temporary storage for feedback
feedback_data = []

# Home page route
@app.route('/')
def home():
    return render_template('index.html', menu=menu_data)

# Admin page route
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Upload menu route
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get form data
        menu_data['breakfast'] = request.form.get('breakfast')
        menu_data['lunch'] = request.form.get('lunch')
        menu_data['snacks'] = request.form.get('snacks')
        menu_data['dinner'] = request.form.get('dinner')
        return redirect('/')  # Redirect to home page after submission
    return render_template('upload_menu.html')

# Feedback form route
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Get feedback form data
        name = request.form.get('name')
        fb_text = request.form.get('feedback')
        # Save feedback to the list
        feedback_data.append({'name': name, 'feedback': fb_text})
        return redirect('/')  # Redirect to home page after submission
    return render_template('feedback.html')

# View feedback route
@app.route('/view_feedback')
def view_feedback():
    return render_template('view_feedback.html', feedback_list=feedback_data)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
