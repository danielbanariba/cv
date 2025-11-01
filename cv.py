from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import json
import argparse

# LÍMITES ESTÁNDAR PARA EL CONTENIDO DEL CV
CV_LIMITS = {
    "profile_length": 500,             # Caracteres en el perfil
    "max_jobs": 3,                     # Máximo de trabajos en experiencia
    "max_responsibilities": 5,         # Máximo de responsabilidades por trabajo
    "max_projects": 4,                 # Máximo de proyectos
    "max_education": 3,                # Máximo de entradas de educación
    "max_certifications": 4,           # Máximo de certificaciones
    "max_skills_per_category": 8,      # Máximo de habilidades por categoría
    "max_char_per_responsibility": 120 # Máximo caracteres por responsabilidad
}

def load_json(json_file):
    """Carga datos desde un archivo JSON"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar JSON: {e}")
        return None

def get_value(data, key, default=""):
    """Obtiene un valor del diccionario de forma segura"""
    if isinstance(data, dict):
        return data.get(key, default)
    return default

def validate_cv_content(data):
    """
    Valida si el contenido del CV excede los límites recomendados.
    Devuelve (is_valid, issues), donde is_valid es un booleano y
    issues es una lista de problemas encontrados.
    """
    issues = []
    
    # Validar perfil
    profile = get_value(data, 'profile', "")
    if len(profile) > CV_LIMITS["profile_length"]:
        issues.append(f"El perfil excede el límite de {CV_LIMITS['profile_length']} caracteres (tiene {len(profile)} caracteres)")
    
    # Validar experiencia laboral
    experience = get_value(data, 'experience', [])
    if len(experience) > CV_LIMITS["max_jobs"]:
        issues.append(f"El CV tiene {len(experience)} trabajos, excediendo el límite de {CV_LIMITS['max_jobs']}")
    
    for idx, job in enumerate(experience):
        responsibilities = get_value(job, 'responsibilities', [])
        if len(responsibilities) > CV_LIMITS["max_responsibilities"]:
            issues.append(f"El trabajo '{get_value(job, 'position', f'Trabajo {idx+1}')}' tiene {len(responsibilities)} responsabilidades, excediendo el límite de {CV_LIMITS['max_responsibilities']}")
        
        # Validar longitud de cada responsabilidad
        for resp_idx, resp in enumerate(responsibilities):
            if len(resp) > CV_LIMITS["max_char_per_responsibility"]:
                issues.append(f"La responsabilidad #{resp_idx+1} en '{get_value(job, 'position', f'Trabajo {idx+1}')}' excede {CV_LIMITS['max_char_per_responsibility']} caracteres")
    
    # Validar proyectos
    projects = get_value(data, 'projects', [])
    if len(projects) > CV_LIMITS["max_projects"]:
        issues.append(f"El CV tiene {len(projects)} proyectos, excediendo el límite de {CV_LIMITS['max_projects']}")
    
    # Validar educación
    education = get_value(data, 'education', [])
    if len(education) > CV_LIMITS["max_education"]:
        issues.append(f"El CV tiene {len(education)} entradas de educación, excediendo el límite de {CV_LIMITS['max_education']}")
    
    # Validar certificaciones
    certifications = get_value(data, 'certifications', [])
    if len(certifications) > CV_LIMITS["max_certifications"]:
        issues.append(f"El CV tiene {len(certifications)} certificaciones, excediendo el límite de {CV_LIMITS['max_certifications']}")
    
    # Validar habilidades
    skills = get_value(data, 'skills', {})
    for skill_cat, skill_list in skills.items():
        # Aproximar el número de habilidades contando por comas
        if skill_list:
            num_skills = len(skill_list.split(',')) if isinstance(skill_list, str) else 1
            if num_skills > CV_LIMITS["max_skills_per_category"]:
                issues.append(f"La categoría de habilidades '{skill_cat}' tiene aproximadamente {num_skills} habilidades, excediendo el límite de {CV_LIMITS['max_skills_per_category']}")
    
    # Determinar si el CV es válido
    is_valid = len(issues) == 0
    
    return is_valid, issues

def setup_styles(base_font_size=10):
    """Configura los estilos con tamaño de fuente ajustable"""
    styles = getSampleStyleSheet()
    styles['Normal'].fontSize = base_font_size
    styles['Normal'].spaceBefore = 1
    styles['Normal'].spaceAfter = 1

    # Añadir estilos personalizados
    styles.add(ParagraphStyle(name='Header', fontName='Helvetica-Bold', fontSize=base_font_size+6, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='SubHeader', fontName='Helvetica', fontSize=base_font_size, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='SectionTitle', fontName='Helvetica-Bold', fontSize=base_font_size, spaceBefore=2, spaceAfter=1, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='SmallText', fontName='Helvetica', fontSize=base_font_size, alignment=TA_RIGHT, spaceAfter=1))
    styles.add(ParagraphStyle(name='ProjectTitle', fontName='Helvetica-Bold', fontSize=base_font_size, spaceAfter=1))
    styles.add(ParagraphStyle(name='ProjectDescription', fontName='Helvetica', fontSize=base_font_size, leftIndent=20, spaceAfter=2))
    styles.add(ParagraphStyle(name='BulletPoint', parent=styles['Normal'], 
                            leftIndent=20, 
                            bulletIndent=10, 
                            spaceBefore=0,
                            spaceAfter=1))
    styles.add(ParagraphStyle(name='CompanyName', fontName='Helvetica-Bold', fontSize=base_font_size, leading=14, spaceAfter=1))
    styles.add(ParagraphStyle(name='Location', fontName='Helvetica', fontSize=base_font_size, leading=14, alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='JobPosition', fontName='Helvetica', fontSize=base_font_size, leading=14, textColor=colors.gray, spaceAfter=2))
    styles.add(ParagraphStyle(name='ExperienceBullet', fontName='Helvetica', fontSize=base_font_size, leftIndent=15, firstLineIndent=-15, 
                               leading=12, spaceBefore=0, spaceAfter=1, bulletIndent=0, bulletText='•', textColor=colors.black))
    styles.add(ParagraphStyle(name='Technologies', fontName='Helvetica-Oblique', fontSize=base_font_size-1, leftIndent=20, spaceAfter=3, textColor=colors.gray))
    
    return styles

def build_cv_content(data, styles):
    """Construye el contenido del CV y lo devuelve como una lista de elementos"""
    story = []
    
    # 1. INFORMACIÓN PERSONAL
    personal_info = get_value(data, 'personal_info', {})
    
    # Nombre
    name = get_value(personal_info, 'name', "Nombre no especificado")
    story.append(Paragraph(name, styles['Header']))
    story.append(Spacer(1, 0.1*inch))
    
    # Información de contacto
    location = get_value(personal_info, 'location')
    if location:
        story.append(Paragraph(location, styles['SubHeader']))
    
    email = get_value(personal_info, 'email')
    phone = get_value(personal_info, 'phone')
    if email and phone:
        contact_info = f"{email} • {phone}"
    elif email:
        contact_info = email
    elif phone:
        contact_info = phone
    else:
        contact_info = ""
    
    if contact_info:
        story.append(Paragraph(contact_info, styles['SubHeader']))
    
    # Enlaces
    website = get_value(personal_info, 'website')
    github = get_value(personal_info, 'github')
    linkedin = get_value(personal_info, 'linkedin')
    
    links_parts = []
    if website:
        links_parts.append(f"<a href='{website}' color='blue'>{website}</a>")
    if github:
        links_parts.append(f"<a href='{github}' color='blue'>GitHub</a>")
    if linkedin:
        links_parts.append(f"<a href='{linkedin}' color='blue'>LinkedIn</a>")
    
    if links_parts:
        links = " • ".join(links_parts)
        story.append(Paragraph(links, styles['SubHeader']))
    
    story.append(Spacer(1, 0.05*inch))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.05*inch))
    
    # 2. PERFIL PROFESIONAL (opcional)
    profile = get_value(data, 'profile')
    if profile:
        story.append(Paragraph(profile, styles['Normal']))
        story.append(Spacer(1, 0.05*inch))
    
    # 3. SECCIONES DEL CV
    section_titles = get_value(data, 'section_titles', {})
    
    # 3.1 EXPERIENCIA LABORAL
    experience = get_value(data, 'experience', [])
    if experience:
        experience_title = get_value(section_titles, 'experience', "EXPERIENCIA LABORAL")
        story.append(Paragraph(experience_title, styles['SectionTitle']))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
        
        for job in experience:
            company = get_value(job, 'company', "")
            date_range = get_value(job, 'date_range', "")
            
            if company or date_range:
                exp_table_data = [
                    [Paragraph(f"<b>{company}</b>", styles['CompanyName']) if company else "",
                     Paragraph(date_range, styles['Location']) if date_range else ""]
                ]
                exp_table = Table(exp_table_data, colWidths=[4*inch, 3*inch])
                exp_table.setStyle(TableStyle([
                    ('ALIGN', (0,0), (0,-1), 'LEFT'),
                    ('ALIGN', (-1,0), (-1,-1), 'RIGHT'),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                    ('TOPPADDING', (0,0), (-1,-1), 3),
                ]))
                story.append(exp_table)
            
            position = get_value(job, 'position', "")
            if position:
                story.append(Paragraph(position, styles['JobPosition']))
            
            responsibilities = get_value(job, 'responsibilities', [])
            for point in responsibilities:
                story.append(Paragraph(point, styles['ExperienceBullet']))
            
            technologies = get_value(job, 'technologies', "")
            if technologies:
                story.append(Paragraph(f"<i>Tecnologías:</i> {technologies}", styles['Technologies']))
            
            story.append(Spacer(1, 0.05*inch))
    
    # 3.2 HABILIDADES TÉCNICAS
    skills = get_value(data, 'skills', {})
    if skills:
        skills_title = get_value(section_titles, 'skills', "HABILIDADES TÉCNICAS")
        story.append(Paragraph(skills_title, styles['SectionTitle']))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
        story.append(Spacer(1, 0.05*inch))
        
        skill_labels = get_value(data, 'skill_labels', {
            "languages": "Lenguajes",
            "frameworks": "Frameworks",
            "databases": "Bases de Datos",
            "cloud": "Cloud & Infraestructura",
            "testing": "Testing & QA",
            "other": "Otros"
        })
        
        # Crear lista de skills (solo incluir los que existen)
        skill_items = []
        
        for key, label in skill_labels.items():
            if key in skills and skills[key]:
                skill_items.append(f"• {label}: {skills[key]}")
        
        for skill in skill_items:
            story.append(Paragraph(skill, styles['BulletPoint']))
        
        story.append(Spacer(1, 0.05*inch))
    
    # 3.3 PROYECTOS DESTACADOS
    projects = get_value(data, 'projects', [])
    if projects:
        projects_title = get_value(section_titles, 'projects', "PROYECTOS DESTACADOS")
        story.append(Paragraph(projects_title, styles['SectionTitle']))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
        story.append(Spacer(1, 0.05*inch))
        
        for project in projects:
            title = get_value(project, 'title', "")
            if title:
                story.append(Paragraph(title, styles['ProjectTitle']))
            
            description = get_value(project, 'description', "")
            if description:
                story.append(Paragraph(description, styles['ProjectDescription']))
            
            technologies = get_value(project, 'technologies', "")
            if technologies:
                story.append(Paragraph(f"<i>Tecnologías:</i> {technologies}", styles['Technologies']))
        
        story.append(Spacer(1, 0.05*inch))
    
    # 3.4 EDUCACIÓN
    education = get_value(data, 'education', [])
    if education:
        education_title = get_value(section_titles, 'education', "EDUCACIÓN")
        story.append(Paragraph(education_title, styles['SectionTitle']))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
        story.append(Spacer(1, 0.05*inch))
        
        education_data = []
        for edu in education:
            institution = get_value(edu, 'institution', "")
            location = get_value(edu, 'location', "")
            degree = get_value(edu, 'degree', "")
            date_range = get_value(edu, 'date_range', "")
            
            if institution or location:
                education_data.append([
                    Paragraph(institution, styles['ProjectTitle']) if institution else "",
                    Paragraph(location, styles['SmallText']) if location else ""
                ])
            
            if degree or date_range:
                education_data.append([
                    Paragraph(degree, styles['ProjectDescription']) if degree else "",
                    Paragraph(date_range, styles['SmallText']) if date_range else ""
                ])
            
            education_data.append([Spacer(1, 0.05*inch), Spacer(1, 0.05*inch)])
        
        if education_data:
            if len(education_data) > 0:
                education_data = education_data[:-1]  # Eliminar último espaciador
                
                t = Table(education_data, colWidths=[5*inch, 2*inch])
                t.setStyle(TableStyle([
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('ALIGN', (0,0), (0,-1), 'LEFT'),
                    ('ALIGN', (1,0), (1,-1), 'RIGHT'),
                ]))
                story.append(t)
        
        story.append(Spacer(1, 0.05*inch))
    
    # 3.5 CERTIFICACIONES
    certifications = get_value(data, 'certifications', [])
    if certifications:
        certs_title = get_value(section_titles, 'certifications', "CERTIFICACIONES Y CURSOS ADICIONALES")
        story.append(Paragraph(certs_title, styles['SectionTitle']))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
        story.append(Spacer(1, 0.05*inch))
        
        for cert in certifications:
            story.append(Paragraph(f"• {cert}", styles['BulletPoint']))
        
        story.append(Spacer(1, 0.05*inch))
    
    # 3.6 IDIOMAS
    languages = get_value(data, 'languages', [])
    if languages:
        languages_title = get_value(section_titles, 'languages', "IDIOMAS")
        story.append(Paragraph(languages_title, styles['SectionTitle']))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
        story.append(Spacer(1, 0.05*inch))

        for lang in languages:
            if isinstance(lang, dict):
                language = get_value(lang, 'language', '')
                level = get_value(lang, 'level', '')
                if language and level:
                    story.append(Paragraph(f"• {language}: {level}", styles['BulletPoint']))
                elif language:
                    story.append(Paragraph(f"• {language}", styles['BulletPoint']))
            else:
                story.append(Paragraph(f"• {lang}", styles['BulletPoint']))

        story.append(Spacer(1, 0.05*inch))

    # 3.7 REFERENCIAS
    references = get_value(data, 'references', [])
    if references:
        references_title = get_value(section_titles, 'references', "REFERENCIAS")
        story.append(Paragraph(references_title, styles['SectionTitle']))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
        story.append(Spacer(1, 0.05*inch))

        for ref in references:
            name = get_value(ref, 'name', "")
            position = get_value(ref, 'position', "")
            company = get_value(ref, 'company', "")
            phone = get_value(ref, 'phone', "")

            if name:
                story.append(Paragraph(f"<b>{name}</b>", styles['ProjectTitle']))

            if position and company:
                story.append(Paragraph(f"{position} - {company}", styles['Normal']))
            elif position:
                story.append(Paragraph(position, styles['Normal']))
            elif company:
                story.append(Paragraph(company, styles['Normal']))

            if phone:
                story.append(Paragraph(f"Teléfono: {phone}", styles['Normal']))

            story.append(Spacer(1, 0.1*inch))

    return story

def generate_cv_pdf(data, output_filename):
    """Genera un PDF del CV usando los datos proporcionados"""
    # Primero validar si el contenido del CV está dentro de los límites recomendados
    is_valid, issues = validate_cv_content(data)
    
    if not is_valid:
        print("\n┌─ ADVERTENCIA: ───────────────────────────────────────────────────────")
        print("│ Tiene que reducir un poco el contenido del CV.")
        print("│")
        print("│ Problemas detectados:")
        for issue in issues:
            print(f"│ • {issue}")
        print("│")
        print("│ Recomendaciones para un CV efectivo de una página:")
        print(f"│ • Perfil profesional: máximo {CV_LIMITS['profile_length']} caracteres")
        print(f"│ • Experiencia laboral: máximo {CV_LIMITS['max_jobs']} trabajos")
        print(f"│ • Responsabilidades: máximo {CV_LIMITS['max_responsibilities']} por trabajo")
        print(f"│ • Proyectos: máximo {CV_LIMITS['max_projects']}")
        print(f"│ • Educación: máximo {CV_LIMITS['max_education']} entradas")
        print(f"│ • Certificaciones: máximo {CV_LIMITS['max_certifications']}")
        print("└─────────────────────────────────────────────────────────────────────")
        print("\nSe generará el CV de todos modos, pero puede que no quepa en una página.\n")
    
    # Configuración del documento
    width, height = 8.5*inch, 11.2*inch
    doc = SimpleDocTemplate(
        output_filename, 
        pagesize=(width, height),
        rightMargin=0.5*inch, 
        leftMargin=0.5*inch,
        topMargin=0.2*inch, 
        bottomMargin=0.5*inch
    )
    
    # Crear y configurar estilos
    styles = setup_styles(base_font_size=10)
    
    # Generar contenido del CV
    story = build_cv_content(data, styles)
    
    # Construir el documento
    try:
        doc.build(story)
        print(f"CV generado correctamente. Verifica el archivo '{output_filename}'")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")
        print("El contenido es demasiado extenso para caber en una página con el formato estándar.")
        print("Por favor, reduzca el contenido según las recomendaciones anteriores.")

def main():
    parser = argparse.ArgumentParser(description="Generador de CV desde archivo JSON")
    parser.add_argument("--json-file", help="Archivo JSON con los datos del CV")
    parser.add_argument("--output-file", default="cv_generado.pdf", help="Nombre del archivo PDF de salida")
    parser.add_argument("--only-validate", action="store_true", help="Solo validar el contenido sin generar el PDF")
    
    args = parser.parse_args()
    
    if args.json_file:
        # Cargar datos del archivo JSON
        data = load_json(args.json_file)
        if data:
            if args.only_validate:
                # Solo validar el contenido
                is_valid, issues = validate_cv_content(data)
                if is_valid:
                    print("✓ El contenido del CV está dentro de los límites recomendados.")
                else:
                    print("⚠ Tiene que reducir un poco el contenido del CV:")
                    for issue in issues:
                        print(f"  • {issue}")
            else:
                # Generar el PDF
                generate_cv_pdf(data, args.output_file)
        else:
            print(f"Error: El archivo {args.json_file} no existe o no es válido")
    else:
        # Si no se proporciona un archivo JSON, usar un conjunto de datos vacío
        if args.only_validate:
            print("Error: Se requiere un archivo JSON para validar")
        else:
            generate_cv_pdf({}, args.output_file)

if __name__ == "__main__":
    main()