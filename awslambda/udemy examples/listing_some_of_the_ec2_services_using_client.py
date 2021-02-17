#below will list all EC2 instances with all info in us-east-1
'''
import boto3
from pprint import pprint # for better output format, more readable.
aws_mag_con=boto3.session.Session(profile_name="developer")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

response=ec2_con_cli.describe_instances()['Reservations']
for each_item in response:
        pprint(each_item['Instances'])
'''
#-----------------------------------------------------------------------------
#below will list (Image Id,Instance Id, Instance Launch Time) of All EC2's, Output will be like this:
# The Image Id is: ami-047a51fa27710816e
# The Instance Id Is: i-0acb97cd8906ce8a2
# The Instance Launch Time is: 2021-02-10
'''
import boto3
from pprint import pprint # for better output format, more readable.
aws_mag_con=boto3.session.Session(profile_name="developer")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

response=ec2_con_cli.describe_instances()['Reservations']
for each_item in response:
	for each in each_item['Instances']:
		print("=============================")
		print("The Image Id is: {}\nThe Instance Id Is: {}\nThe Instance Launch Time is: {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%Y-%m-%d")))
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#below lists (volume id , AvailabilityZone,VolumeType) of All EC2's in us-east-1, you can change and find any info about Volumes. Output like this:
# =======================
# The volume id is: vol-072eeb35d369a137e
# The AvailabilityZone is: us-east-1a
# The VolumeType is: gp2
# =======================
# The volume id is: vol-0b2c59a884f075fa0
# The AvailabilityZone is: us-east-1d
# The VolumeType is: gp2
import boto3
from pprint import pprint # for better output format, more readable.
aws_mag_con=boto3.session.Session(profile_name="developer")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

response=ec2_con_cli.describe_volumes()['Volumes']
for each_item in response:
	print("=======================")
	print("The volume id is: {}\nThe AvailabilityZone is: {}\nThe VolumeType is: {}".format(each_item['VolumeId'],each_item['AvailabilityZone'],each_item['VolumeType']))
