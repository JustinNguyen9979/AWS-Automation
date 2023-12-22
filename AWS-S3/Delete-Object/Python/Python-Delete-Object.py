import boto3

def delete_s3_object(bucket_name, key):
    # Khởi tạo client cho Amazon S3
    s3_client = boto3.client('s3')

    try:
        # Gọi API để xóa đối tượng
        response = s3_client.delete_object(
            Bucket=bucket_name,
            Key=key
        )
        print(f"Object {key} deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Đặt tên bucket của bạn và tên đối tượng cần xóa
    bucket_name = 'justinaws-demo'
    object_key = 'aws-data/logs-data-10.txt'

    # Gọi hàm để xóa đối tượng
    delete_s3_object(bucket_name, object_key)
