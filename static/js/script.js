// Portfolio Interactive Functionality
// Initialize all functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    console.log('DOM fully loaded and parsed');
    
    try {
        initNavigation();
        console.log('Navigation initialized');
    } catch (e) {
        console.error('Error initializing navigation:', e);
    }
    
    try {
        initMobileMenu();
        console.log('Mobile menu initialized');
    } catch (e) {
        console.error('Error initializing mobile menu:', e);
    }
    
    try {
        initScrollAnimations();
        console.log('Scroll animations initialized');
    } catch (e) {
        console.error('Error initializing scroll animations:', e);
    }
    
    try {
        initSkillBars();
        console.log('Skill bars initialized');
    } catch (e) {
        console.error('Error initializing skill bars:', e);
    }
    
    try {
        initContactForm();
        console.log('Contact form initialized');
    } catch (e) {
        console.error('Error initializing contact form:', e);
    }
    
    try {
        initSmoothScrolling();
        console.log('Smooth scrolling initialized');
    } catch (e) {
        console.error('Error initializing smooth scrolling:', e);
    }
    
    try {
        initProjectInteractions();
        console.log('Project interactions initialized');
    } catch (e) {
        console.error('Error initializing project interactions:', e);
    }
    
    try {
        // Only initialize testimonials slider if the section exists
        if (document.getElementById('testimonials-slider')) {
            initTestimonialsSlider();
            console.log('Testimonials slider initialized');
        } else {
            console.log('Testimonials section is hidden, skipping slider initialization');
        }
    } catch (e) {
        console.error('Error initializing testimonials slider:', e);
    }
    
    try {
        initThemeToggle();
        console.log('Theme toggle initialized');
    } catch (e) {
        console.error('Error initializing theme toggle:', e);
    }
    
    try {
        initProjectModals();
        console.log('Project modals initialized');
    } catch (e) {
        console.error('Error initializing project modals:', e);
    }
});

// Navigation functionality
function initNavigation() {
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-link');

    // Handle navbar background on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(25, 42, 86, 0.98)';
        } else {
            navbar.style.background = 'rgba(25, 42, 86, 0.95)';
        }
    });

    // Active link highlighting
    function updateActiveLink() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPos = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPos >= sectionTop && scrollPos <= sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', updateActiveLink);
}

// Mobile menu functionality
function initMobileMenu() {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (!navToggle || !navMenu) return;

    // Toggle mobile menu
    navToggle.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        navToggle.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        });
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        }
    });
}

