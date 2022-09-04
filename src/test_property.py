import unittest
import boto3
import config
import property_class

class PropertyTest(unittest.TestCase):

    s3_session = boto3.client(
        service_name='s3',
        aws_access_key_id=config.AWS_ACCESS_KEY,
        aws_secret_access_key=config.AWS_ACCESS_SECRET,
        region_name=config.AWS_REGION
    )

    def __property_data(self):
        return {
            "reportUrl": "https://angebot-melden.immobilienscout24.de/report?realEstateId=34008641&publicationState=live",
            "id": "34008641",
            "title": "Sanierte Altbau-3-Zimmer-Wohnung in beliebter Kreuzberglage",
            "pictures": [
                {
                    "urlScaleAndCrop": "https://pictures.immobilienscout24.de/listings/08651165-3a63-4287-805e-6f1ee7cbfef6-618763994.jpg/ORIG/legacy_thumbnail/%WIDTH%x%HEIGHT%/format/jpg/quality/50"
                }
            ],
            "titlePicture": {
                "preview": "https://pictures.immobilienscout24.de/listings/08651165-3a63-4287-805e-6f1ee7cbfef6-618763994.jpg/ORIG/resize/800x600>/format/jpg/quality/20",
                "full": "https://pictures.immobilienscout24.de/listings/08651165-3a63-4287-805e-6f1ee7cbfef6-618763994.jpg/ORIG/resize/800x600>/format/jpg/quality/80"
            },
            "address": {
                "line": "Gneisenaustraße 96, 10961 Berlin, Kreuzberg",
                "lat": 52.4922,
                "lon": 13.3932
            },
            "isProject": False,
            "isPrivate": False,
            "listingType": "S",
            "published": "3 days ago",
            "isNewObject": False,
            "attributes": [
                {
                    "label": "",
                    "value": "€858"
                },
                {
                    "label": "",
                    "value": "80 m²"
                },
                {
                    "label": "",
                    "value": "3 rms"
                }
            ],
            "realEstateType": "apartmentrent"
        }

    def test_load_from_api(self):
        item = property_class.new("dummy", "dummy", "dummy")
        item.load_from_api(self.__property_data())
        print(vars(item))
        self.assertTrue(item.property_id == 34008641)

    def test_scenario(self):
        item = property_class.new(ApartmentTest.s3_session, config.AWS_S3_BUCKET_NAME)
        item.load_from_api(self.__property_data())

        ApartmentTest.s3_session.delete_object(Bucket=config.AWS_S3_BUCKET_NAME, Key=f"{item.property_type}/{item.property_id}")
        self.assertFalse(item.is_exist())
        self.assertTrue(item.insert())
        self.assertTrue(item.is_exist())
        ApartmentTest.s3_session.delete_object(Bucket=config.AWS_S3_BUCKET_NAME, Key=f"{item.property_type}/{item.property_id}")
