// Section Visibility Debugger
document.addEventListener('DOMContentLoaded', function() {
    console.log("Section Visibility Debugger initialized");
    
    // Check all sections
    const sections = document.querySelectorAll('section');
    console.log(`Found ${sections.length} sections on the page`);
    
    sections.forEach((section, index) => {
        const id = section.id || `section-${index}`;
        const styles = window.getComputedStyle(section);
        const visible = styles.display !== 'none' && styles.visibility !== 'hidden' && styles.opacity !== '0';
        
        console.log(`Section ${id}: ${visible ? 'VISIBLE' : 'HIDDEN'}`);
        console.log(`  - Display: ${styles.display}`);
        console.log(`  - Visibility: ${styles.visibility}`);
        console.log(`  - Opacity: ${styles.opacity}`);
        console.log(`  - Position: ${styles.position}`);
        console.log(`  - Z-index: ${styles.zIndex}`);
        console.log(`  - Height: ${section.offsetHeight}px`);
        console.log(`  - Offset Top: ${section.offsetTop}px`);
        
        // If section is not visible, try to fix it
        if (!visible) {
            console.log(`  - Attempting to fix visibility for ${id}`);
            section.style.display = 'block';
            section.style.visibility = 'visible';
            section.style.opacity = '1';
            section.style.position = 'relative';
            section.style.zIndex = '1';
        }
        
        // Log all section children (top level) to check for visibility issues
        const children = section.children;
        console.log(`  - Section has ${children.length} direct children`);
        
        Array.from(children).forEach((child, childIndex) => {
            const childStyles = window.getComputedStyle(child);
            const childVisible = childStyles.display !== 'none' && childStyles.visibility !== 'hidden' && childStyles.opacity !== '0';
            
            console.log(`    Child ${childIndex}: ${childVisible ? 'VISIBLE' : 'HIDDEN'} (${child.tagName.toLowerCase()}${child.className ? '.' + child.className.split(' ')[0] : ''})`);
            
            // If child is not visible, try to fix it
            if (!childVisible) {
                child.style.display = 'block';
                child.style.visibility = 'visible';
                child.style.opacity = '1';
            }
        });
    });
    
    // Check specifically for testimonials section
    const testimonialsSection = document.getElementById('testimonials');
    if (testimonialsSection) {
        console.log("Testimonials section details:");
        console.log("  - Section exists:", !!testimonialsSection);
        
        const slider = document.getElementById('testimonials-slider');
        console.log("  - Slider exists:", !!slider);
        
        if (slider) {
            const testimonials = slider.querySelectorAll('.testimonial-card');
            console.log(`  - Testimonial cards found: ${testimonials.length}`);
            
            testimonials.forEach((card, i) => {
                const cardStyles = window.getComputedStyle(card);
                console.log(`    Card ${i} visibility: display=${cardStyles.display}, visibility=${cardStyles.visibility}, opacity=${cardStyles.opacity}`);
                
                // Force the card to be visible
                card.style.display = 'block';
                card.style.visibility = 'visible';
                card.style.opacity = '1';
            });
            
            // Check controls
            const prevBtn = document.getElementById('prev-testimonial');
            const nextBtn = document.getElementById('next-testimonial');
            
            console.log(`  - Control buttons: prev=${!!prevBtn}, next=${!!nextBtn}`);
        }
    } else {
        console.log("Testimonials section is not present in the DOM (likely hidden by configuration)");
    }
});
