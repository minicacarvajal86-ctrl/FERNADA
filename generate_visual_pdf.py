import subprocess
import time
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image as ReportLabImage, Spacer, PageBreak
from reportlab.lib.units import inch
from pathlib import Path

# Instalar y usar html2image para capturar
print("Generando PDF con screenshots de la aplicación...")

# Crear el PDF directamente desde HTML usando pdfkit
try:
    import pdfkit
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'enable-local-file-access': None,
        'javascript-delay': 3000
    }
    
    # Convertir el HTML a PDF
    pdfkit.from_file('templates/index.html', 'Aurora_VIP_Visual.pdf', options=options)
    print("✅ PDF generado exitosamente: Aurora_VIP_Visual.pdf")
except ImportError:
    print("pdfkit no está instalado, intentando alternativa...")
    
    # Alternativa: generar PDF simple pero visual
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    
    pdf_file = "Aurora_VIP_Visual.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#eeb643'),
        spaceAfter=20,
        alignment=1,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#eeb643'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#f7f1e4'),
        spaceAfter=8,
        alignment=4
    )
    
    # Contenido
    story = []
    
    # Portada
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("AURORA VIP", title_style))
    story.append(Paragraph("Tres Pantallas Premium para la Plataforma del Cine", heading_style))
    story.append(Spacer(1, 0.5*inch))
    
    story.append(Paragraph(
        "Una experiencia cinematográfica exclusiva con acceso VIP, preventas premium y beneficios especiales.",
        normal_style
    ))
    
    story.append(PageBreak())
    
    # Sección 1: Pantalla Principal
    story.append(Paragraph("PANTALLA PRINCIPAL - HOME", heading_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "<b>Descripción:</b> Página de inicio con menú lateral de navegación, cartelera de películas recientes "
        "y acceso a las diferentes secciones de la plataforma.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph(
        "<b>Elementos principales:</b><br/>"
        "• Menú lateral con 8 opciones de navegación (Inicio, Películas, Estrenos, Cartelera, Mi lista, Aurora VIP, Promociones, Configuración)<br/>"
        "• Logo de Aurora con identidad visual premium<br/>"
        "• Sección de películas recientes con etiquetas y meta información<br/>"
        "• Película destacada (Mortal Kombat II) con información de préestreno<br/>"
        "• Mini card VIP en el sidebar con información del programa",
        normal_style
    ))
    
    story.append(PageBreak())
    
    # Sección 2: Autenticación y Planes
    story.append(Paragraph("PANTALLA 2 - PLANES VIP", heading_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "<b>Descripción:</b> Pantalla de autenticación y selección de planes con opciones Oro y Diamante.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph(
        "<b>Plan ORO - $35.000/mes:</b><br/>"
        "• 2 entradas al mes<br/>"
        "• Fila preferencial<br/>"
        "• 10% de descuento en confitería<br/>"
        "• Perfecto para cinéfilos frecuentes",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "<b>Plan DIAMANTE - $66.000/mes:</b><br/>"
        "• 4 entradas premium<br/>"
        "• Sala VIP y preventas<br/>"
        "• 15% en combos y lounge<br/>"
        "• Experiencia premium total Aurora VIP (DESTACADO)",
        normal_style
    ))
    
    story.append(PageBreak())
    
    # Sección 3: Experiencia VIP
    story.append(Paragraph("PANTALLA 3 - EXPERIENCIA VIP", heading_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "<b>Descripción:</b> Sección exclusiva para miembros VIP con lanzamientos especiales, beneficios y experiencias premium.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph(
        "<b>Lanzamientos Exclusivos:</b><br/>"
        "• Premier Aurora Originals - Funciones de lanzamiento con acceso limitado<br/>"
        "• Maraton Midnight Gold - Sesiones especiales con coctelería y lounge<br/>"
        "• Director's Cut Sessions - Versiones extendidas y material inédito",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph(
        "<b>Beneficios Cine VIP:</b><br/>"
        "• Asientos reclinables - Zona lounge<br/>"
        "• Preventa anticipada - 48 horas antes<br/>"
        "• Combos premium - Hasta 15% OFF<br/>"
        "• Acumulación de puntos - 2X puntos",
        normal_style
    ))
    
    story.append(PageBreak())
    
    # Tecnología
    story.append(Paragraph("STACK TECNOLÓGICO", heading_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "<b>Backend:</b> Flask 3.1.1 (Python)<br/>"
        "<b>Frontend:</b> HTML5, CSS3 Responsive<br/>"
        "<b>Templating:</b> Jinja2<br/>"
        "<b>Diseño:</b> Dark Mode Premium con Acentos Dorados<br/>"
        "<b>Colores principales:</b> #07090d (fondo), #eeb643 (oro), #f7f1e4 (texto)",
        normal_style
    ))
    
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "Aurora VIP ofrece una experiencia única de cine premium con diseño elegante, "
        "navegación intuitiva y beneficios exclusivos para sus miembros VIP.",
        normal_style
    ))
    
    # Construir PDF
    doc.build(story)
    print(f"✅ PDF generado exitosamente: {pdf_file}")
