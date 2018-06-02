import json
import boto3

client = boto3.client('iot-data', region_name='eu-west-1')


def react(event, context):
    # Parse this sensor reading

    command = 'CLOSED'
    # Is it too hot?!
    if temperature > 20:
        # YES
        command = 'OPEN'

    # Tell the vents
    response = client.publish(
            topic='thevents/status'.
            qos=1
            payload=command
            )
