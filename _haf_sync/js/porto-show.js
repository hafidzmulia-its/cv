document.addEventListener('DOMContentLoaded', function () {
    const root = document.getElementById('project-detail-root');
    const projects = Array.isArray(window.portfolioProjects) ? window.portfolioProjects : [];
    const params = new URLSearchParams(window.location.search);
    const slug = params.get('project');
    const project = projects.find((item) => item.slug === slug);

    if (!root) {
        return;
    }

    if (!project) {
        root.innerHTML = `
            <div class="container detail-shell">
                <div class="detail-card detail-empty">
                    <h1 class="font-montserrat">Project not found</h1>
                    <p>The requested portfolio entry is missing or the URL slug is invalid.</p>
                    <a href="index.html#projects" class="detail-action detail-action-primary">Back to projects</a>
                </div>
            </div>
        `;
        return;
    }

    const domain = project.domain || project.category;
    const overview = Array.isArray(project.overview) && project.overview.length > 0
        ? project.overview
        : [
            project.summary,
            `This project sits in the ${project.category.toLowerCase()} category and is presented here as part of the broader portfolio catalog.`
        ];
    const highlights = Array.isArray(project.highlights) && project.highlights.length > 0
        ? project.highlights
        : [
            `Delivered as a ${project.status.toLowerCase()} project.`,
            `Main stack represented by ${(project.tags || []).slice(0, 4).join(', ')}.`,
            `Repository visibility: ${project.repoVisibility}.`
        ];
    const stack = project.stack && Object.keys(project.stack).length > 0
        ? project.stack
        : {
            'Primary Stack': (project.tags || []).join(', ') || 'Not specified',
            Domain: domain,
            'Repository Type': project.repoVisibility,
            'Delivery Status': project.status
        };

    document.title = `${project.title} - Hafidz Mulia`;

    const screenshots = Array.isArray(project.screenshots) && project.screenshots.length > 0
        ? project.screenshots
        : [
            { title: 'Screenshot Placeholder 1', description: `Add a main interface capture for ${project.title} later.` },
            { title: 'Screenshot Placeholder 2', description: 'Add an internal workflow, dashboard, or form flow screenshot later.' },
            { title: 'Screenshot Placeholder 3', description: 'Add a mobile view, analytics view, or another supporting screen later.' }
        ];

    root.innerHTML = `
        <div class="container detail-shell">
            <header class="detail-header">
                <p class="detail-eyebrow">${escapeDetailText(project.category)}</p>
                <h1 class="detail-title font-montserrat">${escapeDetailText(project.title)}</h1>
                <p class="detail-summary">${escapeDetailText(project.summary)}</p>
                <div class="detail-chip-row">
                    <span class="detail-chip">${escapeDetailText(project.period)}</span>
                    <span class="detail-chip">${escapeDetailText(project.role)}</span>
                    <span class="detail-chip">${escapeDetailText(domain)}</span>
                    <span class="detail-chip">${escapeDetailText(project.status)}</span>
                </div>
                <div class="detail-action-row">
                    <a class="detail-action detail-action-primary" href="index.html#projects">Back to Portfolio</a>
                    ${project.liveUrl ? `<a class="detail-action detail-action-secondary" href="${project.liveUrl}" target="_blank" rel="noopener noreferrer">Open Live Project</a>` : ''}
                    ${project.repoUrl ? `<a class="detail-action detail-action-secondary" href="${project.repoUrl}" target="_blank" rel="noopener noreferrer">Open Repository</a>` : `<span class="detail-action detail-action-secondary">Repository: ${escapeDetailText(project.repoVisibility)}</span>`}
                </div>
            </header>

            <div class="detail-grid">
                <div class="detail-body">
                    <section class="detail-card">
                        <h2 class="font-montserrat">Project Overview</h2>
                        <div class="detail-text-block">
                            ${overview.map((paragraph) => `<p>${escapeDetailText(paragraph)}</p>`).join('')}
                        </div>
                    </section>

                    <section class="detail-card">
                        <h2 class="font-montserrat">Screenshots Carousel</h2>
                        <div class="carousel-shell">
                            <div class="carousel-stage">
                                <div class="carousel-track">
                                    ${screenshots.map((item) => item.image
                                        ? `<div class="carousel-slide"><img class="carousel-media" src="${item.image}" alt="${escapeDetailText(item.title)}"></div>`
                                        : `<div class="carousel-slide"><div class="carousel-placeholder"><div><strong>${escapeDetailText(item.title)}</strong><p>${escapeDetailText(item.description)}</p></div></div></div>`
                                    ).join('')}
                                </div>
                            </div>
                            <div class="carousel-controls">
                                <div class="carousel-buttons">
                                    <button class="carousel-btn" type="button" data-carousel-prev>&larr;</button>
                                    <button class="carousel-btn" type="button" data-carousel-next>&rarr;</button>
                                </div>
                                <div class="carousel-dots">
                                    ${screenshots.map((_, index) => `<button class="carousel-dot ${index === 0 ? 'active' : ''}" type="button" data-carousel-dot="${index}" aria-label="Go to slide ${index + 1}"></button>`).join('')}
                                </div>
                            </div>
                        </div>
                    </section>
                </div>

                <aside class="detail-body">
                    <section class="detail-card">
                        <h3 class="font-montserrat">Metadata</h3>
                        <div class="detail-meta-grid">
                            <div class="detail-meta-item">
                                <span class="detail-meta-label">Role</span>
                                <strong>${escapeDetailText(project.role)}</strong>
                            </div>
                            <div class="detail-meta-item">
                                <span class="detail-meta-label">Period</span>
                                <strong>${escapeDetailText(project.period)}</strong>
                            </div>
                            <div class="detail-meta-item">
                                <span class="detail-meta-label">Domain</span>
                                <strong>${escapeDetailText(domain)}</strong>
                            </div>
                            <div class="detail-meta-item">
                                <span class="detail-meta-label">Repository</span>
                                <strong>${escapeDetailText(project.repoUrl ? 'Public' : project.repoVisibility)}</strong>
                            </div>
                            <div class="detail-meta-item">
                                <span class="detail-meta-label">Live Access</span>
                                <strong>${escapeDetailText(project.liveUrl ? 'Available' : 'Not published publicly')}</strong>
                            </div>
                        </div>
                    </section>

                    <section class="detail-card">
                        <h3 class="font-montserrat">Key Highlights</h3>
                        <ul class="detail-list">
                            ${highlights.map((item) => `<li>${escapeDetailText(item)}</li>`).join('')}
                        </ul>
                    </section>

                    <section class="detail-card">
                        <h3 class="font-montserrat">Tech Stack</h3>
                        <div class="detail-meta-grid">
                            ${Object.entries(stack).map(([label, value]) => `
                                <div class="detail-meta-item">
                                    <span class="detail-meta-label">${escapeDetailText(label)}</span>
                                    <strong>${escapeDetailText(value)}</strong>
                                </div>
                            `).join('')}
                        </div>
                        <div class="detail-stack-tags" style="margin-top: 1rem;">
                            ${(project.tags || []).map((tag) => `<span class="project-tag">${escapeDetailText(tag)}</span>`).join('')}
                        </div>
                    </section>
                </aside>
            </div>
        </div>
    `;

    initializeCarousel(root);
});

function initializeCarousel(root) {
    const track = root.querySelector('.carousel-track');
    const dots = Array.from(root.querySelectorAll('[data-carousel-dot]'));
    const prevButton = root.querySelector('[data-carousel-prev]');
    const nextButton = root.querySelector('[data-carousel-next]');

    if (!track || dots.length === 0) {
        return;
    }

    let currentIndex = 0;

    const updateCarousel = () => {
        track.style.transform = `translateX(-${currentIndex * 100}%)`;
        dots.forEach((dot, index) => dot.classList.toggle('active', index === currentIndex));
    };

    prevButton?.addEventListener('click', () => {
        currentIndex = currentIndex === 0 ? dots.length - 1 : currentIndex - 1;
        updateCarousel();
    });

    nextButton?.addEventListener('click', () => {
        currentIndex = currentIndex === dots.length - 1 ? 0 : currentIndex + 1;
        updateCarousel();
    });

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            currentIndex = index;
            updateCarousel();
        });
    });
}

function escapeDetailText(value) {
    return String(value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}