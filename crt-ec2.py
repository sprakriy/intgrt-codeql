import boto3

# Replace with your desired region
region = 'us-east-1' 

# Replace with a valid AMI ID for your region (e.g., Amazon Linux 2 AMI)
# You can find AMIs in the EC2 console or programmatically.
ami_id = 'ami-0abcdef1234567890' 

# Replace with your desired instance type (e.g., t2.micro is eligible for the free tier)
instance_type = 't2.micro'

# Replace with the name of an existing Key Pair in your AWS account
# This is required for SSH access to your instance.
key_pair_name = 'my-ec2-keypair' 

# Optional: Replace with a valid Security Group ID for your region
# This controls inbound/outbound traffic to your instance.
# security_group_ids = ['sg-0123456789abcdef0'] 

# Optional: Replace with a valid Subnet ID if launching in a specific subnet
# subnet_id = 'subnet-0123456789abcdef0'

try:
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Launch the EC2 instance
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName=key_pair_name,
        # SecurityGroupIds=security_group_ids, # Uncomment and set if needed
        # SubnetId=subnet_id, # Uncomment and set if needed
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'MyPythonEC2Instance'
                    },
                ]
            },
        ]
    )

    # Print the instance details
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Successfully launched EC2 instance with ID: {instance_id}")

except Exception as e:
    print(f"Error launching EC2 instance: {e}")