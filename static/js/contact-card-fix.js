// Simple contact cards renderer without animations
document.addEventListener('DOMContentLoaded', function() {
    console.log('Initializing contact cards...');
    
    // Get the contact info container
    const contactInfo = document.querySelector('.contact-info');
    if (!contactInfo) {
        console.log('Contact info container not found');
        return;
    }
    
    // Clear all existing cards to prevent duplicates
    contactInfo.innerHTML = '';
    
    // Create fresh contact cards from portfolio data
    const createContactCard = (icon, title, content) => {
        const card = document.createElement('div');
        card.className = 'contact-card';
        
        // Add icon
        const iconDiv = document.createElement('div');
        iconDiv.className = 'contact-icon';
        const iconElement = document.createElement('i');
        iconElement.className = icon;
        iconDiv.appendChild(iconElement);
        
        // Add details
        const details = document.createElement('div');
        details.className = 'contact-details';
        
        const heading = document.createElement('h4');
        heading.textContent = title;
        
        const paragraph = document.createElement('p');
        paragraph.textContent = content;
        
        details.appendChild(heading);
        details.appendChild(paragraph);
        
        // Add everything to the card
        card.appendChild(iconDiv);
        card.appendChild(details);
        
        return card;
    };
    
    // Add email card
    const emailElement = document.querySelector('meta[name="email"]');
    const email = emailElement ? emailElement.getAttribute('content') : 'pi.pratik.ingale@gmail.com';
    contactInfo.appendChild(createContactCard('fas fa-envelope', 'Email', email));
    
    // Add phone card
    const phoneElement = document.querySelector('meta[name="phone"]');
    const phone = phoneElement ? phoneElement.getAttribute('content') : '+91 8310270881';
    contactInfo.appendChild(createContactCard('fas fa-phone', 'Phone', phone));
    
    // Add location card
    const locationElement = document.querySelector('meta[name="location"]');
    const location = locationElement ? locationElement.getAttribute('content') : 'Bengaluru, KA';
    contactInfo.appendChild(createContactCard('fas fa-map-marker-alt', 'Location', location));
    
    console.log('Contact cards created successfully');
});
