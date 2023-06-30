import boto3

#RETRIEVE ALL SNAPSHOTS
def get_all_snapshots():
    ec2 = boto3.client('ec2')

    response = ec2.describe_snapshots(OwnerIds=['self'])
    snapshots = response['Snapshots']
    print(response)

    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot['VolumeId']
        start_time = snapshot['StartTime']
        state = snapshot['State']
        description = snapshot['Description']
        print(f"Snapshot ID: {snapshot_id}")
        print(f"Volume ID: {volume_id}")
        print(f"Start Time: {start_time}")
        print(f"State: {state}")
        print(f"Description: {description}")
        print("------------------------------")

get_all_snapshots()
