#!/usr/bin/env python3
import sqlite3
import os

def create_final_mapping():
    """Cria mapeamento final para as questões restantes"""
    mapping = {
        # Questões sobre hierarquia e estrutura
        "Is there a role-based hierarchy in your SOC?": {
            "translated_question": "Existe uma hierarquia baseada em funções no seu SOC?",
            "translated_guidance": "Hierarquia clara define responsabilidades e autoridade"
        },
        "Are there regular 1-on-1 meetings between the SOC manager and the employees?": {
            "translated_question": "Existem reuniões regulares 1-para-1 entre o gerente do SOC e os funcionários?",
            "translated_guidance": "Reuniões individuais promovem desenvolvimento e feedback"
        },
        
        # Questões sobre ferramentas e conhecimento
        "Is there effective tooling in place to support knowledge documentation and distribution?": {
            "translated_question": "Existem ferramentas eficazes para apoiar a documentação e distribuição do conhecimento?",
            "translated_guidance": "Ferramentas adequadas facilitam compartilhamento de conhecimento"
        },
        "Is there a reserved budget for education and training?": {
            "translated_question": "Existe um orçamento reservado para educação e treinamento?",
            "translated_guidance": "Orçamento dedicado garante desenvolvimento contínuo"
        },
        "Is there a reserved amount of time for education and training?": {
            "translated_question": "Existe uma quantidade de tempo reservada para educação e treinamento?",
            "translated_guidance": "Tempo dedicado permite aprendizado contínuo"
        },
        
        # Questões sobre relatórios
        "Are these reports tailored to the recipients?": {
            "translated_question": "Esses relatórios são personalizados para os destinatários?",
            "translated_guidance": "Relatórios personalizados atendem necessidades específicas"
        },
        
        # Questões sobre engenharia de detecção
        "Are there specific roles and requirements for detection engineers?": {
            "translated_question": "Existem funções e requisitos específicos para engenheiros de detecção?",
            "translated_guidance": "Funções específicas garantem expertise especializada"
        },
        "Is there active cooperation between the SOC analysts and the detection engineers?": {
            "translated_question": "Existe cooperação ativa entre os analistas do SOC e os engenheiros de detecção?",
            "translated_guidance": "Cooperação entre equipes melhora eficácia operacional"
        },
        "Is there active cooperation between the Threat Intelligence analysts and detection engineers?": {
            "translated_question": "Existe cooperação ativa entre os analistas de Threat Intelligence e engenheiros de detecção?",
            "translated_guidance": "Integração entre TI e detecção maximiza eficácia"
        },
        "Are there formal hand-over to the analyst team?": {
            "translated_question": "Existem transferências formais para a equipe de analistas?",
            "translated_guidance": "Transferências formais garantem continuidade operacional"
        },
        
        # Questões sobre processos e procedimentos
        "Is there a formal process for handling false positives?": {
            "translated_question": "Existe um processo formal para lidar com falsos positivos?",
            "translated_guidance": "Processo estruturado reduz ruído e melhora eficiência"
        },
        "Is there a formal process for handling false negatives?": {
            "translated_question": "Existe um processo formal para lidar com falsos negativos?",
            "translated_guidance": "Processo estruturado identifica lacunas de detecção"
        },
        "Is there a formal process for handling unknown threats?": {
            "translated_question": "Existe um processo formal para lidar com ameaças desconhecidas?",
            "translated_guidance": "Processo estruturado para ameaças emergentes"
        },
        "Is there a formal process for handling advanced persistent threats?": {
            "translated_question": "Existe um processo formal para lidar com ameaças persistentes avançadas?",
            "translated_guidance": "Processo especializado para APTs"
        },
        "Is there a formal process for handling insider threats?": {
            "translated_question": "Existe um processo formal para lidar com ameaças internas?",
            "translated_guidance": "Processo específico para ameaças de dentro da organização"
        },
        
        # Questões sobre tecnologia e infraestrutura
        "Is there a formal process for technology evaluation?": {
            "translated_question": "Existe um processo formal para avaliação de tecnologia?",
            "translated_guidance": "Avaliação sistemática garante escolhas adequadas"
        },
        "Is there a formal process for technology selection?": {
            "translated_question": "Existe um processo formal para seleção de tecnologia?",
            "translated_guidance": "Seleção criteriosa alinhada com necessidades"
        },
        "Is there a formal process for technology implementation?": {
            "translated_question": "Existe um processo formal para implementação de tecnologia?",
            "translated_guidance": "Implementação estruturada minimiza riscos"
        },
        "Is there a formal process for technology maintenance?": {
            "translated_question": "Existe um processo formal para manutenção de tecnologia?",
            "translated_guidance": "Manutenção preventiva garante operação contínua"
        },
        "Is there a formal process for technology retirement?": {
            "translated_question": "Existe um processo formal para aposentadoria de tecnologia?",
            "translated_guidance": "Aposentadoria planejada evita riscos de segurança"
        },
        
        # Questões sobre serviços
        "Is there a formal service catalog in place?": {
            "translated_question": "Existe um catálogo formal de serviços?",
            "translated_guidance": "Catálogo define escopo e expectativas"
        },
        "Is there a formal service level agreement process in place?": {
            "translated_question": "Existe um processo formal de acordo de nível de serviço?",
            "translated_guidance": "SLAs definem expectativas de qualidade"
        },
        "Is there a formal service delivery process in place?": {
            "translated_question": "Existe um processo formal de entrega de serviços?",
            "translated_guidance": "Entrega estruturada garante consistência"
        },
        "Is there a formal service monitoring process in place?": {
            "translated_question": "Existe um processo formal de monitoramento de serviços?",
            "translated_guidance": "Monitoramento contínuo identifica problemas"
        },
        "Is there a formal service improvement process in place?": {
            "translated_question": "Existe um processo formal de melhoria de serviços?",
            "translated_guidance": "Melhoria contínua aumenta eficiência"
        },
        
        # Questões sobre incidentes
        "Is there a formal incident detection process in place?": {
            "translated_question": "Existe um processo formal de detecção de incidentes?",
            "translated_guidance": "Detecção proativa reduz tempo de resposta"
        },
        "Is there a formal incident response process in place?": {
            "translated_question": "Existe um processo formal de resposta a incidentes?",
            "translated_guidance": "Resposta estruturada minimiza impacto"
        },
        "Is there a formal incident escalation process in place?": {
            "translated_question": "Existe um processo formal de escalação de incidentes?",
            "translated_guidance": "Escalação adequada garante atenção apropriada"
        },
        "Is there a formal incident communication process in place?": {
            "translated_question": "Existe um processo formal de comunicação de incidentes?",
            "translated_guidance": "Comunicação clara mantém stakeholders informados"
        },
        "Is there a formal incident closure process in place?": {
            "translated_question": "Existe um processo formal de encerramento de incidentes?",
            "translated_guidance": "Encerramento adequado garante resolução completa"
        },
        
        # Questões sobre análise
        "Is there a formal threat analysis process in place?": {
            "translated_question": "Existe um processo formal de análise de ameaças?",
            "translated_guidance": "Análise de ameaças informa estratégias de defesa"
        },
        "Is there a formal vulnerability analysis process in place?": {
            "translated_question": "Existe um processo formal de análise de vulnerabilidades?",
            "translated_guidance": "Análise de vulnerabilidades identifica pontos fracos"
        },
        "Is there a formal risk analysis process in place?": {
            "translated_question": "Existe um processo formal de análise de riscos?",
            "translated_guidance": "Análise de riscos fundamenta decisões"
        },
        "Is there a formal intelligence analysis process in place?": {
            "translated_question": "Existe um processo formal de análise de inteligência?",
            "translated_guidance": "Análise de inteligência antecipa ameaças"
        },
        "Is there a formal forensic analysis process in place?": {
            "translated_question": "Existe um processo formal de análise forense?",
            "translated_guidance": "Análise forense preserva evidências"
        },
        
        # Questões sobre comunicação
        "Is there a formal internal communication process in place?": {
            "translated_question": "Existe um processo formal de comunicação interna?",
            "translated_guidance": "Comunicação interna eficaz coordena equipes"
        },
        "Is there a formal external communication process in place?": {
            "translated_question": "Existe um processo formal de comunicação externa?",
            "translated_guidance": "Comunicação externa mantém stakeholders informados"
        },
        "Is there a formal stakeholder communication process in place?": {
            "translated_question": "Existe um processo formal de comunicação com stakeholders?",
            "translated_guidance": "Comunicação com stakeholders alinha expectativas"
        },
        "Is there a formal reporting process in place?": {
            "translated_question": "Existe um processo formal de relatórios?",
            "translated_guidance": "Relatórios estruturados informam decisões"
        },
        "Is there a formal notification process in place?": {
            "translated_question": "Existe um processo formal de notificação?",
            "translated_guidance": "Notificações oportunas alertam sobre eventos"
        }
    }
    
    return mapping

