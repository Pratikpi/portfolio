"""
Portfolio data management module
Separates data from application logic for better maintainability
"""

def get_site_config():
    """Get site configuration"""
    return {
        "sections": {
            "hero": True,
            "about": True,
            "experience": True,
            "projects": True,
            "skills": True,
            "education": True,
            "recognition": True,
            "testimonials": False,
            "blog": False,
            "contact": True
        }
    }

def get_portfolio_data():
    """Get portfolio data"""
    return {
        "personal_info": {
            "name": "Pratik Ingale",
            "title": "Senior Software Engineer",
            "location": "Bengaluru, KA",
            "phone": "+91 8310270881",
            "email": "pi.pratik.ingale@gmail.com",
            "linkedin": "https://linkedin.com/in/pratik-ingale",
            "github": "pratik-ingale",
            "twitter": "https://twitter.com/pratik_ingale",
            "medium": "pratik.ingale",
            "bio": "I am a passionate cloud-native Python backend developer with expertise in building scalable systems and automating infrastructure. My journey in software engineering has been driven by a strong desire to create efficient, maintainable solutions that solve real-world problems. I enjoy working at the intersection of development and operations, leveraging modern DevOps practices to streamline software delivery.",
            "summary": "Cloud-native Python backend developer with 3 years of hands-on experience building scalable backend systems, automating CI/CD pipelines, and deploying containerized solutions across multi-cloud environments. Proven expertise in Kubernetes, Helm, Jenkins, Flask, and GitOps practices."
        },
        "about": {
            "heading": "About Me",
            "introduction": "I'm a DevOps and cloud enthusiast who bridges the gap between development and operations, creating scalable and resilient infrastructure solutions.",
            "description": "With 3+ years in the software engineering field, I've specialized in developing automated pipelines, Kubernetes deployments, and cloud-native architecture. My experience spans building robust backend systems, optimizing infrastructure, and implementing modern DevOps practices that improve team productivity and application reliability. I'm passionate about keeping up with the latest technologies and finding innovative ways to solve complex technical challenges.",
            "interests": ["Cloud Architecture", "Infrastructure Automation", "Kubernetes Ecosystem", "Continuous Integration", "Python Development"],
            "statistics": [
                {"value": "3+", "label": "Years Experience"},
                {"value": "10+", "label": "CI/CD Pipelines"},
                {"value": "6+", "label": "Cloud Projects"},
                {"value": "3", "label": "Cloud Platforms"}
            ],
            "quote": "I believe the best engineering solutions come from a deep understanding of both code and infrastructure, combined with a relentless focus on automation."
        },
        # Add all other portfolio data sections here...
        "experience": [
            {
                "title": "Senior Software Engineer",
                "company": "Nokia Solutions Networks",
                "location": "Bengaluru, KA",
                "period": "July 2024 – Present",
                "achievements": [
                    "Developed automated CI/CD pipelines and infrastructure in the Base Image Refresh Automation team to improve security, scalability, and reliability of multi-cloud deployments",
                    "Automated 10+ CI/CD pipelines using custom-built utilities for Gerrit, Jenkins, Helm, and JIRA, reducing manual release tasks by over 70%",
                    "Built a parallel image rebuild framework using master-worker architecture, reducing image creation time from 1 day to under 2.5 hours"
                ]
            }
        ],
        "projects": [],  # Add projects data
        "skills": [],    # Add skills data
        "education": [], # Add education data
    }
