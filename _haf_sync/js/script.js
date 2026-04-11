// Portfolio Website JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Portfolio website loaded successfully!');
    
    // Initialize components
    renderFeaturedProjects();
    initializeNavigation();
    initializeAnimations();
    initializeContactForm();
    initializeLovableBadge();
    initializeSmoothScrolling();
    initializeButtonInteractions();
    initializeScrollToTop();
    updateDurations();
});
function calculateDuration(startDate, endDate = new Date()) {
    const start = new Date(startDate);
    const end = new Date(endDate);
    
    let years = end.getFullYear() - start.getFullYear();
    let months = end.getMonth() - start.getMonth();
    
    // Adjust if months is negative
    if (months < 0) {
        years--;
        months += 12;
    }
    
    // Format output
    if (years === 0) {
        return `${months} month${months !== 1 ? 's' : ''}`;
    } else if (months === 0) {
        return `${years} year${years !== 1 ? 's' : ''}`;
    } else {
        return `${years} year${years !== 1 ? 's' : ''} ${months} month${months !== 1 ? 's' : ''}`;
    }
}
// Navigation functionality
function initializeNavigation() {
    const nav = document.querySelector('nav');
    const navLinks = document.querySelectorAll('.nav-link');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');
    
    // Add scroll effect to navigation
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > 50) {
            nav?.classList.add('nav-scrolled');
        } else {
            nav?.classList.remove('nav-scrolled');
        }
        
        lastScrollY = currentScrollY;
    });
    
    // Mobile menu toggle
    mobileMenuBtn?.addEventListener('click', () => {
        navMenu?.classList.toggle('nav-menu-open');
        mobileMenuBtn?.classList.toggle('active');
    });
    
    // Navigation link clicks
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            // Add active class to clicked link
            link.classList.add('active');
            
            // Close mobile menu if open
            navMenu?.classList.remove('nav-menu-open');
            mobileMenuBtn?.classList.remove('active');
        });
    });
}

