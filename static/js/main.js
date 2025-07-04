// Main JavaScript file for SOC CMM Assessment System

// Global utility functions
window.SOC_CMM = {
    // API helper functions
    async apiCall(url, options = {}) {
        try {
            const response = await fetch(url, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API call failed:', error);
            throw error;
        }
    },

    // Show loading spinner
    showLoading(element) {
        if (typeof element === 'string') {
            element = document.getElementById(element);
        }
        if (element) {
            element.innerHTML = `
                <div class="text-center">
                    <div class="spinner"></div>
                    <p style="margin-top: 1rem; color: var(--text-secondary);">Loading...</p>
                </div>
            `;
        }
    },

    // Show error message
    showError(element, message = 'An error occurred') {
        if (typeof element === 'string') {
            element = document.getElementById(element);
        }
        if (element) {
            element.innerHTML = `
                <div class="alert alert-danger">
                    <i class="fas fa-exclamation-triangle"></i>
                    ${message}
                </div>
            `;
        }
    },

    // Format date
    formatDate(dateString) {
        return new Date(dateString).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    },

    // Format score
    formatScore(score, decimals = 1) {
        return parseFloat(score).toFixed(decimals);
    },

    // Get maturity level text
    getMaturityLevel(score) {
        const level = Math.round(score);
        const levels = {
            1: 'Initial',
            2: 'Developing', 
            3: 'Defined',
            4: 'Managed',
            5: 'Optimized'
        };
        return levels[level] || 'Unknown';
    },

    // Get score color
    getScoreColor(score) {
        if (score >= 4.5) return '#10b981';
        if (score >= 3.5) return '#22c55e';
        if (score >= 2.5) return '#eab308';
        if (score >= 1.5) return '#f59e0b';
        return '#ef4444';
    },

    // Animate number counting
    animateNumber(element, start, end, duration = 1000) {
        if (typeof element === 'string') {
            element = document.getElementById(element);
        }
        
        const startTime = performance.now();
        const difference = end - start;
        
        function updateNumber(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Easing function
            const easeOutQuart = 1 - Math.pow(1 - progress, 4);
            const current = start + (difference * easeOutQuart);
            
            element.textContent = current.toFixed(1);
            
            if (progress < 1) {
                requestAnimationFrame(updateNumber);
            }
        }
        
        requestAnimationFrame(updateNumber);
    },

    // Animate progress bar
    animateProgressBar(element, percentage, duration = 1000) {
        if (typeof element === 'string') {
            element = document.getElementById(element);
        }
        
        element.style.width = '0%';
        
        setTimeout(() => {
            element.style.transition = `width ${duration}ms ease-out`;
            element.style.width = percentage + '%';
        }, 100);
    },

    // Local storage helpers
    storage: {
        set(key, value) {
            try {
                localStorage.setItem(key, JSON.stringify(value));
            } catch (error) {
                console.warn('Failed to save to localStorage:', error);
            }
        },

        get(key, defaultValue = null) {
            try {
                const item = localStorage.getItem(key);
                return item ? JSON.parse(item) : defaultValue;
            } catch (error) {
                console.warn('Failed to read from localStorage:', error);
                return defaultValue;
            }
        },

        remove(key) {
            try {
                localStorage.removeItem(key);
            } catch (error) {
                console.warn('Failed to remove from localStorage:', error);
            }
        }
    },

    // Notification system
    notify(message, type = 'info', duration = 5000) {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-${this.getNotificationIcon(type)}"></i>
                <span>${message}</span>
                <button class="notification-close" onclick="this.parentElement.parentElement.remove()">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        `;

        // Add styles if not already present
        if (!document.getElementById('notification-styles')) {
            const styles = document.createElement('style');
            styles.id = 'notification-styles';
            styles.textContent = `
                .notification {
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    z-index: 1000;
                    min-width: 300px;
                    max-width: 500px;
                    border-radius: var(--border-radius);
                    box-shadow: var(--shadow-lg);
                    animation: slideIn 0.3s ease-out;
                }
                
                .notification-content {
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                    padding: 1rem;
                    background: var(--surface-color);
                    border-radius: var(--border-radius);
                    border-left: 4px solid;
                }
                
                .notification-info .notification-content { border-left-color: var(--primary-color); }
                .notification-success .notification-content { border-left-color: var(--success-color); }
                .notification-warning .notification-content { border-left-color: var(--warning-color); }
                .notification-error .notification-content { border-left-color: var(--danger-color); }
                
                .notification-close {
                    background: none;
                    border: none;
                    cursor: pointer;
                    color: var(--text-secondary);
                    margin-left: auto;
                }
                
                @keyframes slideIn {
                    from {
                        transform: translateX(100%);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
            `;
            document.head.appendChild(styles);
        }

        document.body.appendChild(notification);

        // Auto remove after duration
        if (duration > 0) {
            setTimeout(() => {
                if (notification.parentElement) {
                    notification.remove();
                }
            }, duration);
        }
    },

    getNotificationIcon(type) {
        const icons = {
            info: 'info-circle',
            success: 'check-circle',
            warning: 'exclamation-triangle',
            error: 'times-circle'
        };
        return icons[type] || 'info-circle';
    }
};

// Initialize common functionality
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling to all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading states to forms
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<div class="spinner"></div> Processing...';
                submitBtn.disabled = true;
                
                // Reset after 10 seconds as fallback
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 10000);
            }
        });
    });

    // Add hover effects to cards
    document.querySelectorAll('.card').forEach(card => {
        if (card.style.cursor === 'pointer' || card.onclick) {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            });
        }
    });

    // Add keyboard navigation support
    document.addEventListener('keydown', function(e) {
        // ESC key closes modals
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal:not(.hidden)').forEach(modal => {
                modal.classList.add('hidden');
            });
        }
    });

    // Add touch support for mobile
    if ('ontouchstart' in window) {
        document.body.classList.add('touch-device');
    }
});

// Export for use in other scripts
window.SOC_CMM = window.SOC_CMM;

