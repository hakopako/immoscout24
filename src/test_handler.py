import unittest
import handler  

class HandlerTest(unittest.TestCase):

    def test_validate_event(self):
        params = {
            "query": "searchType=region&geocodes=/de/berlin/berlin/mitte/mitte,/de/berlin/berlin/mitte/gesundbrunnen,/de/berlin/berlin/friedrichshain-kreuzberg/kreuzberg,/de/berlin/berlin/tempelhof-schoeneberg/tempelhof,/de/berlin/berlin/pankow/prenzlauer-berg,/de/berlin/berlin/mitte/tiergarten,/de/berlin/berlin/tempelhof-schoeneberg/schoeneberg,/de/berlin/berlin/treptow-koepenick/alt-treptow,/de/berlin/berlin/friedrichshain-kreuzberg/friedrichshain,/de/berlin/berlin/neukoelln/neukoelln&price=-1100&priceType=calculatedtotalrent&numberofrooms=2-&livingspace=50-&exclusioncriteria=swapflat&haspromotion=false&pagenumber=1&pagesize=20&sorting=-firstactivation&realestatetype=apartmentrent&channel=is24&publishedafter=###publishedafter###&features=adKeysAndStringValues,virtualTour,contactDetails,viareporting,nextgen,calculatedTotalRent,listingsInListFirstSummary,grouping,projectsInAllRealestateTypes",
            "property-type": "apartment",
            "notification-type": {
                "slack" : {
                    "color": "#cccccc"
                }
            }
        }
        self.assertTrue(handler.validate_event(params))

    def test_main_apartment_rent(self):
        handler.main({
            "query": "searchType=region&geocodes=/de/berlin/berlin/mitte/mitte,/de/berlin/berlin/mitte/gesundbrunnen,/de/berlin/berlin/friedrichshain-kreuzberg/kreuzberg,/de/berlin/berlin/tempelhof-schoeneberg/tempelhof,/de/berlin/berlin/pankow/prenzlauer-berg,/de/berlin/berlin/mitte/tiergarten,/de/berlin/berlin/tempelhof-schoeneberg/schoeneberg,/de/berlin/berlin/treptow-koepenick/alt-treptow,/de/berlin/berlin/friedrichshain-kreuzberg/friedrichshain,/de/berlin/berlin/neukoelln/neukoelln&price=-1100&priceType=calculatedtotalrent&numberofrooms=2-&livingspace=50-&exclusioncriteria=swapflat&haspromotion=false&pagenumber=1&pagesize=20&sorting=-firstactivation&realestatetype=apartmentrent&channel=is24&publishedafter=###publishedafter###&features=adKeysAndStringValues,virtualTour,contactDetails,viareporting,nextgen,calculatedTotalRent,listingsInListFirstSummary,grouping,projectsInAllRealestateTypes",
            "property-type": "apartment",
            "notification-type": {
                "slack" : {
                    "color": "#cccccc"
                }
            }
        }, "")

    def test_main_haus_buy(self):
        handler.main({
            "query": "searchType=region&pagenumber=1&pagesize=20&channel=is24&realestatetype=housebuy&publishedafter=###publishedafter###&geocodes=/de/brandenburg,/de/berlin&price=-25000&sorting=-firstactivation",
            "property-type": "hauskauf",
            "notification-type": {
                "slack" : {
                    "color": "#48BB78"
                }
            }
        }, "")
