import boto3

# aws_mag_con_root=boto3.session.Session(profile_name="root")   # if you have root profile it will show account Id and user Id same since it is root.
# sts_con_cli=aws_mag_con_root.client(service_name="sts",region_name="us-east-1")
# response=sts_con_cli.get_caller_identity()  # find "get_caller_identity()" from boto3 docs.
# print(response.get('Account'))

aws_mag_con_ayavuz=boto3.session.Session(profile_name="developer")
sts_con_cli=aws_mag_con_ayavuz.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity() # find "get_caller_identity()" from boto3 docs.
print(response['Account'])