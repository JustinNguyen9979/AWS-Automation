import { S3Client, DeleteObjectCommand } from "@aws-sdk/client-s3";

const REGION = process.env.REGION || "ap-southeast-1";
const BUCKET = process.env.BUCKET || "justinaws-demo";
const KEY = process.env.KEY || "app1/logs-data-1.txt";
const s3Client = new S3Client({
  region: REGION,
});

const deleteObjects = async (bucket, key) => {
  console.log("Bucket: ", bucket);
  console.log("Key: ", key);
  const input = {
    Bucket: bucket,
    Key: key,
  };

  try {
    const command = new DeleteObjectCommand(input);
    const response = await s3Client.send(command);
    console.log(`Deleted ${key} successfully!`);
  } catch (error) {
    if (error instanceof Error) {
      console(error.message);
      return error;
    }
  }
};

const handler = async () => {
  await deleteObjects(BUCKET, KEY);
};

handler();
