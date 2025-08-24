// Adjust section spacing dynamically
document.addEventListener('DOMContentLoaded', function() {
    // Get all sections
    const sections = document.querySelectorAll('section');
    
    // Apply spacing fixes
    sections.forEach((section, index) => {
        if (index > 0) {
            // Skip the first section (hero)
            section.style.paddingTop = '50px';
            section.style.paddingBottom = '50px';
            section.style.marginTop = '20px';
            section.style.marginBottom = '20px';
        }
    });
    
    // Specifically adjust navbar offset
    const navbar = document.getElementById('navbar');
    if (navbar) {
        const navbarHeight = navbar.offsetHeight;
        document.documentElement.style.setProperty('--navbar-height', navbarHeight + 'px');
    }
    
    console.log('Section spacing adjustments applied');
});
