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
        }
    ])

    # Lặp qua các reservations và instances để in ra thông tin
    for reservation in response['Reservations']:
        for instance_info in reservation['Instances']:
            instance_id = instance_info['InstanceId']
            state = instance_info['State']['Name']

            print(f"Instance {instance_id} is in state: {state}")

    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully.'
    }
