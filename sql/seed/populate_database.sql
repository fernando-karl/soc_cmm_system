-- SOC CMM Assessment System - Database Population Script
-- Populate domains, aspects, questions and answer_options tables

-- First, let's populate the domains table
INSERT INTO domains (id, name, description, order_index) VALUES
(1, 'Business', 'Business alignment, governance, and strategic aspects of the SOC', 1),
(2, 'People', 'Human resources, skills, and organizational aspects of the SOC', 2),
(3, 'Process', 'Operational processes, procedures, and workflows of the SOC', 3),
(4, 'Technology', 'Technical infrastructure, tools, and systems used by the SOC', 4),
(5, 'Services', 'Service delivery, capabilities, and service management aspects', 5);

-- Now let's populate the aspects table for each domain
-- Business domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(1, 1, 'Business Drivers', 'Business drivers and strategic alignment', 1),
(2, 1, 'Customers', 'Customer identification and management', 2),
(3, 1, 'Charter', 'SOC charter and mission statement', 3),
(4, 1, 'Governance', 'Governance structure and processes', 4),
(5, 1, 'Privacy & Policy', 'Privacy policies and compliance', 5);

-- People domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(6, 2, 'Employees', 'Employee management and staffing', 1),
(7, 2, 'Skills & Competencies', 'Skills development and competency management', 2),
(8, 2, 'Training & Development', 'Training programs and professional development', 3),
(9, 2, 'Performance Management', 'Performance evaluation and management', 4),
(10, 2, 'Organizational Structure', 'Organizational design and structure', 5);

-- Process domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(11, 3, 'Process Management', 'Process governance and management', 1),
(12, 3, 'Security Monitoring', 'Security monitoring processes', 2),
(13, 3, 'Security Incident Management', 'Incident response and management', 3),
(14, 3, 'Security Analysis', 'Security analysis and investigation', 4),
(15, 3, 'Threat Intelligence', 'Threat intelligence processes', 5),
(16, 3, 'Threat Hunting', 'Proactive threat hunting', 6),
(17, 3, 'Vulnerability Management', 'Vulnerability assessment and management', 7),
(18, 3, 'Log Management', 'Log collection and management', 8);

-- Technology domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(19, 4, 'Technology Management', 'Technology governance and management', 1),
(20, 4, 'SIEM / UEBA', 'Security Information and Event Management', 2),
(21, 4, 'NDR', 'Network Detection and Response', 3),
(22, 4, 'EDR', 'Endpoint Detection and Response', 4),
(23, 4, 'SOAR', 'Security Orchestration, Automation and Response', 5),
(24, 4, 'Infrastructure', 'Technical infrastructure and platforms', 6),
(25, 4, 'Integration', 'System integration and interoperability', 7),
(26, 4, 'Security', 'Security controls and measures', 8);

-- Services domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(27, 5, 'Service Management', 'Service governance and management', 1),
(28, 5, 'Security Monitoring Service', 'Security monitoring service delivery', 2),
(29, 5, 'Security Incident Management Service', 'Incident management service delivery', 3),
(30, 5, 'Security Analysis Service', 'Security analysis service delivery', 4),
(31, 5, 'Threat Intelligence Service', 'Threat intelligence service delivery', 5),
(32, 5, 'Threat Hunting Service', 'Threat hunting service delivery', 6),
(33, 5, 'Vulnerability Management Service', 'Vulnerability management service delivery', 7),
(34, 5, 'Log Management Service', 'Log management service delivery', 8);

