import unittest
import apartment, slack, config

class SlackClientTest(unittest.TestCase):

    def setUp(self):
        self.slack_client = slack.Slack(
            url=config.SLACK_URL,
            debug=config.SLACK_DEBUG
        )


    def __apartment_data(self):
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

    def test_send(self):
        item = apartment.new("dummy", "dummy")
        item.load_from_api(self.__apartment_data())
        self.slack_client.send(item)
        self.assertTrue(True)

    def test_error(self):
        self.slack_client.error("aaaaa")
        self.assertTrue(True)
        self.slack_client.error("aaaaa", "<!channel> Application is disabled.")
        self.assertTrue(True)

    def test_info(self):
        self.slack_client.info("aaaaa")
        self.assertTrue(True)
