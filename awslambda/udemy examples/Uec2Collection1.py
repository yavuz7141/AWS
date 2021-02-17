import boto3


aws_man_con=boto3.session.Session(profile_name="developer")#1st Get AWS Managament console,like web login
iam_con=aws_man_con.resource("iam")#2nd Get IAM console

for each_user in iam_con.users.all(): #we want to work with all users, if want to work with groups type "iam.con.groups()"
    print(each_user.name)