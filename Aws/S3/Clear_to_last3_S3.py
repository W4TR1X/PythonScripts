import os
import boto3

# SECRET Parameters
# os.environ['AWS_ACCESS_KEY_ID'] = 'YOUR_AWS_ACCESS_KEY_ID'
# os.environ['AWS_SECRET_ACCESS_KEY'] = 'YOUR_AWS_SECRET_ACCESS_KEY'

AWS_S3_ENDPOINT = os.getenv('AWS_S3_ENDPOINT')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME') 
AWS_PATH = os.getenv('AWS_PATH')

s3_client = boto3.client('s3', endpoint_url=AWS_S3_ENDPOINT)

print('S3 Cleaner: Cleaning older files...')
response = s3_client.list_objects_v2(Bucket=AWS_BUCKET_NAME, Prefix=AWS_PATH)
if 'Contents' in response:
    sorted_files = sorted(response['Contents'], key=lambda x: x['LastModified'] , reverse=True)
    if len(sorted_files) > 2:
        sorted_files = sorted_files[3:]
        for file in sorted_files:
            s3_client.delete_object(Bucket=AWS_BUCKET_NAME, Key=file['Key'])
        print("S3 Cleaner: Cleaned.")
    else:
        print("S3 Cleaner: Not enough files.")
else:
    print("S3 Cleaner: No files found.")
