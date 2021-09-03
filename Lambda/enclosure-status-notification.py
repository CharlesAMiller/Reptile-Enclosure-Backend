import json

print('Loading function')


import boto3

def lambda_handler(event, context):

    # Create an SNS client to send notification
    sns = boto3.client('sns')
    dynamodb = boto3.client('dynamodb')

    try:
        print(event)
        response = dynamodb.get_item(TableName='EnclosureInfo', Key={'id': {'S': str(event["id"])}})
        sensor_params = response['Item']['sensors']['M'][str(event["sensor_id"])]['M']
        sensor_max = float(sensor_params["max"]['N'])
        sensor_min = float(sensor_params["min"]['N'])
        value = float(event["value"])
        print(sensor_max, sensor_min, value)
        if value > sensor_max or value < sensor_min:
            message_text = "Your enclosure is reporting a {0} of {1}, which {2} the limit of {3}".format(
                event["type"],
                str(value),
                "excedes" if value > sensor_max else "is below",
                str(sensor_max) if value > sensor_max else str(sensor_min)
                )
            print("Sending message", message_text)
            response = sns.publish(
                TopicArn = "arn:aws:sns:us-west-2:530995168627:EnclosureStatusWarning",
                Message = message_text)
            
            return response
        else:
            return "Wahoo!"
        
    except Exception as e:
        print(e)

    return "Whoops"
