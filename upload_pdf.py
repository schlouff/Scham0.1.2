import io
from google.cloud import storage

def upload_pdf_to_gcs(bucket_name, source_file, destination_blob_name):
    """Lädt eine Datei oder ein BytesIO-Objekt in den Google Cloud Storage Bucket hoch."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    if isinstance(source_file, io.BytesIO):
        blob.upload_from_file(source_file, content_type='application/pdf')
    elif isinstance(source_file, str):
        blob.upload_from_filename(source_file)
    else:
        raise ValueError("source_file muss entweder ein BytesIO-Objekt oder ein Dateipfad (string) sein.")

    print(f"Datei wurde erfolgreich als {destination_blob_name} in {bucket_name} hochgeladen.")

# Beispielaufruf wurde entfernt, da er in der Hauptanwendung erfolgt