import os
import sys
import tempfile
import boto3
import jmespath
from subprocess import call

def main():
    client = boto3.client('ec2')
    ips = _public_ips(client)
    try:
        temp = tempfile.NamedTemporaryFile()
        for ip in ips:
            temp.write(ip)
            temp.write("\n")
        temp.flush()
        call(["nmap", "-iL", temp.name] + sys.argv[1:])
    finally:
        temp.close()

flatten = lambda l: [item for sublist in l for item in sublist]

def _public_ips(client):
    # TODO: Paginate.
    response = client.describe_instances()
    return flatten(jmespath.search('Reservations[*].Instances[*].PublicIpAddress', response))
