import datetime
import config
import property_class
import immoscout24api
import slack
import boto3

def validate_event(event) -> bool:
    """
    event = {
        "query": "",
        "property-type": "",
        "notification-type": {
            "slack" : {
                "color": ""
            }
        }
    }
    """
    try:
        if len(event["query"]) == 0:
            raise Exception("invalid query")
        if len(event["property-type"]) == 0:
            raise Exception("invalid property-type")
        if len(event["notification-type"]) == 0:
            raise Exception("notification-type")
    except Exception as e:
        print(e)
        return False

    return True

def main(event, context):
    if not validate_event(event):
        return False

    slack_client = slack.Slack(
        url=config.SLACK_URL,
        color=event["notification-type"]["slack"]["color"],
        debug=config.SLACK_DEBUG
    )
    s3_session = boto3.client(
        service_name='s3',
        aws_access_key_id=config.AWS_ACCESS_KEY,
        aws_secret_access_key=config.AWS_ACCESS_SECRET,
        region_name=config.AWS_REGION
    )
    immoscout24_client = immoscout24api.Client(
        s3_session=s3_session,
        bucket=config.AWS_S3_BUCKET_NAME
    )

    publishedafter = (datetime.datetime.now() - datetime.timedelta(hours=8)).isoformat(timespec="seconds") # "2022-02-03T13:21:54"
    params = event["query"].replace("###publishedafter###", publishedafter)
    property_type = event["property-type"]

    try:
        properties = immoscout24_client.search(params)
        for data in properties:
            if "id" not in data:
              continue
            item = property_class.new(
                s3_session=s3_session,
                bucket=config.AWS_S3_BUCKET_NAME,
                property_type=property_type
            )
            item.load_from_api(data)
            if not item.is_exist():
                item.insert()
                slack_client.send(item)
    except Exception as e:
        slack_client.error(str(e))
