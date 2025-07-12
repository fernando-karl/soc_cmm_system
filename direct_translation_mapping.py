#!/usr/bin/env python3
import sqlite3
import json
import os

def load_json_files():
    """Carrega os arquivos JSON original e traduzido"""
    try:
        with open('soc_cmm_questions.json', 'r', encoding='utf-8') as f:
            english_data = json.load(f)
        print("Arquivo JSON em inglês carregado")
    except FileNotFoundError:
        print("Arquivo soc_cmm_questions.json não encontrado!")
        return None, None
    
    try:
        with open('soc_cmm_questions-port.json', 'r', encoding='utf-8') as f:
            portuguese_data = json.load(f)
        print("Arquivo JSON em português carregado")
    except FileNotFoundError:
        print("Arquivo soc_cmm_questions-port.json não encontrado!")
        return None, None
    
    return english_data, portuguese_data

def extract_all_questions(data):
    """Extrai todas as questões do JSON"""
    questions = []
    
    def process_section(section_data):
        for section_name, section_content in section_data.items():
            if isinstance(section_content, dict):
                # É um subseção
                process_section(section_content)
            elif isinstance(section_content, list):
                # É uma lista de questões
                for question in section_content:
                    if isinstance(question, dict) and 'question' in question:
                        questions.append({
                            'question': question['question'],
                            'guidance': question.get('guidance', ''),
                            'id': question.get('id', '')
                        })
    
    # Processa cada domínio
    for domain_name, domain_data in data.items():
        if isinstance(domain_data, dict):
            process_section(domain_data)
    
    return questions

def create_direct_mapping(english_questions, portuguese_questions):
    """Cria mapeamento direto entre questões em inglês e português"""
    mapping = {}
    
    # Cria um dicionário das questões em português para busca rápida
    portuguese_dict = {}
    for pq in portuguese_questions:
        portuguese_dict[pq['question']] = pq
    
    # Para cada questão em inglês, procura uma correspondente em português
    for eq in english_questions:
        english_text = eq['question']
        
        # Procura por correspondência exata ou similar
        found = False
        
        # 1. Procura por correspondência exata
        for pq in portuguese_questions:
            if pq['question'] == english_text:
                mapping[english_text] = {
                    'translated_question': pq['question'],
                    'translated_guidance': pq['guidance']
                }
                found = True
                break
        
        # 2. Se não encontrou, procura por questões que começam de forma similar
        if not found:
            # Remove pontuação e normaliza para comparação
            english_clean = english_text.lower().replace('?', '').replace('.', '').strip()
            
            for pq in portuguese_questions:
                portuguese_clean = pq['question'].lower().replace('?', '').replace('.', '').strip()
                
                # Se as primeiras palavras são similares
                if (english_clean.startswith(portuguese_clean[:20]) or 
                    portuguese_clean.startswith(english_clean[:20])):
                    mapping[english_text] = {
                        'translated_question': pq['question'],
                        'translated_guidance': pq['guidance']
                    }
                    found = True
                    break
    
    print(f"Mapeamento direto criado com {len(mapping)} traduções")
    return mapping

def get_english_questions_from_db(db_path):
    """Busca todas as questões em inglês da base de dados"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, question_text 
        FROM questions 
        WHERE question_text LIKE '%Is there%' 
           OR question_text LIKE '%Are there%' 
           OR question_text LIKE '%Do you%' 
           OR question_text LIKE '%Does the%' 
           OR question_text LIKE '%Is the%' 
           OR question_text LIKE '%Are the%' 
           OR question_text LIKE '%Does your%' 
           OR question_text LIKE '%Is your%' 
           OR question_text LIKE '%Are your%'
           OR question_text LIKE '%Does this%'
           OR question_text LIKE '%Is this%'
           OR question_text LIKE '%Are this%'
           OR question_text LIKE '%Do the%'
           OR question_text LIKE '%Have you%'
           OR question_text LIKE '%Has the%'
           OR question_text LIKE '%Have the%'
    """)
    
    english_questions = cursor.fetchall()
    conn.close()
    
    return english_questions

