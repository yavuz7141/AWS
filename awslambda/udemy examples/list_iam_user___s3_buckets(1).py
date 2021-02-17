# #Manual Steps to see/list all iam users:
# ========================================
#   step1: Get AWS Management Console
#   Step2: Get IAM Console
#          Options: Users, Groups, roles...
#-------below lists IAM users in my AWS account--------------
import boto3

aws_mag_con=boto3.session.Session(profile_name="developer")#step1: Get AWS Management Console
iam_con=aws_mag_con.resource('iam')#Step2: Get IAM Console

for each_user in iam_con.users.all():
    print(each_user.name)
# ----------below script lists s3 buckets in s3 ----------------
import boto3
aws_mag_con=boto3.session.Session(profile_name="developer")
s3_con=aws_mag_con.resource('s3')

for each_bucket in s3_con.buckets.all():
    print(each_bucket.name)