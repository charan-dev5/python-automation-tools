from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd
import datetime
import os

os.makedirs(r"c:/Dev/Floor8/pdf/invoices", exist_ok=True)

df = pd.read_excel(r"c:/Dev/Floor8/pdf/customer.xlsx")

def generate_invoice(client_name, items, invoice_number):
    filename = rf"c:/Dev/Floor8/pdf/invoices/invoice_{invoice_number}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 800, "INVOICE")

    c.setFont("Helvetica", 12)
    c.drawString(100, 770, f"Invoice Number: {invoice_number}")
    c.drawString(100, 750, f"Client: {client_name}")
    c.drawString(100, 730, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 690, "Item")
    c.drawString(350, 690, "price")


    c.setFont("Helvetica", 12)
    y = 670
    total = 0
    for item, price in items:
        c.drawString(100, y, item)
        c.drawString(350, y, f"${price}")
        total += price
        y -= 25

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y - 10, f"Total: ${total}")

    c.save()

for index, row in df.iterrows():
    items = [
        (row["item1"], row["price1"]),
        (row["item2"], row["price2"]),
    ]
    generate_invoice(row["client_name"], items, row["invoice_number"])
    print(f"Generated: {row['invoice_number']} for {row['client_name']}")

print(f"Done. {len(df)} invoices generated.")                