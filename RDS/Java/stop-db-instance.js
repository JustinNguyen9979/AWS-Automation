import { RDSClient, StopDBInstanceCommand } from '@aws-sdk/client-rds'; // ES Modules import

const client = new RDSClient({
  region: 'ap-northeast-1',
});

export const handler = async (event) => {
  // TODO implement

  const inputDBCluster = {
    DBClusterIdentifier: 'aurora-sls-dev',
  };
  const inputDBInstance = {
    DBInstanceIdentifier: 'rds-mysql-demo',
  };

  // const command = new StopDBClusterCommand(inputDBCluster);
  const command = new StopDBInstanceCommand(inputDBInstance);
  const response = await client.send(command);

  const result = {
    statusCode: 200,
    body: JSON.stringify('Hello from Lambda!'),
  };
  return result;
};