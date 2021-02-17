# below script starts entered ec2 (Instance ID) and checks the status of ec2 every 10 sec until it is running

'''
import boto3 
import time
aws_con=boto3.session.Session(profile_name="developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")

my_inst_ob=ec2_con_re.Instance("i-06e6f0a39938f1184")
print("Starting given instance....")
my_inst_ob.start()

while True:
    my_inst_ob=ec2_con_re.Instance('i-06e6f0a39938f1184')
    print("Current status of EC2 is: ", my_inst_ob.state['Name'])
    if my_inst_ob.state['Name']=="running":
        break
    print("waiting to get running status...")
    time.sleep(10)
print("Now your instance is up and running")


#==============================================================================================================================
# starts entered ec2 (Instance ID) and checks the status by  using "wait_until_running()"function in boto3 instead long "while True" script.

import boto3 
import time
aws_con=boto3.session.Session(profile_name="developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")

my_inst_ob=ec2_con_re.Instance("i-002d4110f1199166f")
print("Starting given instance....")
#print(dir(my_inst_ob)     ***dir > shows all options in ec2 like,start,stop,reboot,vpc,volumes etc...
my_inst_ob.start()
my_inst_ob.wait_until_running()  #Resource waiter waits for 200sec(40 checks after every 5 sec)
print("Now your instance is up and running")


#=================================================================================================================================
# does same job as above. this time by using client object instead resource object
# here we are starting ec2 using client object ,we use waiter for client itself. 
import boto3 
import time
aws_con=boto3.session.Session(profile_name="developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")

print("Starting ec2 instace...")
ec2_con_cli.start_instances(InstanceIds=['i-002d4110f1199166f'])
waiter=ec2_con_cli.get_waiter('instance_running') # find get_waiter('instance_running') from boto3 doc
waiter.wait(InstanceIds=['i-002d4110f1199166f']) #40 checks after every 15 sec. also find "waiter.wait(InstanceIds=['InstanceId'])" from boto3
print("Now your ec2 instace is up and running")
'''
'''
#=================================================================================================================================
# this is the best option among others, here we are starting ec2 using resource object, then we attach  waiter from client object.
#using waiter from client object is better option compare to waiterless as it waits 600 sec to start ec2. waiterless version waits 200 sec.
import boto3 
import time
aws_con=boto3.session.Session(profile_name="developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")

my_inst_ob=ec2_con_re.Instance("i-002d4110f1199166f")
print("Starting given instance....")
my_inst_ob.start()
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-002d4110f1199166f'])
print("Now your ec2 instace is up and running")
'''
#=========================================================================================================================================
# stops given ec2 instance 
import boto3 
import time
aws_con=boto3.session.Session(profile_name="developer")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")

my_inst_ob=ec2_con_re.Instance("i-04dd89bda76f05826")
print("Stopping given instance....")
my_inst_ob.stop()
waiter=ec2_con_cli.get_waiter('instance_stopped')
waiter.wait(InstanceIds=['i-04dd89bda76f05826'])
print("Now your ec2 instance  stopped")
