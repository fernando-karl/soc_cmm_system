#!/usr/bin/env python3
import sqlite3
import json
import re

def load_json_data():
    """Carrega os dados do JSON para mapeamento"""
    with open('soc_cmm_questions-port.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_aspect_mapping():
    """Cria mapeamento de textos para códigos de aspecto"""
    mapping = {}
    
    # Mapeamento manual baseado na estrutura do JSON
    # Domínio Negócio (1)
    mapping["Drivers de Negócio"] = "1.1"
    mapping["Clientes"] = "1.2"
    mapping["Estatuto"] = "1.3"
    mapping["Governança"] = "1.4"
    mapping["Privacidade e Política"] = "1.5"
    
    # Domínio Pessoas (2)
    mapping["Funcionários"] = "2.1"
    mapping["Funções e Hierarquia"] = "2.2"
    mapping["Gerenciamento de Pessoas"] = "2.3"
    mapping["Gerenciamento do Conhecimento"] = "2.4"
    mapping["Treinamento e Educação"] = "2.5"
    
    # Domínio Processo (3)
    mapping["Gerenciamento"] = "3.1"
    mapping["Coleta de Dados"] = "3.2"
    mapping["Análise"] = "3.3"
    mapping["Resposta"] = "3.4"
    mapping["Gerenciamento de Casos"] = "3.5"
    mapping["Comunicação"] = "3.6"
    
    # Domínio Tecnologia (4)
    mapping["SIEM / UEBA"] = "4.1"
    mapping["NDR"] = "4.2"
    mapping["EDR"] = "4.3"
    
    # Domínio Serviços (5)
    mapping["Monitoramento de Segurança"] = "5.1"
    mapping["Gerenciamento de Incidentes de Segurança"] = "5.2"
    mapping["Análise de Segurança"] = "5.3"
    mapping["Inteligência de Ameaças"] = "5.4"
    mapping["Caça a Ameaças"] = "5.5"
    mapping["Gerenciamento de Vulnerabilidades"] = "5.6"
    mapping["Gerenciamento de Logs"] = "5.7"
    
    # Mapeamentos específicos para subaspectos
    mapping["Maturidade"] = "4.1"  # Para SIEM/UEBA
    mapping["Capacidade"] = "4.1"  # Para SIEM/UEBA
    
    return mapping

def fix_aspect_ids():
    """Corrige os aspect_id que são textos para códigos numéricos"""
    conn = sqlite3.connect('soc_cmm_portuguese.db')
    cursor = conn.cursor()
    
    # Carrega o mapeamento
    mapping = create_aspect_mapping()
    
    # Primeiro, vamos ver quais aspect_id precisam ser corrigidos
    cursor.execute("SELECT DISTINCT aspect_id FROM questions WHERE aspect_id NOT LIKE '%.%'")
    text_aspect_ids = [row[0] for row in cursor.fetchall()]
    
    print("Aspect IDs que precisam ser corrigidos:")
    for aspect_id in text_aspect_ids:
        print(f"  {aspect_id}")
    
    # Contador de atualizações
    updated_count = 0
    
    # Atualiza os aspect_id baseado no mapeamento
    for text_id, numeric_id in mapping.items():
        cursor.execute("""
            UPDATE questions 
            SET aspect_id = ? 
            WHERE aspect_id = ?
        """, (numeric_id, text_id))
        
        if cursor.rowcount > 0:
            print(f"Atualizado: '{text_id}' -> '{numeric_id}' ({cursor.rowcount} registros)")
            updated_count += cursor.rowcount
    
    # Tratamento especial para aspect_id que são nomes de ferramentas/serviços
    # Estes devem ser mapeados para os aspectos corretos baseado no contexto
    
    # Para ferramentas SOC (domínio Tecnologia)
    tech_tools = {
        "SIEM / UEBA": "4.1",
        "NDR": "4.2", 
        "EDR": "4.3",
        "SOAR": "4.4"  # Assumindo que SOAR é 4.4
    }
    
    for tool, aspect_id in tech_tools.items():
        cursor.execute("""
            UPDATE questions 
            SET aspect_id = ? 
            WHERE aspect_id = ?
        """, (aspect_id, tool))
        
        if cursor.rowcount > 0:
            print(f"Atualizado ferramenta: '{tool}' -> '{aspect_id}' ({cursor.rowcount} registros)")
            updated_count += cursor.rowcount
    
    # Para serviços SOC (domínio Serviços)
    service_names = {
        "Monitoramento de Segurança": "5.1",
        "Gerenciamento de Incidentes de Segurança": "5.2",
        "Análise de Segurança": "5.3",
        "Inteligência de Ameaças": "5.4",
        "Caça a Ameaças": "5.5",
        "Gerenciamento de Vulnerabilidades": "5.6",
        "Gerenciamento de Logs": "5.7"
    }
    
    for service, aspect_id in service_names.items():
        cursor.execute("""
            UPDATE questions 
            SET aspect_id = ? 
            WHERE aspect_id = ?
        """, (aspect_id, service))
        
        if cursor.rowcount > 0:
            print(f"Atualizado serviço: '{service}' -> '{aspect_id}' ({cursor.rowcount} registros)")
            updated_count += cursor.rowcount
    
    # Para campos de perfil (domínio Geral)
    profile_fields = {
        "Detalhes da Avaliação.Data da avaliação": "0.1",
        "Detalhes da Avaliação.Nome(s)": "0.2",
        "Detalhes da Avaliação.Departamento(s)": "0.3",
        "Detalhes da Avaliação.Propósito pretendido da avaliação": "0.4",
        "Detalhes da Avaliação.Tipo de avaliação": "0.5",
        "Detalhes da Avaliação.Estilo de avaliação": "0.6",
        "Perfil da Organização e SOC.Tamanho da empresa (FTE)": "0.7",
        "Perfil da Organização e SOC.Setor": "0.8",
        "Perfil da Organização e SOC.Número de anos de operações do SOC": "0.9",
        "Perfil da Organização e SOC.Tamanho do SOC (FTEs)": "0.10",
        "Perfil da Organização e SOC.Modelo organizacional do SOC": "0.11",
        "Perfil da Organização e SOC.Região do SOC": "0.12",
        "Perfil da Organização e SOC.Operação geográfica": "0.13",
        "Maturidade Alvo.Domínio de negócio": "0.14",
        "Maturidade Alvo.Domínio de pessoas": "0.15",
        "Maturidade Alvo.Domínio de processo": "0.16",
        "Maturidade Alvo.Domínio de tecnologia": "0.17",
        "Maturidade Alvo.Domínio de serviços": "0.18",
        "Capacidade Alvo.Domínio de tecnologia": "0.19",
        "Capacidade Alvo.Domínio de serviços": "0.20"
    }
    
    for field, aspect_id in profile_fields.items():
        cursor.execute("""
            UPDATE questions 
            SET aspect_id = ? 
            WHERE aspect_id = ?
        """, (aspect_id, field))
        
        if cursor.rowcount > 0:
            print(f"Atualizado campo de perfil: '{field}' -> '{aspect_id}' ({cursor.rowcount} registros)")
            updated_count += cursor.rowcount
    
    # Verifica se ainda há aspect_id como texto
    cursor.execute("SELECT DISTINCT aspect_id FROM questions WHERE aspect_id NOT LIKE '%.%'")
    remaining_text_aspect_ids = [row[0] for row in cursor.fetchall()]
    
    if remaining_text_aspect_ids:
        print("\nAspect IDs que ainda precisam ser corrigidos:")
        for aspect_id in remaining_text_aspect_ids:
            print(f"  {aspect_id}")
    else:
        print("\nTodos os aspect_id foram corrigidos!")
    
    print(f"\nTotal de registros atualizados: {updated_count}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Corrigindo aspect_id que são textos...")
    fix_aspect_ids()
    print("Processo concluído!") 