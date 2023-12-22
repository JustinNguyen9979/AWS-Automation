import {
  S3Client,
  ListObjectsV2Command,
  DeleteObjectCommand,
} from "@aws-sdk/client-s3";

const REGION = process.env.REGION || "ap-southeast-1";
const BUCKET = process.env.BUCKET || "justinaws-demo";
const PREFIX = process.env.PREFIX || "app1/";

const s3Client = new S3Client({
  region: REGION,
});

const deleteObjectsInFolder = async (bucket, prefix) => {
  console.log("Bucket: ", bucket);
  console.log("Prefix: ", prefix);

  try {
    // Lấy danh sách đối tượng trong thư mục
    const listCommand = new ListObjectsV2Command({
      Bucket: bucket,
      Prefix: prefix,
    });

    const { Contents } = await s3Client.send(listCommand);

    // Xóa từng đối tượng một
    for (const object of Contents) {
      const deleteCommand = new DeleteObjectCommand({
        Bucket: bucket,
        Key: object.Key,
      });

      await s3Client.send(deleteCommand);
      console.log(`Deleted ${object.Key} successfully!`);
    }

    console.log(`All objects in ${prefix} deleted successfully!`);
  } catch (error) {
    console.error("Error:", error.message);
    return error;
  }
};

const handler = async () => {
  await deleteObjectsInFolder(BUCKET, PREFIX);
};

handler();
