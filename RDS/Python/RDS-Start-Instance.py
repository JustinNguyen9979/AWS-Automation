import boto3

def lambda_handler(event, context):
    region = 'ap-northeast-1'
    db_instance_identifier = 'rds-mysql-demo'

    # Khởi tạo client RDS
    rds_client = boto3.client('rds', region_name=region)

    try:
        # Thử khởi động instance RDS
        response = rds_client.start_db_instance(
            DBInstanceIdentifier=db_instance_identifier
        )

        # Ghi log thông báo thành công
        print(f"Start RDS Instance {db_instance_identifier}: {response}")

        return {
            'statusCode': 200,
            'body': f"Start success RDS instance {db_instance_identifier}."
        }
    except Exception as e:
        # Ghi log thông báo lỗi
        print(f"Error starting RDS instance {db_instance_identifier}: {e}")
        return {
            'statusCode': 500,
            'body': f"Error starting RDS instance {db_instance_identifier}: {str(e)}"
        }
