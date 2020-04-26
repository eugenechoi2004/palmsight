import json
import boto3
import logging
from botocore.exceptions import ClientError
import flask 
import os
import sys
client = boto3.client('sagemaker')
client2 = boto3.client('sagemaker-runtime')
import base64
import json
def createndpointconfig():
    print(client.create_endpoint_config(
    EndpointConfigName='sample-endpointcfg-134EEA74-A9CA-4B4F-8DB1-B9721EEFC63B-1',
    ProductionVariants=[
        {
            'VariantName': 'variant-1',
            'ModelName': 'sample-model-134EEA74-A9CA-4B4F-8DB1-B9721EEFC63B-1',
            'InitialInstanceCount': 1,
            'InstanceType': 'ml.m4.xlarge',
        },
    ]))

