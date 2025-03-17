from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def generate_cv_pdf(filename):
    # Crear un tamaño de página personalizado (width, height)
    custom_page_size = (8.5*inch, 12*inch)  # Más largo que letter pero mismo ancho
    
    doc = SimpleDocTemplate(filename, pagesize=custom_page_size,
                            rightMargin=0.5*inch, leftMargin=0.5*inch,
                            topMargin=0.3*inch, bottomMargin=0.75*inch)
    
    styles = getSampleStyleSheet()
    styles['Normal'].fontSize = 10
    styles['Normal'].spaceBefore = 1
    styles['Normal'].spaceAfter = 1

    # Estilos base
    styles.add(ParagraphStyle(name='Header', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='SubHeader', fontName='Helvetica', fontSize=10, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='SectionTitle', fontName='Helvetica-Bold', fontSize=10, spaceBefore=4, spaceAfter=1, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='SmallText', fontName='Helvetica', fontSize=10, alignment=TA_RIGHT, spaceAfter=2))
    styles.add(ParagraphStyle(name='ProjectTitle', fontName='Helvetica-Bold', fontSize=10, spaceAfter=1))
    styles.add(ParagraphStyle(name='ProjectDescription', fontName='Helvetica', fontSize=10, leftIndent=20, spaceAfter=5))
    styles.add(ParagraphStyle(name='BulletPoint', parent=styles['Normal'], 
                            leftIndent=20, 
                            bulletIndent=10, 
                            spaceBefore=0,
                            spaceAfter=2))

    # Estilos para la experiencia laboral
    styles.add(ParagraphStyle(
        name='JobTitle',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.black,
        spaceAfter=8
    ))

    styles.add(ParagraphStyle(
        name='DateText',
        fontName='Helvetica',
        fontSize=10,
        textColor=colors.black,
        alignment=TA_RIGHT,
        spaceAfter=8
    ))

    styles.add(ParagraphStyle(
        name='ExperienceBullet',
        fontName='Helvetica',
        fontSize=10,
        leftIndent=15,
        firstLineIndent=-15,
        leading=14,
        spaceBefore=0,
        spaceAfter=2,
        bulletIndent=0,
        bulletText='•',
        textColor=colors.black
    ))

    # Estilo para el nombre de la empresa
    styles.add(ParagraphStyle(
        name='CompanyName',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.black,
        spaceAfter=2
    ))

    # Estilo para la ubicación
    styles.add(ParagraphStyle(
        name='Location',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.black,
        alignment=TA_RIGHT
    ))

    # Estilo para el puesto (modificado para usar una fuente válida)
    styles.add(ParagraphStyle(
        name='JobPosition',
        fontName='Helvetica',  # Cambiado de Helvetica-Italic a Helvetica
        fontSize=10,
        leading=14,
        textColor=colors.gray,  # Cambiado a gris para distinguirlo
        spaceAfter=4
    ))
    
    story = []

    # Encabezado
    story.append(Paragraph("Daniel Alejandro Barrientos", styles['Header']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Tegucigalpa, Honduras • danielbanariba@protonmail.com • (+504) 3324-5827", styles['SubHeader']))
    story.append(Paragraph("<a href='https://www.danielbanariba.dev' color='blue'>www.danielbanariba.dev</a> • <a href='https://github.com/danielbanariba' color='blue'>GitHub</a> • <a href='https://www.linkedin.com/in/danielbanariba/' color='blue'>LinkedIn</a>", styles['SubHeader']))
    story.append(Spacer(1, 0.1*inch))

    # Línea divisoria
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))

    # Perfil profesional
    story.append(Paragraph(
        "Ingeniero en Sistemas y Programador entusiasta con experiencia en desarrollo de APIs RESTful, arquitecturas serverless y procesos de QA. Enfocado en la entrega de soluciones que superan las expectativas técnicas y de calidad, combinando conocimientos en desarrollo backend y testing para crear productos robustos y eficientes.", 
        styles['Normal']))
    story.append(Spacer(1, 0.1*inch))

    # Experiencia Laboral
    story.append(Paragraph("EXPERIENCIA LABORAL", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))

    # Primera posición en GuabaBIT
    exp_table_data = [
        [Paragraph("<b>GuabaBIT</b>", styles['CompanyName']),
         Paragraph("Octubre 2024 - Marzo 2024", styles['Location'])]
    ]
    exp_table = Table(exp_table_data, colWidths=[4.5*inch, 2.5*inch])
    exp_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (-1,0), (-1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(exp_table)
    
    # Añadir título del puesto
    story.append(Paragraph("Desarrollador Backend Y QA Tester", styles['JobPosition']))

    # Puntos de experiencia para la primera posición
    guabait = [
        "Desarrollo de APIs utilizando NestJS, implementando mejores prácticas de desarrollo",
        "Gestión de infraestructura en AWS y administración de bases de datos NoSQL con DynamoDB",
        "Documentación de código y APIs mediante Swagger",
        "Realización de pruebas de API con Postman, creando colecciones y scripts automatizados",
        "Implementación de casos de prueba utilizando Jira para garantizar la calidad del software",
        "Reporte y seguimiento de bugs y mejoras en la plataforma",
        "Creación de historias de usuario para optimizar la experiencia del usuario"
    ]
    for point in guabait:
        story.append(Paragraph(point, styles['ExperienceBullet']))

    story.append(Spacer(1, 0.15*inch))

    # Segunda posición en GuabaBIT
    # exp_table_data = [
    #     [Paragraph("<b>GuabaBIT</b>", styles['CompanyName']),
    #      Paragraph("Remoto", styles['Location'])]
    # ]
    # exp_table = Table(exp_table_data, colWidths=[4.5*inch, 2.5*inch])
    # exp_table.setStyle(TableStyle([
    #     ('ALIGN', (0,0), (0,-1), 'LEFT'),
    #     ('ALIGN', (-1,0), (-1,-1), 'RIGHT'),
    #     ('VALIGN', (0,0), (-1,-1), 'TOP'),
    #     ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    #     ('TOPPADDING', (0,0), (-1,-1), 6),
    # ]))
    # story.append(exp_table)
    
    # # Añadir título del puesto
    # story.append(Paragraph("QA Tester", styles['JobPosition']))

    # # Puntos de experiencia para la segunda posición
    # choyc_points = [
    #     "Implementación de casos de prueba utilizando Jira para garantizar la calidad del software",
    #     "Reporte y seguimiento de bugs y mejoras en la plataforma",
    #     "Creación de historias de usuario para optimizar la experiencia del usuario"
    # ]
    # for point in choyc_points:
    #     story.append(Paragraph(point, styles['ExperienceBullet']))

    story.append(Spacer(1, 0.15*inch))

    # Habilidades Técnicas
    story.append(Paragraph("HABILIDADES TÉCNICAS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    skills = [
        "• Lenguajes: Python (Avanzado), Java (Avanzado), TypeScript (Intermedio)",
        "• Frameworks Backend: NestJS, Astro, FastAPI, Reflex, Spring Boot",
        "• Bases de Datos: Oracle, MySQL, PostgreSQL, MongoDB, DynamoDB",
        "• Cloud & Infraestructura: AWS, Azure, Terraform, Docker",
        "• Testing & QA: Selenium, Jira, Jest, Postman, Playwright",
        "• Otros: RESTful APIs, Arquitectura Serverless, CI/CD, Git"
    ]
    for skill in skills:
        story.append(Paragraph(skill, styles['BulletPoint']))
    story.append(Spacer(1, 0.1*inch))

    # Proyectos Destacados
    story.append(Paragraph("PROYECTOS DESTACADOS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    projects = [
        ("Analyzepy", "Herramienta que traduce código de Python a JavaScript, utilizando técnicas avanzadas de parsing y generación de código. Implementado con Python y Reflex."),
        ("Canal de YouTube Automatizado", "Programa que automatiza la edición y subida de videos a YouTube, aplicando efectos y transiciones. Utiliza Python"),
    ]
    for title, description in projects:
        story.append(Paragraph(title, styles['ProjectTitle']))
        story.append(Paragraph(description, styles['ProjectDescription']))
    story.append(Spacer(1, 0.1*inch))

    # Educación
    story.append(Paragraph("EDUCACIÓN", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    education = [
        [Paragraph("Universidad Nacional Autónoma de Honduras", styles['ProjectTitle']), 
         Paragraph("Tegucigalpa, Honduras", styles['SmallText'])],
        [Paragraph("Pasante de la carrera de Ingeniería en Sistemas", styles['ProjectDescription']), 
         Paragraph("2019-2025", styles['SmallText'])],
        [Spacer(1, 0.05*inch), Spacer(1, 0.05*inch)],
        [Paragraph("ORACLE NEXT EDUCATION F2 T5 BACK-END", styles['ProjectTitle']), 
         Paragraph("Online", styles['SmallText'])],
        [Paragraph("Curso de Desarrollo Backend", styles['ProjectDescription']), 
         Paragraph("2023", styles['SmallText'])],
    ]
    t = Table(education, colWidths=[5*inch, 2*inch])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.1*inch))

    # Certificaciones y Cursos Adicionales
    story.append(Paragraph("CERTIFICACIONES Y CURSOS ADICIONALES", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    certifications = [
        "• Programación Java y Python: INFOP, 2023",
        "• Conceptos Fundamentales de Java y Fundamentos en Java: INFOP, 2021",
        "• Pensamiento Computacional Con Python: Platzi, 2021"
    ]
    for cert in certifications:
        story.append(Paragraph(cert, styles['BulletPoint']))
    story.append(Spacer(1, 0.1*inch))

    # Idiomas
    story.append(Paragraph("IDIOMAS", styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("• Español: Nativo", styles['BulletPoint']))
    story.append(Paragraph("• Inglés: Intermedio", styles['BulletPoint']))

    doc.build(story)

# Generar el PDF
generate_cv_pdf("cv_actualizado.pdf")