from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Site configuration
site_config = {
    "sections": {
        "hero": True,
        "about": True,
        "experience": True,
        "projects": True,
        "skills": True,
        "education": True,
        "recognition": True,
        "testimonials": False,  # Set to False to hide the testimonials section
        "blog": False,
        "contact": True
    }
}

# Portfolio data
portfolio_data = {
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
    "experience": [
        {
            "title": "Senior Software Engineer",
            "company": "Nokia Solutions Networks",
            "location": "Bengaluru, KA",
            "period": "July 2024 – Present",
            "achievements": [
                "Developed automated CI/CD pipelines and infrastructure in the Base Image Refresh Automation team to improve security, scalability, and reliability of multi-cloud deployments",
                "Automated 10+ CI/CD pipelines using custom-built utilities for Gerrit, Jenkins, Helm, and JIRA, reducing manual release tasks by over 70%",
                "Built a parallel image rebuild framework using master-worker architecture, reducing image creation time from 1 day to under 2.5 hours",
                "Deployed Prometheus and Grafana for lab environment metrics tracking, enabling 30% infrastructure cost savings through proactive resource optimization",
                "Built and deployed a Flask Validation API with LDAP auth, now actively used by 6+ teams to streamline internal compliance validations",
                "Restructured Jenkins job hierarchies and automated Helm chart/registry syncs, reducing manual errors and cutting configuration time from a week to under 7 hours",
                "Initiated unit test development from scratch, increasing test coverage by 33%; mentored 3 engineers who now lead key DevOps, SRE, and backend roles",
                "Managed JIRA, Jenkins, GitLab, and Gerrit under production and non-prod functional accounts, acting as critical owner for high-impact tool chain operations"
            ]
        },
        {
            "title": "Associate Software Engineer", 
            "company": "Nokia Solutions Networks",
            "location": "Bengaluru, KA",
            "period": "Aug 2022 – June 2024",
            "achievements": [
                "Delivered platform-agnostic backend and CI/CD solutions across AKS and Tanzu (TKG), contributing to scalable deployment of containerized services",
                "Designed and maintained CI/CD pipelines for critical services (Kafka, NGINX Ingress, Nokia Common Services) across 2 platforms, standardizing certification workflows",
                "Created 3 reusable Helm charts for services including Cert Manager and MariaDB, which were adopted by 2 additional teams to accelerate cloud-native onboarding",
                "Deployed both Istio and non-Istio service meshes to support hybrid networking requirements, increasing deployment flexibility across platforms",
                "Automated namespace-restricted kubeconfig generation and RBAC-based access control for Kubernetes clusters, improving onboarding security and efficiency",
                "Authored detailed comparisons between Azure-native and internal Nokia services to guide cloud adoption strategies and architectural decisions",
                "Migrated 3 asset pipelines from legacy systems to containerized flows, reducing runtime from ~18 hours to ~9 hours and improving delivery velocity",
                "Centralized X-Ray test result uploads across asset pipelines, standardizing reporting and ensuring test result reliability",
                "Built Kafka testing framework and integrated Mirror-Maker certification into ACC pipeline, streamlining test automation and expanding certification coverage",
                "Contributed key enhancements to the CI/CD framework to support onboarding of new components and custom pipeline requirements"
            ]
        },
        {
            "title": "Student Trainee",
            "company": "Nokia Solutions Networks", 
            "location": "Bengaluru, KA",
            "period": "Jan 2022 – May 2022",
            "achievements": [
                "Deployed and configured Apache Spark and RabbitMQ on Nokia Container Services (NCS), enabling scalable stream and message processing in internal lab clusters",
                "Set up ingress controllers to securely expose services in Kubernetes clusters, improving internal access and traffic routing",
                "Supported lifecycle operations (install, upgrade, decommission) for cloud-native services deployed on NCS and RedHat OpenShift (OCP), contributing to system stability and performance"
            ]
        }
    ],
    "projects": [
        {
            "name": "Base Image Refresh Automation",
            "description": "Automated CI/CD pipelines and infrastructure to improve security, scalability, and reliability of multi-cloud deployments",
            "technologies": ["Python", "Jenkins", "Helm", "Kubernetes", "JIRA"],
            "impact": "Reduced manual release tasks by over 70%",
            "image": "cicd_project.png"
        },
        {
            "name": "Parallel Image Rebuild Framework",
            "description": "Built master-worker architecture framework for parallel image rebuilding",
            "technologies": ["Python", "Docker", "Kubernetes", "Jenkins"],
            "impact": "Reduced image creation time from 1 day to under 2.5 hours",
            "image": "k8s_monitoring.png"
        },
        {
            "name": "Flask Validation API",
            "description": "Internal compliance validation API with LDAP authentication",
            "technologies": ["Flask", "Python", "LDAP", "REST API"],
            "impact": "Actively used by 6+ teams for streamlined compliance validations",
            "image": "cicd_project.png"
        },
        {
            "name": "Infrastructure Monitoring Solution", 
            "description": "Deployed Prometheus and Grafana for comprehensive lab environment metrics tracking",
            "technologies": ["Prometheus", "Grafana", "Kubernetes", "Docker"],
            "impact": "Enabled 30% infrastructure cost savings through proactive optimization",
            "image": "k8s_monitoring.png"
        }
    ],
    "skills": {
        "Languages & Frameworks": {
            "Python": 90,
            "Flask": 85,
            "SQL": 80,
            "Bash": 85,
            "C++": 70,
            "Java": 75
        },
        "DevOps & Cloud": {
            "Kubernetes": 90,
            "Helm": 85,
            "Jenkins": 90,
            "GitLab CI": 85,
            "Docker": 90,
            "Ansible": 80,
            "Git": 95,
            "Gerrit": 80,
            "Jira": 85
        },
        "Platforms": {
            "Azure AKS": 85,
            "AWS EKS": 80,
            "GCP GKE": 75,
            "RedHat OCP": 80,
            "Tanzu TKG": 85
        },
        "Tools & Platforms": {
            "PostgreSQL": 80,
            "Linux": 90,
            "X-Ray": 75,
            "Artifactory": 75,
            "Prometheus": 85,
            "Grafana": 85
        }
    },
    "education": [
        {
            "institution": "KLE Technological University",
            "location": "Hubballi, KA", 
            "degree": "Bachelor of Engineering in Computer Science and Engineering",
            "period": "Aug 2018 – June 2022",
            "gpa": "8.52",
            "achievements": [
                "Graduated with distinction in the top 10% of the class",
                "Specialized in Cloud Computing and Distributed Systems",
                "Final year project: 'Containerized Microservices Deployment Framework'"
            ]
        },
        {
            "institution": "Karnataka Pre-University Board",
            "location": "Hubballi, KA", 
            "degree": "Higher Secondary Education, Science Stream",
            "period": "June 2016 – March 2018",
            "gpa": "92.3%",
            "achievements": [
                "Secured 92.3% marks with distinction in Physics, Chemistry, Mathematics, and Computer Science",
                "Ranked in the top 5% of students in the district"
            ]
        }
    ],
    "recognition": [
        "Functional Account Owner: Granted full responsibility over tools like JIRA, Jenkins, Gerrit, and GitLab across production and non-prod environments — a role typically reserved for senior engineers.",
        "Cross-Team CI/CD Leadership: Spearheaded the development of reusable CI/CD workflows adopted by 3+ engineering teams, reducing delivery inconsistency and redundant effort.",
        "Azure Enablement Champion: Delivered structured knowledge-sharing sessions on Azure-native infrastructure and DevOps tooling, improving onboarding speed and upskilling new engineers."
    ],
    "testimonials": [
        {
            "name": "Aditya Sharma",
            "position": "Engineering Manager, Nokia",
            "message": "Pratik is an exceptional engineer with a natural ability to tackle complex infrastructure challenges. His work on the parallel image rebuild framework completely transformed our delivery timelines.",
            "avatar": "profile_pic_template.png"
        },
        {
            "name": "Sneha Patel",
            "position": "Senior DevOps Engineer, Nokia",
            "message": "Working with Pratik on the CI/CD pipeline automation project was a highlight of my career. His technical expertise and collaborative approach raised the bar for our entire team.",
            "avatar": "profile_pic_template.png"
        },
        {
            "name": "Rajat Verma",
            "position": "Cloud Architect, Nokia",
            "message": "Pratik's contributions to our Kubernetes monitoring solutions demonstrated his deep understanding of cloud-native technologies and his commitment to operational excellence.",
            "avatar": "profile_pic_template.png"
        }
    ],
    "blog_posts": [
        {
            "title": "Mastering Kubernetes Multi-Cluster Management",
            "excerpt": "Learn how to effectively manage multiple Kubernetes clusters across different cloud providers, with focus on centralized monitoring and GitOps-based deployments.",
            "date": "August 10, 2025",
            "tags": ["Kubernetes", "DevOps", "Multi-Cloud"],
            "image": "k8s_monitoring.png"
        },
        {
            "title": "Automating CI/CD for Python Microservices",
            "excerpt": "A comprehensive guide to building automated CI/CD pipelines for Python-based microservices using Jenkins, Docker, and Kubernetes.",
            "date": "July 15, 2025",
            "tags": ["Python", "CI/CD", "Microservices"],
            "image": "cicd_project.png"
        },
        {
            "title": "Optimizing Cloud Infrastructure Costs",
            "excerpt": "Practical strategies and tools for reducing cloud costs without sacrificing performance or reliability across multi-cloud environments.",
            "date": "June 22, 2025",
            "tags": ["Cloud", "Cost Optimization", "Infrastructure"],
            "image": "k8s_monitoring.png"
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data, config=site_config)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        try:
            # Configure email
            sender_email = "your-email@gmail.com"  # Replace with your email
            receiver_email = portfolio_data["personal_info"]["email"]
            password = "your-app-password"  # Use app password for Gmail
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = f"Portfolio Contact: {subject}"
            
            # Create email body
            body = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            
            Message:
            {message}
            """
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to server and send email
            # Uncomment the below lines when you're ready to actually send emails
            # server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.starttls()
            # server.login(sender_email, password)
            # server.send_message(msg)
            # server.quit()
            
            return jsonify({'status': 'success', 'message': 'Thank you for your message! I will get back to you soon.'})
        except Exception as e:
            print(f"Error sending email: {e}")
            return jsonify({'status': 'error', 'message': 'Sorry, there was an error sending your message. Please try again later.'})

    return redirect(url_for('index'))

@app.route('/download-resume')
def download_resume():
    # Serve the resume PDF from static folder
    return send_from_directory('static/files', 'Pratik-Ingale_Senior-Software-Engineer.pdf', as_attachment=True)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form.get('newsletter-email')
        
        try:
            # Here you would add code to save the email to a database or send to a mailing service
            # For now, we'll just return a success message
            return jsonify({'status': 'success', 'message': 'Thank you for subscribing to my newsletter!'})
        except Exception as e:
            print(f"Error processing subscription: {e}")
            return jsonify({'status': 'error', 'message': 'Sorry, there was an error processing your subscription. Please try again later.'})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
