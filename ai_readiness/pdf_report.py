from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from textwrap import wrap


# -------------------------
# DOUGHNUT CHART
# -------------------------
def draw_doughnut(c, x, y, size, percent):
    drawing = Drawing(size, size)

    pie = Pie()
    pie.x = 0
    pie.y = 0
    pie.width = size
    pie.height = size

    pie.data = [percent, 100 - percent]
    pie.startAngle = 100
    pie.innerRadiusFraction = 0.6

    pie.slices[0].fillColor = colors.HexColor("#22c55e")
    pie.slices[1].fillColor = colors.lightgrey
    pie.slices[0].strokeWidth = 0
    pie.slices[1].strokeWidth = 0

    drawing.add(pie)
    drawing.drawOn(c, x, y)

    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.black)
    c.drawCentredString(
        x + size / 2,
        y + size / 2 - 8,
        f"{int(percent)}%"
    )


# -------------------------
# TEXT WRAPPING (FIXED)
# -------------------------
def draw_wrapped_text(c, text, x, y, max_width, leading=16, font_size=11):
    text_obj = c.beginText(x, y)
    text_obj.setLeading(leading)
    text_obj.setFont("Helvetica", font_size)

    max_chars = int(max_width / 6.8)
    total_lines = 0

    for line in text.splitlines():
        wrapped_lines = wrap(line, max_chars) or [""]
        for wline in wrapped_lines:
            text_obj.textLine(wline)
            total_lines += 1

    c.drawText(text_obj)
    return y - (total_lines * leading)


# -------------------------
# MAIN PDF GENERATOR
# -------------------------
def generate_pdf_report(assessment, output):
    pagesize = landscape(A4)
    c = canvas.Canvas(output, pagesize=pagesize)
    width, height = pagesize

    LEFT_MARGIN = 40
    RIGHT_MARGIN = 40
    TOP_MARGIN = height - 60

    CONTENT_WIDTH = width - LEFT_MARGIN - RIGHT_MARGIN
    LEFT_COL_WIDTH = 650   # wider = horizontal feel

    # -------------------------
    # HEADER
    # -------------------------
    c.setFont("Helvetica-Bold", 18)
    c.drawString(LEFT_MARGIN, TOP_MARGIN, "AI Readiness Report — Forgebyte")

    # -------------------------
    # CLIENT INFO
    # -------------------------
    
    c.setFont("Helvetica-Bold", 14)
    # label_color = colors.HexColor("#374151")
    
    lines = [
        f"Name: ({assessment.person_name or ''})",
        
        f"Company: ({assessment.company_name or ''})",
        
        f"Email: ({assessment.email})",
        
        f"Phone: ({assessment.phone or ''})",
        
        f"Designation: ({assessment.designation or ''})",
        f"Industry: ({assessment.industry or ''})",
    ]
    # HIGHLIGHT_FIELDS = {"Name", "Company", "Email", "Phone", "Designation", "Industry"  }
    y = TOP_MARGIN - 40
    # for label, value in Client_info:
    #     if label in HIGHLIGHT_FIELDS:
    #         c.setFont("Helvetica-Bold", 13)
            
    #         c.setFillColor(label_color)
    #     # else:
    #     #     c.setFont("Helvetica", 11)
    #     #     c.setFillColor(colors.black)
    #         c.drawString(LEFT_MARGIN, y, f"{label}: {value or ''}")
    #         y -= 18
    for ln in lines:
        c.drawString(LEFT_MARGIN, y, ln)
        y -= 16

    # -------------------------
    # DOUGHNUT
    # -------------------------
    pct = float(assessment.capped_score or 0)
    DONUT_SIZE = 140
    DONUT_X = width - RIGHT_MARGIN - DONUT_SIZE
    DONUT_Y = TOP_MARGIN - 150

    draw_doughnut(c, DONUT_X, DONUT_Y, DONUT_SIZE, pct)

    # -------------------------
    # SUMMARY
    # -------------------------
    c.setFont("Helvetica-Bold", 15)
    c.drawString(LEFT_MARGIN, y - 10, "Summary")

    narrative_text = assessment.narrative or ""
    y = draw_wrapped_text(
        c,
        narrative_text,
        x=LEFT_MARGIN,
        y=y - 30,
        max_width=LEFT_COL_WIDTH,
        leading=16,
        font_size=14,
    )

    y -= 10

    # -------------------------
    # PAGE 2 — ANSWERS
    # -------------------------
    c.showPage()
    
    
    y = height - 60
    c.setFont("Helvetica-Bold", 14)
    c.drawString(LEFT_MARGIN,y, "Client Responses (Raw Answers)")

    y = height - 80
    c.setFont("Helvetica", 13)

    for ans in assessment.answers.all():
        if y < 100:
            c.showPage()
            y = height - 60
            c.setFont("Helvetica", 12)

        # Question
        qline = f"{ans.question_id}: {ans.question_text}"
        y = draw_wrapped_text(
            c,
            qline,
            x=LEFT_MARGIN,
            y=y,
            max_width=CONTENT_WIDTH,
            leading=14,
            font_size=12,
        )

        y -= 8

        # Answer
        if ans.numeric_value is not None:
            answer_text = f"Answer (1–5): {ans.numeric_value}"
        elif ans.raw_value:
            answer_text = f"Answer: {ans.raw_value}"
        else:
            answer_text = "Answer: -"

        y = draw_wrapped_text(
            c,
            answer_text,
            x=LEFT_MARGIN + 20,
            y=y,
            max_width=CONTENT_WIDTH - 20,
            leading=14,
            font_size=12,
        )

        y -= 10

    c.save()
