# 1. Import modules and packages
import os
import pandas as pd
from google.cloud import storage

# 2. Set JSON key as environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/vytautas/Documents/other/gcp_bucket_test/shaped-totem-351820-7e75cb04a7b9.json"

# 3. Specify a bucket name and other details
bucket_name = 'bucket_for_pandas_dataframe'
source_file_path = '/Users/vytautas/Documents/other/gcp_bucket_test//my_data.csv'
destination_blob_path = 'subfolder/my_data_on_gcp_bucket.csv'

# 4. Define a special function
def upload_to_storage(bucket_name: str, source_file_path: str, destination_blob_path: str):
  """Uploads a file to the bucket."""
  storage_client = storage.Client()
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(destination_blob_path)
  blob.upload_from_filename(source_file_path)
  print(f'The file {source_file_path} is uploaded to GCP bucket path: {destination_blob_path}')
  return None

# 5. Run the function!
upload_to_storage(bucket_name, source_file_path, destination_blob_path)
