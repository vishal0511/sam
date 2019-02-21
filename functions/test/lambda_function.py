
import boto3

def lambda_handler(event, context):
    #try:
    #    rds_client = boto3.client('rds')
    #except:
     #   print ("vikas inside exception block")
      #  e = sys.exc_info()
       # #e1 = sys.exc_info()[1]
    #    print (e)
     #   #print (e1)
      #  logger.error("FAILED to connect to RDS MySQL instance")
       # sys.exit()
    print ("hello vikas")
    return {'statusCode': '200', 'headers': {'Content-Type': 'application/json'}, 'body': '    Results from api vikas badoni     '} 

