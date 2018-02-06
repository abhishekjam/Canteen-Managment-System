from tempfile import NamedTemporaryFile
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
import os
os.environ["INVOICE_LANG"] = "en"
client = Client('Client company')
provider = Provider('Taste Of Doon Valley', bank_account='43Wf50')
creator = Creator('Verified By Admin')
invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_IN.UTF-8'
invoice.add_item(Item(32, 600, description="Item 1"))
invoice.add_item(Item(60, 50, description="Item 2"))
invoice.add_item(Item(50, 60, description="Item 3"))
invoice.add_item(Item(5, 600, description="Item 4"))
tmp_file = NamedTemporaryFile(delete=False)
pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf", generate_qr_code=True)
