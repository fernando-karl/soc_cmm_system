import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional

class DatabaseManager:
    def __init__(self, db_path: str = "soc_cmm_translated.db"):
        self.db_path = db_path
        #self.init_database()
        #self.populate_initial_data()
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Initialize the database with the schema"""
        with open('database_schema.sql', 'r') as f:
            schema = f.read()
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Execute schema creation
        for statement in schema.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        conn.commit()
        conn.close()
    
    def populate_initial_data(self):
        """Populate the database with SOC CMM data"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Check if data already exists
        cursor.execute("SELECT COUNT(*) FROM domains")
        if cursor.fetchone()[0] > 0:
            conn.close()
            return
        
        # Load the extracted data
        with open('soc_cmm_complete_data.json', 'r') as f:
            data = json.load(f)
        
        # Insert domains
        for domain in data['domains']:
            cursor.execute("""
                INSERT INTO domains (id, name, description, order_index)
                VALUES (?, ?, ?, ?)
            """, (domain['id'], domain['name'], domain['description'], domain['order_index']))
        
        # Insert aspects
        for aspect in data['aspects']:
            cursor.execute("""
                INSERT INTO aspects (id, domain_id, name, code, description, order_index)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (aspect['id'], aspect['domain_id'], aspect['name'], aspect['code'], 
                  aspect['description'], aspect['order_index']))
        
        # Insert questions
        for question in data['questions']:
            cursor.execute("""
                INSERT INTO questions (id, aspect_id, question_text, question_type, order_index)
                VALUES (?, ?, ?, ?, ?)
            """, (question['id'], question['aspect_id'], question['question_text'], 
                  question['question_type'], question['order_index']))
        
        # Insert answer options
        for option in data['answer_options']:
            cursor.execute("""
                INSERT INTO answer_options (id, question_id, option_text, maturity_level, order_index)
                VALUES (?, ?, ?, ?, ?)
            """, (option['id'], option['question_id'], option['option_text'], 
                  option['maturity_level'], option['order_index']))
        
        conn.commit()
        conn.close()
    
    # Customer methods
    def create_customer(self, user_id: int, name: str, email: str = None, organization: str = None) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO customers (user_id, name, email, organization)
            VALUES (?, ?, ?, ?)
        """, (user_id, name, email, organization))
        
        customer_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return customer_id
    
    def get_customers(self, user_id: int = None) -> List[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if user_id:
            cursor.execute("SELECT * FROM customers WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
        else:
            cursor.execute("SELECT * FROM customers ORDER BY created_at DESC")
        
        customers = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return customers
    
    def get_customer(self, customer_id: int) -> Optional[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
        customer = cursor.fetchone()
        
        conn.close()
        return dict(customer) if customer else None
    
    # Assessment methods
    def create_assessment(self, customer_id: int, name: str = None) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if not name:
            name = f"Assessment {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        cursor.execute("""
            INSERT INTO assessments (customer_id, name)
            VALUES (?, ?)
        """, (customer_id, name))
        
        assessment_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return assessment_id
    
    def get_customer_assessments(self, customer_id: int) -> List[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM assessments 
            WHERE customer_id = ? 
            ORDER BY started_at DESC
        """, (customer_id,))
        
        assessments = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return assessments
    
    def get_assessment(self, assessment_id: int) -> Optional[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM assessments WHERE id = ?", (assessment_id,))
        assessment = cursor.fetchone()
        
        conn.close()
        return dict(assessment) if assessment else None
    
    def complete_assessment(self, assessment_id: int):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE assessments 
            SET status = 'completed', completed_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (assessment_id,))
        
        conn.commit()
        conn.close()
    
    # Domain and question methods
    def get_domains(self) -> List[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM domains ORDER BY order_index")
        domains = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return domains
    
    def get_domain_aspects(self, domain_id: int) -> List[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM aspects 
            WHERE domain_id = ? 
            ORDER BY order_index
        """, (domain_id,))
        
        aspects = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return aspects
    
    def get_aspect_questions(self, aspect_id: str) -> List[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT q.*, a.name as aspect_name, d.name as domain_name
            FROM questions q
            JOIN aspects a ON q.aspect_id = a.id
            JOIN domains d ON a.domain_id = d.id
            WHERE q.aspect_id = ?
            ORDER BY q.order_index
        """, (aspect_id,))
        
        questions = [dict(row) for row in cursor.fetchall()]
        
        # Get answer options for each question
        for question in questions:
            cursor.execute("""
                SELECT * FROM answer_options 
                WHERE question_id = ? 
                ORDER BY order_index
            """, (question['id'],))
            question['options'] = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return questions
    
    # Answer methods
    def save_answer(self, assessment_id: int, question_id: int, answer_option_id: int):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT maturity_level FROM answer_options WHERE id = ?
        """, (answer_option_id,))
        
        maturity_score = cursor.fetchone()[0]
        
        # Delete existing answer if any
        cursor.execute("""
            DELETE FROM assessment_answers 
            WHERE assessment_id = ? AND question_id = ?
        """, (assessment_id, question_id))
        
        # Insert new answer
        cursor.execute("""
            INSERT INTO assessment_answers 
            (assessment_id, question_id, answer_option_id, maturity_score)
            VALUES (?, ?, ?, ?)
        """, (assessment_id, question_id, answer_option_id, maturity_score))
        
        conn.commit()
        conn.close()
    
    def get_assessment_answers(self, assessment_id: int) -> List[Dict]:
        """Get all answers for an assessment"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT question_id, answer_option_id, answer_text, maturity_score
            FROM assessment_answers 
            WHERE assessment_id = ?
        """, (assessment_id,))
        
        answers = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return answers
    
    def calculate_assessment_scores(self, assessment_id: int):
        """Calculate and store assessment scores by aspect and domain"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Delete existing scores
        cursor.execute("DELETE FROM assessment_scores WHERE assessment_id = ?", (assessment_id,))
        
        # Calculate aspect scores
        cursor.execute("""
            SELECT 
                a.id as aspect_id,
                a.domain_id,
                AVG(aa.maturity_score) as avg_score,
                COUNT(aa.maturity_score) as question_count
            FROM aspects a
            JOIN questions q ON a.id = q.aspect_id
            LEFT JOIN assessment_answers aa ON q.id = aa.question_id AND aa.assessment_id = ?
            WHERE aa.maturity_score IS NOT NULL
            GROUP BY a.id, a.domain_id
        """, (assessment_id,))
        
        aspect_scores = cursor.fetchall()
        
        for score in aspect_scores:
            percentage = (score[2] / 5.0) * 100  # Convert to percentage (max score is 5)
            cursor.execute("""
                INSERT INTO assessment_scores 
                (assessment_id, aspect_id, domain_id, score, max_score, percentage)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (assessment_id, score[0], score[1], score[2], 5.0, percentage))
        
        # Calculate domain scores
        cursor.execute("""
            SELECT 
                domain_id,
                AVG(score) as avg_score,
                AVG(percentage) as avg_percentage
            FROM assessment_scores
            WHERE assessment_id = ? AND aspect_id IS NOT NULL
            GROUP BY domain_id
        """, (assessment_id,))
        
        domain_scores = cursor.fetchall()
        
        for score in domain_scores:
            cursor.execute("""
                INSERT INTO assessment_scores 
                (assessment_id, domain_id, score, max_score, percentage)
                VALUES (?, ?, ?, ?, ?)
            """, (assessment_id, score[0], score[1], 5.0, score[2]))
        
        conn.commit()
        conn.close()
    
    def get_assessment_scores(self, assessment_id: int) -> Dict:
        """Get assessment scores grouped by domain and aspect"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Get domain scores
        cursor.execute("""
            SELECT d.name, s.score, s.percentage
            FROM assessment_scores s
            JOIN domains d ON s.domain_id = d.id
            WHERE s.assessment_id = ? AND s.aspect_id IS NULL
            ORDER BY d.order_index
        """, (assessment_id,))
        
        domain_scores = [dict(row) for row in cursor.fetchall()]
        
        # Get aspect scores
        cursor.execute("""
            SELECT d.name as domain_name, a.name as aspect_name, s.score, s.percentage
            FROM assessment_scores s
            JOIN aspects a ON s.aspect_id = a.id
            JOIN domains d ON s.domain_id = d.id
            WHERE s.assessment_id = ? AND s.aspect_id IS NOT NULL
            ORDER BY d.order_index, a.order_index
        """, (assessment_id,))
        
        aspect_scores = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return {
            'domain_scores': domain_scores,
            'aspect_scores': aspect_scores
        }
    
    def get_radar_chart_data(self, assessment_id: int) -> Dict:
        """Get data formatted for radar chart visualization"""
        scores = self.get_assessment_scores(assessment_id)
        
        labels = [score['name'] for score in scores['domain_scores']]
        data = [score['percentage'] for score in scores['domain_scores']]
        
        return {
            'labels': labels,
            'datasets': [{
                'label': 'SOC Maturity Level',
                'data': data,
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 2
            }]
        }

