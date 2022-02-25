# Full Documentation for S3 --> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.abort_multipart_upload
import boto3

BUCKET_NAME = "boto-tutorial-bucket"

s3 = boto3.client("s3")

# List all buckets
# buckets_resp = s3.list_buckets()
# for bucket in buckets_resp["Buckets"]:
#     print(bucket)

# List all objects in a bucket
# response = s3.list_objects_v2(Bucket=BUCKET_NAME)
# for obj in response["Contents"]:
#     print(obj)

# Upload file to bucket [Show with public-read, and without it too]
# with open("./burger.jpg", "rb") as f:
#     print(f.name)
#     s3.upload_fileobj(f, BUCKET_NAME, "burger.jpg", ExtraArgs={"ACL": "public-read"})

# Download File
# s3.download_file(BUCKET_NAME, "burger.jpg", "downloaded_burger.jpg")

# Download File with reference
# with open("downloaded_burger.jpg", "wb") as f:
#     s3.download_fileobj(BUCKET_NAME, "burger.jpg", f)

# Presigned URL to give limited access to an unauthorized user
# url = s3.generate_presigned_url(
#     "get_object", Params={"Bucket": BUCKET_NAME, "Key": "burger.jpg"}, ExpiresIn=30
# )
# print(url)


# Create Bucket
# bucket_location = s3.create_bucket(ACL="public-read", Bucket="new-copy-destination-123")
# print(bucket_location)

# Copy object
# response = s3.copy_object(
#     ACL="public-read",
#     Bucket="new-copy-destination-123",
#     CopySource=f"/{BUCKET_NAME}/burger.jpg",
#     Key="CopiedBurger.jpg",
# )
# print(response)

# Get Object
# response = s3.get_object(Bucket=BUCKET_NAME, Key="burger.jpg")
# print(response)
