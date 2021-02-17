import boto3, json
session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'
#ec2East = session.client('ec2', region_name = east)

ec2Client = session.client('ec2', region_name = east)
ec2Resource = session.resource('ec2', region_name=east)

# ec2Client = session.client('ec2', region_name = east)
# ec2Resource = session.resource('ec2', region_name=east)
#regions = [region['RegionName']response=ec2Client.describe_regions()
# print(response)

response=ec2Client.describe_regions()
regions= response['Regions']
print(type(regions))
for i in regions:
    print(i['RegionName'])