document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const navbar = document.querySelector('.navbar');

    const hamburgerIsVisible = () => {
        if (!menuToggle) {
            return false;
        }
        return window.getComputedStyle(menuToggle).display !== 'none';
    };

    const setMenuOpen = (open) => {
        if (!menuToggle || !navLinks) {
            return;
        }
        menuToggle.classList.toggle('is-active', open);
        navLinks.classList.toggle('active', open);
        menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        menuToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        document.body.style.overflow = open ? 'hidden' : '';
    };

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            const willOpen = !navLinks.classList.contains('active');
            setMenuOpen(willOpen);
        });

        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                setMenuOpen(false);
            });
        });

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape' && navLinks.classList.contains('active')) {
                setMenuOpen(false);
                menuToggle.focus();
            }
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetEl = document.querySelector(targetId);

            if (targetEl) {
                targetEl.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        if (!navbar) {
            return;
        }

        const currentScroll = window.pageYOffset;

        // Never hide the bar while the hamburger is the only way to open nav.
        if (hamburgerIsVisible()) {
            navbar.style.transform = 'translateY(0)';
            lastScroll = currentScroll;
            return;
        }

        if (currentScroll > lastScroll && currentScroll > 80) {
            navbar.style.transform = 'translateY(-100%)';
            navbar.style.transition = 'transform 0.3s ease-in-out';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        lastScroll = currentScroll;
    });

    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.section, .hero-content, .project-card, .timeline-item, .skill-category');
    animatedElements.forEach((el) => {
        el.classList.add('reveal');
        observer.observe(el);
    });
});
