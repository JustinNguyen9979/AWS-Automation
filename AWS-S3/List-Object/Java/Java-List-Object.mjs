import { S3Client, ListObjectsV2Command } from "@aws-sdk/client-s3";

const s3Client = new S3Client ({
    region: 'ap-southeast-1',
});

const BUCKET_NAME = 'justinaws-demo';
const PREFIX = 'app1/data-justinaws-';
//app1/justinaws-1.txt
//...
//app1/justinaws-1000.txt

export const listObjects = async () => {
    const input = {
        Bucket: BUCKET_NAME,
        Prefix: PREFIX,
        // MaxKeys: 2
    };

    const command = new ListObjectsV2Command(input);
    let isEnded = false;
    let totalObjects = 0;
    let attempt = 1;
    console.log("Starting program...");

    while(!isEnded) {
        console.log("Attempts: ", attempt);
        const {IsTruncated, Contents, NextContinuationToken} = await s3Client.send(command);
        let s3Key;
        Contents.map((c) =>{
            s3Key = `${c.Key}`;
            console.log("S3 Object Key: ", s3Key);
            totalObjects += 1;
        });
     
        attempt += 1;
        isEnded = IsTruncated ? false : true;
        command.input.ContinuationToken = NextContinuationToken;
    };
    console.log("Total Objects: ", totalObjects);
};

const handler = async() => {
    await listObjects();
};

handler();



//Link tham khảo
//https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/command/ListObjectsV2Command/
