from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

def generate_invoice(client_name, items, invoice_number):
    filename = rf"c:/Dev/Floor8/pdf/invoice_{invoice_number}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 800, "INVOICE")

    c.setFont("Helvetica", 12)
    c.drawString(100, 770, f"Invoice Number: {invoice_number}")
    c.drawString(100, 750, f"Client: {client_name}")
    c.drawString(100, 730, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 690, f"Item")
    c.drawString(350, 690, "Price")

    c.setFont("Helvetica", 12)
    y = 670
    total = 0
    for item , price in items:
        c.drawString(100, y, item)
        c.drawString(350, y, f"${price}")
        total += price
        y -= 25

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y - 10, f"Total: ${total}")

    c.save()
    print(f"Invoice saved: {filename}")

items = [
    ("Web Scraping Script", 50),
    ("Selenium Automation", 75),
    ("PDF Generator", 40),
]

generate_invoice("John Smith", items, "INV-001")