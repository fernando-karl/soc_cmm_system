import pandas as pd
import json
import re

def extract_soc_cmm_questions():
    excel_file_path = 'dataset/soc-cmm2.3.3-basic.xlsx'
    
    # Define the domain mapping based on sheet names
    domain_mapping = {
        'Business': ['Business - BSD', 'Business - CST', 'Business - CHT', 'Business - GOV', 'Business - PRV'],
        'People': ['People - EMP', 'People - R&H', 'People - PEM', 'People - KNM', 'People - T&E'],
        'Process': ['Process - MGT', 'Process - O&F', 'Process - RPT', 'Process - UCM', 'Process - DTE'],
        'Technology': ['Technology - SIM', 'Technology - NDR', 'Technology - EDR', 'Technology - A&O'],
        'Services': ['Services - SCM', 'Services - SIM', 'Services - A&F', 'Services - THR', 'Services - HNT', 'Services - VUL', 'Services - LOG'],
        'Results': ['Results - OVR', 'Results - CSF', 'Results - CSF2', 'Results - SHR']
    }
    
    # Aspect code mapping
    aspect_mapping = {
        'BSD': 'Business Strategy & Direction',
        'CST': 'Cost',
        'CHT': 'Charter',
        'GOV': 'Governance',
        'PRV': 'Privacy',
        'EMP': 'Employment',
        'R&H': 'Retention & Hiring',
        'PEM': 'Performance Management',
        'KNM': 'Knowledge Management',
        'T&E': 'Training & Education',
        'MGT': 'Management',
        'O&F': 'Operations & Functions',
        'RPT': 'Reporting',
        'UCM': 'Use Case Management',
        'DTE': 'Data & Technology Exchange',
        'SIM': 'Security Information Management',
        'NDR': 'Network Detection & Response',
        'EDR': 'Endpoint Detection & Response',
        'A&O': 'Analytics & Orchestration',
        'SCM': 'Service Catalog Management',
        'A&F': 'Analysis & Forensics',
        'THR': 'Threat Hunting & Research',
        'HNT': 'Hunting',
        'VUL': 'Vulnerability Management',
        'LOG': 'Logging',
        'OVR': 'Overview',
        'CSF': 'Critical Success Factors',
        'CSF2': 'Critical Success Factors 2',
        'SHR': 'Sharing'
    }
    
    all_data = {
        'domains': [],
        'aspects': [],
        'questions': [],
        'answer_options': []
    }
    
    domain_id = 1
    aspect_id = 1
    question_id = 1
    option_id = 1
    
    try:
        # Read all sheets
        excel_file = pd.ExcelFile(excel_file_path)
        
        for domain_name, sheet_names in domain_mapping.items():
            # Add domain
            all_data['domains'].append({
                'id': domain_id,
                'name': domain_name,
                'description': f'{domain_name} domain of SOC CMM',
                'order_index': domain_id
            })
            
            for sheet_name in sheet_names:
                if sheet_name in excel_file.sheet_names:
                    print(f"Processing sheet: {sheet_name}")
                    
                    # Extract aspect code from sheet name
                    aspect_code = sheet_name.split(' - ')[1] if ' - ' in sheet_name else sheet_name
                    aspect_name = aspect_mapping.get(aspect_code, aspect_code)
                    
                    # Add aspect
                    all_data['aspects'].append({
                        'id': aspect_id,
                        'domain_id': domain_id,
                        'name': aspect_name,
                        'code': aspect_code,
                        'description': f'{aspect_name} aspect of {domain_name}',
                        'order_index': len(all_data['aspects']) + 1
                    })
                    
                    # Read the sheet
                    df = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=None)
                    
                    # Look for questions and answers in the sheet
                    current_question = None
                    current_question_id = None
                    
                    for index, row in df.iterrows():
                        row_text = ' '.join([str(cell) for cell in row if pd.notna(cell) and str(cell).strip()])
                        
                        # Skip empty rows
                        if not row_text.strip():
                            continue
                            
                        # Look for question patterns
                        if any(keyword in row_text.lower() for keyword in ['question', 'q:', 'assessment', 'evaluate', 'how', 'what', 'which', 'does your']):
                            if len(row_text) > 20:  # Ensure it's substantial enough to be a question
                                current_question = row_text.strip()
                                current_question_id = question_id
                                
                                all_data['questions'].append({
                                    'id': question_id,
                                    'aspect_id': aspect_id,
                                    'question_text': current_question,
                                    'question_type': 'multiple_choice',
                                    'order_index': len(all_data['questions']) + 1
                                })
                                question_id += 1
                        
                        # Look for answer options (maturity levels)
                        elif current_question_id and any(keyword in row_text.lower() for keyword in ['level', 'maturity', 'initial', 'developing', 'defined', 'managed', 'optimized']):
                            # Try to extract maturity level
                            maturity_level = 0
                            if 'initial' in row_text.lower() or 'level 1' in row_text.lower():
                                maturity_level = 1
                            elif 'developing' in row_text.lower() or 'level 2' in row_text.lower():
                                maturity_level = 2
                            elif 'defined' in row_text.lower() or 'level 3' in row_text.lower():
                                maturity_level = 3
                            elif 'managed' in row_text.lower() or 'level 4' in row_text.lower():
                                maturity_level = 4
                            elif 'optimized' in row_text.lower() or 'level 5' in row_text.lower():
                                maturity_level = 5
                            
                            if maturity_level > 0:
                                all_data['answer_options'].append({
                                    'id': option_id,
                                    'question_id': current_question_id,
                                    'option_text': row_text.strip(),
                                    'maturity_level': maturity_level,
                                    'order_index': maturity_level
                                })
                                option_id += 1
                    
                    aspect_id += 1
            
            domain_id += 1
    
    except Exception as e:
        print(f"Error processing Excel file: {e}")
        return None
    
    # If we didn't find enough questions, create some sample questions for each aspect
    if len(all_data['questions']) < 10:
        print("Creating sample questions for each aspect...")
        question_id = 1
        option_id = 1
        all_data['questions'] = []
        all_data['answer_options'] = []
        
        for aspect in all_data['aspects']:
            # Create 2-3 sample questions per aspect
            sample_questions = [
                f"How would you rate the current maturity level of {aspect['name']} in your organization?",
                f"To what extent does your organization have documented processes for {aspect['name']}?",
                f"How effectively does your organization measure and improve {aspect['name']}?"
            ]
            
            for i, question_text in enumerate(sample_questions[:2]):  # Limit to 2 questions per aspect
                all_data['questions'].append({
                    'id': question_id,
                    'aspect_id': aspect['id'],
                    'question_text': question_text,
                    'question_type': 'multiple_choice',
                    'order_index': i + 1
                })
                
                # Create standard maturity level options
                maturity_options = [
                    ("Initial - Ad hoc, reactive approach with minimal documentation", 1),
                    ("Developing - Some processes defined but inconsistently applied", 2),
                    ("Defined - Documented processes that are consistently followed", 3),
                    ("Managed - Processes are measured and controlled", 4),
                    ("Optimized - Continuous improvement and optimization", 5)
                ]
                
                for option_text, maturity_level in maturity_options:
                    all_data['answer_options'].append({
                        'id': option_id,
                        'question_id': question_id,
                        'option_text': option_text,
                        'maturity_level': maturity_level,
                        'order_index': maturity_level
                    })
                    option_id += 1
                
                question_id += 1
    
    return all_data

# Extract the data
extracted_data = extract_soc_cmm_questions()

if extracted_data:
    # Save to JSON file
    with open('soc_cmm_complete_data-v2.json', 'w') as f:
        json.dump(extracted_data, f, indent=2)
    
    print(f"Extraction complete!")
    print(f"Domains: {len(extracted_data['domains'])}")
    print(f"Aspects: {len(extracted_data['aspects'])}")
    print(f"Questions: {len(extracted_data['questions'])}")
    print(f"Answer Options: {len(extracted_data['answer_options'])}")
else:
    print("Failed to extract data from Excel file")

