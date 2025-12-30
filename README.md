# Portfolio - Pratik Ingale

A modern, responsive, and high-performance portfolio website built with **Flask** and **Vanilla CSS**. This project showcases professional experience, skills, and projects with a focus on clean architecture and premium design.

## 🚀 Features

- **Modular Backend**: Built using the Flask Application Factory pattern with Blueprints.
- **Dynamic Content**: All portfolio data is managed in a single source of truth (`app/content.py`), making updates effortless.
- **Premium Design**: Dark-mode first, glassmorphism UI, and fully responsive layout without heavy frameworks.
- **Resume Download**: Integrated secure resume distribution.
- **SEO Optimized**: Semantic HTML5 and meta tags for better visibility.

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3 (Variables, Flexbox/Grid), ES6 JavaScript
- **Deployment**: Ready for WSGI (Gunicorn/uWSGI) or Docker.

## 📂 Project Structure

```
portfolio/
├── app/
│   ├── blueprints/      # Application routes (Main, etc.)
│   ├── static/          # Static assets (CSS, JS, Files)
│   ├── templates/       # HTML templates (Subject to Jinja2 context)
│   ├── config.py        # Configuration settings (Dev/Prod)
│   ├── content.py       # PURE DATA: Edit this file to update your portfolio text!
│   └── __init__.py      # App factory
├── run.py               # Entry point
└── requirements.txt     # Python dependencies
```

## ⚡ Quick Start

1.  **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd portfolio
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python3 run.py
    ```

4.  **Visit:** `http://127.0.0.1:5000`

## 📝 Customization

To update your information (About, Experience, Projects), simply edit **`app/content.py`**. The site will automatically reflect changes.

## 📄 License

[MIT](LICENSE)
