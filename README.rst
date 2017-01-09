=======
aws-nmap
=======

This package provides a simple way to nmap over all public/elastic IPs on an
AWS account.

Install:

    $ pip install aws-nmap

Usage:

    $ aws-nmap -sC -sV

Alternatively you can:

    $ aws ec2 describe-instances --query "Reservations[*].Instances[*].PublicIpAddress" --output=text > /tmp/publicips.txt
    
    $ nmap -iL /tmp/publicips.txt -sC -sV

Assuming you want to look that up every time.