// Smooth scrolling for navigation links
function initSmoothScrolling() {
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 80; // Account for navbar height and some padding

                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
                
                // Update active navigation link
                navLinks.forEach(navLink => {
                    navLink.classList.remove('active');
                });
                this.classList.add('active');
                
                // Close mobile menu if open
                const navMenu = document.getElementById('nav-menu');
                const navToggle = document.getElementById('nav-toggle');
                if (navMenu && navToggle) {
                    navMenu.classList.remove('active');
                    navToggle.classList.remove('active');
                }
            }
        });
    });

    // Also handle other smooth scroll links
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    smoothScrollLinks.forEach(link => {
        if (!link.classList.contains('nav-link')) {
            link.addEventListener('click', function(e) {
                e.preventDefault();

                const targetId = this.getAttribute('href').substring(1);
                const targetSection = document.getElementById(targetId);

                if (targetSection) {
                    const offsetTop = targetSection.offsetTop - 80;

                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        }
    });
}

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('aos-animate');
            }
        });
    }, observerOptions);

    // Add AOS classes to elements that should animate on scroll
    const elementsToAnimate = document.querySelectorAll('.project-card, .recognition-card, .contact-card, .education-card, .testimonial-card, .section-header, .about-content, .contact-form, .contact-info, .timeline-item');
    
    elementsToAnimate.forEach((element, index) => {
        // Add data-aos attribute if it doesn't exist
        if (!element.getAttribute('data-aos')) {
            element.setAttribute('data-aos', 'fade-up');
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
            element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            element.style.transitionDelay = `${index % 5 * 0.1}s`;
        }
        
        observer.observe(element);
    });

    // Add scroll animations to timeline items
    const timelineItems = document.querySelectorAll('.timeline-item');
    timelineItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.2}s`;
        observer.observe(item);
    });

    // Add scroll animations to project cards
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        observer.observe(card);
    });
    
    // Add class to show animated elements
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            document.querySelectorAll('[data-aos]').forEach(element => {
                element.classList.add('aos-animate');
            });
        }, 100);
    });
}

// Animate skill bars
function initSkillBars() {
    const skillBars = document.querySelectorAll('.skill-progress');

    const skillObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const width = progressBar.getAttribute('data-width') + '%';

                // Reset width and animate
                progressBar.style.width = '0%';
                setTimeout(() => {
                    progressBar.style.width = width;
                }, 100);

                skillObserver.unobserve(progressBar);
            }
        });
    }, {
        threshold: 0.5
    });

    skillBars.forEach(bar => {
        skillObserver.observe(bar);
    });
}

// Contact form functionality
function initContactForm() {
    const contactForm = document.getElementById('contact-form');
    const newsletterForm = document.getElementById('newsletter-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(this);
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;

            // Show loading state
            submitButton.textContent = 'Sending...';
            submitButton.disabled = true;

            // Simulate form submission
            fetch('/contact', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showNotification('Message sent successfully!', 'success');
                    contactForm.reset();
                } else {
                    showNotification('Failed to send message. Please try again.', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification('Failed to send message. Please try again.', 'error');
            })
            .finally(() => {
                // Reset button
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            });
        });
    }
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(this);
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;

            // Show loading state
            submitButton.textContent = 'Subscribing...';
            submitButton.disabled = true;

            // Submit form
            fetch('/subscribe', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showNotification('Successfully subscribed to the newsletter!', 'success');
                    newsletterForm.reset();
                } else {
                    showNotification('Failed to subscribe. Please try again.', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification('Failed to subscribe. Please try again.', 'error');
            })
            .finally(() => {
                // Reset button
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            });
        });
    }
}

// Project interactions
function initProjectInteractions() {
    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

// Notification system
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());

    // Create new notification
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span class="notification-message">${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;

    // Add styles
    const styles = {
        position: 'fixed',
        top: '100px',
        right: '20px',
        background: type === 'success' ? '#27ae60' : type === 'error' ? '#e74c3c' : '#3498db',
        color: 'white',
        padding: '15px 20px',
        borderRadius: '8px',
        boxShadow: '0 4px 12px rgba(0, 0, 0, 0.2)',
        zIndex: '9999',
        maxWidth: '300px',
        transform: 'translateX(100%)',
        transition: 'transform 0.3s ease'
    };

    Object.assign(notification.style, styles);
    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 10);

    // Add close functionality
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    });

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
}

// Initialize advanced animations on load
window.addEventListener('load', function() {
    // Add entrance animations to elements
    const elementsToAnimate = document.querySelectorAll('.hero-content > *');
    elementsToAnimate.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';

        setTimeout(() => {
            element.style.transition = 'all 0.6s ease';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 200 + 500);
    });
});

// Theme toggle functionality
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('i');
    
    // Check for saved user preference, if any
    const userPrefersDark = localStorage.getItem('dark-mode') === 'true';
    
    // If user preference is set, apply it
    if (userPrefersDark) {
        document.body.classList.add('dark-mode');
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
    }
    
    themeToggle.addEventListener('click', function() {
        // Toggle dark mode class on body
        document.body.classList.toggle('dark-mode');
        
        // Update icon
        if (document.body.classList.contains('dark-mode')) {
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
            localStorage.setItem('dark-mode', 'true');
        } else {
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon');
            localStorage.setItem('dark-mode', 'false');
        }
    });
}

// Handle window resize
window.addEventListener('resize', function() {
    // Close mobile menu on resize
    const navMenu = document.getElementById('nav-menu');
    const navToggle = document.getElementById('nav-toggle');

    if (window.innerWidth > 768) {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
    }
});

// Performance optimization: Throttle scroll events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Project modals functionality
function initProjectModals() {
    const modal = document.getElementById('project-modal');
    const modalClose = document.querySelector('.modal-close');
    const projectDetailBtns = document.querySelectorAll('.project-details-btn');
    
    if (!modal || !modalClose || projectDetailBtns.length === 0) return;
    
    // Get project data from the backend
    let projectsData = [];
    
    try {
        // For Flask: Projects data should be available in the window scope
        // This assumes you're passing the data from Flask to JavaScript
        const portfolioDataElement = document.createElement('div');
        portfolioDataElement.innerHTML = document.querySelector('.projects-grid').innerHTML;
        
        const projectCards = portfolioDataElement.querySelectorAll('.project-card');
        
        projectCards.forEach(card => {
            const title = card.querySelector('.project-title').textContent;
            const description = card.querySelector('.project-description').textContent;
            const impact = card.querySelector('.project-impact span').textContent;
            const image = card.querySelector('.project-image img').getAttribute('src');
            
            const techTags = card.querySelectorAll('.tech-tag');
            const technologies = Array.from(techTags).map(tag => tag.textContent);
            
            projectsData.push({
                title,
                description,
                impact,
                image,
                technologies
            });
        });
    } catch (error) {
        console.error('Error fetching project data:', error);
    }
    
    // Open modal with project details
    projectDetailBtns.forEach((btn, index) => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            
            const projectIndex = this.getAttribute('data-project');
            const project = projectsData[projectIndex];
            
            if (!project) return;
            
            document.getElementById('modal-project-title').textContent = project.title;
            document.getElementById('modal-project-description').textContent = project.description;
            document.getElementById('modal-project-impact').textContent = project.impact;
            document.getElementById('modal-project-image').src = project.image;
            
            const techContainer = document.getElementById('modal-project-technologies');
            techContainer.innerHTML = '';
            
            project.technologies.forEach(tech => {
                const techTag = document.createElement('span');
                techTag.className = 'tech-tag';
                techTag.textContent = tech;
                techContainer.appendChild(techTag);
            });
            
            modal.classList.add('show');
            document.body.style.overflow = 'hidden'; // Prevent scrolling when modal is open
        });
    });
    
    // Close modal on close button click
    modalClose.addEventListener('click', function() {
        modal.classList.remove('show');
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
        document.body.style.overflow = ''; // Restore scrolling
    });
    
    // Close modal on outside click
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.style.display = 'none';
            }, 300);
            document.body.style.overflow = ''; // Restore scrolling
        }
    });
    
    // Close modal on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('show')) {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.style.display = 'none';
            }, 300);
            document.body.style.overflow = ''; // Restore scrolling
        }
    });
}

// Apply throttling to scroll events
const throttledScrollHandler = throttle(function() {
    // Handle scroll-based animations here if needed
}, 16); // ~60fps

window.addEventListener('scroll', throttledScrollHandler);

// Testimonials slider functionality
function initTestimonialsSlider() {
    const slider = document.getElementById('testimonials-slider');
    const prevBtn = document.getElementById('prev-testimonial');
    const nextBtn = document.getElementById('next-testimonial');
    
    if (!slider || !prevBtn || !nextBtn) return;
    
    let slideIndex = 0;
    const testimonials = slider.querySelectorAll('.testimonial-card');
    const slideWidth = testimonials[0]?.offsetWidth + 40; // Including margin
    const visibleSlides = Math.max(1, Math.floor(slider.offsetWidth / slideWidth));
    const maxSlides = testimonials.length - visibleSlides;
    
    function updateSlider() {
        if (slideIndex < 0) slideIndex = 0;
        if (slideIndex > maxSlides) slideIndex = maxSlides;
        
        slider.scrollTo({
            left: slideIndex * slideWidth,
            behavior: 'smooth'
        });
        
        // Update button states
        prevBtn.disabled = slideIndex === 0;
        nextBtn.disabled = slideIndex >= maxSlides;
        
        // Update visual state
        prevBtn.style.opacity = slideIndex === 0 ? '0.5' : '1';
        nextBtn.style.opacity = slideIndex >= maxSlides ? '0.5' : '1';
    }
    
    prevBtn.addEventListener('click', () => {
        slideIndex--;
        updateSlider();
    });
    
    nextBtn.addEventListener('click', () => {
        slideIndex++;
        updateSlider();
    });
    
    // Initialize state
    updateSlider();
    
    // Update on window resize
    window.addEventListener('resize', () => {
        // Recalculate visible slides and max slides
        const updatedSlideWidth = testimonials[0]?.offsetWidth + 40;
        const updatedVisibleSlides = Math.max(1, Math.floor(slider.offsetWidth / updatedSlideWidth));
        const updatedMaxSlides = testimonials.length - updatedVisibleSlides;
        
        // Adjust current slide index if needed
        if (slideIndex > updatedMaxSlides) {
            slideIndex = updatedMaxSlides;
        }
        
        updateSlider();
    });
    
    // Auto-advance slides every 5 seconds
    let autoSlideInterval = setInterval(() => {
        if (slideIndex < maxSlides) {
            slideIndex++;
        } else {
            slideIndex = 0;
        }
        updateSlider();
    }, 5000);
    
    // Pause auto-advance on hover
    slider.addEventListener('mouseenter', () => {
        clearInterval(autoSlideInterval);
    });
    
    // Resume auto-advance on mouse leave
    slider.addEventListener('mouseleave', () => {
        autoSlideInterval = setInterval(() => {
            if (slideIndex < maxSlides) {
                slideIndex++;
            } else {
                slideIndex = 0;
            }
            updateSlider();
        }, 5000);
    });
}
