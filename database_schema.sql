-- SOC CMM Assessment System Database Schema

-- Customers table
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    organization VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Domains table (Business, People, Process, Technology, Services, Results)
CREATE TABLE domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL
);

-- Aspects table (subcategories within each domain)
CREATE TABLE aspects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(10) NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL,
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- Questions table
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aspect_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    question_type VARCHAR(50) DEFAULT 'multiple_choice',
    order_index INTEGER NOT NULL,
    FOREIGN KEY (aspect_id) REFERENCES aspects(id)
);

-- Answer options table (for multiple choice questions)
CREATE TABLE answer_options (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    option_text TEXT NOT NULL,
    maturity_level INTEGER NOT NULL, -- 0-5 scale
    order_index INTEGER NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- Assessments table (one assessment per customer per time)
CREATE TABLE assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    name VARCHAR(255),
    status VARCHAR(50) DEFAULT 'in_progress', -- in_progress, completed
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Assessment answers table
CREATE TABLE assessment_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    answer_option_id INTEGER,
    answer_text TEXT,
    maturity_score INTEGER, -- calculated score for this answer
    answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assessment_id) REFERENCES assessments(id),
    FOREIGN KEY (question_id) REFERENCES questions(id),
    FOREIGN KEY (answer_option_id) REFERENCES answer_options(id)
);

-- Assessment scores table (aggregated scores by aspect and domain)
CREATE TABLE assessment_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id INTEGER NOT NULL,
    aspect_id INTEGER,
    domain_id INTEGER,
    score DECIMAL(5,2) NOT NULL,
    max_score DECIMAL(5,2) NOT NULL,
    percentage DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (assessment_id) REFERENCES assessments(id),
    FOREIGN KEY (aspect_id) REFERENCES aspects(id),
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- Create indexes for better performance
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_aspects_domain ON aspects(domain_id);
CREATE INDEX idx_questions_aspect ON questions(aspect_id);
CREATE INDEX idx_answer_options_question ON answer_options(question_id);
CREATE INDEX idx_assessments_customer ON assessments(customer_id);
CREATE INDEX idx_assessment_answers_assessment ON assessment_answers(assessment_id);
CREATE INDEX idx_assessment_scores_assessment ON assessment_scores(assessment_id);

