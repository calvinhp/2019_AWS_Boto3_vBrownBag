import csv

import boto3
from pwgen import pwgen

client = boto3.client('rds')

new_dbs = {'saas{:0>2}'.format(db): '' for db in range(10)}

for db in new_dbs.keys():
    new_dbs[db] = pwgen(20)
    client.create_db_cluster(
        AvailabilityZones=[
            "us-east-1b",
            "us-east-1c"
        ],
        BackupRetentionPeriod=1,
        DBClusterIdentifier=db,
        VpcSecurityGroupIds=[
            'sg-0aa5e07ebdabfb0d1'
        ],
        DBSubnetGroupName="default-vpc-0f38b2e75ac4e5349",
        Engine="aurora",
        MasterUsername="root",
        MasterUserPassword=new_dbs[db],
        StorageEncrypted=True,
        EngineMode="serverless",
        ScalingConfiguration={
            "MinCapacity": 2,
            "MaxCapacity": 64,
            "AutoPause": True,
            "SecondsUntilAutoPause": 300
        },
        DeletionProtection=True
    )

with open('newdbs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    [writer.writerow(db) for db in new_dbs.items()]
