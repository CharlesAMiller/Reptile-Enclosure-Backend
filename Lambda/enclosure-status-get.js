const AWS = require('aws-sdk');

const dynamo = new AWS.DynamoDB.DocumentClient();

/**
 * Demonstrates a simple HTTP endpoint using API Gateway. You have full
 * access to the request and response payload, including headers and
 * status code.
 *
 * To scan a DynamoDB table, make a GET request with the TableName as a
 * query string parameter. To put, update, or delete an item, make a POST,
 * PUT, or DELETE request respectively, passing in the payload to the
 * DynamoDB API as a JSON body.
 */
exports.handler = async (event, context) => {
    console.log('Received event:', JSON.stringify(event, null, 2));

    let body;
    let statusCode = '200';
    const headers = {
        'Content-Type': 'application/json',
    };
    
    event.routeKey = event.httpMethod + " " + event.resource; 
    console.log(event);
    try {
        switch (event.routeKey) {
            case "GET /enclosure/{id}":
                body = await dynamo.get({ 
                    TableName: 'EnclosureInfo',
                    Key: {
                        id: event.pathParameters.id
                    }
                }).promise();
                break;
            case "GET /enclosure/{id}/":
                body = await dynamo.get({ 
                    TableName: 'EnclosureInfo',
                    Key: {
                        id: event.pathParameters.id
                    }
                }).promise();
                break;
            case "GET /enclosure/{id}/status":
                body = await dynamo.get({ TableName: "EnclosureStatusRecords", Key: { EnclosureId: event.pathParameters.id}}).promise();
                break
            case "PUT /enclosure/{id}":
                console.log("PUT Reached: ", event.body);
                var item = JSON.parse(event.body);
                var params = {TableName: 'EnclosureInfo', Item: item};
                dynamo.put(params, function(err, data) {
                    if (err) {
                        console.error("Unable to add item. Error JSON:", JSON.stringify(err, null, 2));
                    } else {
                        console.log("Added item:", JSON.stringify(data, null, 2));
                        body = data; 
                    }
                });
                break
            case "GET /enclosure/{id}/data":
                var startTime = "162803419";
                if (event.queryStringParameters !== undefined && event.queryStringParameters.startTime !== undefined)
                    startTime = String(event.queryStringParameters.startTime);
               
                var params = {
                    TableName : "EnclosureStatus",
                    FilterExpression: "CreatedAt > :ca",
                    Filter: 50,
                    ExpressionAttributeValues: {
                         ":ca": startTime
                    },
                };
                
                body = await dynamo.scan(params).promise();
                
                break 
            default:
                throw new Error(`Unsupported route "${event.routeKey}"`);
        }
    } catch (err) {
        statusCode = '400';
        body = err.message;
    } finally {
        body = JSON.stringify(body);
    }

    return {
        statusCode,
        body,
        headers,
    };
};

