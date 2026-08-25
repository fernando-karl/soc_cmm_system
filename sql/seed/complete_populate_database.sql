-- SOC CMM Assessment System - Complete Database Population Script
-- Generated from soc_cmm_questions.json

-- Insert domains
INSERT INTO domains (id, name, description, order_index) VALUES
(1, 'Business', 'Business domain of SOC CMM assessment', 1),
(2, 'People', 'People domain of SOC CMM assessment', 2),
(3, 'Process', 'Process domain of SOC CMM assessment', 3),
(4, 'Technology', 'Technology domain of SOC CMM assessment', 4),
(5, 'Services', 'Services domain of SOC CMM assessment', 5)
;

-- Business domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(1, 1, 'Business Drivers', 'Business Drivers aspect of Business domain', 1);

-- Questions for Business Drivers
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(1, 1, 'Have you identified the main business drivers?', 'dropdown', 'Example business drivers: cyber crime prevention, risk reduction, law / regulation, audit / compliance, business continuity', 1);
-- Answer options for question 1
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(1, 'Not defined', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(1, 'Partially defined', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(1, 'Fully defined', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(2, 1, 'Have you documented the main business drivers?', 'dropdown', 'Documentation of business drivers is important for demonstrable business alignment', 2);
-- Answer options for question 2
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(2, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(2, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(2, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(3, 1, 'Do you use business drivers in the decision making process?', 'dropdown', 'e.g. to determine priorities or make decisions regarding the on-boarding of new services or operations', 3);
-- Answer options for question 3
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(3, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(3, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(3, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(4, 1, 'Do you regularly check if the current service catalogue is aligned with business drivers?', 'dropdown', 'i.e. do you check for services or operations that outside the scope of business drivers?', 4);
-- Answer options for question 4
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(4, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(4, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(4, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(5, 1, 'Have the business drivers been validated with business stakeholders?', 'dropdown', 'Business stakeholders can be C-level management', 5);
-- Answer options for question 5
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(5, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(5, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(5, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(2, 1, 'Customers', 'Customers aspect of Business domain', 2);

-- Questions for Customers
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(6, 2, 'Have you identified the SOC customers?', 'dropdown', 'Types of customers, customer requirements / expectations, etc.', 6);
-- Answer options for question 6
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(6, 'Not identified', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(6, 'Partially identified', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(6, 'Fully identified', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(7, 2, 'Please specify your customers:', 'checkbox', 'Use this as a guideline for answering 2.1. This is also potentially useful for insights and comparison with previous assessments.', 7);
-- Answer options for question 7
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(7, 'Legal', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(7, 'Audit', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(7, 'Engineering / R&D', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(7, 'IT', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(7, 'Business', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(7, 'External customers', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(7, '(Senior) Management', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(7, 'Other customers', 0, 8);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(8, 2, 'Have you documented the main SOC customers?', 'dropdown', 'Formal registration of customer contact details, place in the organization, geolocation, etc.', 8);
-- Answer options for question 8
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(8, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(8, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(8, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(9, 2, 'Do you differentiate output towards these specific customers?', 'dropdown', 'For example, are communication style and contents to Business customers different than that to IT?', 9);
-- Answer options for question 9
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(9, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(9, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(9, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(10, 2, 'Do you have service level agreements with these customers?', 'dropdown', 'Service level agreements are used to provide standardized services operating within known boundaries', 10);
-- Answer options for question 10
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(10, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(10, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(10, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(11, 2, 'Do you regularly send updates to your customers?', 'dropdown', 'For example: changes in service scope or delivery. Can also be reports, dashboards, etc.', 11);
-- Answer options for question 11
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(11, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(11, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(11, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(12, 2, 'Do you actively measure and manage customer satisfaction?', 'dropdown', 'Understanding customer satisfaction will help to better align with business needs', 12);
-- Answer options for question 12
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(12, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(12, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(12, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(3, 1, 'Charter', 'Charter aspect of Business domain', 3);

-- Questions for Charter
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(13, 3, 'Does the SOC have a formal charter document in place?', 'dropdown', 'See 3.2 for charter document elements', 13);
-- Answer options for question 13
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(13, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(13, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(13, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(14, 3, 'Please specify elements of the charter document:', 'checkbox', '', 14);
-- Answer options for question 14
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Mission', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Vision', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Strategy', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Service Scope', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Deliverables', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Responsibilities', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Accountability', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Operational Hours', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Stakeholders', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Objectives / Goals', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(14, 'Statement of success', 0, 11);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(15, 3, 'Is the SOC charter document regularly updated?', 'dropdown', 'Regularity should be matched to your own internal policy. At least yearly is recommended', 15);
-- Answer options for question 15
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(15, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(15, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(15, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(16, 3, 'Is the SOC charter document approved by the business / CISO?', 'dropdown', 'Approval from the relevant stakeholders will aid in business support for SOC operations', 16);
-- Answer options for question 16
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(16, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(16, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(16, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(17, 3, 'Are all stakeholders familiar with the SOC charter document contents?', 'dropdown', 'Making stakeholders aware of the contents helps in getting organizational support for security operations', 17);
-- Answer options for question 17
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(17, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(17, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(17, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(4, 1, 'Governance', 'Governance aspect of Business domain', 4);

-- Questions for Governance
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(18, 4, 'Does the SOC have a governance process in place?', 'dropdown', 'A governance process is required to determine the way the SOC should be managed', 18);
-- Answer options for question 18
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(18, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(18, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(18, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(19, 4, 'Have all governance elements been identified?', 'dropdown', 'Possible governance elements can be found in under 4.3', 19);
-- Answer options for question 19
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(19, 'Not identified', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(19, 'Partially identified', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(19, 'Fully identified', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(20, 4, 'Please specify identified governance elements', 'checkbox', '', 20);
-- Answer options for question 20
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Business Alignment', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Accountability', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Sponsorship', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Mandate', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Relationships & Third Party Management', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Vendor Engagement', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Service Commitment', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Project / Program Management', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Continual Improvement', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Span of control / federation governance', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Outsourced service management', 0, 11);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'SOC KPIs & Metrics', 0, 12);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'SOC risk management', 0, 13);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(20, 'Customer Engagement / Satisfaction', 0, 14);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(21, 4, 'Is cost management in place?', 'dropdown', 'Managing costs is required to justify budget allocation for the SOC and ensure continued service delivery in the future', 21);
-- Answer options for question 21
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(21, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(21, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(21, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(22, 4, 'Please specify cost management elements', 'checkbox', '', 22);
-- Answer options for question 22
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(22, 'People cost', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(22, 'Process cost', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(22, 'Technology cost', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(22, 'Services cost', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(22, 'Facility cost', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(22, 'Budget forecasting', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(22, 'Budget alignment', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(22, 'Return on investment', 0, 8);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(23, 4, 'Are all governance elements formally documented?', 'dropdown', 'Formal documentation should be signed off and stored in a quality management system', 23);
-- Answer options for question 23
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(23, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(23, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(23, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(24, 4, 'Are SOC governance meetings regularly held?', 'dropdown', 'Meetings at different levels (operational, tactical, strategic) should be formalised in Terms of Reference (ToR) and driven by metrics', 24);
-- Answer options for question 24
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(24, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(24, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(24, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(25, 4, 'Is the governance process regularly reviewed?', 'dropdown', 'Frequency should be matched to your own internal policy. At least yearly is recommended', 25);
-- Answer options for question 25
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(25, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(25, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(25, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(26, 4, 'Is the governance process aligned with all stakeholders?', 'dropdown', 'Alignment will help the SOC obtain required mandate, budget and management support', 26);
-- Answer options for question 26
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(26, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(26, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(26, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(27, 4, 'Is the SOC regularly audited or subjected to (external) assessments?', 'dropdown', 'Frequency should be matched to the SOC policy. At least yearly is recommended. 3rd party assessments have a higher objectivity', 27);
-- Answer options for question 27
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(27, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(27, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(27, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(28, 4, 'Is there an active cooperation with other SOCs (external)?', 'dropdown', 'Exchange of best practices, intelligence and actions on threats with other SOCs is vital for improving cyber defence', 28);
-- Answer options for question 28
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(28, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(28, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(28, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(5, 1, 'Privacy & Policy', 'Privacy & Policy aspect of Business domain', 5);

-- Questions for Privacy & Policy
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(29, 5, 'Is there an information security policy in place that supports the SOC activities?', 'dropdown', 'A clear security policy that supports SOC operations provides guidance and helps to enforce mandate for the SOC in the organisation', 29);
-- Answer options for question 29
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(29, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(29, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(29, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(30, 5, 'Has a SOC policy been created?', 'dropdown', 'A SOC policy is to outline the rules to which SOC personnel and SOC management needs to adhere', 30);
-- Answer options for question 30
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(30, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(30, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(30, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(31, 5, 'Please specify elements of the SOC policy', 'checkbox', '', 31);
-- Answer options for question 31
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(31, 'Code of conduct', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(31, 'Rules of engagement & responsibilities', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(31, 'Review frequency of documentation', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(31, 'SOC assessment frequency and type', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(31, 'Knowledge exchange and maintenance', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(31, 'Exercise frequency', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(31, 'Usage of TLP', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(31, 'Working agreements', 0, 8);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(32, 5, 'Is the SOC consulted in the creation and updates of operational security policy?', 'dropdown', 'Consulting the SOC in the creation of security policy will ensure that SOC activities are properly mentioned and enforceable', 32);
-- Answer options for question 32
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(32, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(32, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(32, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(33, 5, 'Is a reporting policy for security incidents in place?', 'dropdown', 'A reporting policy for security incidents will aid the SOC in identifying incidents and threats in the organization', 33);
-- Answer options for question 33
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(33, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(33, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(33, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(34, 5, 'Is a privacy policy regarding security monitoring of employees in place?', 'dropdown', 'A privacy policy should state that monitoring of employees is possible within acceptable limits', 34);
-- Answer options for question 34
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(34, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(34, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(34, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(35, 5, 'Does the SOC operate in compliance with all applicable privacy laws and regulations?', 'dropdown', 'Local laws and regulations as well as company policy may apply and should all be considered', 35);
-- Answer options for question 35
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(35, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(35, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(35, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(36, 5, 'Does the SOC cooperate with legal departments regarding privacy matters?', 'dropdown', 'Cooperation will ensure that the SOC is enabled to perform activities, rather than blocked', 36);
-- Answer options for question 36
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(36, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(36, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(36, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(37, 5, 'Are specific procedures in place for dealing with privacy related investigations?', 'dropdown', 'Privacy related issues require careful examination, especially those potentially leading to court cases', 37);
-- Answer options for question 37
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(37, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(37, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(37, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(38, 5, 'Is the SOC aware of all information that it processes and is subject to privacy regulations?', 'dropdown', 'Such information includes IP addresses, customer identifiers, user names, host names (for personally owned devices), etc.', 38);
-- Answer options for question 38
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(38, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(38, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(38, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(39, 5, 'Is a Privacy Impact Assessment (PIA) regularly conducted?', 'dropdown', 'Can be used to determine the impact of monitoring on privacy, and can help uncover potential violations', 39);
-- Answer options for question 39
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(39, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(39, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(39, 'Yes', 3, 3);

-- People domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(6, 2, 'Employees', 'Employees aspect of People domain', 6);

-- Questions for Employees
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(40, 6, 'How many FTE’s are in your SOC?', 'numeric', 'Include both internal and external FTE''s', 40);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(41, 6, 'Do you use external employees / contractors in your SOC?', 'dropdown', 'External employees can be hired experts to fill in vacant positions or perform project activities', 41);
-- Answer options for question 41
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(41, 'Yes', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(41, 'No', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(42, 6, 'If yes, specify the number of external FTE''s', 'numeric', '', 42);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(43, 6, 'Does the current size of the SOC meet FTE requirements?', 'dropdown', 'i.e. is the SOC size sufficient to realize business goals?', 43);
-- Answer options for question 43
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(43, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(43, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(43, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(44, 6, 'Does the SOC meet requirements for internal to external employee FTE ratio?', 'dropdown', 'Note: requirements do not need to be explicit. Set importance to ''None'' if you have no external employees.', 44);
-- Answer options for question 44
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(44, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(44, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(44, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(45, 6, 'Does the SOC meet requirements for internal to external employee skillset?', 'dropdown', 'i.e. Are there any crucial skills amongst external employees? Set importance to ''None'' if you have no external employees', 45);
-- Answer options for question 45
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(45, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(45, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(45, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(46, 6, 'Are all positions filled?', 'dropdown', 'Unfilled positions may be due to deficiencies in the recruitment process', 46);
-- Answer options for question 46
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(46, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(46, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(46, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(47, 6, 'Do you have a recruitment process in place?', 'dropdown', 'A recruitment process is required to obtain new employees in a market where talent is scarce', 47);
-- Answer options for question 47
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(47, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(47, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(47, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(48, 6, 'Do you have a talent acquisition process in place?', 'dropdown', 'Talent recruitment can be vital for SOC success, but talent retaining is equally important', 48);
-- Answer options for question 48
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(48, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(48, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(48, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(49, 6, 'Do you have specific KSAOs established for SOC personnel?', 'dropdown', 'Knowledge, Skills, Abilities and Other attributes (KSAOs) should be in place: technical, cognitive, social and character', 49);
-- Answer options for question 49
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(49, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(49, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(49, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(50, 6, 'Do you actively seek to create a psychologically safe environment for SOC personnel?', 'dropdown', 'A psychologically safe environment is an environment where everyone is able to speak their mind and feel valued', 50);
-- Answer options for question 50
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(50, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(50, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(50, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(7, 2, 'Roles and Hierarchy', 'Roles and Hierarchy aspect of People domain', 7);

-- Questions for Roles and Hierarchy
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(51, 7, 'Do you formally differentiate roles within the SOC?', 'dropdown', 'Use the roles in 2.2 to determine if you have all roles required in the SOC', 51);
-- Answer options for question 51
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(51, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(51, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(51, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(52, 7, 'Which of the following roles are present in your SOC?', 'checkbox', '', 52);
-- Answer options for question 52
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Security Analyst', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Security / Systems Engineer', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Forensic Analyst', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Security Architect', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Threat Intelligence Analyst', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Data Scientist', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'SOC Manager', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Team Leader', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Incident Handler', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Incident Manager', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Penetration Tester', 0, 11);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Detection engineer', 0, 12);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Automation engineer', 0, 13);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(52, 'Others', 0, 14);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(53, 7, 'Do you differentiate tiers within these roles?', 'dropdown', 'If you have no tiers, and you feel this is not a restriction, select importance ''None''', 53);
-- Answer options for question 53
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(53, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(53, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(53, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(54, 7, 'Are all roles sufficiently staffed?', 'dropdown', 'Consider the staffing levels (desired FTE count) as well as knowledge and experience for all roles', 54);
-- Answer options for question 54
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(54, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(54, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(54, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(55, 7, 'Is there a role-based hierarchy in your SOC?', 'dropdown', 'If you have no hierarchy, and you feel this is not a restriction, select importance ''None''', 55);
-- Answer options for question 55
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(55, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(55, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(55, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(56, 7, 'Have you formally documented all SOC roles?', 'dropdown', 'Possible documentation elements can be found in under 2.7', 56);
-- Answer options for question 56
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(56, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(56, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(56, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(57, 7, 'Please specify elements in the role documentation:', 'checkbox', '', 57);
-- Answer options for question 57
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(57, 'Role description', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(57, 'Role tasks', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(57, 'Role responsibilities', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(57, 'Role expectations', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(57, 'Required technical skills', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(57, 'Required soft skills', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(57, 'Required educational level', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(57, 'Required or preferred certifications', 0, 8);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(58, 7, 'Are responsibilities for each role understood?', 'dropdown', 'Responsibilities for each role should be clearly understood by all SOC personnel', 58);
-- Answer options for question 58
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(58, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(58, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(58, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(59, 7, 'Have you documented career progression requirements for each of these roles?', 'dropdown', 'Career progression for roles can be documented through training, certification, experience and soft skills requirements', 59);
-- Answer options for question 59
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(59, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(59, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(59, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(60, 7, 'Do you regularly revise or update the role descriptions?', 'dropdown', 'To revise is to review and verify whether to documentation is still correct or requires an update', 60);
-- Answer options for question 60
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(60, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(60, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(60, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(8, 2, 'People Management', 'People Management aspect of People domain', 8);

-- Questions for People Management
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(61, 8, 'Do you have a job rotation plan in place?', 'dropdown', 'Job rotation can be used to train employees in a variety of tasks and avoid too much routine', 61);
-- Answer options for question 61
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(61, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(61, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(61, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(62, 8, 'Do you have a career progression process in place?', 'dropdown', 'Career development, promotion, etc.', 62);
-- Answer options for question 62
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(62, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(62, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(62, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(63, 8, 'Do you have a talent management process in place?', 'dropdown', 'Talent should be adequately managed to retain such staff and fully develop their potential.', 63);
-- Answer options for question 63
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(63, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(63, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(63, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(64, 8, 'Do you have team diversity goals?', 'dropdown', 'e.g. background diversity, ethnic diversity, gender diversity, etc.', 64);
-- Answer options for question 64
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(64, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(64, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(64, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(65, 8, 'Have you established team goals?', 'dropdown', 'Team goals help to bring focus to the team and monitor progress', 65);
-- Answer options for question 65
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(65, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(65, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(65, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(66, 8, 'Do you document and track individual team member goals?', 'dropdown', 'Individual team member goals should be set to help grow the employee to full potential', 66);
-- Answer options for question 66
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(66, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(66, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(66, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(67, 8, 'Do you periodically evaluate SOC employees?', 'dropdown', 'Can also be included in the regular organization evaluation process', 67);
-- Answer options for question 67
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(67, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(67, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(67, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(68, 8, 'Do you have a ''new hire'' process in place?', 'dropdown', 'i.e. a defined process to quickly let new employees find their place and perform well in the SOC', 68);
-- Answer options for question 68
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(68, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(68, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(68, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(69, 8, 'Are all SOC employees subjected to screening?', 'dropdown', 'Personnel screening is performed to avoid infiltration or misbehaviour by SOC employees', 69);
-- Answer options for question 69
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(69, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(69, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(69, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(70, 8, 'Do you measure employee satisfaction for improving the SOC?', 'dropdown', 'Employee satisfaction should be taken seriously as lack of satisfaction may lead to key personnel leaving', 70);
-- Answer options for question 70
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(70, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(70, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(70, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(71, 8, 'Are there regular 1-on-1 meetings between the SOC manager and the employees?', 'dropdown', 'Such informal 1-on-1 conversations are used to coach employees and help the SOC manager gain insight in personal challenges', 71);
-- Answer options for question 71
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(71, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(71, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(71, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(72, 8, 'Do you perform regular teambuilding exercises?', 'dropdown', 'Teambuilding exercises are used to promote collaboration between individuals in the team and to raise team spirit', 72);
-- Answer options for question 72
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(72, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(72, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(72, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(73, 8, 'Do you perform regular teambuilding exercises with other teams relevant to the SOC?', 'dropdown', 'In multi-team systems (MTS), the SOC collaborates with other teams. Use cross-team teambuilding to maximize performance', 73);
-- Answer options for question 73
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(73, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(73, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(73, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(74, 8, 'Do you periodically evaluate team performance?', 'dropdown', 'Besides individual performance, team performance and dynamics are also important to measure and improve on', 74);
-- Answer options for question 74
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(74, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(74, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(74, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(9, 2, 'Knowledge Management', 'Knowledge Management aspect of People domain', 9);

-- Questions for Knowledge Management
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(75, 9, 'Do you have a formal knowledge management process in place?', 'dropdown', 'Formal knowledge management helps to optimize knowledge creation and distribution', 75);
-- Answer options for question 75
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(75, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(75, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(75, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(76, 9, 'Do you have a skill matrix in place?', 'dropdown', 'A matrix may consist of: SOC skills, SOC employees and skill levels (novice, intermediate, expert)', 76);
-- Answer options for question 76
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(76, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(76, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(76, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(77, 9, 'Please specify elements of the skill matrix:', 'checkbox', '', 77);
-- Answer options for question 77
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(77, 'All SOC employees', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(77, 'Hard skills', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(77, 'Soft skills', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(77, 'Skill levels (novice, intermediate, expert)', 0, 4);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(78, 9, 'Is the skill matrix actively used for team and personal improvement?', 'dropdown', 'Personal improvement is essential, team improvement requires insight in team dynamics and skill distribution', 78);
-- Answer options for question 78
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(78, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(78, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(78, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(79, 9, 'Do you have a knowledge matrix in place?', 'dropdown', '', 79);
-- Answer options for question 79
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(79, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(79, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(79, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(80, 9, 'Please specify elements of the knowledge matrix:', 'checkbox', '', 80);
-- Answer options for question 80
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(80, 'All SOC employees', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(80, 'All relevant knowledge areas', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(80, 'Knowledge levels (novice, intermediate, expert)', 0, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(81, 9, 'Is the knowledge matrix actively used to determine training and education needs?', 'dropdown', 'The matrix should be used as a means to identify and resolve knowledge gaps', 81);
-- Answer options for question 81
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(81, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(81, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(81, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(82, 9, 'Have you documented SOC team member abilities?', 'dropdown', 'Besides knowledge and skills, team member abilities are also important to document', 82);
-- Answer options for question 82
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(82, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(82, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(82, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(83, 9, 'Do you regularly assess and revise the knowledge management process?', 'dropdown', 'This refers to the knowledge management process as a whole', 83);
-- Answer options for question 83
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(83, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(83, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(83, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(84, 9, 'Is there effective tooling in place to support knowledge documentation and distribution?', 'dropdown', 'Such tooling can help to avoid investigation similar issues multiple times by integrating into the security monitoring process', 84);
-- Answer options for question 84
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(84, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(84, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(84, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(10, 2, 'Training and Education', 'Training and Education aspect of People domain', 10);

-- Questions for Training and Education
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(85, 10, 'Do you have a training program in place?', 'dropdown', 'A training program is used to ensure a minimal level of knowledge for employees', 85);
-- Answer options for question 85
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(85, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(85, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(85, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(86, 10, 'Please specify elements of the training program:', 'checkbox', '', 86);
-- Answer options for question 86
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(86, 'Training on the Job', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(86, 'Product-specific training', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(86, 'Internal company training', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(86, 'Role-based specific training', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(86, 'Soft-skill training', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(86, 'Formal education', 0, 6);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(87, 10, 'Do you have a certification program in place?', 'dropdown', 'A certification program is used to provide a demonstrable minimum level of knowledge and skills', 87);
-- Answer options for question 87
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(87, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(87, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(87, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(88, 10, 'Please specify elements of the certification program:', 'checkbox', '', 88);
-- Answer options for question 88
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(88, 'Internal certification track', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(88, 'External certification track', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(88, 'Re-certification track (continuous education)', 0, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(89, 10, 'Is the training and certification program connected to evaluation and career progression?', 'dropdown', 'e.g. certain training and certifications are required to grow from a junior level function to a more senior level function', 89);
-- Answer options for question 89
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(89, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(89, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(89, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(90, 10, 'Is there a reserved budget for education and training?', 'dropdown', 'i.e. a fixed percentage of the total SOC budget that is allocated for education and cannot be used for other purposes', 90);
-- Answer options for question 90
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(90, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(90, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(90, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(91, 10, 'Is there a reserved amount of time for education and training?', 'dropdown', 'This is an extension of education budget', 91);
-- Answer options for question 91
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(91, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(91, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(91, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(92, 10, 'Do you have regular workshops for knowledge development?', 'dropdown', 'Workshops are an informal way of distributing knowledge', 92);
-- Answer options for question 92
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(92, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(92, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(92, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(93, 10, 'Do you regularly revise and update the training and certification programs?', 'dropdown', 'Training and certification must be a relevant reflection of SOC knowledge and skill requirements', 93);
-- Answer options for question 93
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(93, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(93, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(93, 'Yes', 3, 3);

-- Process domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(11, 3, 'Management', 'Management aspect of Process domain', 11);

-- Questions for Management
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(94, 11, 'Is there a SOC management process in place?', 'dropdown', 'A SOC management process is used to manage all aspects SOC service delivery and quality', 94);
-- Answer options for question 94
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(94, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(94, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(94, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(95, 11, 'Are SOC management elements formally identified and documented?', 'dropdown', 'Possible SOC management elements can be found in under 1.3', 95);
-- Answer options for question 95
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(95, 'Not identified', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(95, 'Partially identified', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(95, 'Fully identified', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(96, 11, 'Please specify identified SOC management elements:', 'checkbox', '', 96);
-- Answer options for question 96
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'Internal relationship management', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'External relationship management', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'Vendor management', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'Continuous service improvement', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'Project methodology', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'Process documentation and diagrams', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'RACI matrix', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'Service Catalogue', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'Service on-boarding procedure', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(96, 'Service off-loading procedure', 0, 10);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(97, 11, 'Is the SOC management process regularly reviewed?', 'dropdown', 'Regular review of the SOC management process ensures optimal performance', 97);
-- Answer options for question 97
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(97, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(97, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(97, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(98, 11, 'Is the SOC management process aligned with all stakeholders?', 'dropdown', 'Alignment with stakeholders will ensure the SOC delivers services that meet customer expectations', 98);
-- Answer options for question 98
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(98, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(98, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(98, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(99, 11, 'Have you implemented a process for continuous improvement (CI)?', 'dropdown', 'Continuous improvement is a vital process for SOCs to evolve their capabilities', 99);
-- Answer options for question 99
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(99, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(99, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(99, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(100, 11, 'Specify elements of the continuous improvement program:', 'checkbox', '', 100);
-- Answer options for question 100
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(100, 'Daily progress tracking', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(100, 'Weekly planning', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(100, 'Backlog management', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(100, 'Work item effort estimation', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(100, 'Work item prioritisation', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(100, 'Refinement', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(100, 'Capacity for change', 0, 7);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(101, 11, 'Have you implemented a process to manage SOC quality assurance (QA)?', 'dropdown', 'Quality assurance is aimed at ensuring SOC processes, technology and services meet their quality requirements', 101);
-- Answer options for question 101
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(101, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(101, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(101, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(102, 11, 'Please specify elements of the quality assurance program:', 'checkbox', '', 102);
-- Answer options for question 102
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(102, 'Ticket quality assurance', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(102, 'Incident quality assurance', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(102, 'Service quality assurance', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(102, 'Process quality assurance', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(102, 'Report quality assurance', 0, 5);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(103, 11, 'Have you implemented a SOC architecture process?', 'dropdown', 'A SOC architecture describes how different components', 103);
-- Answer options for question 103
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(103, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(103, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(103, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(104, 11, 'Please specify elements of the SOC architecture:', 'checkbox', '', 104);
-- Answer options for question 104
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(104, 'SOC process architecture', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(104, 'SOC technology architecture', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(104, 'SOC service architecture', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(104, 'Architecture diagrams', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(104, 'Architecture principles', 0, 5);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(12, 3, 'Operations and Facilities', 'Operations and Facilities aspect of Process domain', 12);

-- Questions for Operations and Facilities
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(105, 12, 'Do you have a documented exercise plan?', 'dropdown', 'An exercise plan lists the type of exercises to be conducted, the frequency and the exercise goals', 105);
-- Answer options for question 105
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(105, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(105, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(105, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(106, 12, 'Please specify types of exercises included in the plan', 'checkbox', '', 106);
-- Answer options for question 106
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(106, 'Table-top exercises', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(106, 'Playbook drills', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(106, 'Cyber range', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(106, 'Capture the flag', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(106, 'Purple/Red/Black team exercises', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(106, 'Public exercises', 0, 6);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(107, 12, 'Do you perform security operations exercises regularly?', 'dropdown', 'Regularity should be matched to your own internal policy', 107);
-- Answer options for question 107
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(107, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(107, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(107, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(108, 12, 'Are the results from exercises documented?', 'dropdown', 'Results from exercises should be structurally documented for future reference and identification of improvements', 108);
-- Answer options for question 108
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(108, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(108, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(108, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(109, 12, 'Is the output from exercises actively used to improve security operations?', 'dropdown', 'Exercise output should be used to structurally improve security operations', 109);
-- Answer options for question 109
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(109, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(109, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(109, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(110, 12, 'Do you have standard operating procedures?', 'dropdown', 'Standard operating procedures are used to provide consistent output', 110);
-- Answer options for question 110
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(110, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(110, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(110, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(111, 12, 'Do you use checklists for recurring activities?', 'dropdown', 'Checklists can be useful to avoid recurring activities from being overlooked', 111);
-- Answer options for question 111
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(111, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(111, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(111, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(112, 12, 'Do you use documented workflows?', 'dropdown', 'Workflows are used to standardize steps in, for example, security analysis', 112);
-- Answer options for question 112
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(112, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(112, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(112, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(113, 12, 'Do you have a SOC operational handbook?', 'dropdown', 'A SOC operational handbook contains an overview of SOC tasks, as well as rules of engagement and expected behavior', 113);
-- Answer options for question 113
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(113, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(113, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(113, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(114, 12, 'Have you established an Operational Security (OPSEC) program?', 'dropdown', 'An OPSEC program dictates security rules to ensure the integrity and confidentiality of SOC processes, tools and information', 114);
-- Answer options for question 114
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(114, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(114, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(114, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(115, 12, 'Is the configuration management process integrated in the SOC?', 'dropdown', 'SOC services and procedures should be aligned and integrated with the organization''s configuration management process', 115);
-- Answer options for question 115
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(115, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(115, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(115, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(116, 12, 'Is the change management process integrated in the SOC?', 'dropdown', 'SOC services and procedures should be aligned and integrated with the organization''s change management process', 116);
-- Answer options for question 116
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(116, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(116, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(116, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(117, 12, 'Is the problem management process integrated in the SOC?', 'dropdown', 'SOC services and procedures should be aligned and integrated with the organization''s problem management process', 117);
-- Answer options for question 117
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(117, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(117, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(117, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(118, 12, 'Is the incident management process integrated in the SOC?', 'dropdown', 'SOC services and procedures should be aligned and integrated with the organization''s incident management process', 118);
-- Answer options for question 118
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(118, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(118, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(118, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(119, 12, 'Is the asset management process integrated in the SOC?', 'dropdown', 'SOC services and procedures should be aligned and integrated with the organization''s asset management process', 119);
-- Answer options for question 119
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(119, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(119, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(119, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(120, 12, 'Do you have a dedicated physical SOC location?', 'dropdown', 'A dedicated physical location decreases likelihood of unauthorized access and provides confidentiality for security incidents', 120);
-- Answer options for question 120
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(120, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(120, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(121, 12, 'Do you have a war room for the SOC?', 'dropdown', 'A dedicated facility for coordination of major security incidents', 121);
-- Answer options for question 121
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(121, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(121, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(122, 12, 'Do you have a dedicated network for the SOC?', 'dropdown', 'Given the confidentiality of the SOC and the importance of monitoring, it is recommended to use a separate network', 122);
-- Answer options for question 122
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(122, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(122, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(123, 12, 'Do you have physical access control to the SOC location?', 'dropdown', 'e.g. key cards (badges) for access with access logging', 123);
-- Answer options for question 123
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(123, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(123, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(124, 12, 'Do you have a secure physical storage location?', 'dropdown', 'Secure storage facilities can be used to store evidence collected during investigations or other operational security purposes', 124);
-- Answer options for question 124
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(124, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(124, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(125, 12, 'Do you have a video wall for monitoring purposes?', 'dropdown', 'A video wall can be used to display the real-time security status and can be used for decision making as well as PR', 125);
-- Answer options for question 125
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(125, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(125, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(126, 12, 'Do you have a call-center capability for the SOC?', 'dropdown', 'Since communication and coordination are important features of a SOC, call-center capability may be required', 126);
-- Answer options for question 126
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(126, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(126, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(127, 12, 'Do you have specialized analyst workstations?', 'dropdown', 'e.g. multiple screen setup, virtual machines, etc.', 127);
-- Answer options for question 127
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(127, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(127, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(128, 12, 'Have you optimized secure remote working capabilities for SOC employees?', 'dropdown', 'Secure working enabled means secure access (MFA, encryption, etc.), secure working facilitated also means equipped and performing', 128);
-- Answer options for question 128
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(128, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(128, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(128, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(129, 12, 'Do you use shift schedules?', 'dropdown', 'Shift schedules are used to ensure full shift coverage', 129);
-- Answer options for question 129
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(129, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(129, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(130, 12, 'Have schedules been created to optimize vigilance during shifts?', 'dropdown', 'Schedules should be created to optimize vigilance. Thus, shift should include mandatory breaks and not be too long', 130);
-- Answer options for question 130
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(130, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(130, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(130, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(131, 12, 'Do you have a shift log?', 'dropdown', 'A shift log covers all exceptions found during the shift, running investigations, etc.', 131);
-- Answer options for question 131
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(131, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(131, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(132, 12, 'Do you have a formally described shift turnover procedure?', 'dropdown', 'i.e. a procedure for handing over a shift and exchanging information regarding running tasks or issues for further follow-up', 132);
-- Answer options for question 132
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(132, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(132, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(132, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(133, 12, 'Do you have a daily SOC operational stand-up?', 'dropdown', 'This can also be a call in case physical attendance is not possible for all attendees', 133);
-- Answer options for question 133
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(133, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(133, 'Yes', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(134, 12, 'Do you have stand-by arrangements with employees within the SOC?', 'dropdown', 'i.e. is there a formal stand-by function that obligates employees to be able to be reached within a certain time?', 134);
-- Answer options for question 134
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(134, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(134, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(134, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(135, 12, 'Do you have a Document Management System in place?', 'dropdown', 'The system should support different file types, authorizations and version management; possibly even encryption', 135);
-- Answer options for question 135
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(135, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(135, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(135, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(136, 12, 'Do you have a knowledge & collaboration platform in place?', 'dropdown', 'e.g. a wiki space or SharePoint that allows collaboration and supports team efforts', 136);
-- Answer options for question 136
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(136, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(136, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(136, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(13, 3, 'Reporting & communication', 'Reporting & communication aspect of Process domain', 13);

-- Questions for Reporting & communication
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(137, 13, 'Do you regularly provide reports?', 'dropdown', 'Regular reports help to keep customers informed of SOC activities', 137);
-- Answer options for question 137
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(137, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(137, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(137, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(138, 13, 'Are these reports tailored to the recipients?', 'dropdown', 'e.g. management reports for senior management, technical reports for the IT organization', 138);
-- Answer options for question 138
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(138, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(138, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(138, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(139, 13, 'Are the report contents approved by or reviewed by the recipients?', 'dropdown', 'formal sign-off can be part of a larger service delivery sign-off', 139);
-- Answer options for question 139
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(139, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(139, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(139, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(140, 13, 'Do you have established reporting lines within the organization?', 'dropdown', 'e.g. reporting lines could be: SOC management, IT management, senior management', 140);
-- Answer options for question 140
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(140, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(140, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(140, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(141, 13, 'Do you regularly revise and update the report templates?', 'dropdown', 'Report templates should be regularly optimized to ensure continued', 141);
-- Answer options for question 141
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(141, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(141, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(141, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(142, 13, 'Do you have formal agreements with the recipients regarding reports?', 'dropdown', 'For example: timelines of delivery, report contents, etc.', 142);
-- Answer options for question 142
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(142, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(142, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(142, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(143, 13, 'Do you provide different types of reports to your recipients?', 'dropdown', 'Different types of reports provide more insight into security operations', 143);
-- Answer options for question 143
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(143, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(143, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(143, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(144, 13, 'Please specify SOC report types:', 'checkbox', '', 144);
-- Answer options for question 144
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(144, 'Technical security reports', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(144, 'Executive security reports', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(144, 'Operational reports', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(144, 'Incident reports', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(144, 'Newsletter or digest', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(144, 'KPI reports', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(144, 'Trend reports', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(144, 'Real-time reporting dashboards', 0, 8);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(145, 13, 'Do you use different types of metrics in your reports?', 'dropdown', 'Different types of metrics provide more insight into security operations', 145);
-- Answer options for question 145
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(145, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(145, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(145, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(146, 13, 'Please specify SOC metric types', 'checkbox', '', 146);
-- Answer options for question 146
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(146, 'Quantitative metrics', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(146, 'Qualitative metrics', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(146, 'Incident & case metrics', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(146, 'Timing metrics', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(146, 'Metrics regarding SLAs', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(146, 'Proactive and reactive metrics', 0, 6);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(147, 13, 'Do you provide advisories to the organization regarding threats and vulnerabilities?', 'dropdown', 'Advisories are used to inform customers of security threats and vulnerabilities', 147);
-- Answer options for question 147
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(147, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(147, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(147, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(148, 13, 'Do you perform risk / impact assessments of these advisories?', 'dropdown', 'i.e. do you add organizational context to these advisories?', 148);
-- Answer options for question 148
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(148, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(148, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(148, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(149, 13, 'Do you perform follow-up of these advisories?', 'dropdown', 'i.e. do you assist in coordination when required?', 149);
-- Answer options for question 149
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(149, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(149, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(149, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(150, 13, 'Do you provide education and security awareness to the organization?', 'dropdown', 'The SOC may be involved in security awareness and education to make users in the organisation aware of their role in cyber security', 150);
-- Answer options for question 150
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(150, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(150, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(150, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(151, 13, 'Do you measure the effect of education and security awareness efforts?', 'dropdown', 'Measuring the efforts is necessary for improvement of the security awareness function', 151);
-- Answer options for question 151
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(151, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(151, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(151, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(152, 13, 'Do you use communication templates?', 'dropdown', 'Communication templates help to standardize and professionalize SOC communication to stakeholders', 152);
-- Answer options for question 152
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(152, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(152, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(152, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(153, 13, 'Do you have a communication matrix in place?', 'dropdown', 'A communication matrix can be used to decide when, how and with whom to communicate', 153);
-- Answer options for question 153
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(153, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(153, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(153, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(154, 13, 'Is communication training (verbal/written) available for SOC personnel?', 'dropdown', 'Communication training helps SOC personnel to communicate effectively', 154);
-- Answer options for question 154
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(154, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(154, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(154, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(155, 13, 'Are communication skills element of SOC role descriptions?', 'dropdown', 'Communication skills are important for analysts to explain their findings and recommendations', 155);
-- Answer options for question 155
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(155, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(155, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(155, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(14, 3, 'Use Case Management', 'Use Case Management aspect of Process domain', 14);

-- Questions for Use Case Management
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(156, 14, 'Is there a use case management process or framework in place?', 'dropdown', 'A framework, such as MaGMa UCF, can be used to guide use case lifecycle and document use case in a standardized format', 156);
-- Answer options for question 156
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(156, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(156, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(156, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(157, 14, 'Are use cases formally documented?', 'dropdown', 'Formal documentation may include use case documentation templates', 157);
-- Answer options for question 157
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(157, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(157, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(157, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(158, 14, 'Are use cases approved by relevant stakeholders?', 'dropdown', 'e.g. business stakeholders, IT stakeholders, CISOs, audit & compliance, risk management, etc.', 158);
-- Answer options for question 158
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(158, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(158, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(158, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(159, 14, 'Is the use case management process aligned with other important processes?', 'dropdown', 'e.g. integration with the threat / risk management process to revise use cases when the threat landscape changes', 159);
-- Answer options for question 159
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(159, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(159, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(159, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(160, 14, 'Are use cases created using a standardized process?', 'dropdown', 'i.e. a standardized approach to derive use cases from threats or business requirements', 160);
-- Answer options for question 160
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(160, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(160, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(160, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(161, 14, 'Are use cases created using a top-down approach?', 'dropdown', 'e.g. use cases can be derived from business requirements, risk assessments, threat management / intelligence', 161);
-- Answer options for question 161
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(161, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(161, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(161, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(162, 14, 'Can use cases be traced from high-level drivers to low-level implementation?', 'dropdown', 'Top-down traceability is important to determine completeness of implementation and demonstrable risk reduction', 162);
-- Answer options for question 162
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(162, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(162, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(162, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(163, 14, 'Can use cases be traced from low-level implementation to high-level drivers?', 'dropdown', 'Bottom-up traceability is important for contextualizing use case output and business alignment', 163);
-- Answer options for question 163
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(163, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(163, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(163, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(164, 14, 'Are use cases measured for implementation and effectiveness?', 'dropdown', 'Metrics can be applied to use cases to determine growth and maturity by measuring effectiveness and implementation', 164);
-- Answer options for question 164
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(164, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(164, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(164, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(165, 14, 'Are use cases scored and prioritized based on risk levels?', 'dropdown', 'Risks can be (cyber)threats, but also non-compliance or penalties (laws & regulations)', 165);
-- Answer options for question 165
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(165, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(165, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(165, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(166, 14, 'Are use cases regularly revised and updated?', 'dropdown', 'Use cases should be subjected to life cycle management and may require updates or may be outdated and decommissioned', 166);
-- Answer options for question 166
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(166, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(166, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(166, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(167, 14, 'Do you measure use cases against the MITRE ATT&CK® framework for gap analysis purposes?', 'dropdown', 'By measuring use cases against MITRE ATT&CK®, it is possible to determine strengths and weaknesses in your layered detection approach', 167);
-- Answer options for question 167
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(167, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(167, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(167, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(168, 14, 'Are monitoring rules tagged with MITRE ATT&CK® framework identifiers?', 'dropdown', 'Tagging monitoring rules with MITRE ATT&CK® identifiers allows for reporting on sightings of attack techniques', 168);
-- Answer options for question 168
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(168, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(168, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(168, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(169, 14, 'Have you created a MITRE ATT&CK® risk profile for your organization?', 'dropdown', 'The creation of a risk profile in MITRE ATT&CK® can help to identify relevant attack techniques', 169);
-- Answer options for question 169
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(169, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(169, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(169, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(170, 14, 'Have you prioritized MITRE ATT&CK® techniques for relevance?', 'dropdown', 'Using organizational context (protection and detection mechanisms), ATT&CK® techniques can be prioritized', 170);
-- Answer options for question 170
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(170, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(170, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(170, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(171, 14, 'Is use case output (alerts) used in threat intelligence activities?', 'dropdown', 'Using MITRE ATT&CK®, it is possible to connect alerts to specific threat actors, or potentially even active campaigns', 171);
-- Answer options for question 171
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(171, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(171, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(171, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(172, 14, 'Is threat intelligence used for the creation and updates of use cases?', 'dropdown', 'Threat intelligence can provide input into security monitoring, especially when using MITRE ATT&CK® to connect both', 172);
-- Answer options for question 172
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(172, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(172, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(172, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(173, 14, 'Do you determine and document visibility requirements for each use case?', 'dropdown', 'Data source requirements should be part of use case design', 173);
-- Answer options for question 173
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(173, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(173, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(173, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(174, 14, 'Do you measure visibility status for your use cases for gap analysis purposes?', 'dropdown', 'Measuring visibility status of use cases will help to identify use cases that require additional data sources for detection optimization', 174);
-- Answer options for question 174
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(174, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(174, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(174, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(175, 14, 'Do you map data source visibility to the MITRE ATT&CK® framework?', 'dropdown', 'Mapping available data sources to MITRE ATT&CK® data source requirements will help identify gaps in visibility of attack techniques', 175);
-- Answer options for question 175
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(175, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(175, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(175, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(15, 3, 'Detection Engineering & Validation', 'Detection Engineering & Validation aspect of Process domain', 15);

-- Questions for Detection Engineering & Validation
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(176, 15, 'Do you have a detection engineering process in place?', 'dropdown', 'A detection engineering process supports the creation and deployment of detection rules for security monitoring purposes', 176);
-- Answer options for question 176
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(176, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(176, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(176, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(177, 15, 'Is the detection engineering process formally documented?', 'dropdown', 'Formal documentation supports process standardisation, and allows for faster training of new engineers', 177);
-- Answer options for question 177
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(177, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(177, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(177, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(178, 15, 'Are there specific roles and requirements for detection engineers?', 'dropdown', 'Detection engineers have a skillset that is different from security analysts and security engineers', 178);
-- Answer options for question 178
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(178, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(178, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(178, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(179, 15, 'Is there active cooperation between the SOC analysts and the detection engineers?', 'dropdown', 'SOC analyst deal with alerts resulting from detections created by engineers, so a tight interaction is required to optimize the ruleset', 179);
-- Answer options for question 179
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(179, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(179, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(179, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(180, 15, 'Is there active cooperation between the Threat Intelligence analysts and detection engineers?', 'dropdown', 'Threat intelligence is a major input into the creation or updating of detection rules', 180);
-- Answer options for question 180
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(180, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(180, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(180, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(181, 15, 'Are there formal hand-over to the analyst team?', 'dropdown', 'Once the detections are created, they must be operationalized. This should be done with a formal hand-over to production', 181);
-- Answer options for question 181
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(181, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(181, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(181, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(182, 15, 'Is there a testing enviroment to test and validate detections before deploying them?', 'dropdown', 'A testing environment allows for thorough testing of new detections, which ensures a higher level of quality', 182);
-- Answer options for question 182
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(182, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(182, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(182, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(183, 15, 'Is there a formal release process in place for new detections?', 'dropdown', 'A formal release process includes automated deployment of rules and adheres to organizational change management procedures', 183);
-- Answer options for question 183
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(183, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(183, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(183, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(184, 15, 'Do you apply a versioning system to detections?', 'dropdown', 'A versioning system will allow to revert back to previous versions of detections', 184);
-- Answer options for question 184
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(184, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(184, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(184, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(185, 15, 'Do you have a roll-back procedure in place in case of problems with detections?', 'dropdown', 'A roll-back procedure enabled reverting back to a good state if a deployment has an adverse effect on security monitoring', 185);
-- Answer options for question 185
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(185, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(185, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(185, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(186, 15, 'Do you perform adversary emulation or automated detection testing?', 'dropdown', 'These validation activities provides insights into how well security monitoring is able to detect certain adversaries or attack techniques', 186);
-- Answer options for question 186
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(186, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(186, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(186, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(187, 15, 'Do you test for detection of MITRE ATT&CK® techniques?', 'dropdown', 'Testing for MITRE ATT&CK® techniques can augment mapping of use cases and visibility in Mitre ATT&CK', 187);
-- Answer options for question 187
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(187, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(187, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(187, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(188, 15, 'Do you test detection analytics not directly associated with MITRE ATT&CK®?', 'dropdown', 'Not all use cases and risks have a relationship to MITRE ATT&CK®. These use cases should be tested as well', 188);
-- Answer options for question 188
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(188, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(188, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(188, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(189, 15, 'Do you test response playbooks?', 'dropdown', 'Testing both detection and response provides a more complete view of SOC capabilities', 189);
-- Answer options for question 189
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(189, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(189, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(189, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(190, 15, 'Is detection validation fully integrated in the detection engineering process / pipeline?', 'dropdown', 'When deploying new or updated detection, automated detection testing should be executed as a quality gate', 190);
-- Answer options for question 190
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(190, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(190, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(190, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(191, 15, 'Is the outcome from detection validation used as input into monitoring and detection engineering?', 'dropdown', 'Output should lead to updates in detections and new detections, as well as instructions for SOC analysts', 191);
-- Answer options for question 191
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(191, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(191, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(191, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(192, 15, 'Do you monitor the data ingestion status for data sources?', 'dropdown', 'Monitoring data ingestion is used to identify data ingestion problems or inactive data sources', 192);
-- Answer options for question 192
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(192, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(192, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(192, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(193, 15, 'Do you actively measure and improve data source coverage?', 'dropdown', 'Data source coverage should be optimized to avoid blind spots in monitoring', 193);
-- Answer options for question 193
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(193, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(193, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(193, 'Yes', 3, 3);

-- Technology domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(16, 4, 'Maturity', 'Maturity aspect of Technology domain', 16);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(194, 16, 'Has functional ownership of the solution been formally assigned?', 'dropdown', 'Functional ownership includes functional accountability', 194);
-- Answer options for question 194
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(194, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(194, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(194, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(195, 16, 'Has technical ownership of the solution been formally assigned?', 'dropdown', 'Technical ownership includes technical accountability', 195);
-- Answer options for question 195
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(195, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(195, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(195, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(196, 16, 'Has the solution been technically documented?', 'dropdown', 'A technical description of the SIEM system components and configuration', 196);
-- Answer options for question 196
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(196, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(196, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(196, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(197, 16, 'Has the solution been functionally documented?', 'dropdown', 'A description of the SIEM functional configuration (rules, filters, lists, etc.)', 197);
-- Answer options for question 197
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(197, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(197, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(197, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(198, 16, 'Is there dedicated personnel for support?', 'dropdown', 'Dedicated personnel should be in place to ensure that support is always available. Can also be staff with outsourced provider', 198);
-- Answer options for question 198
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(198, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(198, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(198, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(199, 16, 'Is the personnel for support formally trained?', 'dropdown', 'Training helps to jump start new hires, and to learn a proper way of working with the tool', 199);
-- Answer options for question 199
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(199, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(199, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(199, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(200, 16, 'Is the personnel for support certified?', 'dropdown', 'Certification demonstrates ability to handle the tooling properly', 200);
-- Answer options for question 200
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(200, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(200, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(200, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(201, 16, 'Is there a support contract for the solution?', 'dropdown', 'A support contract may cover on-site support, support availability, response times, escalation and full access to resources', 201);
-- Answer options for question 201
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(201, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(201, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(201, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(202, 16, 'Is the system regularly maintained?', 'dropdown', 'Systems should be regularly maintained to keep up with the latest features and bug fixes', 202);
-- Answer options for question 202
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(202, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(202, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(202, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(203, 16, 'Is remote maintenance on the system managed?', 'dropdown', 'Remote maintenance by a third party may be part of system maintenance procedures', 203);
-- Answer options for question 203
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(203, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(203, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(203, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(204, 16, 'Are maintenance & configuration updates executed through the change management process?', 'dropdown', 'Maintenance and configuration updates should follow the formal change management process', 204);
-- Answer options for question 204
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(204, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(204, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(204, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(205, 16, 'Have you established maintenance windows?', 'dropdown', 'Setting maintenance windows helps to structure the maintenance process and make it more predictable', 205);
-- Answer options for question 205
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(205, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(205, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(205, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(206, 16, 'Is maintenance performed using authorised and trusted tooling?', 'dropdown', 'Performing maintenance with authorised and trusted tooling helps to ensure security and integrity of the system', 206);
-- Answer options for question 206
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(206, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(206, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(206, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(207, 16, 'Is there high availability (HA) in place for the solution?', 'dropdown', 'Can be fully implemented HA, partially implemented, hot spare, etc.', 207);
-- Answer options for question 207
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(207, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(207, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(207, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(208, 16, 'Is there data backup / replication in place for the solution?', 'dropdown', 'May not be feasible for all SIEM solutions', 208);
-- Answer options for question 208
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(208, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(208, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(208, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(209, 16, 'Is there configuration backup / replication in place for the solution?', 'dropdown', 'Configuration synchronization could be part of a HA setup', 209);
-- Answer options for question 209
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(209, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(209, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(209, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(210, 16, 'Is there a Disaster Recovery plan in place for this solution?', 'dropdown', 'A DR plan is required to restore service in case of catastrophic events', 210);
-- Answer options for question 210
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(210, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(210, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(210, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(211, 16, 'Is the Disaster Recovery plan regularly tested?', 'dropdown', 'Testing the DR plan is required to ensure that it is complete, functional and tasks and responsibilities for involved personnel are understood', 211);
-- Answer options for question 211
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(211, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(211, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(211, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(212, 16, 'Is there a separate development / test environment for this solution?', 'dropdown', 'A separate test environment allows for testing of new configurations before deployment in production', 212);
-- Answer options for question 212
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(212, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(212, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(212, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(213, 16, 'Is access to the solution limited to authorized personnel?', 'dropdown', 'The system will contain confidential information and information that possibly impacts employee privacy', 213);
-- Answer options for question 213
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(213, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(213, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(213, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(214, 16, 'Are access rights regularly reviewed and revoked if required?', 'dropdown', 'Revocation is part of normal employee termination. Special emergency revocation should be in place for suspected misuse', 214);
-- Answer options for question 214
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(214, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(214, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(214, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(215, 16, 'Is a break glass procedure in place?', 'dropdown', 'A break glass procedure and account is required to gain access to the tooling even in case of major IT outages', 215);
-- Answer options for question 215
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(215, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(215, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(215, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(17, 4, 'Maturity', 'Maturity aspect of Technology domain', 17);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(216, 17, 'Has functional ownership of the solution been formally assigned?', 'dropdown', 'Functional ownership includes functional accountability', 216);
-- Answer options for question 216
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(216, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(216, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(216, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(217, 17, 'Has technical ownership of the solution been formally assigned?', 'dropdown', 'Technical ownership includes technical accountability', 217);
-- Answer options for question 217
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(217, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(217, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(217, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(218, 17, 'Has the solution been technically documented?', 'dropdown', 'A technical description of the NDR system components and configuration', 218);
-- Answer options for question 218
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(218, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(218, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(218, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(219, 17, 'Has the solution been functionally documented?', 'dropdown', 'A description of the NDR functional configuration (rules, alerts, thresholds, etc.)', 219);
-- Answer options for question 219
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(219, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(219, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(219, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(220, 17, 'Is there dedicated personnel for support?', 'dropdown', 'Dedicated personnel should be in place to ensure that support is always available. Can also be staff with outsourced provider', 220);
-- Answer options for question 220
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(220, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(220, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(220, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(221, 17, 'Is the personnel for support formally trained?', 'dropdown', 'Training helps to jump start new hires, and to learn a proper way of working with the tool', 221);
-- Answer options for question 221
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(221, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(221, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(221, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(222, 17, 'Is the personnel for support certified?', 'dropdown', 'Certification demonstrates ability to handle the tooling properly', 222);
-- Answer options for question 222
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(222, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(222, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(222, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(223, 17, 'Is there a support contract for the solution?', 'dropdown', 'A support contract may cover on-site support, support availability, response times, escalation and full access to resources', 223);
-- Answer options for question 223
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(223, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(223, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(223, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(224, 17, 'Is the system regularly maintained?', 'dropdown', 'Systems should be regularly maintained to keep up with the latest features and bug fixes', 224);
-- Answer options for question 224
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(224, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(224, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(224, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(225, 17, 'Is remote maintenance on the system managed?', 'dropdown', 'Remote maintenance by a third party may be part of system maintenance procedures', 225);
-- Answer options for question 225
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(225, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(225, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(225, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(226, 17, 'Are maintenance & configuration updates executed through the change management process?', 'dropdown', 'Maintenance and configuration updates should follow the formal change management process', 226);
-- Answer options for question 226
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(226, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(226, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(226, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(227, 17, 'Have you established maintenance windows?', 'dropdown', 'Setting maintenance windows helps to structure the maintenance process and make it more predictable', 227);
-- Answer options for question 227
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(227, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(227, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(227, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(228, 17, 'Is maintenance performed using authorised and trusted tooling?', 'dropdown', 'Performing maintenance with authorised and trusted tooling helps to ensure security and integrity of the system', 228);
-- Answer options for question 228
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(228, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(228, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(228, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(229, 17, 'Is there high availability (HA) in place for the solution?', 'dropdown', 'Can be fully implemented HA, partially implemented, hot spare, etc.', 229);
-- Answer options for question 229
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(229, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(229, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(229, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(230, 17, 'Is there data backup / replication in place for the solution?', 'dropdown', 'Data may include logs and PCAP files', 230);
-- Answer options for question 230
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(230, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(230, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(230, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(231, 17, 'Is there configuration backup / replication in place for the solution?', 'dropdown', 'Configuration synchronization could be part of a HA setup', 231);
-- Answer options for question 231
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(231, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(231, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(231, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(232, 17, 'Is there a Disaster Recovery plan in place for this solution?', 'dropdown', 'A DR plan is required to restore service in case of catastrophic events', 232);
-- Answer options for question 232
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(232, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(232, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(232, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(233, 17, 'Is the Disaster Recovery plan regularly tested?', 'dropdown', 'Testing the DR plan is required to ensure that it is complete, functional and tasks and responsibilities for involved personnel are understood', 233);
-- Answer options for question 233
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(233, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(233, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(233, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(234, 17, 'Is there a separate development / test environment for this solution?', 'dropdown', 'A separate test environment allows for testing of new configurations before deployment in production', 234);
-- Answer options for question 234
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(234, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(234, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(234, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(235, 17, 'Is access to the solution limited to authorized personnel?', 'dropdown', 'The IDPS system will contain confidential information and possibly information that impacts employee privacy', 235);
-- Answer options for question 235
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(235, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(235, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(235, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(236, 17, 'Are access rights regularly reviewed and revoked if required?', 'dropdown', 'Revocation is part of normal employee termination. Special emergency revocation should be in place for suspected misuse', 236);
-- Answer options for question 236
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(236, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(236, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(236, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(237, 17, 'Is a break glass procedure in place?', 'dropdown', 'A break glass procedure and account is required to gain access to the tooling even in case of major IT outages', 237);
-- Answer options for question 237
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(237, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(237, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(237, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(18, 4, 'Maturity', 'Maturity aspect of Technology domain', 18);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(238, 18, 'Has functional ownership of the solution been formally assigned?', 'dropdown', 'Functional ownership includes functional accountability', 238);
-- Answer options for question 238
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(238, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(238, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(238, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(239, 18, 'Has technical ownership of the solution been formally assigned?', 'dropdown', 'Technical ownership includes technical accountability', 239);
-- Answer options for question 239
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(239, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(239, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(239, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(240, 18, 'Has the solution been technically documented?', 'dropdown', 'A technical description of the security analytics system components and configuration', 240);
-- Answer options for question 240
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(240, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(240, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(240, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(241, 18, 'Has the solution been functionally documented?', 'dropdown', 'A description of the EDR functional configuration (rules, alerts, thresholds, etc.)', 241);
-- Answer options for question 241
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(241, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(241, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(241, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(242, 18, 'Is there dedicated personnel for support?', 'dropdown', 'Dedicated personnel should be in place to ensure that support is always available. Can also be staff with outsourced provider', 242);
-- Answer options for question 242
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(242, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(242, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(242, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(243, 18, 'Is the personnel for support formally trained?', 'dropdown', 'Training helps to jump start new hires, and to learn a proper way of working with the tool', 243);
-- Answer options for question 243
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(243, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(243, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(243, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(244, 18, 'Is the personnel for support certified?', 'dropdown', 'Certification demonstrates ability to handle the tooling properly', 244);
-- Answer options for question 244
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(244, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(244, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(244, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(245, 18, 'Is there a support contract for the solution?', 'dropdown', 'A support contract may cover on-site support, support availability, response times, escalation and full access to resources', 245);
-- Answer options for question 245
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(245, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(245, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(245, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(246, 18, 'Is the system regularly maintained?', 'dropdown', 'Systems should be regularly maintained to keep up with the latest features and bug fixes', 246);
-- Answer options for question 246
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(246, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(246, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(246, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(247, 18, 'Is remote maintenance on the system managed?', 'dropdown', 'Remote maintenance by a third party may be part of system maintenance procedures', 247);
-- Answer options for question 247
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(247, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(247, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(247, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(248, 18, 'Are maintenance & configuration updates executed through the change management process?', 'dropdown', 'Maintenance and configuration updates should follow the formal change management process', 248);
-- Answer options for question 248
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(248, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(248, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(248, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(249, 18, 'Have you established maintenance windows?', 'dropdown', 'Setting maintenance windows helps to structure the maintenance process and make it more predictable', 249);
-- Answer options for question 249
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(249, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(249, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(249, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(250, 18, 'Is maintenance performed using authorised and trusted tooling?', 'dropdown', 'Performing maintenance with authorised and trusted tooling helps to ensure security and integrity of the system', 250);
-- Answer options for question 250
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(250, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(250, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(250, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(251, 18, 'Is there high availability (HA) in place for the solution?', 'dropdown', 'Can be fully implemented HA, partially implemented, hot spare, etc. May not be applicable', 251);
-- Answer options for question 251
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(251, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(251, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(251, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(252, 18, 'Is there data backup / replication in place for the solution?', 'dropdown', 'May not be applicable to all EDR solutions', 252);
-- Answer options for question 252
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(252, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(252, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(252, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(253, 18, 'Is there configuration backup / replication in place for the solution?', 'dropdown', 'Configuration synchronization could be part of a HA setup', 253);
-- Answer options for question 253
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(253, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(253, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(253, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(254, 18, 'Is there a Disaster Recovery plan in place for this solution?', 'dropdown', 'A DR plan is required to restore service in case of catastrophic events', 254);
-- Answer options for question 254
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(254, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(254, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(254, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(255, 18, 'Is the Disaster Recovery plan regularly tested?', 'dropdown', 'Testing the DR plan is required to ensure that it is complete, functional and tasks and responsibilities for involved personnel are understood', 255);
-- Answer options for question 255
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(255, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(255, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(255, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(256, 18, 'Is there a separate development / test environment for this solution?', 'dropdown', 'A separate test environment allows for testing of new configurations before deployment in production', 256);
-- Answer options for question 256
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(256, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(256, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(256, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(257, 18, 'Is access to the solution limited to authorized personnel?', 'dropdown', 'The analytics system will contain confidential information and information that possibly impacts employee privacy', 257);
-- Answer options for question 257
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(257, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(257, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(257, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(258, 18, 'Are access rights regularly reviewed and revoked if required?', 'dropdown', 'Revocation is part of normal employee termination. Special emergency revocation should be in place for suspected misuse', 258);
-- Answer options for question 258
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(258, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(258, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(258, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(259, 18, 'Is a break glass procedure in place?', 'dropdown', 'A break glass procedure and account is required to gain access to the tooling even in case of major IT outages', 259);
-- Answer options for question 259
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(259, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(259, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(259, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(19, 4, 'Maturity', 'Maturity aspect of Technology domain', 19);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(260, 19, 'Has functional ownership of the solution been formally assigned?', 'dropdown', 'Functional ownership includes functional accountability', 260);
-- Answer options for question 260
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(260, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(260, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(260, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(261, 19, 'Has technical ownership of the solution been formally assigned?', 'dropdown', 'Technical ownership includes technical accountability', 261);
-- Answer options for question 261
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(261, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(261, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(261, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(262, 19, 'Has the solution been technically documented?', 'dropdown', 'A technical description of the automation & orchestration system components and configuration', 262);
-- Answer options for question 262
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(262, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(262, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(262, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(263, 19, 'Has the solution been functionally documented?', 'dropdown', 'A description of the automation & orchestration system functional configuration (workflows, integrations, etc.)', 263);
-- Answer options for question 263
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(263, 'Not documented', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(263, 'Partially documented', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(263, 'Fully documented', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(264, 19, 'Is there dedicated personnel for support?', 'dropdown', 'Dedicated personnel should be in place to ensure that support is always available. Can also be staff with outsourced provider', 264);
-- Answer options for question 264
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(264, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(264, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(264, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(265, 19, 'Is the personnel for support formally trained?', 'dropdown', 'Training helps to jump start new hires, and to learn a proper way of working with the tool', 265);
-- Answer options for question 265
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(265, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(265, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(265, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(266, 19, 'Is the personnel for support certified?', 'dropdown', 'Certification demonstrates ability to handle the tooling properly', 266);
-- Answer options for question 266
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(266, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(266, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(266, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(267, 19, 'Is there a support contract for the solution?', 'dropdown', 'A support contract may cover on-site support, support availability, response times, escalation and full access to resources', 267);
-- Answer options for question 267
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(267, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(267, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(267, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(268, 19, 'Is the system regularly maintained?', 'dropdown', 'Systems should be regularly maintained to keep up with the latest features and bug fixes', 268);
-- Answer options for question 268
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(268, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(268, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(268, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(269, 19, 'Is remote maintenance on the system managed?', 'dropdown', 'Remote maintenance by a third party may be part of system maintenance procedures', 269);
-- Answer options for question 269
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(269, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(269, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(269, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(270, 19, 'Are maintenance & configuration updates executed through the change management process?', 'dropdown', 'Maintenance and configuration updates should follow the formal change management process', 270);
-- Answer options for question 270
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(270, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(270, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(270, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(271, 19, 'Have you established maintenance windows?', 'dropdown', 'Setting maintenance windows helps to structure the maintenance process and make it more predictable', 271);
-- Answer options for question 271
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(271, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(271, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(271, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(272, 19, 'Is maintenance performed using authorised and trusted tooling?', 'dropdown', 'Performing maintenance with authorised and trusted tooling helps to ensure security and integrity of the system', 272);
-- Answer options for question 272
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(272, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(272, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(272, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(273, 19, 'Is there high availability (HA) in place for the solution?', 'dropdown', 'Can be fully implemented HA, partially implemented, hot spare, etc.', 273);
-- Answer options for question 273
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(273, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(273, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(273, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(274, 19, 'Is there data backup / replication in place for the solution?', 'dropdown', 'May not be required for this particular solution', 274);
-- Answer options for question 274
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(274, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(274, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(274, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(275, 19, 'Is there configuration backup / replication in place for the solution?', 'dropdown', 'Configuration synchronization could be part of a HA setup', 275);
-- Answer options for question 275
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(275, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(275, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(275, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(276, 19, 'Is there a Disaster Recovery plan in place for this solution?', 'dropdown', 'A DR plan is required to restore service in case of catastrophic events', 276);
-- Answer options for question 276
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(276, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(276, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(276, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(277, 19, 'Is the Disaster Recovery plan regularly tested?', 'dropdown', 'Testing the DR plan is required to ensure that it is complete, functional and tasks and responsibilities for involved personnel are understood', 277);
-- Answer options for question 277
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(277, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(277, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(277, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(278, 19, 'Is there a separate development / test environment for this solution?', 'dropdown', 'A separate test environment allows for testing of new configurations before deployment in production', 278);
-- Answer options for question 278
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(278, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(278, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(278, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(279, 19, 'Is access to the solution limited to authorized personnel?', 'dropdown', 'The automation system may have automated actions that can impact the usage of systems and should be restricted', 279);
-- Answer options for question 279
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(279, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(279, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(279, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(280, 19, 'Are access rights regularly reviewed and revoked if required?', 'dropdown', 'Revocation is part of normal employee termination. Special emergency revocation should be in place for suspected misuse', 280);
-- Answer options for question 280
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(280, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(280, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(280, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(281, 19, 'Is a break glass procedure in place?', 'dropdown', 'A break glass procedure and account is required to gain access to the tooling even in case of major IT outages', 281);
-- Answer options for question 281
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(281, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(281, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(281, 'Yes', 3, 3);

-- Services domain aspects
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(20, 5, 'Maturity', 'Maturity aspect of Services domain', 20);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(282, 20, 'Have you formally described the security monitoring service?', 'dropdown', 'A service description should be in place', 282);
-- Answer options for question 282
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(282, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(282, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(282, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(283, 20, 'Please specify elements of the security monitoring service document:', 'checkbox', '', 283);
-- Answer options for question 283
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Key performance indicators', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Quality indicators', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Service dependencies', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Service levels', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Hours of operation', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Service customers and stakeholders', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Purpose', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Service input / triggers', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Service output / deliverables', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Service activities', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(283, 'Service roles & responsibilities', 0, 11);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(284, 20, 'Is the service measured for quality?', 'dropdown', 'Are the quality indicators from the previous questions used for reporting on the service?', 284);
-- Answer options for question 284
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(284, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(284, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(284, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(285, 20, 'Is the service measured for service delivery in accordance with service levels?', 'dropdown', 'Service levels should be used to formally commit the SOC to service delivery', 285);
-- Answer options for question 285
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(285, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(285, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(285, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(286, 20, 'Are customers and/or stakeholders regularly updated about the service?', 'dropdown', 'Changes to the service scope, delivery, etc.', 286);
-- Answer options for question 286
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(286, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(286, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(286, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(287, 20, 'Is there a contractual agreement between the SOC and the customers?', 'dropdown', 'Contractual agreements should also cover penalties', 287);
-- Answer options for question 287
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(287, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(287, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(287, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(288, 20, 'Is sufficient personnel allocated to the process to ensure required service delivery?', 'dropdown', 'Allocation of dedicated personnel will ensure highest service quality', 288);
-- Answer options for question 288
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(288, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(288, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(288, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(289, 20, 'Is the service aligned with other relevant processes?', 'dropdown', 'e.g. alignment with configuration management, incident management, etc.', 289);
-- Answer options for question 289
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(289, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(289, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(289, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(290, 20, 'Is there a incident resolution / service continuity process in place for this service?', 'dropdown', 'Service continuity is important to comply with contractual agreements, even in case of major incidents', 290);
-- Answer options for question 290
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(290, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(290, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(290, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(291, 20, 'Has a set of procedures been created for this service?', 'dropdown', 'Procedures support process standardization and quality. Personnel should be trained to use procedures correctly and structurally', 291);
-- Answer options for question 291
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(291, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(291, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(291, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(292, 20, 'Is there an onboarding and offloading procedure for this service?', 'dropdown', 'Customer onboarding and offloading procedures support efficient service delivery and ensure customers are (dis)connected properly', 292);
-- Answer options for question 292
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(292, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(292, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(292, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(293, 20, 'Are best practices applied to the service?', 'dropdown', 'Best practices should be used to optimize this service', 293);
-- Answer options for question 293
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(293, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(293, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(293, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(294, 20, 'Are use cases used in the security monitoring service?', 'dropdown', 'e.g. user login brute-force, denial of service, non-compliance, etc.', 294);
-- Answer options for question 294
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(294, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(294, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(294, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(295, 20, 'Is process data gathered for prediction of service performance?', 'dropdown', 'Service performance measurement requires establishment of performance goals', 295);
-- Answer options for question 295
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(295, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(295, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(295, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(296, 20, 'Is the service continuously being improved based on improvement goals?', 'dropdown', 'Improvement based on based evaluation, (maturity) assessment, tests, etc.', 296);
-- Answer options for question 296
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(296, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(296, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(296, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(21, 5, 'Capability', 'Capability aspect of Services domain', 21);

-- Questions for Capability
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(297, 21, 'Early detection', 'checkbox', '', 297);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(298, 21, 'Intrusion detection', 'checkbox', '', 298);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(299, 21, 'Exfiltration detection', 'checkbox', '', 299);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(300, 21, 'Subtle event detection', 'checkbox', '', 300);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(301, 21, 'Malware detection', 'checkbox', '', 301);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(302, 21, 'Anomaly detection', 'checkbox', '', 302);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(303, 21, 'Real-time detection', 'checkbox', '', 303);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(304, 21, 'Alerting & notification', 'checkbox', '', 304);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(305, 21, 'False-positive reduction', 'checkbox', '', 305);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(306, 21, 'Continuous tuning', 'checkbox', '', 306);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(307, 21, 'Coverage management', 'checkbox', '', 307);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(308, 21, 'Status monitoring', 'checkbox', '', 308);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(309, 21, 'Perimeter monitoring', 'checkbox', '', 309);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(310, 21, 'Host monitoring', 'checkbox', '', 310);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(311, 21, 'Network & traffic monitoring', 'checkbox', '', 311);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(312, 21, 'Access & usage monitoring', 'checkbox', '', 312);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(313, 21, 'User / identity monitoring', 'checkbox', '', 313);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(314, 21, 'Application & service monitoring', 'checkbox', '', 314);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(315, 21, 'Behavior monitoring', 'checkbox', '', 315);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(316, 21, 'Database monitoring', 'checkbox', '', 316);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(317, 21, 'Data loss monitoring', 'checkbox', '', 317);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(318, 21, 'Device loss / theft monitoring', 'checkbox', '', 318);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(319, 21, 'Third-party monitoring', 'checkbox', '', 319);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(320, 21, 'Physical environment monitoring', 'checkbox', '', 320);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(321, 21, 'Cloud monitoring', 'checkbox', '', 321);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(322, 21, 'Mobile device monitoring', 'checkbox', '', 322);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(323, 21, 'OT monitoring', 'checkbox', '', 323);
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(22, 5, 'Maturity', 'Maturity aspect of Services domain', 22);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(324, 22, 'Have you adopted a maturity assessment methodology for Security Incident Management?', 'dropdown', '', 324);
-- Answer options for question 324
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(324, 'Yes', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(324, 'No', 2, 2);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(325, 22, 'If yes, please specify the methodology', 'text', 'e.g., SOC-CMM 4CERT, SIM3, CREST, etc.', 325);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(326, 22, 'If yes, please specify the maturity level (can have up to 2 digits)', 'numeric', 'Please convert to a 5-point scale if required. For example: 3.6 on a 4-point scale = 4.5 on a 5-point scale', 326);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(327, 22, 'Have you adopted a standard for the Security Incident Management process?', 'dropdown', 'e.g. NIST 800-62r1, CERT handbook, etc.', 327);
-- Answer options for question 327
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(327, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(327, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(327, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(328, 22, 'Have you formally described the security incident management process?', 'dropdown', 'A service description should be in place', 328);
-- Answer options for question 328
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(328, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(328, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(328, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(329, 22, 'Please specify elements of the security incident management document:', 'checkbox', '', 329);
-- Answer options for question 329
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Security incident definition', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Service levels', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Workflow', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Decision tree', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Hours of operation', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Service customers and stakeholders', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Purpose', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Service input / triggers', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Service output / deliverables', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Service activities', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(329, 'Service roles & responsibilities', 0, 11);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(330, 22, 'Is the service measured for quality?', 'dropdown', 'Are the quality indicators from the previous questions used for reporting on the service?', 330);
-- Answer options for question 330
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(330, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(330, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(330, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(331, 22, 'Is the service measured for service delivery in accordance with service levels?', 'dropdown', 'Service levels should be used to formally commit the SOC to service delivery', 331);
-- Answer options for question 331
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(331, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(331, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(331, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(332, 22, 'Are customers and/or stakeholders regularly updated about the service?', 'dropdown', 'Changes to the service scope, delivery, etc.', 332);
-- Answer options for question 332
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(332, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(332, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(332, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(333, 22, 'Is there a contractual agreement between the SOC and the customers?', 'dropdown', 'Contractual agreements should also cover penalties', 333);
-- Answer options for question 333
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(333, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(333, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(333, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(334, 22, 'Is sufficient personnel allocated to the process to ensure required service delivery?', 'dropdown', 'Allocation of dedicated personnel will ensure highest service quality', 334);
-- Answer options for question 334
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(334, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(334, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(334, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(335, 22, 'Is the service aligned with other relevant processes?', 'dropdown', 'e.g. alignment with configuration management, incident management, etc.', 335);
-- Answer options for question 335
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(335, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(335, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(335, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(336, 22, 'Is the incident response team authorized to perform (invasive) actions when required?', 'dropdown', 'This is a mandate issue. The team should have mandate beforehand to optimize incident response times', 336);
-- Answer options for question 336
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(336, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(336, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(336, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(337, 22, 'Is there an onboarding and offloading procedure for this service?', 'dropdown', 'Customer onboarding and offloading procedures support efficient service delivery and ensure customers are (dis)connected properly', 337);
-- Answer options for question 337
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(337, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(337, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(337, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(338, 22, 'Are best practices applied to the service?', 'dropdown', 'Best practices should be used to optimize this service', 338);
-- Answer options for question 338
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(338, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(338, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(338, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(339, 22, 'Is the service supported by predefined workflows or scenarios?', 'dropdown', 'Workflows and scenario''s can be used to structure follow-up and determine expected incident progression', 339);
-- Answer options for question 339
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(339, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(339, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(339, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(340, 22, 'Is process data gathered for prediction of service performance?', 'dropdown', 'Service performance measurement requires establishment of performance goals', 340);
-- Answer options for question 340
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(340, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(340, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(340, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(341, 22, 'Is the service continuously being improved based on improvement goals?', 'dropdown', 'Improvement based on based evaluation, (maturity) assessment, tests, etc.', 341);
-- Answer options for question 341
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(341, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(341, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(341, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(23, 5, 'Capability', 'Capability aspect of Services domain', 23);

-- Questions for Capability
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(342, 23, 'Incident logging procedure', 'checkbox', '', 342);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(343, 23, 'Incident resolution procedure', 'checkbox', '', 343);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(344, 23, 'Incident investigation procedure', 'checkbox', '', 344);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(345, 23, 'Escalation procedure', 'checkbox', '', 345);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(346, 23, 'Evidence collection procedure', 'checkbox', '', 346);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(347, 23, 'Incident containment procedures', 'checkbox', '', 347);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(348, 23, 'IR Training', 'checkbox', '', 348);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(349, 23, 'Table-top exercises', 'checkbox', '', 349);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(350, 23, 'Red team / blue team exercises', 'checkbox', '', 350);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(351, 23, 'RACI matrix', 'checkbox', '', 351);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(352, 23, 'Response authorization', 'checkbox', '', 352);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(353, 23, 'Incident template', 'checkbox', '', 353);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(354, 23, 'Incident tracking system', 'checkbox', '', 354);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(355, 23, 'False-positive reduction', 'checkbox', '', 355);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(356, 23, 'Priority assignment', 'checkbox', '', 356);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(357, 23, 'Severity assignment', 'checkbox', '', 357);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(358, 23, 'Categorization', 'checkbox', '', 358);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(359, 23, 'Critical bridge', 'checkbox', '', 359);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(360, 23, 'War room', 'checkbox', '', 360);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(361, 23, 'Communication plan & email templates', 'checkbox', '', 361);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(362, 23, 'Backup communication technology', 'checkbox', '', 362);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(363, 23, 'Secure communication channels', 'checkbox', '', 363);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(364, 23, '(dedicated) information sharing platform', 'checkbox', '', 364);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(365, 23, 'Change management integration', 'checkbox', '', 365);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(366, 23, 'Malware extraction & analysis', 'checkbox', '', 366);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(367, 23, 'On-site incident response', 'checkbox', '', 367);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(368, 23, 'Remote incident response', 'checkbox', '', 368);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(369, 23, 'Third-party escalation', 'checkbox', '', 369);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(370, 23, 'Evaluation template', 'checkbox', '', 370);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(371, 23, 'Reporting template', 'checkbox', '', 371);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(372, 23, 'Incident closure', 'checkbox', '', 372);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(373, 23, 'Lessons learned extraction for process improvement', 'checkbox', '', 373);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(374, 23, 'External security incident support agreements', 'checkbox', '', 374);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(375, 23, 'Exercises with other incident response teams', 'checkbox', '', 375);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(376, 23, 'Root Cause Analysis', 'checkbox', '', 376);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(377, 23, 'Restore integrity verification', 'checkbox', '', 377);
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(24, 5, 'Maturity', 'Maturity aspect of Services domain', 24);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(378, 24, 'Have you formally described the security analysis & forensics service?', 'dropdown', 'A service description should be in place', 378);
-- Answer options for question 378
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(378, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(378, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(378, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(379, 24, 'Please specify elements of the security analysis service document:', 'checkbox', '', 379);
-- Answer options for question 379
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Key performance indicators', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Quality indicators', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Service dependencies', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Service levels', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Hours of operation', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Service customers and stakeholders', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Purpose', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Service input / triggers', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Service output / deliverables', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Service activities', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(379, 'Service roles & responsibilities', 0, 11);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(380, 24, 'Is the service measured for quality?', 'dropdown', 'Are the quality indicators from the previous questions used for reporting on the service?', 380);
-- Answer options for question 380
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(380, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(380, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(380, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(381, 24, 'Is the service measured for service delivery in accordance with service levels?', 'dropdown', 'Service levels should be used to formally commit the SOC to service delivery', 381);
-- Answer options for question 381
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(381, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(381, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(381, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(382, 24, 'Are customers and/or stakeholders regularly updated about the service?', 'dropdown', 'Changes to the service scope, delivery, etc.', 382);
-- Answer options for question 382
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(382, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(382, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(382, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(383, 24, 'Is there a contractual agreement between the SOC and the customers?', 'dropdown', 'Contractual agreements should also cover penalties', 383);
-- Answer options for question 383
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(383, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(383, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(383, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(384, 24, 'Is sufficient personnel allocated to the process to ensure required service delivery?', 'dropdown', 'Allocation of dedicated personnel will ensure highest service quality', 384);
-- Answer options for question 384
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(384, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(384, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(384, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(385, 24, 'Is the service aligned with other relevant processes?', 'dropdown', 'e.g. alignment with configuration management, incident management, etc.', 385);
-- Answer options for question 385
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(385, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(385, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(385, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(386, 24, 'Is there a incident resolution / service continuity process in place for this service?', 'dropdown', 'Service continuity is important to comply with contractual agreements, even in case of major incidents', 386);
-- Answer options for question 386
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(386, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(386, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(386, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(387, 24, 'Has a set of procedures been created for this service?', 'dropdown', 'Procedures support process standardization and quality. Personnel should be trained to use procedures correctly and structurally', 387);
-- Answer options for question 387
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(387, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(387, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(387, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(388, 24, 'Is there an onboarding and offloading procedure for this service?', 'dropdown', 'Customer onboarding and offloading procedures support efficient service delivery and ensure customers are (dis)connected properly', 388);
-- Answer options for question 388
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(388, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(388, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(388, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(389, 24, 'Are best practices applied to the service?', 'dropdown', 'Best practices should be used to optimize this service', 389);
-- Answer options for question 389
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(389, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(389, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(389, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(390, 24, 'Is the service supported by predefined workflows or scenarios?', 'dropdown', 'Use cases can be used to guide the analysis workflows', 390);
-- Answer options for question 390
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(390, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(390, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(390, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(391, 24, 'Is process data gathered for prediction of service performance?', 'dropdown', 'Service performance measurement requires establishment of performance goals', 391);
-- Answer options for question 391
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(391, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(391, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(391, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(392, 24, 'Is the service continuously being improved based on improvement goals?', 'dropdown', 'Improvement based on based evaluation, (maturity) assessment, tests, etc.', 392);
-- Answer options for question 392
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(392, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(392, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(392, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(25, 5, 'Capability', 'Capability aspect of Services domain', 25);

-- Questions for Capability
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(393, 25, 'Event analysis', 'checkbox', '', 393);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(394, 25, 'Event analysis toolkit', 'checkbox', '', 394);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(395, 25, 'Trend analysis', 'checkbox', '', 395);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(396, 25, 'Incident analysis', 'checkbox', '', 396);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(397, 25, 'Visual analysis', 'checkbox', '', 397);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(398, 25, 'Static malware analysis', 'checkbox', '', 398);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(399, 25, 'Dynamic malware analysis', 'checkbox', '', 399);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(400, 25, 'Tradecraft analysis', 'checkbox', '', 400);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(401, 25, 'Historic analysis', 'checkbox', '', 401);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(402, 25, 'Network analysis', 'checkbox', '', 402);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(403, 25, 'Memory analysis', 'checkbox', '', 403);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(404, 25, 'Mobile device analysis', 'checkbox', '', 404);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(405, 25, 'Volatile information collection', 'checkbox', '', 405);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(406, 25, 'Remote evidence collection', 'checkbox', '', 406);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(407, 25, 'Forensic hardware toolkit', 'checkbox', '', 407);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(408, 25, 'Forensic analysis software toolkit', 'checkbox', '', 408);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(409, 25, 'Dedicated analysis workstations', 'checkbox', '', 409);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(410, 25, 'Security analysis & forensics handbook', 'checkbox', '', 410);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(411, 25, 'Security analysis & forensics workflows', 'checkbox', '', 411);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(412, 25, 'Case management system', 'checkbox', '', 412);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(413, 25, 'Report templates', 'checkbox', '', 413);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(414, 25, 'Evidence seizure procedure', 'checkbox', '', 414);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(415, 25, 'Evidence transport procedure', 'checkbox', '', 415);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(416, 25, 'Chain of custody preservation procedure', 'checkbox', '', 416);
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(26, 5, 'Maturity', 'Maturity aspect of Services domain', 26);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(417, 26, 'Have you formally described the threat intelligence service?', 'dropdown', 'A service description should be in place', 417);
-- Answer options for question 417
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(417, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(417, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(417, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(418, 26, 'Please specify elements of the threat intelligence service document:', 'checkbox', '', 418);
-- Answer options for question 418
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Key performance indicators', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Quality indicators', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Service dependencies', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Service levels', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Hours of operation', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Service customers and stakeholders', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Purpose', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Service input / triggers', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Service output / deliverables', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Service activities', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(418, 'Service roles & responsibilities', 0, 11);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(419, 26, 'Is the service measured for quality?', 'dropdown', 'Are the quality indicators from the previous questions used for reporting on the service?', 419);
-- Answer options for question 419
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(419, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(419, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(419, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(420, 26, 'Is the service measured for service delivery in accordance with service levels?', 'dropdown', 'Service levels should be used to formally commit the SOC to service delivery', 420);
-- Answer options for question 420
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(420, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(420, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(420, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(421, 26, 'Are customers and/or stakeholders regularly updated about the service?', 'dropdown', 'Changes to the service scope, delivery, etc.', 421);
-- Answer options for question 421
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(421, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(421, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(421, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(422, 26, 'Is there a contractual agreement between the SOC and the customers?', 'dropdown', 'Contractual agreements should also cover penalties', 422);
-- Answer options for question 422
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(422, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(422, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(422, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(423, 26, 'Is sufficient personnel allocated to the process to ensure required service delivery?', 'dropdown', 'Allocation of dedicated personnel will ensure highest service quality', 423);
-- Answer options for question 423
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(423, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(423, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(423, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(424, 26, 'Is the service aligned with other relevant processes?', 'dropdown', 'e.g. the security monitoring process, and mainly the security incident management process', 424);
-- Answer options for question 424
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(424, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(424, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(424, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(425, 26, 'Is there a incident resolution / service continuity process in place for this service?', 'dropdown', 'Service continuity is important to comply with contractual agreements, even in case of major incidents', 425);
-- Answer options for question 425
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(425, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(425, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(425, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(426, 26, 'Has a set of procedures been created for this service?', 'dropdown', 'Procedures support process standardization and quality. Personnel should be trained to use procedures correctly and structurally', 426);
-- Answer options for question 426
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(426, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(426, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(426, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(427, 26, 'Is there an onboarding and offloading procedure for this service?', 'dropdown', 'Customer onboarding and offloading procedures support efficient service delivery and ensure customers are (dis)connected properly', 427);
-- Answer options for question 427
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(427, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(427, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(427, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(428, 26, 'Are best practices applied to the service?', 'dropdown', 'Best practices should be used to optimize this service', 428);
-- Answer options for question 428
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(428, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(428, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(428, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(429, 26, 'Is process data gathered for prediction of service performance?', 'dropdown', 'Service performance measurement requires establishment of performance goals', 429);
-- Answer options for question 429
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(429, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(429, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(429, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(430, 26, 'Is the service continuously being improved based on improvement goals?', 'dropdown', 'Improvement based on based evaluation, (maturity) assessment, tests, etc.', 430);
-- Answer options for question 430
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(430, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(430, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(430, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(27, 5, 'Capability', 'Capability aspect of Services domain', 27);

-- Questions for Capability
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(431, 27, 'Continuous intelligence gathering', 'checkbox', '', 431);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(432, 27, 'Automated intelligence gathering & processing', 'checkbox', '', 432);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(433, 27, 'Centralized collection & distribution', 'checkbox', '', 433);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(434, 27, 'Intelligence collection from open / public sources', 'checkbox', '', 434);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(435, 27, 'Intelligence collection from closed communities', 'checkbox', '', 435);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(436, 27, 'Intelligence collection from intelligence provider', 'checkbox', '', 436);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(437, 27, 'Intelligence collection from business partners', 'checkbox', '', 437);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(438, 27, 'Intelligence collection from mailing lists', 'checkbox', '', 438);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(439, 27, 'Intelligence collection from internal sources', 'checkbox', '', 439);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(440, 27, 'Structured data analysis', 'checkbox', '', 440);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(441, 27, 'Unstructured data analysis', 'checkbox', '', 441);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(442, 27, 'Past incident analysis', 'checkbox', '', 442);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(443, 27, 'Trend analysis', 'checkbox', '', 443);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(444, 27, 'Automated alerting', 'checkbox', '', 444);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(445, 27, 'Adversary movement tracking', 'checkbox', '', 445);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(446, 27, 'Attacker identification', 'checkbox', '', 446);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(447, 27, 'Threat identification', 'checkbox', '', 447);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(448, 27, 'Threat prediction', 'checkbox', '', 448);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(449, 27, 'TTP extraction', 'checkbox', '', 449);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(450, 27, 'Deduplication', 'checkbox', '', 450);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(451, 27, 'Enrichment', 'checkbox', '', 451);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(452, 27, 'Contextualization', 'checkbox', '', 452);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(453, 27, 'Prioritization', 'checkbox', '', 453);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(454, 27, 'Threat intelligence reporting', 'checkbox', '', 454);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(455, 27, 'Threat landscaping', 'checkbox', '', 455);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(456, 27, 'Forecasting', 'checkbox', '', 456);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(457, 27, 'Sharing within the company', 'checkbox', '', 457);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(458, 27, 'Sharing with the industry', 'checkbox', '', 458);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(459, 27, 'Sharing outside the industry', 'checkbox', '', 459);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(460, 27, 'Sharing in standardized format (e.g. STIX)', 'checkbox', '', 460);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(461, 27, 'Management of the CTI infrastructure (Threat Intelligence Platform)', 'checkbox', '', 461);
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(28, 5, 'Maturity', 'Maturity aspect of Services domain', 28);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(462, 28, 'Do you use a standardized threat hunting methodology?', 'dropdown', 'Can be an internally developed approach or a publically available methodolology, such as TaHiTI', 462);
-- Answer options for question 462
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(462, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(462, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(462, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(463, 28, 'Have you formally described the threat hunting service?', 'dropdown', 'A service description should be in place', 463);
-- Answer options for question 463
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(463, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(463, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(463, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(464, 28, 'Please specify elements of the threat hunting service document:', 'checkbox', '', 464);
-- Answer options for question 464
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Key performance indicators', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Quality indicators', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Service dependencies', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Service levels', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Hours of operation', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Service customers and stakeholders', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Purpose', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Service input / triggers', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Service output / deliverables', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Service activities', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(464, 'Service roles & responsibilities', 0, 11);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(465, 28, 'Is the service measured for quality?', 'dropdown', 'Are the quality indicators from the previous questions used for reporting on the service?', 465);
-- Answer options for question 465
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(465, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(465, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(465, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(466, 28, 'Is the service measured for service delivery in accordance with service levels?', 'dropdown', 'Service levels should be used to formally commit the SOC to service delivery', 466);
-- Answer options for question 466
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(466, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(466, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(466, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(467, 28, 'Are customers and/or stakeholders regularly updated about the service?', 'dropdown', 'Changes to the service scope, delivery, etc.', 467);
-- Answer options for question 467
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(467, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(467, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(467, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(468, 28, 'Is there a contractual agreement between the SOC and the customers?', 'dropdown', 'Contractual agreements should also cover penalties', 468);
-- Answer options for question 468
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(468, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(468, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(468, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(469, 28, 'Is sufficient personnel allocated to the process to ensure required service delivery?', 'dropdown', 'Allocation of dedicated personnel will ensure highest service quality', 469);
-- Answer options for question 469
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(469, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(469, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(469, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(470, 28, 'Is the service aligned with other relevant processes?', 'dropdown', 'e.g. threat intelligence, security monitoring, security incident response', 470);
-- Answer options for question 470
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(470, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(470, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(470, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(471, 28, 'Is there a incident resolution / service continuity process in place for this service?', 'dropdown', 'Service continuity is important to comply with contractual agreements, even in case of major incidents', 471);
-- Answer options for question 471
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(471, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(471, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(471, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(472, 28, 'Has a set of procedures been created for this service?', 'dropdown', 'Procedures support process standardization and quality. Personnel should be trained to use procedures correctly and structurally', 472);
-- Answer options for question 472
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(472, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(472, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(472, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(473, 28, 'Is there an onboarding and offloading procedure for this service?', 'dropdown', 'Customer onboarding and offloading procedures support efficient service delivery and ensure customers are (dis)connected properly', 473);
-- Answer options for question 473
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(473, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(473, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(473, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(474, 28, 'Are best practices applied to the service?', 'dropdown', 'Best practices should be used to optimize this service', 474);
-- Answer options for question 474
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(474, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(474, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(474, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(475, 28, 'Is process data gathered for prediction of service performance?', 'dropdown', 'Service performance measurement requires establishment of performance goals', 475);
-- Answer options for question 475
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(475, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(475, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(475, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(476, 28, 'Is the service continuously being improved based on improvement goals?', 'dropdown', 'Improvement based on based evaluation, (maturity) assessment, tests, etc.', 476);
-- Answer options for question 476
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(476, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(476, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(476, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(29, 5, 'Capability', 'Capability aspect of Services domain', 29);

-- Questions for Capability
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(477, 29, 'Hash value hunting', 'checkbox', '', 477);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(478, 29, 'IP address hunting', 'checkbox', '', 478);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(479, 29, 'Domain name hunting', 'checkbox', '', 479);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(480, 29, 'Network artefact hunting', 'checkbox', '', 480);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(481, 29, 'Host-based artefact hunting', 'checkbox', '', 481);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(482, 29, 'Adversary tools hunting', 'checkbox', '', 482);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(483, 29, 'Adversary TTP hunting', 'checkbox', '', 483);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(484, 29, 'Inbound threat hunting', 'checkbox', '', 484);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(485, 29, 'Outbound threat hunting', 'checkbox', '', 485);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(486, 29, 'Internal threat hunting', 'checkbox', '', 486);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(487, 29, 'Outlier detection', 'checkbox', '', 487);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(488, 29, 'Hunting coverage', 'checkbox', '', 488);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(489, 29, 'Leveraging of existing tooling', 'checkbox', '', 489);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(490, 29, 'Custom hunting scripts and tools', 'checkbox', '', 490);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(491, 29, 'Dedicated hunting platform', 'checkbox', '', 491);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(492, 29, 'Continuous hunting data collection', 'checkbox', '', 492);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(493, 29, 'Historic hunting', 'checkbox', '', 493);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(494, 29, 'Automated hunting', 'checkbox', '', 494);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(495, 29, 'Hunt alerting', 'checkbox', '', 495);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(496, 29, 'Vulnerability information integration', 'checkbox', '', 496);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(497, 29, 'Threat intelligence integration', 'checkbox', '', 497);
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(30, 5, 'Maturity', 'Maturity aspect of Services domain', 30);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(498, 30, 'Have you formally described the vulnerability management service?', 'dropdown', 'A service description should be in place', 498);
-- Answer options for question 498
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(498, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(498, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(498, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(499, 30, 'Please specify elements of the vulnerability management service document:', 'checkbox', '', 499);
-- Answer options for question 499
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Key performance indicators', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Quality indicators', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Service dependencies', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Service levels', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Hours of operation', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Service customers and stakeholders', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Purpose', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Service input / triggers', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Service output / deliverables', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Service activities', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(499, 'Service roles & responsibilities', 0, 11);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(500, 30, 'Is the service measured for quality?', 'dropdown', 'Are the quality indicators from 1.3.2 used for reporting on the service?', 500);
-- Answer options for question 500
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(500, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(500, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(500, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(501, 30, 'Is the service measured for service delivery in accordance with service levels?', 'dropdown', 'Service levels should be used to formally commit the SOC to service delivery', 501);
-- Answer options for question 501
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(501, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(501, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(501, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(502, 30, 'Are customers and/or stakeholders regularly updated about the service?', 'dropdown', 'Changes to the service scope, delivery, etc.', 502);
-- Answer options for question 502
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(502, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(502, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(502, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(503, 30, 'Is there a contractual agreement between the SOC and the customers?', 'dropdown', 'Contractual agreements should also cover penalties', 503);
-- Answer options for question 503
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(503, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(503, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(503, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(504, 30, 'Is sufficient personnel allocated to the process to ensure required service delivery?', 'dropdown', 'Allocation of dedicated personnel will ensure highest service quality', 504);
-- Answer options for question 504
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(504, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(504, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(504, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(505, 30, 'Is the service aligned with other relevant processes?', 'dropdown', 'e.g. the security monitoring process, and mainly the security incident management process', 505);
-- Answer options for question 505
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(505, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(505, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(505, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(506, 30, 'Is there a incident resolution / service continuity process in place for this service?', 'dropdown', 'Service continuity is important to comply with contractual agreements, even in case of major incidents', 506);
-- Answer options for question 506
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(506, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(506, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(506, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(507, 30, 'Has a set of procedures been created for this service?', 'dropdown', 'Procedures support process standardization and quality. Personnel should be trained to use procedures correctly and structurally', 507);
-- Answer options for question 507
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(507, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(507, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(507, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(508, 30, 'Is there an onboarding and offloading procedure for this service?', 'dropdown', 'Customer onboarding and offloading procedures support efficient service delivery and ensure customers are (dis)connected properly', 508);
-- Answer options for question 508
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(508, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(508, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(508, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(509, 30, 'Are best practices applied to the service?', 'dropdown', 'Best practices should be used to optimize this service. Adoption of a standard like NIST 800-40r4 is part of best practices', 509);
-- Answer options for question 509
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(509, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(509, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(509, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(510, 30, 'Is process data gathered for prediction of service performance?', 'dropdown', 'Service performance measurement requires establishment of performance goals', 510);
-- Answer options for question 510
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(510, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(510, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(510, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(511, 30, 'Is the service continuously being improved based on improvement goals?', 'dropdown', 'Improvement based on based evaluation, (maturity) assessment, tests, etc.', 511);
-- Answer options for question 511
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(511, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(511, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(511, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(31, 5, 'Capability', 'Capability aspect of Services domain', 31);

-- Questions for Capability
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(512, 31, 'Network mapping', 'checkbox', '', 512);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(513, 31, 'Vulnerability identification', 'checkbox', '', 513);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(514, 31, 'Risk identification', 'checkbox', '', 514);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(515, 31, 'Risk acceptance', 'checkbox', '', 515);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(516, 31, 'Security baseline scanning', 'checkbox', '', 516);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(517, 31, 'Authenticated scanning', 'checkbox', '', 517);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(518, 31, 'Incident management integration', 'checkbox', '', 518);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(519, 31, 'Asset management integration', 'checkbox', '', 519);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(520, 31, 'Configuration management integration', 'checkbox', '', 520);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(521, 31, 'Patch management integration', 'checkbox', '', 521);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(522, 31, 'Trend identification', 'checkbox', '', 522);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(523, 31, 'Enterprise vulnerability repository', 'checkbox', '', 523);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(524, 31, 'Enterprise application inventory', 'checkbox', '', 524);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(525, 31, 'Vulnerability Management procedures', 'checkbox', '', 525);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(526, 31, 'Scanning policy tuning', 'checkbox', '', 526);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(527, 31, 'Detailed Vulnerability Reporting', 'checkbox', '', 527);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(528, 31, 'Management Reporting', 'checkbox', '', 528);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(529, 31, 'Scheduled scanning', 'checkbox', '', 529);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(530, 31, 'Ad-hoc specific scanning', 'checkbox', '', 530);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(531, 31, 'Vulnerability information gathering & analysis', 'checkbox', '', 531);
INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(32, 5, 'Maturity', 'Maturity aspect of Services domain', 32);

-- Questions for Maturity
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(532, 32, 'Have you formally described the log management service?', 'dropdown', 'A service description should be in place', 532);
-- Answer options for question 532
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(532, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(532, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(532, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(533, 32, 'Please specify elements of the log management service document:', 'checkbox', '', 533);
-- Answer options for question 533
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Key performance indicators', 0, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Quality indicators', 0, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Service dependencies', 0, 3);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Service levels', 0, 4);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Hours of operation', 0, 5);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Service customers and stakeholders', 0, 6);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Purpose', 0, 7);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Service input / triggers', 0, 8);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Service output / deliverables', 0, 9);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Service activities', 0, 10);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(533, 'Service roles & responsibilities', 0, 11);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(534, 32, 'Is the service measured for quality?', 'dropdown', 'Are the quality indicators from 1.3.2 used for reporting on the service?', 534);
-- Answer options for question 534
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(534, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(534, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(534, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(535, 32, 'Is the service measured for service delivery in accordance with service levels?', 'dropdown', 'Service levels should be used to formally commit the SOC to service delivery', 535);
-- Answer options for question 535
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(535, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(535, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(535, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(536, 32, 'Are customers and/or stakeholders regularly updated about the service?', 'dropdown', 'Changes to the service scope, delivery, etc.', 536);
-- Answer options for question 536
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(536, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(536, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(536, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(537, 32, 'Is there a contractual agreement between the SOC and the customers?', 'dropdown', 'Contractual agreements should also cover penalties', 537);
-- Answer options for question 537
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(537, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(537, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(537, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(538, 32, 'Is sufficient personnel allocated to the process to ensure required service delivery?', 'dropdown', 'Allocation of dedicated personnel will ensure highest service quality', 538);
-- Answer options for question 538
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(538, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(538, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(538, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(539, 32, 'Is the service aligned with other relevant processes?', 'dropdown', 'e.g. the security monitoring process, and mainly the security incident management process', 539);
-- Answer options for question 539
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(539, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(539, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(539, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(540, 32, 'Is there a incident resolution / service continuity process in place for this service?', 'dropdown', 'Service continuity is important to comply with contractual agreements, even in case of major incidents', 540);
-- Answer options for question 540
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(540, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(540, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(540, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(541, 32, 'Has a set of procedures been created for this service?', 'dropdown', 'Procedures support process standardization and quality. Personnel should be trained to use procedures correctly and structurally', 541);
-- Answer options for question 541
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(541, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(541, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(541, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(542, 32, 'Is there an onboarding and offloading procedure for this service?', 'dropdown', 'Customer onboarding and offloading procedures support efficient service delivery and ensure customers are (dis)connected properly', 542);
-- Answer options for question 542
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(542, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(542, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(542, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(543, 32, 'Are best practices applied to the service?', 'dropdown', 'Best practices should be used to optimize this service', 543);
-- Answer options for question 543
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(543, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(543, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(543, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(544, 32, 'Is process data gathered for prediction of service performance?', 'dropdown', 'Service performance measurement requires establishment of performance goals', 544);
-- Answer options for question 544
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(544, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(544, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(544, 'Yes', 3, 3);

INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(545, 32, 'Is the service continuously being improved based on improvement goals?', 'dropdown', 'Improvement based on based evaluation, (maturity) assessment, tests, etc.', 545);
-- Answer options for question 545
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(545, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(545, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, score, order_index) VALUES
(545, 'Yes', 3, 3);

INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES
(33, 5, 'Capability', 'Capability aspect of Services domain', 33);

-- Questions for Capability
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(546, 33, 'End-point log collection', 'checkbox', '', 546);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(547, 33, 'Application log collection', 'checkbox', '', 547);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(548, 33, 'Database log collection', 'checkbox', '', 548);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(549, 33, 'Network flow data collection', 'checkbox', '', 549);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(550, 33, 'Network device log collection', 'checkbox', '', 550);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(551, 33, 'Security device log collection', 'checkbox', '', 551);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(552, 33, 'Centralized aggregation and storage', 'checkbox', '', 552);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(553, 33, 'Multiple retention periods', 'checkbox', '', 553);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(554, 33, 'Secure log transfer', 'checkbox', '', 554);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(555, 33, 'Support for multiple log formats', 'checkbox', '', 555);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(556, 33, 'Support for multiple transfer techniques', 'checkbox', '', 556);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(557, 33, 'Data normalization', 'checkbox', '', 557);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(558, 33, 'Log searching and filtering', 'checkbox', '', 558);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(559, 33, 'Alerting', 'checkbox', '', 559);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(560, 33, 'Reporting and dashboards', 'checkbox', '', 560);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(561, 33, 'Log tampering detection', 'checkbox', '', 561);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(562, 33, 'Log collection policy', 'checkbox', '', 562);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(563, 33, 'Logging policy', 'checkbox', '', 563);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(564, 33, 'Data retention policy', 'checkbox', '', 564);
INSERT INTO questions (id, aspect_id, question_text, field_type, guidance, order_index) VALUES
(565, 33, 'Privacy and Sensitive data handling policy', 'checkbox', '', 565);