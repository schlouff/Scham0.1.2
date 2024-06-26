import io
import tempfile
import requests
from PIL import Image
from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas


def create_a6_postcard(image_url):
    # Bild von der URL herunterladen
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))

    # A6-Größe in Punkten (1 Punkt = 1/72 Zoll)
    a6_width, a6_height = A6

    # Verwende ein temporäres Verzeichnis für die PDF-Datei
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        output_filename = tmp_file.name

        # PDF-Canvas erstellen
        c = canvas.Canvas(output_filename, pagesize=A6)

        # Bild auf A6-Größe skalieren und zentrieren
        img_width, img_height = img.size
        scale = min(a6_width / img_width, a6_height / img_height)
        new_width = img_width * scale
        new_height = img_height * scale
        x_offset = (a6_width - new_width) / 2
        y_offset = (a6_height - new_height) / 2

        # Bild auf PDF zeichnen
        c.drawImage(io.BytesIO(response.content), x_offset, y_offset, width=new_width, height=new_height)

        # PDF speichern
        c.showPage()
        c.save()

    return output_filename

# Hier könnten Sie in Zukunft weitere Funktionen hinzufügen, z.B.:
# def add_text_to_postcard(pdf_file, text, position):
#     ...

# def create_postcard_back(recipient_address, sender_address):
#     ...