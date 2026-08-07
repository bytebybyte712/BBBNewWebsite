from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "byte-by-byte-media-kit.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

BG = colors.HexColor("#0D1114")
SURFACE = colors.HexColor("#141B20")
TEXT = colors.HexColor("#F5F8FA")
MUTED = colors.HexColor("#AEBBC3")
GREEN = colors.HexColor("#00E676")
BLUE = colors.HexColor("#00B0FF")
LINE = colors.HexColor("#2A3942")

styles = getSampleStyleSheet()
title = ParagraphStyle("Title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=34, leading=38, textColor=TEXT, spaceAfter=16)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=23, leading=27, textColor=TEXT, spaceAfter=13)
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=GREEN, spaceBefore=8, spaceAfter=8)
body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.6, leading=14, textColor=MUTED, spaceAfter=10)
small = ParagraphStyle("Small", parent=body, fontName="Courier", fontSize=7.8, leading=11, textColor=BLUE, spaceAfter=8)
center = ParagraphStyle("Center", parent=body, alignment=TA_CENTER, textColor=TEXT)

def page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, LETTER[0], LETTER[1], fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(0.65 * inch, 0.55 * inch, 7.85 * inch, 0.55 * inch)
    canvas.setFont("Courier", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.65 * inch, 0.34 * inch, "BYTE BY BYTE - OFFICIAL MEDIA KIT")
    canvas.drawRightString(7.85 * inch, 0.34 * inch, str(doc.page))
    canvas.restoreState()

def img(path, width, height):
    result = Image(str(ROOT / path), width=width, height=height)
    result.hAlign = "LEFT"
    return result

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER, rightMargin=0.65*inch, leftMargin=0.65*inch, topMargin=0.6*inch, bottomMargin=0.72*inch)
story = []

