from flask import Flask,render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is the about page.</p>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