-- Now let's populate some key questions with their answer options
-- Business Drivers questions
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(1, 1, 'Have you identified the main business drivers?', 'dropdown', 'Example business drivers: cyber crime prevention, risk reduction, law / regulation, audit / compliance, business continuity', 1),
(2, 1, 'Have you documented the main business drivers?', 'dropdown', 'Documentation of business drivers is important for demonstrable business alignment', 2),
(3, 1, 'Do you use business drivers in the decision making process?', 'dropdown', 'e.g. to determine priorities or make decisions regarding the on-boarding of new services or operations', 3),
(4, 1, 'Do you regularly check if the current service catalogue is aligned with business drivers?', 'dropdown', 'i.e. do you check for services or operations that outside the scope of business drivers?', 4),
(5, 1, 'Have the business drivers been validated with business stakeholders?', 'dropdown', 'Business stakeholders can be C-level management', 5);

-- Answer options for Business Drivers questions
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(1, 'Not defined', 1, 1),
(1, 'Partially defined', 2, 2),
(1, 'Fully defined', 3, 3),
(2, 'Not documented', 1, 1),
(2, 'Partially documented', 2, 2),
(2, 'Fully documented', 3, 3),
(3, 'No', 1, 1),
(3, 'Partially', 2, 2),
(3, 'Yes', 3, 3),
(4, 'No', 1, 1),
(4, 'Partially', 2, 2),
(4, 'Yes', 3, 3),
(5, 'No', 1, 1),
(5, 'Partially', 2, 2),
(5, 'Yes', 3, 3);

-- Customers questions
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(6, 2, 'Have you identified the SOC customers?', 'dropdown', 'Types of customers, customer requirements / expectations, etc.', 1),
(7, 2, 'Please specify your customers:', 'checkbox', 'Use this as a guideline for answering 2.1. This is also potentially useful for insights and comparison with previous assessments.', 2),
(8, 2, 'Have you documented the main SOC customers?', 'dropdown', 'Formal registration of customer contact details, place in the organization, geolocation, etc.', 3),
(9, 2, 'Do you differentiate output towards these specific customers?', 'dropdown', 'For example, are communication style and contents to Business customers different than that to IT?', 4),
(10, 2, 'Do you have service level agreements with these customers?', 'dropdown', 'Service level agreements are used to provide standardized services operating within known boundaries', 5);

-- Answer options for Customers questions
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(6, 'Not identified', 1, 1),
(6, 'Partially identified', 2, 2),
(6, 'Fully identified', 3, 3),
(7, 'Legal', 0, 1),
(7, 'Audit', 0, 2),
(7, 'Engineering / R&D', 0, 3),
(7, 'IT', 0, 4),
(7, 'Business', 0, 5),
(7, 'External customers', 0, 6),
(7, '(Senior) Management', 0, 7),
(7, 'Other customers', 0, 8),
(8, 'Not documented', 1, 1),
(8, 'Partially documented', 2, 2),
(8, 'Fully documented', 3, 3),
(9, 'No', 1, 1),
(9, 'Partially', 2, 2),
(9, 'Yes', 3, 3),
(10, 'No', 1, 1),
(10, 'Partially', 2, 2),
(10, 'Yes', 3, 3);

-- Charter questions
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(11, 3, 'Does the SOC have a formal charter document in place?', 'dropdown', 'See 3.2 for charter document elements', 1),
(12, 3, 'Please specify elements of the charter document:', 'checkbox', '', 2),
(13, 3, 'Is the SOC charter document regularly updated?', 'dropdown', 'Regularity should be matched to your own internal policy. At least yearly is recommended', 3),
(14, 3, 'Is the SOC charter document approved by the business / CISO?', 'dropdown', 'Approval from the relevant stakeholders will aid in business support for SOC operations', 4),
(15, 3, 'Are all stakeholders familiar with the SOC charter document contents?', 'dropdown', 'Making stakeholders aware of the contents helps in getting organizational support for security operations', 5);

