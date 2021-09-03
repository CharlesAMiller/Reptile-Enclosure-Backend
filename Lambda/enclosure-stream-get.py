import json
import boto3 

def lambda_handler(event, context):
    # TODO implement
    kinesis_client = boto3.client('kinesisvideo',region_name='us-west-2')
    response = kinesis_client.get_data_endpoint(
        StreamARN='<YOUR_STREAM_ARN>',
        APIName='GET_HLS_STREAMING_SESSION_URL'
    )

    client = boto3.client('kinesis-video-archived-media', region_name='us-west-2', endpoint_url=response['DataEndpoint'])
     
    try: 
        response = client.get_hls_streaming_session_url(
            StreamARN='<YOUR_STREAM_ARN>',
            PlaybackMode='LIVE',
            DiscontinuityMode='ALWAYS',
            Expires=300,
        )
        
        if response['ResponseMetadata']["HTTPStatusCode"] == 200:
            return {
                'statusCode': 200,
                'body': json.dumps(response['HLSStreamingSessionURL'])
            }
    except:
        print("Unable to get streaming session url!")
    

    
    return {
        'statusCode': response['ResponseMetadata']["HTTPStatusCode"],
        'body': 'https://flutter.github.io/assets-for-api-docs/assets/videos/bee.mp4'
    }

'''    

'''  
