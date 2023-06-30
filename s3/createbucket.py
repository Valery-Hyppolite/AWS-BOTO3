import boto3, logging, os
from botocore.exceptions import ClientError

#CREATE AN S3 BUCKET
def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            service_name = boto3.client('s3')
            service_name.create_bucket(Bucket=bucket_name)
        else:
            service_name = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            service_name.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

create_bucket(bucket_name='myfirstbotot3bucket2023test')





