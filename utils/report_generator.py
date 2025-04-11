# Re-executing the PDF generation code after code state reset

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
from io import BytesIO


def generate_pdf_report(output_path, resume_text, extracted_data, feedback, score=None, matched_skills=None):
    buffer = output_path if isinstance(output_path, BytesIO) else open(output_path, "wb")
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CenterTitle', alignment=TA_CENTER, fontSize=18, spaceAfter=20, textColor=colors.HexColor("#2E86AB")))
    styles.add(ParagraphStyle(name='SubHeading', alignment=TA_LEFT, fontSize=14, spaceAfter=10, textColor=colors.HexColor("#1A5276")))
    styles.add(ParagraphStyle(name='NormalText', alignment=TA_LEFT, fontSize=11, spaceAfter=6))
    styles.add(ParagraphStyle(name='Boxed', alignment=TA_LEFT, fontSize=10, backColor=colors.whitesmoke, borderPadding=(6,6,6,6)))

    elements = []

    # Title
    elements.append(Paragraph("Smart Resume Analysis Report", styles['CenterTitle']))
    elements.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['NormalText']))
    elements.append(Spacer(1, 12))

    # Summary Section
    elements.append(Paragraph("🔍 Resume Summary", styles['SubHeading']))
    summary_data = [
        ["Skills Extracted", ", ".join(extracted_data.get("skills", [])[:10]) + ("..." if len(extracted_data.get("skills", [])) > 10 else "")],
        ["Education", ", ".join(extracted_data.get("education", [])[:3])],
        ["Experience", ", ".join(extracted_data.get("experience", [])[:3])],
    ]
    summary_table = Table(summary_data, colWidths=[120, 380])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 14))

    # Score Breakdown
    elements.append(Paragraph("📊 Resume Score Breakdown", styles['SubHeading']))
    elements.append(Paragraph(f"Skills Score: {extracted_data.get('skills_score', 0)}%", styles['NormalText']))
    elements.append(Paragraph(f"Experience Score: {extracted_data.get('experience_score', 0)}%", styles['NormalText']))
    elements.append(Paragraph(f"Education Score: {extracted_data.get('education_score', 0)}%", styles['NormalText']))
    elements.append(Spacer(1, 12))

    # Job Matching
    if score is not None and matched_skills is not None:
        elements.append(Paragraph("🎯 Job Skill Matching", styles['SubHeading']))
        elements.append(Paragraph(f"Skill Match Score: {score}%", styles['NormalText']))
        elements.append(Paragraph("Matched Skills:", styles['NormalText']))
        for skill in matched_skills:
            elements.append(Paragraph(f"✔ {skill}", styles['NormalText']))
        elements.append(Spacer(1, 12))

    # Feedback
    elements.append(Paragraph("📝 Personalized Feedback", styles['SubHeading']))
    elements.append(Paragraph(feedback, styles['Boxed']))
    elements.append(Spacer(1, 14))

    # # Resume Text (Optional, long)
    # elements.append(Paragraph("📄 Full Resume Text (Extracted)", styles['SubHeading']))
    # elements.append(Paragraph(resume_text[:3000] + ("..." if len(resume_text) > 3000 else ""), styles['NormalText']))

    doc.build(elements)

    if isinstance(output_path, str):
        buffer.close()
