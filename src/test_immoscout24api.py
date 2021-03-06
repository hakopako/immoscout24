import unittest, datetime
import immoscout24api

class Immoscout24ApiTest(unittest.TestCase):

    def test_generate_token(self):
        immoscout24_test_client = immoscout24api.Client("dummy", "dummy")
        actual = immoscout24_test_client.generate_token()
        print(actual)
        self.assertTrue(len(actual) > 0)

    def test_get_search_result(self):
        token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InByb18yMDIxLTEyLTE1VDEzOjQ2OjI0LjAyMTgzMVoifQ.eyJzY29wZSI6WyJST0xFX1VTRVIiLCJTXzNMT0FVVEhfQVVUT19DT05GSVJNQVRJT04iLCJTX0FDQ0VTU19NT0RJU19BUElfUFJJQ0VfSElTVE9SWSIsIlNfRVhQT1NFIiwiU19HSVNfR0VPQ09ERSIsIlNfR0lTX0dFT0hJRVJBUkNIWSIsIlNfR0lTX0dFT19BVVRPQ09NUExFVEUiLCJTX0dJU19SRVZFUlNFX0dFT0NPREUiLCJTX0tBVUZQTEFORVIiLCJTX0xPR0lOX0FTX1VTRVIiLCJTX1JFQUxfRVNUQVRFX1JFQUQiLCJTX1JFQUxfRVNUQVRFX1dSSVRFIiwiU19SRVBPUlRJTkdfRU5BQkxFRCIsIlNfUkVUUklFVkVfQ09OVEFDVF9ERVRBSUxTX1BIT05FIiwiU19SRVRSSUVWRV9VTlBVQkxJU0hFRF9FWFBPU0UiLCJTX1NFQVJDSF9JUzI0IiwiU19TRUFSQ0hfVU5MSU1JVEVEX1BBR0VfU0laRSIsIlZBTFVBVElPTl9QREZfUkVBRCIsIlZBTFVBVElPTl9QREZfV1JJVEUiLCJjb25zdW1lckVudGl0bGVtZW50Lm15LnJlYWQiLCJjb252ZXJzYXRpb24udXNlci5hbGwiLCJtb2JpbGUuc29sdmVuY3kucmVhZCIsIm1vYmlsZS5zb2x2ZW5jeS53cml0ZSIsIm9jYS5vZmZlcnMucmVhZCIsIm9jYS5wcmljZXJhbmdlLnJlYWQiLCJwZGV2Lm1hcGkucHJvamVjdC5yZWFkIiwicHJpY2VoaXN0b3J5LnJlYWQiLCJwcm9maWxlLmFwaS5yZWFkIiwicHJvZmlsZS5hcGkud3JpdGUiLCJwcm9qZWN0ZXhwb3NlLm1hcGkubWFpbCIsInByb2plY3RleHBvc2UubWFwaS5yZWFkIiwicHJvamVjdGV4cG9zZS5tYXBpLnJlcG9ydCIsInByb3NwZWN0b3IuYXBpIiwicHVibGlzaGVkcHJvZmlsZS5yZWFkIiwicmVjb21tZW5kZWQuZXhwb3Nlcy5hcGkiLCJyZWxvY2F0aW9ucmVxdWVzdCIsInNvbHZlbmN5LmFwaSIsInN1YnNjcmlwdGlvbi5hcGkucmVhZCIsInN1YnNjcmlwdGlvbi5hcGkud3JpdGUiLCJzdXJ2ZXkuYXBpLnJlYWQiLCJzdXJ2ZXkuYXBpLndyaXRlIl0sImtpZCI6InByb18yMDIxLTEyLTE1VDEzOjQ2OjI0LjAyMTgzMVoiLCJleHAiOjE2NDQxNjg5MTMsImp0aSI6IjRmNjc0ZDE0LTE5Y2EtNDllNS1hNzZkLTRkZDc0MDQ0ZTcxOSIsImNsaWVudF9pZCI6IkltbW9iaWxpZW5TY291dDI0LWlQaG9uZS1Xb2huZW4tQXBwS2V5In0.cDgOqe1tuTqOT7u0qiyOeCyo3ozilD5PV8Ymj8sI6O-eQ8-MzIw3WykXRfZY5lLsfadxROW3Xi-ZJWQ7wXyOgVSzkq_jKpbuHdDx5t21q2Qz_IVs2Lby4xgWa-YQVgdrICtCNE3UxoAzVC_0uko51xFBoS4PZC2o0yBlBbG4bYR-A4k8OD4rwBWwRCv3NHC4L_GQmb1zYcjGpuUxghK27VjQvFvx2y_r2SMFLrsXgPjeOOGVuuv180pYpP0nWPZxvt9KVwjueAeIv9g27dfORCCi-ikiJZXUNIPUR6YnxG0Z5OuHteqNrBa__d6Iu3oROpSdvysEkHqRLZaQiAC2RQ"
        publishedafter = (datetime.datetime.now() - datetime.timedelta(hours=24)).isoformat(timespec="seconds") # "2022-02-03T13:21:54"
        params = "searchType=region&geocodes=/de/berlin/berlin/mitte/mitte,/de/berlin/berlin/mitte/wedding,/de/berlin/berlin/mitte/gesundbrunnen,/de/berlin/berlin/friedrichshain-kreuzberg/kreuzberg,/de/berlin/berlin/tempelhof-schoeneberg/tempelhof,/de/berlin/berlin/pankow/prenzlauer-berg,/de/berlin/berlin/mitte/tiergarten,/de/berlin/berlin/tempelhof-schoeneberg/schoeneberg,/de/berlin/berlin/treptow-koepenick/alt-treptow,/de/berlin/berlin/friedrichshain-kreuzberg/friedrichshain&price=-1100&priceType=calculatedtotalrent&numberofrooms=2-&livingspace=50-&exclusioncriteria=swapflat&haspromotion=false&pagenumber=1&pagesize=20&sorting=-firstactivation&realestatetype=apartmentrent&channel=is24&publishedafter=" + publishedafter + "&features=adKeysAndStringValues,virtualTour,contactDetails,viareporting,nextgen,calculatedTotalRent,listingsInListFirstSummary,grouping,projectsInAllRealestateTypes"
        immoscout24_test_client = immoscout24api.Client("dummy", "dummy")
        (err, actual) = immoscout24_test_client.get_search_result(token=token, params=params)
        print(err)
        print(actual)
        self.assertTrue(len(actual) > 0)
