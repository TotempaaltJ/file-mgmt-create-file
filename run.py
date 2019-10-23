import sys
from datetime import datetime
import boto3
from botocore.client import Config
import toml

config = toml.load('config.toml')

# Initialize a session using DigitalOcean Spaces.
session = boto3.session.Session()
client = session.client('s3',
                        region_name=config['aws']['region_name'],
                        endpoint_url=config['aws']['endpoint_url'],
                        aws_access_key_id=config['aws']['access_key_id'],
                        aws_secret_access_key=config['aws']['secret_access_key'])

filename = datetime.now().isoformat()

client.put_object(
    Bucket=config['aws']['bucket_name'],
    Key=f'@inbox/uncategorized-{filename}.txt',
    Body=bytes(sys.argv[1], encoding='utf-8'))
