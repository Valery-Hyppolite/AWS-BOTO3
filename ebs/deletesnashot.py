import boto3

def delete_ebs_snapshot(snapshot_ids):
    ec2 = boto3.client('ec2')

    for snapshot_id in  snapshot_ids:
        print(snapshot_id)
        response = ec2.delete_snapshot(SnapshotId=snapshot_id)
        print(f"Snapshot '{snapshot_id}' deleted")

# Specify the snapshot IDs you want to delete
snapshot_ids = ['snap-0fe9b1ff1f891f037', 'snap-07b460ccefab6fca7']

# Delete the snapshots
delete_ebs_snapshot(snapshot_ids)
