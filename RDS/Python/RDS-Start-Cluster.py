import boto3

def lambda_handler(event, context):
    region = 'ap-northeast-1'
    db_cluster_identifier = 'rds-cluster-demo'

    # Khởi tạo client RDS
    rds_client = boto3.client('rds', region_name=region)

    try:
        # Thử chạy instance RDS
        response = rds_client.start_db_cluster(
            DBClusterIdentifier=db_cluster_identifier
        )

        # Ghi log thông báo thành công
        print(f"Start RDS Cluster {db_cluster_identifier}: {response}")

        return {
            'statusCode': 200,
            'body': f"Initiate a successful start for the RDS Cluster {db_cluster_identifier}."
        }
    except Exception as e:
        # Ghi log thông báo lỗi
        print(f"Error starting cluster RDS {db_cluster_identifier}: {e}")
        return {
            'statusCode': 500,
            'body': f"Error starting cluster RDS {db_cluster_identifier}: {str(e)}"
        }
