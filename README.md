# Flask Beginner's Toolkit

A simple and beginner-friendly Flask application to help learn web development with Python and Flask.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Routes](#api-routes)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- Simple Flask web server setup
- HTML template rendering
- Static file serving (CSS, images, etc.)
- Easy-to-understand project structure for beginners
- Debug mode enabled for development

## 📁 Project Structure

```
my-flask-toolkit/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── toolkit-document.md   # Additional documentation
├── static/
│   └── style.css         # CSS stylesheets
└── template/
    └── index.html        # HTML templates
```

## 📦 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd my-flask-toolkit
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Run the Flask application**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Open your web browser and navigate to: `http://localhost:5000`
   - You should see the homepage with "Hello, World! 🚀" message

3. **Stop the server**
   - Press `Ctrl+C` in the terminal

## 🌐 Routes

| Route | Description |
|-------|-------------|
| `/` | Home page - displays welcome message and learning list |
| `/about` | About page - information about the project |

## ⚙️ Configuration

### Debug Mode

The application runs in debug mode by default (`debug=True`). This enables:
- Hot reloading when code changes
- Detailed error messages
- Interactive debugger

**To disable debug mode** (for production), edit `app.py`:
```python
app.run(debug=False)
```

### Port Configuration

The default port is `5000`. To use a different port, modify `app.py`:
```python
app.run(debug=True, port=8080)
```

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
# Change the port in app.py or run on a different port
python app.py  # Then modify port in app.py
```

### Module Not Found Error
Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Templates Not Found
- Verify the `template/` folder exists (note: Flask uses `templates/` by default)
- Update `app.py` if your folder name is different:
  ```python
  app = Flask(__name__, template_folder='template')
  ```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License. See the LICENSE file for more details.

---

**Happy coding!** 🎉
