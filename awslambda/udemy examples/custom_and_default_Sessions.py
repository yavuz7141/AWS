#Note; boto3 documentation represents  default Session actions
# aws configure --profile p_name

# [root]
# aws_access_key_id = AKIAJRCMPX5GEZQLWWTA
# aws_secret_access_key = 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
# [ec2_developer]
# aws_access_key_id = AKIA5XNJJZL57MQ4WGWM
# aws_secret_access_key = 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
# [s3_developer]
# aws_access_key_id = AKIA5XNJJZL5QC3Q7IUX
# aws_secret_access_key = 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
# ====================================================================
# Custom Session:

import boto3
aws_mag_con=boto3.session.Session(profile_name="developer")

iam_con_re=aws_mag_con.resource(service_name='iam',region_name="us-east-2")
iam_con_client=aws_mag_con.client(service_name='iam',region_name="us-east-2")

# ===============================================================================
# Default:

# import boto3
# iam_con_re=boto3.resource(service_name="iam",region_name="us-east-1")

# ===============================================================================


# import boto3
# aws_mag_con=boto3.session.Session(profile_name="root")

# # ec2 = aws_mag_con.resource('ec2')
# ---------------------------------------------------------