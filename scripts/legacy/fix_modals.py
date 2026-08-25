import os

def fix_template_modals():
    # Fix index.html - remove auto-opening modal
    index_path = '/home/ubuntu/soc_cmm_system/templates/index.html'
    with open(index_path, 'r') as f:
        content = f.read()
    
    # Remove the script that auto-opens the modal
    content = content.replace('''<script>
function showAbout() {
    document.getElementById('aboutModal').classList.remove('hidden');
}

function hideAbout() {
    document.getElementById('aboutModal').classList.add('hidden');
}

// Close modal when clicking outside
document.getElementById('aboutModal').addEventListener('click', function(e) {
    if (e.target === this) {
        hideAbout();
    }
});
</script>''', '''<script>
function showAbout() {
    document.getElementById('aboutModal').classList.remove('hidden');
}

function hideAbout() {
    document.getElementById('aboutModal').classList.add('hidden');
}

// Close modal when clicking outside
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('aboutModal');
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                hideAbout();
            }
        });
    }
});
</script>''')
    
    with open(index_path, 'w') as f:
        f.write(content)
    
    # Fix customers.html - similar modal fixes
    customers_path = '/home/ubuntu/soc_cmm_system/templates/customers.html'
    with open(customers_path, 'r') as f:
        content = f.read()
    
    # Add proper modal initialization
    content = content.replace('''// Close modals when clicking outside
document.getElementById('createCustomerModal').addEventListener('click', function(e) {
    if (e.target === this) {
        hideCreateCustomer();
    }
});

document.getElementById('assessmentsModal').addEventListener('click', function(e) {
    if (e.target === this) {
        hideAssessments();
    }
});''', '''// Close modals when clicking outside
document.addEventListener('DOMContentLoaded', function() {
    const createModal = document.getElementById('createCustomerModal');
    const assessmentsModal = document.getElementById('assessmentsModal');
    
    if (createModal) {
        createModal.addEventListener('click', function(e) {
            if (e.target === this) {
                hideCreateCustomer();
            }
        });
    }
    
    if (assessmentsModal) {
        assessmentsModal.addEventListener('click', function(e) {
            if (e.target === this) {
                hideAssessments();
            }
        });
    }
});''')
    
    with open(customers_path, 'w') as f:
        f.write(content)
    
    print("Modal fixes applied!")

if __name__ == "__main__":
    fix_template_modals()