// Smooth scrolling for navigation links
function initializeSmoothScrolling() {
    // Handle navigation clicks
    document.querySelectorAll('button[class*="nav-link"], a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href') || this.getAttribute('data-href');
            if (href && href.startsWith('#')) {
                e.preventDefault();
                
                let targetId = href.substring(1);
                
                // Map button text to section IDs
                const buttonText = this.textContent.trim().toLowerCase();
                switch(buttonText) {
                    case 'about':
                        targetId = 'about';
                        break;
                    case 'experience':
                        targetId = 'experience';
                        break;
                    case 'education':
                        targetId = 'education';
                        break;
                    case 'skills':
                        targetId = 'skills';
                        break;
                    case 'projects':
                        targetId = 'projects';
                        break;
                    case 'contact':
                        targetId = 'contact';
                        break;
                }
                
                const targetSection = document.getElementById(targetId);
                if (targetSection) {
                    const headerOffset = 80; // Account for fixed header
                    const elementPosition = targetSection.offsetTop;
                    const offsetPosition = elementPosition - headerOffset;
                    
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}

// Animation functionality
function initializeAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in-up');
                entry.target.style.animationDelay = '0s';
            }
        });
    }, observerOptions);
    
    // Observe elements with animation classes
    const animatedElements = document.querySelectorAll('.card, .skill-category, .project-card, .timeline-item');
    animatedElements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.1}s`;
        observer.observe(el);
    });
    
    // Add staggered animation delays
    const experienceItems = document.querySelectorAll('.timeline-item');
    experienceItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
    });
    
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
}

// Contact form functionality
function initializeContactForm() {
    const contactForm = document.querySelector('#contact form, .contact-form form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', handleFormSubmit);
    }
}

async function handleFormSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const submitBtn = form.querySelector('button[type="submit"], .form-submit');
    
    // Disable submit button
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';
    }
    
    try {
        // If using Formspree (as in original)
        const response = await fetch(form.action || 'https://formspree.io/f/xrbzgnaz', {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });
        
        if (response.ok) {
            showToast('Message sent successfully! I\'ll get back to you soon.', 'success');
            form.reset();
        } else {
            throw new Error('Network response was not ok');
        }
    } catch (error) {
        console.error('Error submitting form:', error);
        showToast('Failed to send message. Please try again.', 'error');
    } finally {
        // Re-enable submit button
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-send mr-2 h-5 w-5"><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"></path><path d="m21.854 2.147-10.94 10.939"></path></svg>Send Message';
        }
    }
}

// Toast notification system
function showToast(message, type = 'info') {
    // Create toast container if it doesn't exist
    let toaster = document.querySelector('[data-sonner-toaster]');
    if (!toaster) {
        toaster = document.createElement('ol');
        toaster.className = 'fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px]';
        toaster.setAttribute('data-sonner-toaster', '');
        toaster.setAttribute('data-theme', 'light');
        toaster.setAttribute('data-y-position', 'bottom');
        toaster.setAttribute('data-x-position', 'right');
        toaster.style.cssText = '--width: 356px; --offset-right: 32px; --offset-bottom: 32px; --mobile-offset-right: 16px; --mobile-offset-bottom: 16px;';
        document.body.appendChild(toaster);
    }
    
    // Create toast element
    const toast = document.createElement('li');
    toast.className = 'relative cursor-default select-none';
    toast.setAttribute('data-sonner-toast', '');
    toast.setAttribute('data-styled', 'true');
    toast.setAttribute('data-mounted', 'true');
    toast.setAttribute('data-type', type);
    toast.setAttribute('data-visible', 'true');
    toast.style.cssText = '--y: translateY(0); --z-index: 1;';
    
    const iconMap = {
        success: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
        error: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>',
        info: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>'
    };
    
    toast.innerHTML = `
        <div data-icon="" style="color: ${type === 'success' ? 'hsl(140, 100%, 27%)' : type === 'error' ? 'hsl(360, 100%, 45%)' : 'hsl(210, 92%, 45%)'};">
            ${iconMap[type] || iconMap.info}
        </div>
        <div data-content="">
            <div data-title="">${message}</div>
        </div>
    `;
    
    toaster.appendChild(toast);
    
    // Remove toast after 4 seconds
    setTimeout(() => {
        toast.remove();
    }, 4000);
}

// Lovable badge functionality
function initializeLovableBadge() {
    // Don't show the lovable-badge if the page is in an iframe or if it's being rendered by puppeteer (screenshot service)
    if (window.self !== window.top || navigator.userAgent.includes('puppeteer')) {
        const badge = document.getElementById('lovable-badge');
        if (badge) {
            badge.style.display = 'none';
        }
    }

    // Add click event listener to close button
    const closeButton = document.getElementById('lovable-badge-close');
    if (closeButton) {
        closeButton.addEventListener('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            const badge = document.getElementById('lovable-badge');
            if (badge) {
                badge.style.display = 'none';
            }
        });
    }
}

// Button interactions
function initializeButtonInteractions() {
    console.log('Initializing button interactions...');
    
    // Get in Touch button
    const getInTouchBtn = document.querySelector('button[class*="btn-primary"]');
    console.log('Get in Touch button found:', getInTouchBtn);
    if (getInTouchBtn && getInTouchBtn.textContent.includes('Get in Touch')) {
        getInTouchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Get in Touch button clicked');
            const contactSection = document.getElementById('contact');
            if (contactSection) {
                contactSection.scrollIntoView({ behavior: 'smooth' });
                showToast('Scrolling to contact section', 'info');
            } else {
                console.error('Contact section not found');
                showToast('Contact section not found', 'error');
            }
        });
    }
    
    // Download CV button
    const downloadCvBtn = document.querySelector('button[class*="btn-secondary"]');
    console.log('Download CV button found:', downloadCvBtn);
    if (downloadCvBtn && downloadCvBtn.textContent.includes('Download CV')) {
        downloadCvBtn.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Download CV button clicked');
            try {
                // Create temporary download link
                const link = document.createElement('a');
                link.href = 'cv-hafidz-mulia.pdf';
                link.download = 'Hafidz-Mulia-CV.pdf';
                link.style.display = 'none';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                showToast('CV download started!', 'success');
            } catch (error) {
                console.error('Error downloading CV:', error);
                showToast('Error downloading CV', 'error');
            }
        });
    }
}

// Scroll to top functionality
function initializeScrollToTop() {
    // Create scroll to top button
    const scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.innerHTML = '↑';
    scrollToTopBtn.className = 'scroll-to-top';
    scrollToTopBtn.style.cssText = `
        position: fixed;
        bottom: 20px;
        left: 20px;
        width: 50px;
        height: 50px;
        background: var(--gradient-primary);
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        font-size: 20px;
        font-weight: bold;
        display: none;
        z-index: 1000;
        transition: var(--transition-smooth);
        box-shadow: var(--shadow-lg);
    `;
    
    document.body.appendChild(scrollToTopBtn);
    
    // Show/hide scroll to top button
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollToTopBtn.style.display = 'block';
        } else {
            scrollToTopBtn.style.display = 'none';
        }
    });
    
    // Scroll to top when clicked
    scrollToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Typing animation for hero text
function initializeTypingAnimation() {
    const heroTitle = document.querySelector('.hero-title, h1');
    if (heroTitle && heroTitle.textContent.includes('Hafidz Mulia')) {
        const text = heroTitle.textContent;
        heroTitle.textContent = '';
        
        let i = 0;
        const typeWriter = () => {
            if (i < text.length) {
                heroTitle.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        };
        
        // Start typing animation after a delay
        setTimeout(typeWriter, 500);
    }
}

// Parallax effect for hero section
function initializeParallax() {
    const hero = document.querySelector('.hero, section:first-of-type');
    
    if (hero) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            
            if (scrolled <= window.innerHeight) {
                hero.style.transform = `translateY(${rate}px)`;
            }
        });
    }
}

// Initialize additional features when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeButtonInteractions();
    initializeScrollToTop();
    initializeTypingAnimation();
    initializeParallax();
});

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Performance optimization
const debouncedScrollHandler = debounce(() => {
    // Any scroll-heavy operations can go here
}, 10);

window.addEventListener('scroll', debouncedScrollHandler);

// Update duration displays
function updateDurations() {
    // Update specific duration by ID
    const coordinatorDuration = document.getElementById('coordinator-duration');
    if (coordinatorDuration) {
        const duration = calculateDuration('2024-08-01');
        coordinatorDuration.textContent = `${duration}`;
    }
    const himatikaDuration = document.getElementById('himatika-duration');
    if (himatikaDuration) {
        const duration = calculateDuration('2023-05-01');
        himatikaDuration.textContent = `${duration}`;
    }
    
    // You can add more duration updates here
    // Example: Update Timedoor Academy duration
    const timedoorElements = document.querySelectorAll('.experience-date');
    timedoorElements.forEach(element => {
        if (element.textContent.includes('Aug 2024 - Present') && element.id !== 'coordinator-duration') {
            const duration = calculateDuration('2024-08-01');
            element.textContent = `${duration}`;
        }
    });
}

// Error handling
window.addEventListener('error', (e) => {
    console.error('JavaScript error:', e.error);
});

// Export functions for testing (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initializeNavigation,
        initializeAnimations,
        initializeContactForm,
        showToast,
        handleFormSubmit
    };
}
function renderFeaturedProjects() {
    const filterBar = document.getElementById('project-filter-bar');
    const grid = document.getElementById('featured-projects-grid');
    const count = document.getElementById('project-results-count');
    const projects = Array.isArray(window.portfolioProjects) ? [...window.portfolioProjects] : [];

    if (!filterBar || !grid || projects.length === 0) {
        return;
    }

    const filters = [
        { id: 'featured', label: 'Featured' },
        { id: 'all', label: 'All Repos' },
        { id: 'nextjs', label: 'Next.js / React' },
        { id: 'laravel', label: 'Laravel / PHP' },
        { id: 'gis', label: 'GIS / Maps' },
        { id: 'health', label: 'Health-Tech' },
        { id: 'education', label: 'Education' },
        { id: 'systems', label: 'Internal Systems' },
        { id: 'frontend', label: 'Frontend' },
        { id: 'experiments', label: 'Experiments' }
    ];

    let activeFilter = 'featured';

    const getProjectsForFilter = (filterId) => {
        const filtered = filterId === 'all'
            ? projects
            : projects.filter((project) => filterId === 'featured'
                ? project.featured
                : Array.isArray(project.categories) && project.categories.includes(filterId));

        return filtered.sort((a, b) => (b.sortKey || 0) - (a.sortKey || 0) || a.title.localeCompare(b.title));
    };

    const renderFilterButtons = () => {
        filterBar.innerHTML = filters.map((filter) => {
            const isActive = filter.id === activeFilter;
            return `<button class="project-filter-btn${isActive ? ' active' : ''}" data-project-filter="${filter.id}" type="button">${filter.label}</button>`;
        }).join('');
    };

    const createProjectCard = (project) => {
        const imageMarkup = project.coverImage
            ? `<img src="${project.coverImage}" alt="${escapeProjectText(project.title)}" class="project-image">`
            : `<div class="project-image project-image-placeholder"><span>${escapeProjectText(project.coverLabel || project.title)}</span></div>`;

        const pills = [
            project.period,
            project.role,
            project.status,
            `${project.repoVisibility} Repo`
        ].filter(Boolean).map((value) => `<span class="project-meta-pill">${escapeProjectText(value)}</span>`).join('');

        const detailLink = `<a href="porto-show.html?project=${project.slug}" class="project-link project-link-show">Show</a>`;

        const primaryLink = project.liveUrl
            ? `<a href="${project.liveUrl}" target="_blank" rel="noopener noreferrer" class="project-link project-link-primary">Live Site</a>`
            : project.repoUrl
                ? `<a href="${project.repoUrl}" target="_blank" rel="noopener noreferrer" class="project-link project-link-primary">GitHub</a>`
                : `<span class="project-link project-link-disabled">Private Repo</span>`;

        const secondaryLink = project.liveUrl && project.repoUrl
            ? `<a href="${project.repoUrl}" target="_blank" rel="noopener noreferrer" class="project-link project-link-secondary">GitHub</a>`
            : '';

        return `
            <article class="project-card project-card-catalog">
                <div class="project-image-container">
                    ${imageMarkup}
                    <div class="project-overlay"></div>
                    <span class="project-status-badge">${escapeProjectText(project.status)}</span>
                </div>
                <div class="project-content">
                    <p class="project-kicker">${escapeProjectText(project.category)}</p>
                    <h3 class="project-title font-montserrat">${escapeProjectText(project.title)}</h3>
                    <p class="project-roleline">${escapeProjectText(project.role)}</p>
                    <div class="project-meta">${pills}</div>
                    <p class="project-description">${escapeProjectText(project.summary)}</p>
                    <div class="project-tags">
                        ${(project.tags || []).map((tag) => `<span class="project-tag">${escapeProjectText(tag)}</span>`).join('')}
                    </div>
                    <div class="project-links">
                        ${detailLink}
                        ${primaryLink}
                        ${secondaryLink}
                    </div>
                </div>
            </article>
        `;
    };

    const renderProjects = () => {
        const visibleProjects = getProjectsForFilter(activeFilter);
        grid.innerHTML = visibleProjects.map(createProjectCard).join('');
        count.textContent = `${visibleProjects.length} project${visibleProjects.length !== 1 ? 's' : ''}`;
    };

    filterBar.addEventListener('click', (event) => {
        const button = event.target.closest('[data-project-filter]');
        if (!button) {
            return;
        }

        activeFilter = button.getAttribute('data-project-filter') || 'featured';
        renderFilterButtons();
        renderProjects();
    });

    renderFilterButtons();
    renderProjects();
}

function escapeProjectText(value) {
    return String(value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}