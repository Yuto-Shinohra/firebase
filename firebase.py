import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from firebase_admin import storage
from google.cloud import storage
import os

GOOGLE_APPLICATION_CREDENTIALS = "/Users/yuto_shinohara/Documents/Programming/python/textdata/python firebase/loadimage-9bac0-firebase-adminsdk-abrf6-6458eb0b50.json"
FIREBASE_STORAGE_BUCKET = "loadimage-9bac0.appspot.com"

cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred,{'storageBucket':FIREBASE_STORAGE_BUCKET})
#bucket = storage.bucket()

def upload_blob(source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
def download_blob(source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(
        "Blob {} downloaded to {}.".format(
            source_blob_name, destination_file_name
        )
    )

def blob_list(prefix=""):
    storage_client = storage.Client()
    bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
    blobs = list(bucket.list_blobs(prefix=prefix))
    print(
        "Blob list to {}.".format(
            blobs
        )
    )
    return blobs


if __name__ == "__main__":
    download_blob(source_blob_name, destination_file_name)