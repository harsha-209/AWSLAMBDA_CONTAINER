import json
import boto3
import time
def handler(event, context):
    ec2_cons = boto3.client('ec2')
    filter_custome = {'Name': 'tag:Name','Values': ['arm64',]}
    response = ec2_cons.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['workernode',]}])
    print(response)
