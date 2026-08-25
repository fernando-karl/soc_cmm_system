#!/usr/bin/env python3
import sqlite3
import re
import os

def create_comprehensive_mapping():
    """Cria um mapeamento abrangente para traduzir questões restantes"""
    mapping = {
        # Questões sobre SOC e funcionários
        "Does the SOC meet requirements for internal to external employee FTE ratio?": {
            "translated_question": "O SOC atende aos requisitos para a proporção de funcionários internos para externos?",
            "translated_guidance": "Proporção adequada garante controle interno e expertise externa"
        },
        "Does the SOC meet requirements for internal to external employee skillset?": {
            "translated_question": "O SOC atende aos requisitos para o conjunto de habilidades de funcionários internos e externos?",
            "translated_guidance": "Habilidades complementares entre equipes internas e externas"
        },
        "Do you have a recruitment process in place?": {
            "translated_question": "Você possui um processo de recrutamento?",
            "translated_guidance": "Processo de recrutamento estruturado garante contratações adequadas"
        },
        "Do you have a talent acquisition process in place?": {
            "translated_question": "Você possui um processo de aquisição de talentos?",
            "translated_guidance": "Aquisição estratégica de talentos para o SOC"
        },
        "Do you have specific KSAOs established for SOC personnel?": {
            "translated_question": "Você possui KSAs específicos estabelecidos para o pessoal do SOC?",
            "translated_guidance": "Conhecimentos, habilidades e aptidões definidos para cada função"
        },
        
        # Questões sobre processos e políticas
        "Do you have a formal performance management process in place?": {
            "translated_question": "Você possui um processo formal de gestão de desempenho?",
            "translated_guidance": "Gestão de desempenho estruturada melhora a produtividade"
        },
        "Do you have a formal career development process in place?": {
            "translated_question": "Você possui um processo formal de desenvolvimento de carreira?",
            "translated_guidance": "Desenvolvimento de carreira motiva e retém talentos"
        },
        "Do you have a formal training and development process in place?": {
            "translated_question": "Você possui um processo formal de treinamento e desenvolvimento?",
            "translated_guidance": "Treinamento contínuo mantém a equipe atualizada"
        },
        "Do you have a formal knowledge management process in place?": {
            "translated_question": "Você possui um processo formal de gestão do conhecimento?",
            "translated_guidance": "Gestão do conhecimento preserva expertise organizacional"
        },
        "Do you have a formal succession planning process in place?": {
            "translated_question": "Você possui um processo formal de planejamento de sucessão?",
            "translated_guidance": "Planejamento de sucessão garante continuidade operacional"
        },
        
        # Questões sobre tecnologia e ferramentas
        "Do you have a formal technology evaluation process in place?": {
            "translated_question": "Você possui um processo formal de avaliação de tecnologia?",
            "translated_guidance": "Avaliação sistemática de tecnologias garante escolhas adequadas"
        },
        "Do you have a formal technology selection process in place?": {
            "translated_question": "Você possui um processo formal de seleção de tecnologia?",
            "translated_guidance": "Seleção criteriosa de tecnologias alinhada com necessidades"
        },
        "Do you have a formal technology implementation process in place?": {
            "translated_question": "Você possui um processo formal de implementação de tecnologia?",
            "translated_guidance": "Implementação estruturada minimiza riscos e maximiza benefícios"
        },
        "Do you have a formal technology maintenance process in place?": {
            "translated_question": "Você possui um processo formal de manutenção de tecnologia?",
            "translated_guidance": "Manutenção preventiva garante operação contínua"
        },
        "Do you have a formal technology retirement process in place?": {
            "translated_question": "Você possui um processo formal de aposentadoria de tecnologia?",
            "translated_guidance": "Aposentadoria planejada evita riscos de segurança"
        },
        
        # Questões sobre serviços
        "Do you have a formal service catalog in place?": {
            "translated_question": "Você possui um catálogo formal de serviços?",
            "translated_guidance": "Catálogo de serviços define escopo e expectativas"
        },
        "Do you have a formal service level agreement process in place?": {
            "translated_question": "Você possui um processo formal de acordo de nível de serviço?",
            "translated_guidance": "SLAs definem expectativas de qualidade e prazo"
        },
        "Do you have a formal service delivery process in place?": {
            "translated_question": "Você possui um processo formal de entrega de serviços?",
            "translated_guidance": "Entrega estruturada garante consistência e qualidade"
        },
        "Do you have a formal service monitoring process in place?": {
            "translated_question": "Você possui um processo formal de monitoramento de serviços?",
            "translated_guidance": "Monitoramento contínuo identifica problemas proativamente"
        },
        "Do you have a formal service improvement process in place?": {
            "translated_question": "Você possui um processo formal de melhoria de serviços?",
            "translated_guidance": "Melhoria contínua aumenta eficiência e qualidade"
        },
        
        # Questões sobre incidentes
        "Do you have a formal incident detection process in place?": {
            "translated_question": "Você possui um processo formal de detecção de incidentes?",
            "translated_guidance": "Detecção proativa reduz tempo de resposta"
        },
        "Do you have a formal incident response process in place?": {
            "translated_question": "Você possui um processo formal de resposta a incidentes?",
            "translated_guidance": "Resposta estruturada minimiza impacto de incidentes"
        },
        "Do you have a formal incident escalation process in place?": {
            "translated_question": "Você possui um processo formal de escalação de incidentes?",
            "translated_guidance": "Escalação adequada garante atenção apropriada"
        },
        "Do you have a formal incident communication process in place?": {
            "translated_question": "Você possui um processo formal de comunicação de incidentes?",
            "translated_guidance": "Comunicação clara mantém stakeholders informados"
        },
        "Do you have a formal incident closure process in place?": {
            "translated_question": "Você possui um processo formal de encerramento de incidentes?",
            "translated_guidance": "Encerramento adequado garante resolução completa"
        },
        
        # Questões sobre análise
        "Do you have a formal threat analysis process in place?": {
            "translated_question": "Você possui um processo formal de análise de ameaças?",
            "translated_guidance": "Análise de ameaças informa estratégias de defesa"
        },
        "Do you have a formal vulnerability analysis process in place?": {
            "translated_question": "Você possui um processo formal de análise de vulnerabilidades?",
            "translated_guidance": "Análise de vulnerabilidades identifica pontos fracos"
        },
        "Do you have a formal risk analysis process in place?": {
            "translated_question": "Você possui um processo formal de análise de riscos?",
            "translated_guidance": "Análise de riscos fundamenta decisões de segurança"
        },
        "Do you have a formal intelligence analysis process in place?": {
            "translated_question": "Você possui um processo formal de análise de inteligência?",
            "translated_guidance": "Análise de inteligência antecipa ameaças"
        },
        "Do you have a formal forensic analysis process in place?": {
            "translated_question": "Você possui um processo formal de análise forense?",
            "translated_guidance": "Análise forense preserva evidências para investigação"
        },
        
        # Questões sobre comunicação
        "Do you have a formal internal communication process in place?": {
            "translated_question": "Você possui um processo formal de comunicação interna?",
            "translated_guidance": "Comunicação interna eficaz coordena equipes"
        },
        "Do you have a formal external communication process in place?": {
            "translated_question": "Você possui um processo formal de comunicação externa?",
            "translated_guidance": "Comunicação externa mantém stakeholders informados"
        },
        "Do you have a formal stakeholder communication process in place?": {
            "translated_question": "Você possui um processo formal de comunicação com stakeholders?",
            "translated_guidance": "Comunicação com stakeholders alinha expectativas"
        },
        "Do you have a formal reporting process in place?": {
            "translated_question": "Você possui um processo formal de relatórios?",
            "translated_guidance": "Relatórios estruturados informam decisões"
        },
        "Do you have a formal notification process in place?": {
            "translated_question": "Você possui um processo formal de notificação?",
            "translated_guidance": "Notificações oportunas alertam sobre eventos importantes"
        }
    }
    
    return mapping