-- Answer options for Charter questions
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(11, 'No', 1, 1),
(11, 'Partially', 2, 2),
(11, 'Yes', 3, 3),
(12, 'Mission', 0, 1),
(12, 'Vision', 0, 2),
(12, 'Strategy', 0, 3),
(12, 'Service Scope', 0, 4),
(12, 'Deliverables', 0, 5),
(12, 'Responsibilities', 0, 6),
(12, 'Accountability', 0, 7),
(12, 'Operational Hours', 0, 8),
(12, 'Stakeholders', 0, 9),
(12, 'Objectives / Goals', 0, 10),
(12, 'Statement of success', 0, 11),
(13, 'No', 1, 1),
(13, 'Partially', 2, 2),
(13, 'Yes', 3, 3),
(14, 'No', 1, 1),
(14, 'Partially', 2, 2),
(14, 'Yes', 3, 3),
(15, 'No', 1, 1),
(15, 'Partially', 2, 2),
(15, 'Yes', 3, 3);

-- People domain questions
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(16, 6, 'How many FTE''s are in your SOC?', 'numeric', 'Include both internal and external FTE''s', 1),
(17, 6, 'Do you use external employees / contractors in your SOC?', 'dropdown', 'External employees can be hired experts to fill in vacant positions or perform project activities', 2),
(18, 6, 'If yes, specify the number of external FTE''s', 'numeric', '', 3),
(19, 6, 'Does the current size of the SOC meet FTE requirements?', 'dropdown', 'i.e. is the SOC size sufficient to realize business goals?', 4),
(20, 6, 'Does the SOC meet requirements for internal to external employee FTE ratio?', 'dropdown', 'i.e. is the SOC size sufficient to realize business goals?', 5);

-- Answer options for People questions
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(17, 'Yes', 1, 1),
(17, 'No', 0, 2),
(19, 'No', 1, 1),
(19, 'Partially', 2, 2),
(19, 'Yes', 3, 3),
(20, 'No', 1, 1),
(20, 'Partially', 2, 2),
(20, 'Yes', 3, 3);

-- Technology domain questions (SIEM/UEBA)
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(21, 20, 'SIEM / UEBA', 'checkbox', 'Security Information and Event management tooling. Used to gather logging information from company assets and correlate events. Also includes User and Entity Behaviour Analytics (UEBA)', 1),
(22, 21, 'NDR', 'checkbox', 'Network security solution, used detect network exploits and anomalous network activity and perform network forensics', 1),
(23, 22, 'EDR', 'checkbox', 'End-point security solution, used to prevent, detect and respond to threats on end-points', 1),
(24, 23, 'SOAR', 'checkbox', 'Used to automate workflows and SOC actions, support incident response and orchestrate between different security products', 1);

-- Services domain questions
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(25, 28, 'Security Monitoring', 'checkbox', 'The security monitoring service aims at detecting security incidents and events', 1),
(26, 29, 'Security Incident Management', 'checkbox', 'The security incident management service aims at responding to security incidents in a timely, accurate and organized fashion', 1),
(27, 30, 'Security Analysis', 'checkbox', 'The security analysis service supports security monitoring and security incident management. Analysis includes event analysis and forensic analysis', 1),
(28, 31, 'Threat Intelligence', 'checkbox', 'The threat intelligence service provides information about potential threats that can be used in security monitoring, security incident response, security analysis and threat hunting', 1),
(29, 32, 'Threat Hunting', 'checkbox', 'The hunting service takes a proactive approach to finding threats in the infrastructure. Threat intelligence is often used to guide hunting efforts', 1),
(30, 33, 'Vulnerability Management', 'checkbox', 'The vulnerability management service is used to detect vulnerabilities in assets by discovery and actively scanning assets for known vulnerabilities', 1),
(31, 34, 'Log Management', 'checkbox', 'The log management service is used to collect, store and retain logging. Can be used for compliance purposes as well as investigation purposes', 1);

-- Add more comprehensive questions for each domain...
-- This is a sample of the most important questions. The complete dataset would include all questions from the JSON file.

-- Note: This script provides a foundation. You may want to add more questions and answer options
-- based on the complete JSON file structure. The questions above represent key assessment areas
-- for each domain of the SOC CMM framework. 