from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__, template_folder='template')

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html', 
                         title="Flask Beginner's Toolkit",
                         message="Hello, World! 🚀")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)