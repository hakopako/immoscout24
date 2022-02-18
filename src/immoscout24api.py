import urllib3
import json
import datetime

class TokenExpiredException(Exception): {}

class Client:

    def __init__(self, s3_session, bucket: str):
        self.s3_session = s3_session
        self.bucket = bucket
        self.http = urllib3.PoolManager()

    def generate_token(self) -> str:
        endpoint = "https://publicauth.immobilienscout24.de/oauth/token"
        request_headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "Connection",
            "User-Agent": "ImmoScout_23.10_15.2.1_._",
            "Accept-Language":"en-GB,en;q=0.9",
            "Host": "publicauth.immobilienscout24.de",
            "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
            "Content-Length":"109"
        }
        request_body = "grant_type=client_credentials&client_id=ImmobilienScout24-iPhone-Wohnen-AppKey&client_secret=pMxNytaNhHPujeeK"
        response = self.http.request("POST", endpoint, headers=request_headers, body=request_body, timeout=5)
        return json.loads(response.data.decode('utf-8'))["access_token"]

    def get_search_result(self, token: str, params: str) -> (Exception, list):
        endpoint = "https://api.mobile.immobilienscout24.de/search?" + params
        request_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "Connection",
            "x-is24-device": "iphone",
            "User-Agent": "ImmoScout_23.10_15.2.1_._",
            "Accept-Language":"en",
            "Host": "api.mobile.immobilienscout24.de"
        }
        response = self.http.request("GET", endpoint, headers=request_headers, timeout=5)
        data = json.loads(response.data.decode('utf-8'))
        if "error" in data:
            if data["error"] in ["invalid_token", "oauthToken mandatory"] :
                return (TokenExpiredException(data["error"]), [])
            else:
                return (Exception(data["error"]), [])
        return (None, data["results"])

    def search(self, params: str) -> list:
        retry = 0
        while retry < 2:
            response = self.s3_session.get_object(Bucket=self.bucket, Key="api-token.txt")
            immoscout24_token = response["Body"].read().decode('utf-8')
            (err, result) = self.get_search_result(token=immoscout24_token, params=params)
            if err is None:
                return result
            else: # TODO: TokenExpiredException 
                token = self.generate_token()
                self.s3_session.put_object(Bucket=self.bucket, Key="api-token.txt", Body=token)
                retry += 1
        return []
