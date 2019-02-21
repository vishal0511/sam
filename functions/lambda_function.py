
import boto3

def lambda_handler(event, context):
    #try:
    #    rds_client = boto3.client('rds')
    #    user = "dbiamuser"  
     #   region= "us-east-1"
     #   token = rds_client.generate_db_auth_token(endpoint,3306,user,region)
     #   conn = pymysql.connect(host=endpoint, port=3306, user=user, password=token, db=db_name, auth_plugin_map={'mysql_cleartext_password':None}, cursorclass=pymysql.cursors.DictCursor)
     #   print ("3")
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

