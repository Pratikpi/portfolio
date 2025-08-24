# Pratik Ingale - Portfolio Website

A modern, interactive portfolio website built with Flask showcasing professional experience as a Senior Software Engineer at Nokia Solutions Networks.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Elements**: Smooth animations, hover effects, and scroll animations
- **Modern UI**: Clean, professional design with a cohesive color scheme
- **Dynamic Content**: Built with Flask for easy content management
- **Contact Form**: Working contact form for potential opportunities
- **Skills Visualization**: Animated skill bars showing proficiency levels
- **Project Showcase**: Detailed project cards with technologies and impact metrics

## Quick Start

### Local Development

1. **Clone/Extract the project**
2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate      # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Add your images**:
   - Add your profile picture as `static/images/profile_pic.png`
   - Add project screenshots as `static/images/cicd_project.png` and `static/images/k8s_monitoring.png`

5. **Run the application**:
   ```bash
   python app.py
   ```
6. **Visit**: `http://127.0.0.1:5000`

### PythonAnywhere Deployment

1. **Upload project files** to `/home/yourusername/mysite/`
2. **Create virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 mysite-env
   ```
3. **Install dependencies**:
   ```bash
   cd /home/yourusername/mysite
   pip install -r requirements.txt
   ```
4. **Create web app** (Manual configuration, Python 3.10)
5. **Configure WSGI file**:
   ```python
   import sys
   import os

   project_home = '/home/yourusername/mysite'
   if project_home not in sys.path:
       sys.path = [project_home] + sys.path

   from app import app as application

   if __name__ == "__main__":
       application.run()
   ```
6. **Set virtual environment**: `/home/yourusername/.virtualenvs/mysite-env`
7. **Configure static files**:
   - URL: `/static/`
   - Directory: `/home/yourusername/mysite/static/`
8. **Reload web app**

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern animations
- **Icons**: Font Awesome
- **Deployment**: PythonAnywhere

## Project Structure

```
pratik_portfolio/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/
│   └── index.html         # HTML template
└── static/
    ├── css/
    │   └── style.css      # Stylesheet
    ├── js/
    │   └── script.js      # JavaScript functionality
    └── images/
        ├── profile_pic.png     # Your profile picture
        ├── cicd_project.png    # Project screenshot
        └── k8s_monitoring.png  # Project screenshot
```

## Customization

### Update Personal Information
Edit the `portfolio_data` dictionary in `app.py`:

```python
"personal_info": {
    "name": "Your Name",
    "title": "Your Title", 
    "email": "your.email@example.com",
    # ... etc
}
```

### Add New Projects
Add to the `projects` list in `app.py`:

```python
{
    "name": "New Project",
    "description": "Project description",
    "technologies": ["Python", "Django"],
    "impact": "Impact achieved",
    "image": "new_project.png"
}
```

### Update Skills
Modify the `skills` dictionary with your proficiency levels (0-100):

```python
"Languages & Frameworks": {
    "Python": 90,
    "JavaScript": 85,
    # ... etc
}
```

## Features

### Sections
1. **Hero Section**: Professional introduction with contact information
2. **About**: Professional summary and key achievements
3. **Experience**: Detailed work history with accomplishments
4. **Projects**: Key projects with technologies and impact
5. **Skills**: Technical skills with visual proficiency indicators
6. **Education**: Academic background
7. **Recognition**: Awards and leadership achievements
8. **Contact**: Contact form and information

### Interactive Elements
- Smooth scrolling navigation
- Mobile-responsive hamburger menu
- Animated skill bars
- Hover effects on cards and buttons
- Scroll-triggered animations
- Working contact form with notifications

## Support

For issues or questions:
- Check the Flask documentation: https://flask.palletsprojects.com/
- PythonAnywhere help: https://help.pythonanywhere.com/
- Contact: pi.pratik.ingale@gmail.com

## License

© 2024 Pratik Ingale. All rights reserved.

---

**Your professional portfolio is ready to showcase your expertise to the world!** 🌟