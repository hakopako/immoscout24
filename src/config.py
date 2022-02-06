import os
from dotenv import load_dotenv

if "APP_ENV" not in os.environ or os.environ["APP_ENV"] != "prod":
    load_dotenv("../.env")
    print("[DEBUG] load dotenv")

AWS_ACCESS_KEY = None if "AWS_ACCESS_KEY" not in os.environ or os.environ["AWS_ACCESS_KEY"] == "" else os.environ["AWS_ACCESS_KEY"]
AWS_ACCESS_SECRET = None if "AWS_ACCESS_SECRET" not in os.environ or os.environ["AWS_ACCESS_SECRET"] == "" else os.environ["AWS_ACCESS_SECRET"]
AWS_REGION = None if "AWS_REGION" not in os.environ or os.environ["AWS_REGION"] == "" else os.environ["AWS_REGION"]

AWS_S3_BUCKET_NAME = os.environ["AWS_S3_BUCKET_NAME"]

SLACK_URL = os.environ["SLACK_URL"]
SLACK_DEBUG = False if str.lower(os.environ["SLACK_DEBUG"]) == "false" else True
