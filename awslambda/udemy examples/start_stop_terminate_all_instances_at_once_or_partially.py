# starts All ec2 instances at once in indicated region
'''
import boto3
aws_mag_con=boto3.session.Session(profile_name="developer")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

all_instances_ids=[]
for each_in in ec2_con_re.instances.all():
	all_instances_ids.append(each_in.id)
#print(dir(ec2_con_re.instances))
waiter=ec2_con_cli.get_waiter('instance_running')
print("Starting all instances ......")
ec2_con_re.instances.start()
waiter.wait(InstanceIds=all_instances_ids)
print("your all instaces are up and running")

#==================================================================================================================
# filter and list Non-Prod servers(ec2)  among Prod and Non-Prod servers.

import boto3
aws_mag_con=boto3.session.Session(profile_name="developer")
ec2_con_res=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

np_servers_ids=[]              #  >Non-Prod server Ids
f1={"Name": "tag:Name", "Values":['Non_Prod']}
for each_inst in ec2_con_res.instances.filter(Filters=[f1]):
	print(each_inst.id)


# np_servers_ids.append(each_inst.id) # add Non_Prod instance Ids to list(np_servers_ids=[])
# print("----------------------------")

#===================================================================================================================
# start only Non_Prod instances
'''
import boto3
aws_mag_con=boto3.session.Session(profile_name="developer")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

np_sers_ids=[]
f1={"Name": "tag:Name", "Values":['Non_Prod']}
for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
	for each_in in each_item['Instances']:
		np_sers_ids.append(each_in['InstanceId'])  # add Non_Prod server Ids to list(np_sers_ids=[])
print(np_sers_ids)

print("Starting intances with ids of : ",np_sers_ids)
ec2_con_cli.start_instances(InstanceIds=np_sers_ids)
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=np_sers_ids)
print("Your np instances are up and running....")
