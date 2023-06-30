import logging
import boto3
from botocore.exceptions import ClientError
import os

def uploadfile(file_path, bucketName, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    #If S3 object_name is not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
        s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_path, bucketName, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return ('file was uploaded  successfully',True)

# Get the file path by using the os module
script_dir = os.path.dirname(__file__)
file_name = "createbucket.py"
file_path = os.path.join(script_dir, file_name)

bucketname = "your bucket name"
if os.path.exists(file_path):
    uploadfile(file_path=file_path, bucketName=bucketname)
else:
    print('path doesnt exist')
