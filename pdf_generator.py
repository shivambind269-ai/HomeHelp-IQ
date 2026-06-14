from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(issue, urgency, safety, cost):

    pdf_file = "HomeHelp_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "HomeHelp IQ Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Issue Category: {issue}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Urgency Level: {urgency}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Safety Advice: {safety}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Estimated Cost: {cost}",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_file