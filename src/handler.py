import datetime
import config
import apartment
import immoscout24api
import slack
import boto3


def main(event, context):
    slack_client = slack.Slack(
        url=config.SLACK_URL,
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
    params = "searchType=region&geocodes=/de/berlin/berlin/mitte/mitte,/de/berlin/berlin/mitte/wedding,/de/berlin/berlin/mitte/gesundbrunnen,/de/berlin/berlin/friedrichshain-kreuzberg/kreuzberg,/de/berlin/berlin/tempelhof-schoeneberg/tempelhof,/de/berlin/berlin/pankow/prenzlauer-berg,/de/berlin/berlin/mitte/tiergarten,/de/berlin/berlin/tempelhof-schoeneberg/schoeneberg,/de/berlin/berlin/treptow-koepenick/alt-treptow,/de/berlin/berlin/friedrichshain-kreuzberg/friedrichshain&price=-1100&priceType=calculatedtotalrent&numberofrooms=2-&livingspace=50-&exclusioncriteria=swapflat&haspromotion=false&pagenumber=1&pagesize=20&sorting=-firstactivation&realestatetype=apartmentrent&channel=is24&publishedafter=" + publishedafter + "&features=adKeysAndStringValues,virtualTour,contactDetails,viareporting,nextgen,calculatedTotalRent,listingsInListFirstSummary,grouping,projectsInAllRealestateTypes"

    try:
        apartments = immoscout24_client.search(params)
        for data in apartments:
            item = apartment.new(
                s3_session=s3_session,
                bucket=config.AWS_S3_BUCKET_NAME
            )
            item.load_from_api(data)
            if not item.is_exist():
                item.insert()
                slack_client.send(item)
    except Exception as e:
        slack_client.error(str(e))
