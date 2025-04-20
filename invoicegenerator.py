from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_invoice(customer_name, items):
    filename = f"invoice_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "INVOICE")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Customer: {customer_name}")
    c.drawString(50, height - 100, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

    # Table header
    c.drawString(50, height - 140, "Item")
    c.drawString(250, height - 140, "Qty")
    c.drawString(350, height - 140, "Price")
    c.drawString(450, height - 140, "Total")

    y = height - 160
    total = 0

    for item in items:
        name, qty, price = item
        line_total = qty * price
        total += line_total
        c.drawString(50, y, name)
        c.drawString(250, y, str(qty))
        c.drawString(350, y, f"{price:.2f}")
        c.drawString(450, y, f"{line_total:.2f}")
        y -= 20

    # Total
    c.drawString(350, y - 20, "Grand Total:")
    c.drawString(450, y - 20, f"{total:.2f}")

    c.save()
    print(f"Invoice saved as {filename}")

# Sample usage
items = [
    ("Website Design", 1, 500.00),
    ("Hosting (12 months)", 1, 120.00),
    ("Domain (1 year)", 1, 10.00)
]

generate_invoice("Acme Corp", items)
