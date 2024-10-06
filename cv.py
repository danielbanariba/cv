from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def generate_cv_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=0.5*inch, leftMargin=0.5*inch,
                            topMargin=0.3*inch, bottomMargin=0.75*inch)
    
    styles = getSampleStyleSheet()
    styles['Normal'].fontSize = 10
    styles['Normal'].spaceBefore = 1
    styles['Normal'].spaceAfter = 1

    styles.add(ParagraphStyle(name='Header', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='SubHeader', fontName='Helvetica', fontSize=10, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='SectionTitle', fontName='Helvetica-Bold', fontSize=10, spaceBefore=4, spaceAfter=1, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='BulletPoint', parent=styles['Normal'], leftIndent=20, bulletIndent=10))
    styles.add(ParagraphStyle(name='SmallText', fontName='Helvetica', fontSize=10, alignment=TA_RIGHT, spaceAfter=2))
    styles.add(ParagraphStyle(name='ProjectTitle', fontName='Helvetica-Bold', fontSize=10, spaceAfter=1))
    styles.add(ParagraphStyle(name='ProjectDescription', fontName='Helvetica', fontSize=10, leftIndent=20, spaceAfter=5))
    
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

    story.append(Paragraph(
        "Ingeniero de Software Full Stack con 3+ años de experiencia en desarrollo, especializado en Backend con Python y Java. Creador de soluciones innovadoras, incluyendo una herramienta de traducción de código Python a JavaScript y aplicaciones web escalables. Enfocado en aportar soluciones eficientes y escalables, mi objetivo es aplicar mis conocimientos en desarrollo full stack y contribuir activamente a los proyectos de la empresa. Experiencia en automatización de procesos y desarrollo utilizando frameworks como FastAPI, Django y Spring Boot. Siempre en búsqueda de herramientas y metodologías que optimicen el rendimiento y la calidad del software. Comprometido con la mejora continua y dispuesto a enfrentar desafíos que fortalezcan mi capacidad técnica y permitan crecer junto al equipo.", 
        styles['Normal']))
    story.append(Spacer(1, 0.1*inch))

    # Habilidades Técnicas
    story.append(Paragraph("HABILIDADES TÉCNICAS", styles['SectionTitle']))
    # Línea divisoria
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    skills = [
        "• Lenguajes de Programación: Python (Avanzado), Java (Avanzado), JavaScript (Intermedio)",
        "• Frameworks Backend: Astro, FastAPI, Reflex, Spring Boot",
        "• Bases de Datos: Oracle, MySQL, PostgreSQL, MongoDB",
        "• Herramientas de Desarrollo: Git, Docker, IDEs (PyCharm, Eclipse, Visual Studio Code)",
        "• Metodologías: Agile, Scrum",
        "• Otros: RESTful APIs, Web Scraping, Automatización de Procesos"
    ]
    for skill in skills:
        story.append(Paragraph(skill, styles['BulletPoint']))
    story.append(Spacer(1, 0.1*inch))

    # Proyectos Destacados
    story.append(Paragraph("PROYECTOS DESTACADOS", styles['SectionTitle']))
    # Línea divisoria
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    projects = [
        ("Analyzepy", "Herramienta que traduce código de Python a JavaScript, utilizando técnicas avanzadas de parsing y generación de código. Implementado con Python y Reflex."),
        ("Resuelve Sistemas de Ecuaciones", "Aplicación web para resolver sistemas de ecuaciones lineales, ofreciendo una interfaz amigable. Desarrollado con Python y Reflex."),
        ("Canal de YouTube Automatizado", "Programa que automatiza la edición y subida de videos a YouTube, aplicando efectos y transiciones. Utiliza Python"),
        ("SoundCloud Clone", "Proyecto de clonación de funcionalidades de SoundCloud, incluyendo base de datos, backend y frontend. Utiliza Oracle SQL, Python, FastAPI, HTML y CSS.")
    ]
    for title, description in projects:
        story.append(Paragraph(title, styles['ProjectTitle']))
        story.append(Paragraph(description, styles['ProjectDescription']))
    story.append(Spacer(1, 0.1*inch))

    # Educación
    story.append(Paragraph("EDUCACIÓN", styles['SectionTitle']))
    # Línea divisoria
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
    # Línea divisoria
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
    # Línea divisoria
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("• Español: Nativo", styles['BulletPoint']))
    story.append(Paragraph("• Inglés: Intermedio", styles['BulletPoint']))

    doc.build(story)

# Generar el PDF
generate_cv_pdf("cv_mejorado.pdf")