logo = img("assets/byte-by-byte-logo.png", 1.65*inch, 1.65*inch)
cover_text = [Paragraph("PRESS &amp; MEDIA", small), Paragraph("Byte by Byte<br/><font color='#00E676'>Media Kit</font>", title), Paragraph("Official biographies, photography, project background, guest highlights, and contact information for reporters, educators, and organizations.", body), Spacer(1, 12), Paragraph("BYTE BY BYTE HOST<br/>Creator and Host", small)]
cover = Table([[logo, cover_text]], colWidths=[2.05*inch, 5.0*inch], rowHeights=[3.0*inch])
cover.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),SURFACE),("BOX",(0,0),(-1,-1),1,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),20),("RIGHTPADDING",(0,0),(-1,-1),20)]))
story += [Spacer(1, 0.55*inch), cover, Spacer(1, 30), Paragraph("PROJECT AT A GLANCE", small)]
stats = Table([["3", "3", "198", "6"],["EPISODES", "EXPERT GUESTS", "YOUTUBE VIEWS*", "YOUTUBE LIKES*"]], colWidths=[1.8*inch]*4)
stats.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),SURFACE),("BOX",(0,0),(-1,-1),1,LINE),("INNERGRID",(0,0),(-1,-1),0.5,LINE),("TEXTCOLOR",(0,0),(-1,0),GREEN),("TEXTCOLOR",(0,1),(-1,1),MUTED),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,0),25),("FONTNAME",(0,1),(-1,1),"Courier"),("FONTSIZE",(0,1),(-1,1),7),("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("TOPPADDING",(0,0),(-1,0),15),("BOTTOMPADDING",(0,0),(-1,0),7),("TOPPADDING",(0,1),(-1,1),7),("BOTTOMPADDING",(0,1),(-1,1),15)]))
story += [stats, Spacer(1, 8), Paragraph("* Public YouTube snapshot as of August 4, 2026.", small), PageBreak()]

story += [Paragraph("APPROVED BIOGRAPHIES", small), Paragraph("About the Byte by Byte Host", h1), Paragraph("SHORT BIO", h2), Paragraph("The Byte by Byte host is a rising junior at Deep Run High School's Center for Information Technology and the creator and host of Byte by Byte - Learning from Tech Minds. Through conversations with technology executives, professors, engineers, and entrepreneurs, he helps students understand careers and ideas across data, artificial intelligence, cybersecurity, engineering, and leadership. The host previously served as Vice President and technology leader of his Technology Student Association chapter. He earned five first-place awards at Virginia State TSA competitions, became a finalist at the TSA National Conference in Dallas, and received special recognition from the TSA Advisory Board for outstanding achievement.", body), Paragraph("LONG BIO", h2)]
long_bio = [
"The Byte by Byte host is a rising junior at Deep Run High School and a student in the school's specialized Center for Information Technology. He is passionate about data, artificial intelligence, cybersecurity, and the ways technology is changing careers, organizations, and everyday life.",
"To extend his learning beyond the classroom, the host created and hosts Byte by Byte - Learning from Tech Minds, a student-led podcast and publication platform built around thoughtful conversations with technology leaders. Through interviews with executives, professors, engineers, researchers, and entrepreneurs, he explores not only what these professionals do, but also how they developed their careers, solved difficult problems, led teams, and adapted to change. The project is designed to make technology pathways more understandable and approachable for students.",
"The host's leadership journey began through the Technology Student Association at Holman Middle School, where he was elected Vice President and served as a technology leader for his chapter. He helped lead STEM-focused activities, encouraged student participation, and represented his school in regional, Virginia state, and national competitions. Across categories including STEM Animation, Geospatial Technology, Community Service Video, and Construction Challenge, he earned five first-place awards at Virginia State TSA competitions - the highest honor achieved for Holman Middle School. He was also a finalist at the TSA National Conference in Dallas and received special recognition from the TSA Advisory Board for outstanding achievement.",
"One of his community-service projects raised awareness for cancer research and included interviews with Virginia Commonwealth University medical professionals. That experience reinforced his interest in using communication and technology together to support meaningful causes.",
"Today, the host continues developing his technical knowledge, communication skills, and network of mentors through the Center for Information Technology and Byte by Byte. He hopes the project encourages other students to stay curious, ask informed questions, and see themselves as participants in the future of technology."
]
for paragraph in long_bio: story.append(Paragraph(paragraph, body))
story.append(PageBreak())

story += [Paragraph("PROJECT &amp; GUESTS", small), Paragraph("Learning from Tech Minds", h1), Paragraph("MISSION", h2), Paragraph("Empowering the next generation of innovators by connecting students with world-class technology leaders through thoughtful conversations about AI, engineering, entrepreneurship, and leadership.", body), Paragraph("FEATURED CONVERSATIONS", h2)]
guest_data = [
    [img("assets/peteraiken.png", 1.05*inch, 1.05*inch), Paragraph("<b>Dr. Peter Aiken</b><br/><font color='#00B0FF'>Professor, author, and enterprise data authority</font><br/>Key lesson: Strong AI begins with trustworthy, well-managed data.<br/><font color='#00E676'>126 views / 5 likes*</font>", body)],
    [img("assets/romain.png", 1.05*inch, 1.05*inch), Paragraph("<b>Romain Lheritier</b><br/><font color='#00B0FF'>CEO and Co-Founder, Ippon Technologies</font><br/>Key lesson: Curiosity and continuous learning matter even more as AI accelerates change.<br/><font color='#00E676'>66 views / 1 like*</font>", body)],
    [img("assets/riad-hasan.jpeg", 1.05*inch, 1.05*inch), Paragraph("<b>Riad Hasan</b><br/><font color='#00B0FF'>Fractional CTO and insurance technology leader</font><br/>Key lesson: Begin with the problem and keep human judgment at the center.<br/><font color='#00E676'>6 views / 0 likes*</font>", body)],
]
guest_table = Table(guest_data, colWidths=[1.3*inch, 5.9*inch], rowHeights=[1.25*inch]*3)
guest_table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),SURFACE),("BOX",(0,0),(-1,-1),1,LINE),("INNERGRID",(0,0),(-1,-1),0.5,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10)]))
story += [guest_table, Spacer(1, 8), Paragraph("* Public YouTube snapshot as of August 4, 2026.", small), Spacer(1, 10), Paragraph("TOPICS COVERED", h2), Paragraph("Enterprise data management  /  Artificial intelligence  /  Software engineering  /  Cloud computing  /  Cybersecurity  /  Insurance technology  /  Entrepreneurship  /  Leadership", body), PageBreak()]

story += [Paragraph("MEDIA USE", small), Paragraph("Assets, Contact &amp; Attribution", h1)]
asset_table = Table([[img("assets/IMG_0142.jpg", 1.45*inch, 1.95*inch), img("assets/host-publication.jpg", 1.65*inch, 1.95*inch), img("assets/byte-by-byte-logo.png", 1.95*inch, 1.95*inch)]], colWidths=[2.35*inch,2.35*inch,2.35*inch])
asset_table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),SURFACE),("BOX",(0,0),(-1,-1),1,LINE),("INNERGRID",(0,0),(-1,-1),0.5,LINE),("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("TOPPADDING",(0,0),(-1,-1),12),("BOTTOMPADDING",(0,0),(-1,-1),12)]))
story += [asset_table, Spacer(1, 18), Paragraph("USAGE GUIDANCE", h2), Paragraph("Approved photographs and the Byte by Byte logo may be used in editorial coverage, event promotion, and organizational materials connected to Byte by Byte host or Byte by Byte. Please preserve image proportions, avoid recoloring the logo, and credit 'Byte by Byte' where practical. Contact the project before commercial use or material alteration.", body), Paragraph("CONTACT", h2), Paragraph("Media, speaking, and educational partnership inquiries:<br/><font color='#00E676'><b>bytebybyte712@gmail.com</b></font><br/>Website: thebytebybyte.com<br/>YouTube: @thebytebybyte", body), Spacer(1, 18), Paragraph("Byte by Byte is a student-led educational project created in Richmond, Virginia.", center)]

doc.build(story, onFirstPage=page, onLaterPages=page)
print(OUT)
