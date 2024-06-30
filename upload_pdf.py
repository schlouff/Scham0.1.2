import os
from google.cloud import storage


def upload_pdf_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Lädt eine Datei in den Google Cloud Storage Bucket hoch."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"Datei {source_file_name} wurde erfolgreich als {destination_blob_name} in {bucket_name} hochgeladen.")


# Beispielaufruf
if __name__ == "__main__":
    bucket_name = "vse-schamstaton24-07"
    source_file_name = "/Users/Christo/Downloads/10x15_pdf_mit_bild-4.pdf"
    destination_blob_name = "MemePDFs/datei.pdf"

    upload_pdf_to_gcs(bucket_name, source_file_name, destination_blob_name)