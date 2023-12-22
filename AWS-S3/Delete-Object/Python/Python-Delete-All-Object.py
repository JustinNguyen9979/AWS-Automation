import boto3

def delete_all_objects_in_folder(bucket_name, prefix):
    # Khởi tạo client cho Amazon S3
    s3_client = boto3.client('s3')

    try:
        # Lấy danh sách các đối tượng trong thư mục
        objects_to_delete = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        # Kiểm tra xem có đối tượng nào trong thư mục không
        if 'Contents' in objects_to_delete:
            # Lặp qua danh sách các đối tượng và xóa từng đối tượng
            for obj in objects_to_delete['Contents']:
                s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted object: {obj['Key']}")

            print(f"All objects in folder {prefix} deleted successfully!")
        else:
            print(f"No objects found in folder {prefix}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Đặt tên bucket của bạn và đường dẫn đến thư mục
    bucket_name = 'justinaws-demo'
    folder_prefix = 'aws-data/'

    # Gọi hàm để xóa toàn bộ đối tượng trong thư mục
    delete_all_objects_in_folder(bucket_name, folder_prefix)
