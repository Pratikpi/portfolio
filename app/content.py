portfolio_data = {
    "personal_info": {
        "name": "Pratik Ingale",
        "title": "Senior Software Engineer",
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
            "summary": "Python backend engineer with 4 years of experience. At Nokia I design REST APIs and multithreaded workflow orchestration for cloud-native platforms, with a focus on reusable libraries, event-driven execution, and reliable automation.",
            "hero_bio": "Python backends and workflow orchestration for cloud-native platforms — currently at Nokia.",
            "interests": ["Python Development", "Cloud Architecture", "Infrastructure Automation", "Kubernetes Ecosystem", "Continuous Integration"]
        }
    },
    "skills": {
        "Languages & Backend": ["Python", "Flask", "FastAPI", "SQL", "Bash"],
        "Python Ecosystem": ["SQLAlchemy", "AsyncIO", "Alembic", "Transitions", "Pydantic", "Pytest"],
        "Database": ["PostgreSQL", "SQLite", "Schema Design", "Data Modeling"],
        "DevOps & Cloud": ["Kubernetes (AKS, EKS, GKE, OCP, TKG)", "Helm", "Docker", "GitLab CI", "Jenkins", "Ansible", "Git", "Gerrit"],
        "Observability & Infrastructure": ["Prometheus", "Grafana", "Linux"]
    },
    "experience": [
        {
            "company": "Nokia Solutions Networks",
            "role": "Senior Software Engineer",
            "duration": "July 2024 – Present",
            "location": "Bengaluru, KA",
            "description": [
                "Turned a monolithic workflow engine into a modular Python orchestrator with event-driven state machines and worker queues — parallel execution across five sub-state machines.",
                "Shipped Flask REST APIs for orchestration, cleanup, CRUD, and Jenkins automation, backed by PostgreSQL and internal state stores.",
                "Cut parallel image rebuilds from 8 hours to under 2.5 hours, and Helm/registry sync from a week to under 7 hours.",
                "Raised Pytest coverage by 33% and standardized reusable Python libraries adopted across teams."
            ]
        },
        {
            "company": "Nokia Solutions Networks",
            "role": "Associate Software Engineer",
            "duration": "Aug 2022 – June 2024",
            "location": "Bengaluru, KA",
            "description": [
                "Built Python automation for Kubernetes deployments, including Kafka and NGINX Ingress certification pipelines.",
                "Designed a Kafka/MirrorMaker test framework (Python, Radish, Mako) and halved pipeline runtime (18h → 9h) by replacing SSH with subprocess utilities.",
                "Automated namespace kubeconfig and RBAC with Python and Ansible; added Istio-aware backend test workflows."
            ]
        },
        {
            "company": "Nokia Solutions Networks",
            "role": "Student Trainee",
            "duration": "Jan 2022 – May 2022",
            "location": "Bengaluru, KA",
            "description": [
                "Deployed Spark, Kafka, and RabbitMQ on Kubernetes and configured ingress for backend services on NCS and OpenShift."
            ]
        }
    ],
    "education": [
        {
            "institution": "KLE Technological University",
            "degree": "Bachelor of Engineering in Computer Science and Engineering",
            "year": "Aug 2018 – June 2022",
            "gpa": "8.52",
            "location": "Hubballi, KA"
        }
    ],
    "projects": [
        {
            "name": "Async Workflow Orchestrator",
            "description": "Production-style async orchestration in Python: asyncio workers, state-machine execution, FastAPI triggers and retries, SQLAlchemy persistence on SQLite/PostgreSQL.",
            "tech_stack": ["Python", "FastAPI", "SQLAlchemy", "AsyncIO", "SQLite/PostgreSQL"],
            "link": "https://github.com/pratikpi/async-workflow-orchestrator"
        },
        {
            "name": "PyDM",
            "description": "Segmented download manager using asyncio — concurrent file segments, better bandwidth use, and resume support.",
            "tech_stack": ["Python", "asyncio", "aiohttp", "aiofiles", "tqdm"],
            "link": "https://github.com/pratikpi/PyDM"
        }
    ]
}
