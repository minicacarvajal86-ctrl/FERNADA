from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime

# Crear PDF
pdf_file = "Aurora_VIP_Mockup.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)

# Estilos
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#eeb643'),
    spaceAfter=12,
    alignment=1
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#eeb643'),
    spaceAfter=10,
    spaceBefore=10
)

normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor('#f7f1e4'),
    alignment=4,
    spaceAfter=8
)

# Contenido del PDF
content = []

# Portada
content.append(Spacer(1, 0.5*inch))
content.append(Paragraph("AURORA VIP", title_style))
content.append(Paragraph("Plataforma Premium de Cine", heading_style))
content.append(Spacer(1, 0.3*inch))
content.append(Paragraph(f"Generado el: {datetime.now().strftime('%d de %B de %Y')}", normal_style))
content.append(Spacer(1, 0.5*inch))

# Descripción del proyecto
content.append(Paragraph("Descripción del Proyecto", heading_style))
content.append(Paragraph(
    "Aurora VIP es una plataforma web premium de cine que ofrece una experiencia exclusiva de streaming cinematográfico. "
    "Cuenta con tres pantallas principales: una pantalla de inicio con cartelera de películas, un sistema de autenticación "
    "con planes de suscripción (Oro y Diamante), y una experiencia VIP exclusiva con beneficios premium.",
    normal_style
))
content.append(Spacer(1, 0.3*inch))

# Características principales
content.append(Paragraph("Características Principales", heading_style))
features = [
    "✓ Menú lateral con navegación intuitiva",
    "✓ Cartelera de películas recientes con imágenes de calidad",
    "✓ Calendario de lanzamientos próximos",
    "✓ Planes VIP (Oro y Diamante) con beneficios exclusivos",
    "✓ Sección de experiencias exclusivas para miembros",
    "✓ Beneficios premium: acumulación de puntos, combos con descuento, preventa anticipada",
    "✓ Diseño dark mode con acentos dorados"
]

for feature in features:
    content.append(Paragraph(feature, normal_style))

content.append(Spacer(1, 0.3*inch))

# Planes VIP
content.append(Paragraph("Planes VIP Disponibles", heading_style))
content.append(Spacer(1, 0.2*inch))

plans_data = [
    ["Plan Oro", "Plan Diamante"],
    ["$35.000/mes", "$66.000/mes"],
    ["2 entradas al mes", "4 entradas premium"],
    ["Fila preferencial", "Sala VIP y preventas"],
    ["10% en confitería", "15% en combos y lounge"]
]

plans_table = Table(plans_data, colWidths=[3*inch, 3*inch])
plans_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#c9922f')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#131720')),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#f7f1e4')),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#c9922f')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#10131a'), colors.HexColor('#131720')])
]))

content.append(plans_table)
content.append(Spacer(1, 0.3*inch))

# Beneficios VIP
content.append(Paragraph("Beneficios Exclusivos VIP", heading_style))
benefits = [
    "Asientos reclinables en zona lounge",
    "Preventa anticipada (48 horas antes)",
    "Combos premium con hasta 15% de descuento",
    "Acumulación de puntos (2X puntos)"
]

for benefit in benefits:
    content.append(Paragraph(f"• {benefit}", normal_style))

content.append(Spacer(1, 0.3*inch))

# Tecnología
content.append(Paragraph("Stack Tecnológico", heading_style))
tech = [
    "Backend: Flask 3.1.1 (Python)",
    "Frontend: HTML5, CSS3 con diseño responsive",
    "Templating: Jinja2",
    "Diseño: Dark mode premium con acentos dorados (Aurora Gold)"
]

for t in tech:
    content.append(Paragraph(f"• {t}", normal_style))

# Construir PDF
doc.build(content)
print(f"✅ PDF generado exitosamente: {pdf_file}")
