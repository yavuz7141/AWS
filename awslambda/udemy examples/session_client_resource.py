import boto3

aws_mag_con_developer=boto3.session.Session(profile_name="developer")
#aws_mag_con_developer=boto3.session.Session(profile_name="ec2_developer")

iam_con_re=aws_mag_con_developer.resource(service_name='iam',region_name="us-east-2")
#iam_con_cli=aws_mag_con_root.client(service_name='iam',region_name="us-east-2")

#Listiing iam users with resource object: does same job with client

for each_user in iam_con_re.users.all():
    print(each_user.name)

#Listing iam users with client object: does same job with resource

# for each in iam_con_cli.list_users()['Users']:
#    print(each['UserName'])

