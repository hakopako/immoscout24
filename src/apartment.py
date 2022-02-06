
def new(s3_session, bucket):
    return Apartment(s3_session=s3_session, bucket=bucket)

class Apartment:

    def __init__(self, s3_session=None, bucket=None):
        self.s3_session = s3_session
        self.bucket = bucket

        self.apartment_id = -1
        self.title = ""
        self.photo = ""
        self.address = ""
        self.lat = -1
        self.lon = -1
        self.price = ""
        self.space = ""
        self.room = ""

    def load_from_api(self, data: dict):
        self.apartment_id = int(data["id"])
        self.title = data["title"]
        if len(data["pictures"]) > 0:
            url = data["pictures"][0]["urlScaleAndCrop"]
            self.photo = url.split("/ORIG/")[0]
        self.address = data["address"]["line"]
        self.lat = -1 if "lat" not in data["address"] else data["address"]["lat"]
        self.lon = -1 if "lon" not in data["address"] else data["address"]["lon"]
        self.price = data["attributes"][0]["value"]
        self.space = data["attributes"][1]["value"]
        self.room = data["attributes"][2]["value"]

    def is_exist(self) -> bool:
        if self.s3_session is None:
            raise Error("session is not set")
        try:
            self.s3_session.head_object(Bucket=self.bucket, Key=f"apartment/{self.apartment_id}")
            return True
        except Exception:
            return False

    def insert(self) -> bool:
        if self.s3_session is None:
            raise Error("session is not set")
        self.s3_session.put_object(Bucket=self.bucket, Key=f"apartment/{self.apartment_id}", Body="")
        return True
