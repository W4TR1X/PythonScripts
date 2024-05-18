import os
import boto3

# SECRET Parameters
# os.environ['AWS_ACCESS_KEY_ID'] = 'YOUR_AWS_ACCESS_KEY_ID'
# os.environ['AWS_SECRET_ACCESS_KEY'] = 'YOUR_AWS_SECRET_ACCESS_KEY'

LOCAL_DIRECTORY = os.getenv('LOCAL_DIRECTORY')
LOCAL_FILENAME = os.getenv('LOCAL_FILENAME')

AWS_S3_ENDPOINT = os.getenv('AWS_S3_ENDPOINT')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME') 
AWS_PATH = os.getenv('AWS_PATH')
AWS_FILENAME = os.getenv('AWS_FILENAME')

s3_client = boto3.client('s3', endpoint_url=AWS_S3_ENDPOINT)

file_path = os.path.join(LOCAL_DIRECTORY, LOCAL_FILENAME)

aws_file_path = f"{AWS_PATH}/{AWS_FILENAME}"
s3_client.upload_file(file_path, AWS_BUCKET_NAME, aws_file_path)
print(f"aws upload: '{aws_file_path}' is uploaded")