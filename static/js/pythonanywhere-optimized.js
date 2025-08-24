// Optimized JavaScript for PythonAnywhere - Performance focused
// Combines all functionality into one file to reduce HTTP requests

document.addEventListener('DOMContentLoaded', function() {
    
    // Ensure critical sections are visible immediately
    ensureSectionVisibility();
    
    // Initialize contact form handling
    initializeContactForm();
    
    // Auto-hide flash messages
    autoHideFlashMessages();
    
    // Lazy load images for performance
    initializeLazyLoading();
});

function ensureSectionVisibility() {
    // Force visibility of critical sections
    const sectionsToShow = ['#about', '#contact', '#projects', '#experience'];
    
    sectionsToShow.forEach(sectionId => {
        const section = document.querySelector(sectionId);
        if (section) {
            section.style.display = 'block';
            section.style.visibility = 'visible';
            section.style.opacity = '1';
            
            // Ensure all child elements are visible
            const children = section.querySelectorAll('*');
            children.forEach(child => {
                if (child.style.display === 'none' || child.style.visibility === 'hidden') {
                    child.style.display = 'inherit';
                    child.style.visibility = 'visible';
                    child.style.opacity = '1';
                }
            });
        }
    });
    
    // Ensure contact cards are visible and properly arranged
    const contactCards = document.querySelector('.contact-cards');
    if (contactCards) {
        contactCards.style.display = 'flex';
        contactCards.style.visibility = 'visible';
        contactCards.style.opacity = '1';
        
        const cards = contactCards.querySelectorAll('.contact-card');
        cards.forEach(card => {
            card.style.display = 'flex';
            card.style.visibility = 'visible';
            card.style.opacity = '1';
        });
    }
}

function initializeContactForm() {
    const contactForm = document.querySelector('#contact-form');
    if (!contactForm) return;
    
    // Form validation
    contactForm.addEventListener('submit', function(e) {
        const name = document.querySelector('input[name="name"]').value.trim();
        const email = document.querySelector('input[name="email"]').value.trim();
        const message = document.querySelector('textarea[name="message"]').value.trim();
        
        if (!name || !email || !message) {
            e.preventDefault();
            showMessage('Please fill in all required fields.', 'error');
            return;
        }
        
        // Basic email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            e.preventDefault();
            showMessage('Please enter a valid email address.', 'error');
            return;
        }
        
        // Show loading state
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';
            
            // Re-enable after timeout (in case form doesn't redirect)
            setTimeout(() => {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Send Message';
            }, 5000);
        }
    });
}

function autoHideFlashMessages() {
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(message => {
        setTimeout(() => {
            if (message.parentNode) {
                message.style.animation = 'fadeOut 0.3s ease forwards';
                setTimeout(() => {
                    message.remove();
                }, 300);
            }
        }, 5000); // Hide after 5 seconds
    });
}

function showMessage(text, type = 'info') {
    // Create flash message container if it doesn't exist
    let container = document.querySelector('.flash-messages');
    if (!container) {
        container = document.createElement('div');
        container.className = 'flash-messages';
        document.body.appendChild(container);
    }
    
    // Create message element
    const message = document.createElement('div');
    message.className = `alert alert-${type}`;
    message.textContent = text;
    
    container.appendChild(message);
    
    // Auto-hide
    setTimeout(() => {
        if (message.parentNode) {
            message.style.animation = 'fadeOut 0.3s ease forwards';
            setTimeout(() => {
                message.remove();
            }, 300);
        }
    }, 5000);
}

function initializeLazyLoading() {
    // Simple lazy loading for images (performance optimization)
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback for older browsers
        images.forEach(img => {
            img.src = img.dataset.src;
        });
    }
}

// Smooth scrolling for navigation links (lightweight implementation)
document.addEventListener('click', function(e) {
    if (e.target.matches('a[href^="#"]')) {
        e.preventDefault();
        const targetId = e.target.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }
});

// Performance monitoring for PythonAnywhere (lightweight)
if (typeof performance !== 'undefined' && performance.mark) {
    performance.mark('portfolio-interactive');
    
    window.addEventListener('load', function() {
        performance.mark('portfolio-loaded');
        
        // Log performance metrics (for development/debugging)
        if (console && console.log) {
            try {
                const navigation = performance.getEntriesByType('navigation')[0];
                if (navigation) {
                    console.log('Page load time:', navigation.loadEventEnd - navigation.fetchStart, 'ms');
                }
            } catch (e) {
                // Silently handle any performance API errors
            }
        }
    });
}
