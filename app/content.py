portfolio_data = {
    "personal_info": {
        "name": "Pratik Ingale",
        "title": "Software Developer",
        "email": "pi.pratik.ingale@gmail.com",
        "phone": "+91 8310270881",
        "location": "Bengaluru, KA",
        "social": {
            "linkedin": "https://linkedin.com/in/pratik-pi",
            "github": "https://github.com/pratikpi",
            "twitter": "https://twitter.com/pi_pratik",
            "medium": "pratik.ingale"
        },
        "about": {
            "summary": "Software Developer with 3+ years of experience designing REST APIs, building multithreaded workflow orchestration systems, and developing reliable backend automation in cloud-native environments. Skilled in Python, Flask, FastAPI, SQLAlchemy, Event-Driven Architecture, and modular backend architecture.",
            "hero_bio": "Building high-performance Python backends and automating scalable cloud infrastructure.",
            "interests": ["Python Development", "Cloud Architecture", "Infrastructure Automation", "Kubernetes Ecosystem", "Continuous Integration"]
        }
    },
    "skills": {
        "Languages & Backend": ["Python", "Flask", "FastAPI", "SQL", "Bash"],
        "Python Ecosystem": ["SQLAlchemy", "AsyncIO", "Alembic", "Transitions", "Pydantic", "Pytest"],
        "Database": ["PostgreSQL", "SQLite", "Schema Design", "Data Modeling"],
        "DevOps & Cloud": ["Kubernetes (AKS, EKS, GKE, OCP, TKG)", "Helm", "Docker", "GitLab CI", "Jenkins", "Ansible", "Git", "Gerrit"],
        "Observability": ["Prometheus", "Grafana"]
    },
    "experience": [
        {
            "company": "NOKIA SOLUTIONS NETWORKS",
            "role": "Senior Software Engineer",
            "duration": "July 2024 – Present",
            "location": "Bengaluru, KA",
            "description": [
                "Re-architected a monolithic workflow engine into a modular, Python orchestrator using event-driven state machines and worker queues; enabled parallel execution across 5 sub-state machines.",
                "Designed and deployed 6–10 Flask-based REST API endpoints for orchestration triggers, cleanup workflows, CRUD operations, and Jenkins automation.",
                "Recognized for Python engineering leadership, creating reusable automation libraries and driving code standardization adopted across multiple teams.",
                "Developed a master–worker Python framework for parallel image rebuilds, cutting build time from 8 hours to under 2.5 hours.",
                "Defined code-quality guidelines and standardized Python best practices, improving maintainability and onboarding efficiency.",
                "Automated Helm chart and registry synchronization workflows, reducing configuration time from 1 week to under 7 hours.",
                "Implemented unit testing from scratch using Pytest and improved overall test coverage by 33%.",
                "Coordinated Python-driven interactions with JIRA, Jenkins, GitLab, and Gerrit for production-grade automation.",
                "Integrated backend automation flows with Prometheus/Grafana dashboards for metrics and performance insights."
            ]
        },
        {
            "company": "NOKIA SOLUTIONS NETWORKS",
            "role": "Associate Software Engineer",
            "duration": "Aug 2022 – June 2024",
            "location": "Bengaluru, KA",
            "description": [
                "Built Python-based automation modules powering deployments on Kubernetes, supporting backend workflows for distributed components.",
                "Developed Python-driven CI/CD modules for Kafka and NGINX Ingress certification pipelines.",
                "Designed and implemented a complete Kafka/MirrorMaker testing framework using Python, Radish, and Mako.",
                "Containerized and refactored automation pipelines by replacing SSH with subprocess and modular Python utilities, reducing execution time by 50% (18h → 9h).",
                "Automated namespace-scoped kubeconfig generation and RBAC provisioning with Python + Ansible.",
                "Implemented service mesh–aware backend testing workflows (Istio and non-Istio).",
                "Centralized X-Ray test uploads using Python-driven Jenkins extensions.",
                "Conducted structured knowledge-transfer sessions on Azure architecture and DevOps tooling."
            ]
        },
        {
             "company": "NOKIA SOLUTIONS NETWORKS",
             "role": "Student Trainee",
             "duration": "Jan 2022 – May 2022",
             "location": "Bengaluru, KA",
             "description": [
                 "Deployed distributed systems (Spark, Kafka, RabbitMQ) on Kubernetes.",
                 "Configured ingress controllers and routing rules for backend services on Kubernetes.",
                 "Assisted with lifecycle operations for cloud-native services on NCS and OpenShift."
             ]
        }
    ],
    "education": [
        {
            "institution": "KLE TECHNOLOGICAL UNIVERSITY",
            "degree": "Bachelor of Engineering in Computer Science and Engineering",
            "year": "Aug 2018 – June 2022",
            "gpa": "8.52",
            "location": "Hubballi, KA"
        }
    ],
    "projects": [
        {
            "name": "Async Workflow Orchestrator",
            "description": "Designed a production-style asynchronous workflow orchestration engine in Python using asyncio, thread-based workers, and state-machine-driven execution. Built REST APIs with FastAPI and implemented persistent workflow state using SQLAlchemy.",
            "tech_stack": ["Python", "FastAPI", "SQLAlchemy", "AsyncIO", "SQLite/PostgreSQL"],
            "link": "https://github.com/pratikpi/async-workflow-orchestrator"
        },
        {
            "name": "PyDM",
            "description": "A high-performance, segmented download manager built with Python's asyncio. It maximizes bandwidth utilization by downloading file segments concurrently and features robust resume capabilities.",
            "tech_stack": ["Python", "asyncio", "aiohttp", "aiofiles", "tqdm"],
            "link": "https://github.com/pratikpi/PyDM"
        }
    ]
}