def update_questions_with_mapping(db_path, english_questions, translation_mapping):
    """Atualiza as questões usando o mapeamento"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    updated_count = 0
    not_found = []
    
    for question_id, original_question in english_questions:
        if original_question in translation_mapping:
            translation = translation_mapping[original_question]
            
            cursor.execute("""
                UPDATE questions 
                SET question_text = ?, guidance = ?
                WHERE id = ?
            """, (translation['translated_question'], translation['translated_guidance'], question_id))
            
            if cursor.rowcount > 0:
                updated_count += 1
                print(f"✓ Questão {question_id}: '{original_question[:50]}...' -> '{translation['translated_question'][:50]}...'")
        else:
            not_found.append((question_id, original_question))
    
    print(f"\nResumo:")
    print(f"- Questões atualizadas: {updated_count}")
    print(f"- Questões não encontradas: {len(not_found)}")
    
    if not_found:
        print("\nQuestões não encontradas no mapeamento:")
        for question_id, question_text in not_found[:5]:  # Mostra apenas as primeiras 5
            print(f"  ID {question_id}: {question_text}")
    
    conn.commit()
    conn.close()
    return updated_count, not_found

def create_manual_mapping():
    """Cria mapeamento manual para questões específicas que não foram encontradas automaticamente"""
    manual_mapping = {
        "Do you regularly send updates to your customers?": {
            "translated_question": "Você envia regularmente atualizações para seus clientes?",
            "translated_guidance": "Atualizações regulares mantêm os clientes informados sobre o status dos serviços"
        },
        "Do you actively measure and manage customer satisfaction?": {
            "translated_question": "Você mede e gerencia ativamente a satisfação do cliente?",
            "translated_guidance": "Medir a satisfação do cliente é essencial para melhorar os serviços"
        },
        "Does the SOC have a formal charter document in place?": {
            "translated_question": "O SOC possui um documento de estatuto formal?",
            "translated_guidance": "Um estatuto formal define o escopo e responsabilidades do SOC"
        },
        "Is the SOC charter document approved by the business / CISO?": {
            "translated_question": "O documento de estatuto do SOC é aprovado pelo negócio / CISO?",
            "translated_guidance": "Aprovação formal garante alinhamento com a estratégia de negócio"
        },
        "Does the SOC have a governance process in place?": {
            "translated_question": "O SOC possui um processo de governança?",
            "translated_guidance": "Processos de governança garantem conformidade e eficiência"
        },
        "Is there an information security policy in place that supports the SOC activities?": {
            "translated_question": "Existe uma política de segurança da informação que apoia as atividades do SOC?",
            "translated_guidance": "Políticas claras fornecem base para as operações do SOC"
        },
        "Is the SOC consulted in the creation and updates of operational security policy?": {
            "translated_question": "O SOC é consultado na criação e atualizações da política de segurança operacional?",
            "translated_guidance": "Participação do SOC garante políticas práticas e eficazes"
        },
        "Is the SOC aware of all information that it processes and is subject to privacy regulations?": {
            "translated_question": "O SOC está ciente de todas as informações que processa e está sujeito a regulamentações de privacidade?",
            "translated_guidance": "Conformidade com regulamentações de privacidade é essencial"
        },
        "Do you use external employees / contractors in your SOC?": {
            "translated_question": "Você usa funcionários externos / contratados em seu SOC?",
            "translated_guidance": "Funcionários externos podem complementar a equipe interna"
        },
        "Does the current size of the SOC meet FTE requirements?": {
            "translated_question": "O tamanho atual do SOC atende aos requisitos de FTE?",
            "translated_guidance": "Recursos adequados são necessários para operações eficazes"
        }
    }
    
    return manual_mapping

def main():
    print("=== Mapeamento Direto de Tradução ===")
    
    # Verifica se a base traduzida existe
    if not os.path.exists("soc_cmm_translated.db"):
        print("Arquivo soc_cmm_translated.db não encontrado!")
        return
    
    # 1. Carregar arquivos JSON
    english_data, portuguese_data = load_json_files()
    if not english_data or not portuguese_data:
        return
    
    # 2. Extrair questões
    english_questions = extract_all_questions(english_data)
    portuguese_questions = extract_all_questions(portuguese_data)
    
    print(f"Extraídas {len(english_questions)} questões em inglês")
    print(f"Extraídas {len(portuguese_questions)} questões em português")
    
    # 3. Criar mapeamento automático
    auto_mapping = create_direct_mapping(english_questions, portuguese_questions)
    
    # 4. Adicionar mapeamento manual
    manual_mapping = create_manual_mapping()
    
    # 5. Combinar mapeamentos
    combined_mapping = {**auto_mapping, **manual_mapping}
    print(f"Mapeamento combinado com {len(combined_mapping)} traduções")
    
    # 6. Buscar questões em inglês da base
    english_db_questions = get_english_questions_from_db("soc_cmm_translated.db")
    print(f"Encontradas {len(english_db_questions)} questões em inglês na base")
    
    # 7. Atualizar questões
    updated_count, not_found = update_questions_with_mapping("soc_cmm_translated.db", english_db_questions, combined_mapping)
    
    # 8. Verificar resultado
    conn = sqlite3.connect("soc_cmm_translated.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT COUNT(*) 
        FROM questions 
        WHERE question_text LIKE '%Is there%' 
           OR question_text LIKE '%Are there%' 
           OR question_text LIKE '%Do you%' 
           OR question_text LIKE '%Does the%' 
           OR question_text LIKE '%Is the%' 
           OR question_text LIKE '%Are the%' 
           OR question_text LIKE '%Does your%' 
           OR question_text LIKE '%Is your%' 
           OR question_text LIKE '%Are your%'
    """)
    
    remaining_english = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_questions = cursor.fetchone()[0]
    
    print(f"\nVerificação final:")
    print(f"- Total de questões: {total_questions}")
    print(f"- Questões ainda em inglês: {remaining_english}")
    print(f"- Questões traduzidas: {total_questions - remaining_english}")
    
    conn.close()
    
    print(f"\n=== Processo concluído ===")
    print(f"Questões atualizadas: {updated_count}")

if __name__ == "__main__":
    main() 