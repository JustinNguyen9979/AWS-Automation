import boto3

def list_objects_with_specific_name(bucket_name, target_name):
    # Khởi tạo client cho Amazon S3
    s3_client = boto3.client('s3')

    # Gọi API list_objects_v2 để lấy danh sách các đối tượng trong bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    # Kiểm tra xem có đối tượng nào không
    if 'Contents' in response:
        objects = response['Contents']
        for obj in objects:
            object_key = obj['Key']
            
            # Kiểm tra xem tên đối tượng có chứa target_name không
            if target_name in object_key:
                print(f"Object Key: {object_key}")
    else:
        print("Không có đối tượng trong bucket.")

if __name__ == "__main__":
    # Đặt tên bucket của bạn ở đây
    bucket_name = 'justinaws-demo'
    
    # Đặt tên cụ thể của đối tượng bạn muốn tìm
    target_name = 'logs-data-'
    
    list_objects_with_specific_name(bucket_name, target_name)
