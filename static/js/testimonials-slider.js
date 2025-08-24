// Testimonials slider functionality
function initTestimonialsSlider() {
    console.log("Initializing testimonials slider");
    const slider = document.getElementById('testimonials-slider');
    const prevBtn = document.getElementById('prev-testimonial');
    const nextBtn = document.getElementById('next-testimonial');
    
    if (!slider || !prevBtn || !nextBtn) {
        console.warn("Testimonials slider elements not found", {
            slider: !!slider,
            prevBtn: !!prevBtn,
            nextBtn: !!nextBtn
        });
        return;
    }
    
    const testimonials = slider.querySelectorAll('.testimonial-card');
    if (testimonials.length === 0) {
        console.warn("No testimonial cards found");
        return;
    }
    
    console.log(`Found ${testimonials.length} testimonial cards`);
    
    // Make sure testimonials are visible
    testimonials.forEach(card => {
        card.style.opacity = "1";
        card.style.visibility = "visible";
        card.style.position = "relative";
        card.style.display = "block";
    });
    
    let slideIndex = 0;
    const slideWidth = testimonials[0].offsetWidth + 40; // Including margin
    
    // Calculate visible slides based on container width
    const calculateVisibleSlides = () => {
        const containerWidth = slider.clientWidth;
        return Math.max(1, Math.floor(containerWidth / slideWidth));
    };
    
    let visibleSlides = calculateVisibleSlides();
    let maxSlides = Math.max(0, testimonials.length - visibleSlides);
    
    console.log(`Slider config: slideWidth=${slideWidth}px, visibleSlides=${visibleSlides}, maxSlides=${maxSlides}`);
    
    function updateSlider() {
        // Bound slideIndex to valid range
        if (slideIndex < 0) slideIndex = 0;
        if (slideIndex > maxSlides) slideIndex = maxSlides;
        
        const scrollPos = slideIndex * slideWidth;
        console.log(`Updating slider to position: ${scrollPos}px, index=${slideIndex}`);
        
        // Scroll to position
        slider.scrollTo({
            left: scrollPos,
            behavior: 'smooth'
        });
        
        // Update button states
        prevBtn.disabled = slideIndex === 0;
        nextBtn.disabled = slideIndex >= maxSlides;
        
        // Update visual state
        prevBtn.style.opacity = slideIndex === 0 ? '0.5' : '1';
        nextBtn.style.opacity = slideIndex >= maxSlides ? '0.5' : '1';
    }
    
    // Event handlers
    prevBtn.addEventListener('click', () => {
        console.log("Previous testimonial button clicked");
        slideIndex--;
        updateSlider();
    });
    
    nextBtn.addEventListener('click', () => {
        console.log("Next testimonial button clicked");
        slideIndex++;
        updateSlider();
    });
    
    // Handle window resize
    window.addEventListener('resize', () => {
        console.log("Window resized, recalculating slider dimensions");
        
        // Recalculate visible slides and max slides
        visibleSlides = calculateVisibleSlides();
        maxSlides = Math.max(0, testimonials.length - visibleSlides);
        
        console.log(`Updated slider config: visibleSlides=${visibleSlides}, maxSlides=${maxSlides}`);
        
        // Adjust current slide index if needed
        if (slideIndex > maxSlides) {
            slideIndex = maxSlides;
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
    
    // Force initial update
    setTimeout(() => {
        console.log("Forcing initial slider update");
        updateSlider();
    }, 500);
}

// Automatically initialize when included on the page
document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM loaded in testimonials-slider.js");
    try {
        initTestimonialsSlider();
    } catch (e) {
        console.error("Error initializing testimonials slider:", e);
    }
});

// Make this function available globally
window.initTestimonialsSlider = initTestimonialsSlider;
