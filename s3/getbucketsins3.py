import boto3

#RETRIEVE A LIST OF ALL S3 BUCKETS USING THE CLIENT METHOD
s3 = boto3.client('s3')
response = s3.list_buckets()['Buckets']
print('response:', response)

# OUTPUTT A SPECIFIC BUCKET NAME
print('Existing buckets:')
for bucket in response['Buckets']:
    if bucket['Name'] == 'myfirstbotot3bucket2023test':
        print(bucket['Name'])

#GET ALL S3 BUCKETS WITH THE CLIENT METHOD AND OUTPUT A SPECIFIC BUCKET NAME
s3_client = boto3.client('s3')
print('s3 bucket with resource', s3_client)
for bucket in s3_client.list_buckets()['Buckets']:
        if bucket['Name'] == 'myfirstbotot3bucket2023test':
            print(bucket['Name'])

# GET ALL S3 BUCKETS WITH THE RESOURCE METHOD AND OUTPUT A SPECIFIC BUCKET NAME
s3buckets = boto3.resource('s3')
print('s3 bucket with resource', s3buckets)
for bucket in s3buckets.buckets.all():
    if bucket.name == 'myfirstbotot3bucket2023test':
        print(bucket.name)