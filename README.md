# Overview

This is a tool to get an notification once new apartment shows up on immobilienscout24 so that you can find and apply to the property as fast as possible.  

This tool uses AWS within free-tier and Slack.

- AWS S3: to store apartment id to detect new apartment.
- AWS Lambda: to run this tool
- AWS EventBridge: for cron job
- Slack: to get notification

# Setup

- Set up `.env` config.   
Create `.env` file with the command below and edit the file.

```
$ cp env.default .env
```

- Download required library

```
$ make download-lib
 ----> this will download library to ./src/*
```

# Build src

- `$ make zip-src` will create a zip file in `./dist` to upload AWS Lambda.

# Postman

[Postman](https://www.postman.com/) is an easy way to try out API request.  
Here is the API collection which this tool is using.  

[./immobilienscout24.postman_collection.json](./immobilienscout24.postman_collection.json)
