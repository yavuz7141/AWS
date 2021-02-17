# by Using resorce object: this script filters available(and unused) untagged volumes and deletes
'''
import boto3

aws_mag_con=boto3.session.Session(profile_name="developer")                  # login to management console with developer(role) credentials

ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name='us-east-1')  # login to ec2 console(create resource object)
f_ebs_unused={"Name":"status","Values":["available"]}                        # define  filter (for available volumes) 
for each_volume in ec2_con_re.volumes.filter(Filters=[f_ebs_unused]):        # filter available volumes in all ec2 console
	if not each_volume.tags:                                                 # if volumes dont have tags
		print(each_volume.id, each_volume.state,each_volume.tags)
		print("Deleting unused and untagged volumes.....")
		each_volume.delete()                                                 # delete untagged available volumes

print("Deleted all unused untagged volumes.")
#======================================================================================================
'''
# by Using client object: this script filters available(and unused) untagged volumes and deletes

import boto3

aws_mag_con=boto3.session.Session(profile_name="developer")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name='us-east-1')
for each_item in ec2_con_cli.describe_volumes()['Volumes']:
	if not "Tags" in each_item  and each_item['State']=='available':
		print('Deleting ',each_item['VolumeId'])
		ec2_con_cli.delete_volume(VolumeId=each_item['VolumeId'])
print("Delete all unused and untagged volumes.")
