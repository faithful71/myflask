import os
from flask import Flask, render_template
from datetime import datetime

# Absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '../frontend/templates')
STATIC_DIR = os.path.join(BASE_DIR, '../frontend/static')

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)

@app.route('/')
def home():
    return render_template(
        'index.html',
        title="Flask Toolkit",
        message="Welcome to Flask Toolkit 🚀",
        year=datetime.now().year
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))