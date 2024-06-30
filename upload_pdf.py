import os
from google.cloud import storage


def upload_pdf_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Lädt eine Datei in den Google Cloud Storage Bucket hoch."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    if isinstance(source_file, io.BytesIO):
        blob.upload_from_file(source_file, content_type='application/pdf')
    else:
        blob.upload_from_filename(source_file)

    print(f"Datei wurde erfolgreich als {destination_blob_name} in {bucket_name} hochgeladen.")