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

    # Header
    story.append(Paragraph("Daniel Alejandro Barrientos", styles['Header']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Tegucigalpa, Honduras • danielbanariba@protonmail.com • (+504) 3324-5827", styles['SubHeader']))
    story.append(Paragraph("<a href='https://www.danielbanariba.dev' color='blue'>www.danielbanariba.dev</a> • <a href='https://github.com/danielbanariba' color='blue'>GitHub</a> • <a href='https://www.linkedin.com/in/danielbanariba/' color='blue'>LinkedIn</a>", styles['SubHeader']))
    story.append(Spacer(1, 0.1*inch))

    # Divider line
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph(
        "Full Stack Software Engineer with 3+ years of development experience, specializing in Backend with Python and Java. Creator of innovative solutions, including a Python to JavaScript code translation tool and scalable web applications. Focused on providing efficient and scalable solutions, my goal is to apply my full stack development knowledge and actively contribute to the company's projects. Experience in process automation and development using frameworks such as FastAPI, Django, and Spring Boot. Always seeking tools and methodologies to optimize software performance and quality. Committed to continuous improvement and willing to face challenges that strengthen my technical capacity and allow me to grow alongside the team.", 
        styles['Normal']))
    story.append(Spacer(1, 0.1*inch))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", styles['SectionTitle']))
    # Divider line
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    skills = [
        "• Programming Languages: Python (Advanced), Java (Advanced), JavaScript (Intermediate)",
        "• Backend Frameworks: Astro, FastAPI, Reflex, Spring Boot",
        "• Databases: Oracle, MySQL, PostgreSQL, MongoDB",
        "• Development Tools: Git, Docker, IDEs (PyCharm, Eclipse, Visual Studio Code)",
        "• Methodologies: Agile, Scrum",
        "• Others: RESTful APIs, Web Scraping, Process Automation"
    ]
    for skill in skills:
        story.append(Paragraph(skill, styles['BulletPoint']))
    story.append(Spacer(1, 0.1*inch))

    # Notable Projects
    story.append(Paragraph("NOTABLE PROJECTS", styles['SectionTitle']))
    # Divider line
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    projects = [
        ("Analyzepy", "Tool that translates Python code to JavaScript, using advanced parsing and code generation techniques. Implemented with Python and Reflex."),
        ("Equation System Solver", "Web application for solving systems of linear equations, offering a user-friendly interface. Developed with Python and Reflex."),
        ("Automated YouTube Channel", "Program that automates the editing and uploading of videos to YouTube, applying effects and transitions. Uses Python."),
        ("SoundCloud Clone", "Project cloning SoundCloud functionalities, including database, backend, and frontend. Uses Oracle SQL, Python, FastAPI, HTML, and CSS.")
    ]
    for title, description in projects:
        story.append(Paragraph(title, styles['ProjectTitle']))
        story.append(Paragraph(description, styles['ProjectDescription']))
    story.append(Spacer(1, 0.1*inch))

    # Education
    story.append(Paragraph("EDUCATION", styles['SectionTitle']))
    # Divider line
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    education = [
        [Paragraph("National Autonomous University of Honduras", styles['ProjectTitle']), 
         Paragraph("Tegucigalpa, Honduras", styles['SmallText'])],
        [Paragraph("Systems Engineering (In progress)", styles['ProjectDescription']), 
         Paragraph("2019-2025", styles['SmallText'])],
        [Spacer(1, 0.05*inch), Spacer(1, 0.05*inch)],
        [Paragraph("ORACLE NEXT EDUCATION F2 T5 BACK-END", styles['ProjectTitle']), 
         Paragraph("Online", styles['SmallText'])],
        [Paragraph("Backend Development Course", styles['ProjectDescription']), 
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

    # Certifications and Additional Courses
    story.append(Paragraph("CERTIFICATIONS AND ADDITIONAL COURSES", styles['SectionTitle']))
    # Divider line
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    certifications = [
        "• Java and Python Programming: INFOP, 2023",
        "• Fundamental Concepts of Java and Java Fundamentals: INFOP, 2021",
        "• Computational Thinking With Python: Platzi, 2021"
    ]
    for cert in certifications:
        story.append(Paragraph(cert, styles['BulletPoint']))
    story.append(Spacer(1, 0.1*inch))

    # Languages
    story.append(Paragraph("LANGUAGES", styles['SectionTitle']))
    # Divider line
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("• English: B1", styles['BulletPoint']))

    doc.build(story)

# Generate the PDF
generate_cv_pdf("cv_english.pdf")