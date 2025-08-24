// About section visibility fix script
document.addEventListener('DOMContentLoaded', function() {
    // Force the About section to be visible
    const aboutSection = document.getElementById('about');
    if (aboutSection) {
        aboutSection.style.visibility = 'visible';
        aboutSection.style.opacity = '1';
        aboutSection.style.display = 'block';
        
        // Make all animated elements in the about section visible
        const animatedElements = aboutSection.querySelectorAll('[data-aos]');
        animatedElements.forEach(el => {
            el.classList.add('aos-animate');
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
        
        console.log('About section visibility fix applied');
    } else {
        console.log('About section not found');
    }
});
