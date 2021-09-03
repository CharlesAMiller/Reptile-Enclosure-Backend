import json
import boto3 
import time
from decimal import * 

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    if "sensors" in event:
        for key in range(0, len(event["sensors"])):
            if "value" in event["sensors"][key]:
                event["sensors"][key]["value"] = Decimal(str(event["sensors"][key]["value"]))
        
    table = dynamodb.Table("EnclosureStatusRecords")
    response = table.put_item(Item={'EnclosureId': str(event['id']), 'CreatedAt': str(time.time()), 'data': event})
    
    return response

