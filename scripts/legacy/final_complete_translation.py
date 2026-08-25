#!/usr/bin/env python3
import sqlite3
import json

def load_translations():
    """Carrega as traduções do arquivo JSON"""
    with open('dataset/soc_cmm_questions-port.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_complete_translation_mapping():
    """Cria mapeamento completo de traduções"""
    translations = load_translations()
    mapping = {}
    
    # Mapeamento manual para questões principais que não foram encontradas automaticamente
    manual_mapping = {
        "Have you identified the main business drivers?": "Você identificou os principais drivers de negócio?",
        "Have you documented the main business drivers?": "Você documentou os principais drivers de negócio?",
        "Do you use business drivers in the decision making process?": "Você usa os drivers de negócio no processo de tomada de decisão?",
        "Do you regularly check if the current service catalogue is aligned with business drivers?": "Você verifica regularmente se o catálogo de serviços atual está alinhado com os drivers de negócio?",
        "Have the business drivers been validated with business stakeholders?": "Os drivers de negócio foram validados com as partes interessadas do negócio?",
        "Have you identified the SOC customers?": "Você identificou os clientes do SOC?",
        "Please specify your customers:": "Por favor, especifique seus clientes:",
        "Have you documented the main SOC customers?": "Você documentou os principais clientes do SOC?",
        "Do you differentiate output towards these specific customers?": "Você diferencia a saída para esses clientes específicos?",
        "Do you have service level agreements with these customers?": "Você tem acordos de nível de serviço com esses clientes?",
        "Do you send regular updates to your customers?": "Você envia atualizações regularmente para seus clientes?",
        "Do you measure and actively manage customer satisfaction?": "Você mede e gerencia ativamente a satisfação do cliente?",
        "Does the SOC have a formal charter document?": "O SOC possui um documento de estatuto formal?",
        "Please specify the elements of the charter document:": "Por favor, especifique os elementos do documento de estatuto:",
        "Is the SOC charter document regularly updated?": "O documento de estatuto do SOC é atualizado regularmente?",
        "Is the SOC charter document approved by business / CISO?": "O documento de estatuto do SOC é aprovado pelo negócio / CISO?",
        "Are all stakeholders familiar with the content of the SOC charter document?": "Todas as partes interessadas estão familiarizadas com o conteúdo do documento de estatuto do SOC?",
        "Does the SOC have a governance process implemented?": "O SOC possui um processo de governança implementado?",
        "Have all governance elements been identified?": "Todos os elementos de governança foram identificados?",
        "Please specify the identified governance elements": "Por favor, especifique os elementos de governança identificados",
        "Is cost management implemented?": "O gerenciamento de custos está implementado?",
        "Please specify the cost management elements": "Por favor, especifique os elementos de gerenciamento de custos",
        "Are all governance elements formally documented?": "Todos os elementos de governança estão formalmente documentados?",
        "Are SOC governance meetings held regularly?": "As reuniões de governança do SOC são realizadas regularmente?",
        "Is the governance process regularly reviewed?": "O processo de governança é revisado regularmente?",
        "Is the governance process aligned with all stakeholders?": "O processo de governança está alinhado com todas as partes interessadas?",
        "Is the SOC regularly audited or subjected to (external) assessments?": "O SOC é auditado regularmente ou submetido a avaliações (externas)?",
        "Is there an active cooperation with other SOCs (external)?": "Existe uma cooperação ativa com outros SOCs (externos)?",
        "Is there an information security policy in place that supports SOC activities?": "Existe uma política de segurança da informação que suporta as atividades do SOC?",
        "Has a SOC policy been created?": "Foi criada uma política do SOC?",
        "Please specify the elements of the SOC policy": "Por favor, especifique os elementos da política do SOC",
        "Is the SOC consulted in the creation and updating of operational security policy?": "O SOC é consultado na criação e atualização da política de segurança operacional?",
        "Is there a reporting policy for security incidents?": "Existe uma política de relatórios para incidentes de segurança?",
        "Is there a privacy policy regarding employee security monitoring?": "Existe uma política de privacidade em relação ao monitoramento de segurança de funcionários?",
        "Does the SOC operate in compliance with all applicable privacy laws and regulations?": "O SOC opera em conformidade com todas as leis e regulamentações de privacidade aplicáveis?",
        "Does the SOC cooperate with legal departments regarding privacy matters?": "O SOC coopera com os departamentos jurídicos em relação a questões de privacidade?",
        "Are there specific procedures for handling privacy-related investigations?": "Existem procedimentos específicos para lidar com investigações relacionadas à privacidade?",
        "Is the SOC aware of all information it processes that is subject to privacy regulations?": "O SOC está ciente de todas as informações que processa e que estão sujeitas a regulamentações de privacidade?",
        "Is a Privacy Impact Assessment (PIA) regularly conducted?": "Uma Avaliação de Impacto de Privacidade (PIA) é realizada regularmente?",
        "How many FTEs are there in your SOC?": "Quantos FTEs há no seu SOC?",
        "Do you use external / contracted staff in your SOC?": "Você usa funcionários externos / contratados em seu SOC?",
        "If yes, specify the number of external FTEs": "Se sim, especifique o número de FTEs externos",
        "Does the current SOC size meet the FTE requirements?": "O tamanho atual do SOC atende aos requisitos de FTE?",
        "Does the SOC meet the internal to external FTE ratio requirements?": "O SOC atende aos requisitos de proporção de FTEs internos para externos?",
        "Does the SOC meet the internal to external staff skill set requirements?": "O SOC atende aos requisitos de conjunto de habilidades de funcionários internos para externos?",
        "Are all positions filled?": "Todas as posições estão preenchidas?",
        "Do you have a recruitment process implemented?": "Você tem um processo de recrutamento implementado?",
        "Do you have a talent acquisition process implemented?": "Você tem um processo de aquisição de talentos implementado?",
        "Do you have specific KSAOs established for SOC staff?": "Você tem KSAOs específicos estabelecidos para o pessoal do SOC?",
        "Do you actively seek to create a psychologically safe environment for SOC staff?": "Você busca ativamente criar um ambiente psicologicamente seguro para o pessoal do SOC?"
    }
    
    # Adiciona o mapeamento manual
    mapping.update(manual_mapping)
    
    # Processa o JSON para adicionar mais traduções
    def process_section(section_data, domain_name=""):
        for section_name, section_content in section_data.items():
            if isinstance(section_content, dict):
                process_section(section_content, f"{domain_name}.{section_name}" if domain_name else section_name)
            elif isinstance(section_content, list):
                for question in section_content:
                    if isinstance(question, dict) and 'question' in question:
                        original_text = question['question']
                        translated_text = question.get('question', original_text)
                        guidance = question.get('guidance', '')
                        
                        mapping[original_text] = {
                            'translated_question': translated_text,
                            'translated_guidance': guidance
                        }
    
    for domain_name, domain_data in translations.items():
        if isinstance(domain_data, dict):
            process_section(domain_data, domain_name)
    
    return mapping

def update_database_complete(db_path):
    """Atualiza a base de dados com todas as traduções"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    translation_mapping = create_complete_translation_mapping()
    print(f"Mapeamento criado com {len(translation_mapping)} traduções")
    
    updated_count = 0
    
    # Atualiza questões
    cursor.execute("SELECT id, question_text FROM questions")
    questions = cursor.fetchall()
    
    for question_id, original_question in questions:
        if original_question in translation_mapping:
            translation = translation_mapping[original_question]
            
            if isinstance(translation, dict):
                translated_text = translation['translated_question']
                guidance = translation.get('translated_guidance', '')
            else:
                translated_text = translation
                guidance = ''
            
            cursor.execute("""
                UPDATE questions 
                SET question_text = ?, guidance = ?
                WHERE id = ?
            """, (translated_text, guidance, question_id))
            
            if cursor.rowcount > 0:
                updated_count += 1
                if updated_count <= 10:  # Mostra apenas as primeiras 10
                    print(f"Questão {question_id}: '{original_question[:50]}...' -> '{translated_text[:50]}...'")
    
    print(f"\nTotal de questões atualizadas: {updated_count}")
    
    # Atualiza opções de resposta
    option_translations = {
        "Yes": "Sim",
        "No": "Não",
        "Partially": "Parcialmente",
        "Not defined": "Não definidos",
        "Partially defined": "Parcialmente definidos",
        "Fully defined": "Totalmente definidos",
        "Not documented": "Não documentados",
        "Partially documented": "Parcialmente documentados",
        "Fully documented": "Totalmente documentados",
        "Not identified": "Não identificados",
        "Partially identified": "Parcialmente identificados",
        "Fully identified": "Totalmente identificados"
    }
    
    updated_options = 0
    cursor.execute("SELECT id, option_text FROM answer_options")
    options = cursor.fetchall()
    
    for option_id, original_option in options:
        if original_option in option_translations:
            translated_option = option_translations[original_option]
            cursor.execute("""
                UPDATE answer_options 
                SET option_text = ?
                WHERE id = ?
            """, (translated_option, option_id))
            
            if cursor.rowcount > 0:
                updated_options += 1
    
    print(f"Opções de resposta atualizadas: {updated_options}")
    
    conn.commit()
    conn.close()

def verify_final_translations(db_path):
    """Verifica as traduções finais"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("\nVerificando traduções finais:")
    
    # Verifica algumas questões
    cursor.execute("SELECT question_text FROM questions LIMIT 10")
    questions = cursor.fetchall()
    
    print("Primeiras 10 questões:")
    for i, question in enumerate(questions, 1):
        print(f"  {i}. {question[0][:80]}...")
    
    # Verifica algumas opções
    cursor.execute("SELECT DISTINCT option_text FROM answer_options LIMIT 10")
    options = cursor.fetchall()
    
    print("\nPrimeiras 10 opções de resposta:")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option[0]}")
    
    conn.close()

def main():
    print("=== Tradução Completa da Base de Dados ===")
    
    # Atualiza a base traduzida
    update_database_complete('soc_cmm_translated.db')
    
    # Verifica o resultado
    verify_final_translations('soc_cmm_translated.db')
    
    print("\n=== Processo concluído ===")
    print("Base traduzida: soc_cmm_translated.db")

if __name__ == "__main__":
    main() 