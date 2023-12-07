import boto3

def lambda_handler(event, context):
    # Khu vực và tag cần kiểm tra
    region = 'ap-northeast-1'
    tag_key = 'ENV'
    tag_value = 'EC2-DEMO'

    # Tạo client cho dịch vụ EC2
    ec2 = boto3.client('ec2', region_name=region)

    # Sử dụng phương thức describe_instances để lấy thông tin về các instances
    response = ec2.describe_instances(Filters=[
        {
            'Name': f'tag:{tag_key}',
            'Values': [tag_value]
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running', 'stopped']
        }
    ])

    # Lặp qua các reservations và instances để terminate những instance ở trạng thái 'running' hoặc 'stopped'
    for reservation in response['Reservations']:
        for instance_info in reservation['Instances']:
            instance_id = instance_info['InstanceId']
            
            # Terminate instance
            ec2.terminate_instances(InstanceIds=[instance_id])
            print(f"Terminating instance: {instance_id}")

    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully.'
    }
