"""
Camada de Acesso a Dados (SQLite) para o SOC CMM Assessment System.

Responsável por CRUD de clientes, avaliações, domínios, aspectos, questões,
opções de resposta, respostas e pontuações.
"""
import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional

class DatabaseManager:
    """Gerencia conexões e operações no banco SQLite."""
    def __init__(self, db_path: str = "soc_cmm_bilingual.db"):
        self.db_path = db_path
        #self.init_database()
        #self.populate_initial_data()
    
    def get_connection(self):
        """Abre uma conexão com o SQLite e retorna um cursor com linhas nomeadas."""
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
    #
    # Sistema bilíngue: as colunas `name`/`description`/`question_text`/`option_text`/`guidance`
    # nas tabelas base ficam em inglês (baseline canônico). As traduções vivem em
    # `*_translations` (language='en' duplica o baseline; 'pt_br' tem o conteúdo PT).
    # Todo método público que retorna conteúdo aceita `language` (default 'en')
    # e faz LEFT JOIN + COALESCE para cair no base se a tradução faltar.

    def get_domains(self, language: str = "en") -> List[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT d.id, d.order_index,
                   COALESCE(dt.name, d.name) AS name,
                   COALESCE(dt.description, d.description) AS description
            FROM domains d
            LEFT JOIN domain_translations dt
              ON dt.domain_id = d.id AND dt.language = ?
            ORDER BY d.order_index
            """,
            (language,),
        )
        domains = [dict(row) for row in cursor.fetchall()]

        conn.close()
        return domains

    def get_domain_aspects(self, domain_id: int, language: str = "en") -> List[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT a.id, a.domain_id, a.order_index,
                   COALESCE(at.name, a.name) AS name,
                   COALESCE(at.description, a.description) AS description
            FROM aspects a
            LEFT JOIN aspect_translations at
              ON at.aspect_id = a.id AND at.language = ?
            WHERE a.domain_id = ?
            ORDER BY a.order_index
            """,
            (language, domain_id),
        )

        aspects = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return aspects

    def get_aspect_questions(self, aspect_id: str, language: str = "en") -> List[Dict]:
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT q.id, q.aspect_id, q.question_type, q.order_index,
                   COALESCE(qt.question_text, q.question_text) AS question_text,
                   COALESCE(qt.guidance, q.guidance)           AS guidance,
                   COALESCE(at.name, a.name)                   AS aspect_name,
                   COALESCE(dt.name, d.name)                   AS domain_name
            FROM questions q
            JOIN aspects a ON q.aspect_id = a.id
            JOIN domains d ON a.domain_id = d.id
            LEFT JOIN question_translations qt
              ON qt.question_id = q.id AND qt.language = ?
            LEFT JOIN aspect_translations at
              ON at.aspect_id = a.id AND at.language = ?
            LEFT JOIN domain_translations dt
              ON dt.domain_id = d.id AND dt.language = ?
            WHERE q.aspect_id = ?
            ORDER BY q.order_index
            """,
            (language, language, language, aspect_id),
        )

        questions = [dict(row) for row in cursor.fetchall()]

        # Get answer options for each question (translated)
        for question in questions:
            cursor.execute(
                """
                SELECT o.id, o.question_id, o.maturity_level, o.order_index,
                       COALESCE(ot.option_text, o.option_text) AS option_text
                FROM answer_options o
                LEFT JOIN answer_option_translations ot
                  ON ot.answer_option_id = o.id AND ot.language = ?
                WHERE o.question_id = ?
                ORDER BY o.order_index
                """,
                (language, question["id"]),
            )
            question["options"] = [dict(row) for row in cursor.fetchall()]

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
    
    def get_assessment_scores(self, assessment_id: int, language: str = "en") -> Dict:
        """Get assessment scores grouped by domain and aspect"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Get domain scores (translated)
        cursor.execute(
            """
            SELECT COALESCE(dt.name, d.name) AS name, s.score, s.percentage
            FROM assessment_scores s
            JOIN domains d ON s.domain_id = d.id
            LEFT JOIN domain_translations dt
              ON dt.domain_id = d.id AND dt.language = ?
            WHERE s.assessment_id = ? AND s.aspect_id IS NULL
            ORDER BY d.order_index
            """,
            (language, assessment_id),
        )

        domain_scores = [dict(row) for row in cursor.fetchall()]

        # Get aspect scores (translated)
        cursor.execute(
            """
            SELECT COALESCE(dt.name, d.name) AS domain_name,
                   COALESCE(at.name, a.name) AS aspect_name,
                   s.score, s.percentage
            FROM assessment_scores s
            JOIN aspects a ON s.aspect_id = a.id
            JOIN domains d ON s.domain_id = d.id
            LEFT JOIN domain_translations dt
              ON dt.domain_id = d.id AND dt.language = ?
            LEFT JOIN aspect_translations at
              ON at.aspect_id = a.id AND at.language = ?
            WHERE s.assessment_id = ? AND s.aspect_id IS NOT NULL
            ORDER BY d.order_index, a.order_index
            """,
            (language, language, assessment_id),
        )

        aspect_scores = [dict(row) for row in cursor.fetchall()]

        conn.close()
        return {
            'domain_scores': domain_scores,
            'aspect_scores': aspect_scores
        }

    def get_radar_chart_data(self, assessment_id: int, language: str = "en") -> Dict:
        """Get data formatted for radar chart visualization"""
        scores = self.get_assessment_scores(assessment_id, language)
        
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

    # Admin methods
    def get_all_users(self) -> List[Dict]:
        """Get all users for admin management"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, username, email, full_name, is_active, is_admin, created_at, updated_at
            FROM users
            ORDER BY created_at DESC
        """)
        
        users = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return users
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict]:
        """Get user by ID for admin management"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, username, email, full_name, is_active, is_admin, created_at, updated_at
            FROM users
            WHERE id = ?
        """, (user_id,))
        
        user = cursor.fetchone()
        conn.close()
        
        return dict(user) if user else None
    
    def update_user(self, user_id: int, username: str, email: str, full_name: str = None, is_active: bool = True) -> bool:
        """Update user information"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                UPDATE users 
                SET username = ?, email = ?, full_name = ?, is_active = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (username, email, full_name, is_active, user_id))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            conn.close()
            return False
    
    def delete_user(self, user_id: int) -> bool:
        """Delete a user (admin only)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # First delete all related data
            cursor.execute("DELETE FROM assessment_answers WHERE assessment_id IN (SELECT id FROM assessments WHERE customer_id IN (SELECT id FROM customers WHERE user_id = ?))", (user_id,))
            cursor.execute("DELETE FROM assessment_scores WHERE assessment_id IN (SELECT id FROM assessments WHERE customer_id IN (SELECT id FROM customers WHERE user_id = ?))", (user_id,))
            cursor.execute("DELETE FROM assessments WHERE customer_id IN (SELECT id FROM customers WHERE user_id = ?)", (user_id,))
            cursor.execute("DELETE FROM customers WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            conn.close()
            return False
    
    def get_dashboard_stats(self) -> Dict:
        """Get dashboard statistics for admin"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Total users
        cursor.execute("SELECT COUNT(*) as total FROM users")
        total_users = cursor.fetchone()[0]
        
        # Active users
        cursor.execute("SELECT COUNT(*) as active FROM users WHERE is_active = 1")
        active_users = cursor.fetchone()[0]
        
        # Total customers
        cursor.execute("SELECT COUNT(*) as total FROM customers")
        total_customers = cursor.fetchone()[0]
        
        # Total assessments
        cursor.execute("SELECT COUNT(*) as total FROM assessments")
        total_assessments = cursor.fetchone()[0]
        
        # Assessments by status
        cursor.execute("""
            SELECT status, COUNT(*) as count
            FROM assessments
            GROUP BY status
        """)
        assessments_by_status = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Customers by user
        cursor.execute("""
            SELECT u.username, COUNT(c.id) as customer_count
            FROM users u
            LEFT JOIN customers c ON u.id = c.user_id
            GROUP BY u.id, u.username
            ORDER BY customer_count DESC
        """)
        customers_by_user = [dict(zip(['username', 'customer_count'], row)) for row in cursor.fetchall()]
        
        # Recent assessments
        cursor.execute("""
            SELECT a.id, a.name, a.status, a.started_at, a.completed_at, c.name as customer_name, u.username
            FROM assessments a
            JOIN customers c ON a.customer_id = c.id
            JOIN users u ON c.user_id = u.id
            ORDER BY a.started_at DESC
            LIMIT 10
        """)
        recent_assessments = [dict(zip(['id', 'name', 'status', 'started_at', 'completed_at', 'customer_name', 'username'], row)) for row in cursor.fetchall()]
        
        # Monthly statistics
        cursor.execute("""
            SELECT 
                strftime('%Y-%m', created_at) as month,
                COUNT(*) as new_users
            FROM users
            WHERE created_at >= date('now', '-6 months')
            GROUP BY strftime('%Y-%m', created_at)
            ORDER BY month DESC
        """)
        monthly_users = [dict(zip(['month', 'new_users'], row)) for row in cursor.fetchall()]
        
        cursor.execute("""
            SELECT 
                strftime('%Y-%m', created_at) as month,
                COUNT(*) as new_customers
            FROM customers
            WHERE created_at >= date('now', '-6 months')
            GROUP BY strftime('%Y-%m', created_at)
            ORDER BY month DESC
        """)
        monthly_customers = [dict(zip(['month', 'new_customers'], row)) for row in cursor.fetchall()]
        
        conn.close()
        
        return {
            'total_users': total_users,
            'active_users': active_users,
            'total_customers': total_customers,
            'total_assessments': total_assessments,
            'assessments_by_status': assessments_by_status,
            'customers_by_user': customers_by_user,
            'recent_assessments': recent_assessments,
            'monthly_users': monthly_users,
            'monthly_customers': monthly_customers
        }

