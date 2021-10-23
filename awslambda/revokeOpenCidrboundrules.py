import boto3, json
session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'


ec2East = session.client('ec2', region_name = east)
ec2Resource = session.resource('ec2', region_name=east)

response=ec2East.describe_security_groups(
    Filters=[
        {
            'Name': 'ip-permission.cidr',
            'Values': [
                '0.0.0.0/0',
            ]
        },
        {
            'Name': 'ip-permission.to-port',
            'Values': [
                '443',
            ]
        },
    ],
)
print(response)