from flask import Flask, render_template
from datetime import datetime
import os

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), '../frontend/templates'),
        static_folder=os.path.join(os.path.dirname(__file__), '../frontend/static')
    )

    @app.route('/')
    def home():
        return render_template(
            'index.html',
            title="Flask Toolkit",
            message="Welcome to Flask Toolkit 🚀",
            year=datetime.now().year
        )

    @app.route('/about')
    def about():
        return render_template(
            'about.html',
            title="About - Flask Toolkit",
            year=datetime.now().year
        )

    return app