def translate_common_patterns(question_text):
    """Traduz padrões comuns em questões"""
    patterns = {
        r"Do you have a (.+) in place\?": r"Você possui um \1?",
        r"Does the (.+) have a (.+) in place\?": r"O \1 possui um \2?",
        r"Is there a (.+) in place\?": r"Existe um \1?",
        r"Are there (.+) in place\?": r"Existem \1?",
        r"Do you (.+)\?": r"Você \1?",
        r"Does the (.+) (.+)\?": r"O \1 \2?",
        r"Is the (.+) (.+)\?": r"O \1 \2?",
        r"Are the (.+) (.+)\?": r"Os \1 \2?",
        r"Does your (.+) (.+)\?": r"Seu \1 \2?",
        r"Is your (.+) (.+)\?": r"Seu \1 \2?",
        r"Are your (.+) (.+)\?": r"Seus \1 \2?",
        r"Have you (.+)\?": r"Você tem \1?",
        r"Has the (.+) (.+)\?": r"O \1 \2?",
        r"Have the (.+) (.+)\?": r"Os \1 \2?"
    }
    
    translated = question_text
    for pattern, replacement in patterns.items():
        translated = re.sub(pattern, replacement, translated, flags=re.IGNORECASE)
    
    return translated

def update_remaining_questions(db_path):
    """Atualiza todas as questões restantes em inglês"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Busca todas as questões que ainda estão em inglês
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
    print(f"Encontradas {len(english_questions)} questões ainda em inglês")
    
    # Carrega mapeamento abrangente
    comprehensive_mapping = create_comprehensive_mapping()
    
    updated_count = 0
    pattern_translated = 0
    
    for question_id, original_question in english_questions:
        translated_question = None
        translated_guidance = ""
        
        # 1. Tenta mapeamento específico
        if original_question in comprehensive_mapping:
            translation = comprehensive_mapping[original_question]
            translated_question = translation['translated_question']
            translated_guidance = translation['translated_guidance']
            updated_count += 1
            print(f"✓ Mapeamento específico - Questão {question_id}: '{original_question[:50]}...' -> '{translated_question[:50]}...'")
        
        # 2. Se não encontrou, tenta tradução por padrões
        elif not translated_question:
            translated_question = translate_common_patterns(original_question)
            if translated_question != original_question:
                pattern_translated += 1
                print(f"✓ Tradução por padrão - Questão {question_id}: '{original_question[:50]}...' -> '{translated_question[:50]}...'")
        
        # 3. Atualiza se encontrou tradução
        if translated_question and translated_question != original_question:
            cursor.execute("""
                UPDATE questions 
                SET question_text = ?, guidance = ?
                WHERE id = ?
            """, (translated_question, translated_guidance, question_id))
    
    print(f"\nResumo:")
    print(f"- Questões atualizadas por mapeamento específico: {updated_count}")
    print(f"- Questões atualizadas por padrões: {pattern_translated}")
    print(f"- Total de questões atualizadas: {updated_count + pattern_translated}")
    
    conn.commit()
    conn.close()
    return updated_count + pattern_translated

def verify_final_result(db_path):
    """Verifica o resultado final"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Conta questões ainda em inglês
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
    
    # Conta total de questões
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_questions = cursor.fetchone()[0]
    
    print(f"\nVerificação final:")
    print(f"- Total de questões: {total_questions}")
    print(f"- Questões ainda em inglês: {remaining_english}")
    print(f"- Questões traduzidas: {total_questions - remaining_english}")
    print(f"- Percentual traduzido: {((total_questions - remaining_english) / total_questions * 100):.1f}%")
    
    # Mostra algumas questões traduzidas
    cursor.execute("""
        SELECT question_text 
        FROM questions 
        WHERE question_text NOT LIKE '%Is there%' 
           AND question_text NOT LIKE '%Are there%' 
           AND question_text NOT LIKE '%Do you%' 
           AND question_text NOT LIKE '%Does the%' 
           AND question_text NOT LIKE '%Is the%' 
           AND question_text NOT LIKE '%Are the%' 
           AND question_text NOT LIKE '%Does your%' 
           AND question_text NOT LIKE '%Is your%' 
           AND question_text NOT LIKE '%Are your%'
        ORDER BY id
        LIMIT 10
    """)
    
    translated_samples = cursor.fetchall()
    print(f"\nExemplos de questões traduzidas:")
    for i, (question,) in enumerate(translated_samples, 1):
        print(f"  {i}. {question[:80]}...")
    
    conn.close()

def main():
    print("=== Tradução Abrangente de Questões ===")
    
    # Verifica se a base traduzida existe
    if not os.path.exists("soc_cmm_translated.db"):
        print("Arquivo soc_cmm_translated.db não encontrado!")
        return
    
    # 1. Atualizar questões restantes
    total_updated = update_remaining_questions("soc_cmm_translated.db")
    
    # 2. Verificar resultado final
    verify_final_result("soc_cmm_translated.db")
    
    print(f"\n=== Processo concluído ===")
    print(f"Total de questões atualizadas: {total_updated}")

if __name__ == "__main__":
    main() 