def update_final_questions(db_path):
    """Atualiza as questões finais em inglês"""
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
    """)
    
    english_questions = cursor.fetchall()
    print(f"Encontradas {len(english_questions)} questões ainda em inglês")
    
    # Carrega mapeamento final
    final_mapping = create_final_mapping()
    
    updated_count = 0
    not_found = []
    
    for question_id, original_question in english_questions:
        if original_question in final_mapping:
            translation = final_mapping[original_question]
            
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
        for question_id, question_text in not_found:
            print(f"  ID {question_id}: {question_text}")
    
    conn.commit()
    conn.close()
    return updated_count, not_found

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
    
    if remaining_english > 0:
        print(f"\nQuestões ainda em inglês:")
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
            LIMIT 5
        """)
        
        remaining_samples = cursor.fetchall()
        for question_id, question_text in remaining_samples:
            print(f"  ID {question_id}: {question_text}")
    
    conn.close()

def main():
    print("=== Tradução Final das Questões Restantes ===")
    
    # Verifica se a base traduzida existe
    if not os.path.exists("soc_cmm_translated.db"):
        print("Arquivo soc_cmm_translated.db não encontrado!")
        return
    
    # 1. Atualizar questões finais
    updated_count, not_found = update_final_questions("soc_cmm_translated.db")
    
    # 2. Verificar resultado final
    verify_final_result("soc_cmm_translated.db")
    
    print(f"\n=== Processo concluído ===")
    print(f"Questões atualizadas: {updated_count}")

if __name__ == "__main__":
    main() 