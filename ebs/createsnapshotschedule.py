import boto3

#CREATE A SNAPSHOT WITH NO TAGS
def create_ebs_snapshot2(volume_id, description=''):
    ec2 = boto3.client('ec2')

    response = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=description
    )

    snapshot_id = response['SnapshotId']
    print(f"Snapshot '{snapshot_id}' created for volume '{volume_id}'")

volume_id = 'vol-0ac613a539a1a8316'
description = 'discover-dev'

# Create the snapshot
create_ebs_snapshot2(volume_id, description)


#CREATE A SNAPSHOT WITH TAGS
def create_ebs_snapshot(volume_id, description='', snapshot_name='',  tags=None):
    ec2 = boto3.client('ec2')

    response = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=description,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': tags
            },
        ] if tags else []
    )

    snapshot_id = response['SnapshotId']
    print(f"Snapshot '{snapshot_id}' created for volume '{volume_id}'")

volume_id = 'vol-0ac613a539a1a8316'
description = 'discover-dev'

tags = [
    {'Key': 'discover-dev', 'Value': 'Snapshot102'},
    {'Key': 'Environment', 'Value': 'Production'}
]

snapshot_name='Discover-dev102'

# Create the snapshot with tags
create_ebs_snapshot(volume_id, description, snapshot_name, tags)

