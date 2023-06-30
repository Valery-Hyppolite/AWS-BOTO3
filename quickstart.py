import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    nameofbucket = bucket.name
    #print(nameofbucket)

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# Get the service resource
sqs = boto3.resource('sqs')

# You can now access identifiers and attributes
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))

# search an exiting queue
queuetestq = sqs.create_queue(QueueName='testq')
#print(queuetestq.attributes['QueuArn'].split(':'))

# Print out each queue name, which is part of its ARN
for queue in sqs.queues.all():
    print(queue.url)

response = queue.send_message(MessageBody='hello world')
print(response.get('MessageId'))