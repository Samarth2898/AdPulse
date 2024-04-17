# unit test for ad-service
import unittest
from unittest.mock import MagicMock, patch

from app.services.ad_service import get_all_ads, create_ad, get_ad_by_id, get_ad_by_state, update_ad_state, update_ad


class TestAdService(unittest.TestCase):
    def setUp(self):
        # Mocking the create_session function
        self.mock_create_session = MagicMock()
        self.session_mock = MagicMock()
        self.mock_create_session.return_value = self.session_mock

    def test_create_ad(self):
        json_data = {
            "adid": "",
            "adname": "test2024",
            "adpriority": 4,
            "adstate": "CREATED",
            "adtype": "GUARANTEED",
            "advertiserid": "A12345",
            "bidinfo": None,
            "budget": None,
            "campaignid": "C54321",
            "createdat": "Wed, 10 Apr 2024 16:22:38 GMT",
            "createdby": "kushal.1nagaraj.1@gmail.com",
            "creativeid": "CR12345",
            "enddate": "2024-03-17T21:05:56",
            "frequencycaps": None,
            "landingurl": "https://www.hotstar.com",
            "startdate": "2024-03-17T21:05:56",
            "targetinginfo": None,
            "updatedat": "",
            "updatedby": "aditihk@gmail.com"
        }

        created_ad = create_ad(json_data)
        self.assertIsNotNone(created_ad)
        self.assertEqual(created_ad['adname'], json_data['adname'])


    def test_get_all_ads(self):
        all_ads = get_all_ads()
        self.assertIsNotNone(all_ads)
        self.assertIn("test1Aditi", [ad['adname'] for ad in all_ads])

    def test_get_ad_by_id(self):
        json_data = {
            "adid": "",
            "adname": "test1Aditi",
            "adpriority": 4,
            "adstate": "CREATED",
            "adtype": "GUARANTEED",
            "advertiserid": "A12345",
            "bidinfo": None,
            "budget": None,
            "campaignid": "C54321",
            "createdat": "Wed, 10 Apr 2024 16:22:38 GMT",
            "createdby": "kushal.1nagaraj.1@gmail.com",
            "creativeid": "CR12345",
            "enddate": "2024-03-17T21:05:56",
            "frequencycaps": None,
            "landingurl": "https://www.hotstar.com",
            "startdate": "2024-03-17T21:05:56",
            "targetinginfo": None,
            "updatedat": "",
            "updatedby": "aditihk@gmail.com"
        }

        created_ad = create_ad(json_data)
        ad_id = created_ad['adid']
        ad = get_ad_by_id(ad_id)
        self.assertIsNotNone(ad)
        self.assertEqual(ad['adid'], ad_id)

    def test_update_ad_state(self):
        json_data = {
            "adid": "",
            "adname": "test1Aditi",
            "adpriority": 4,
            "adstate": "CREATED",
            "adtype": "GUARANTEED",
            "advertiserid": "A12345",
            "bidinfo": None,
            "budget": None,
            "campaignid": "C54321",
            "createdat": "Wed, 10 Apr 2024 16:22:38 GMT",
            "createdby": "kushal.1nagaraj.1@gmail.com",
            "creativeid": "CR12345",
            "enddate": "2024-03-17T21:05:56",
            "frequencycaps": None,
            "landingurl": "https://www.hotstar.com",
            "startdate": "2024-03-17T21:05:56",
            "targetinginfo": None,
            "updatedat": "",
            "updatedby": "aditihk@gmail.com"
        }
        created_ad = create_ad(json_data)
        ad_id = created_ad['adid']
        state = "ACTIVE"
        update_ad_state(ad_id, state)
        updated_ad = get_ad_by_id(ad_id)
        self.assertIsNotNone(updated_ad)
        self.assertEqual(updated_ad['adstate'], state)

    def test_update_ad(self):
        json_data = {
            "adid": "",
            "adname": "test1Aditi",
            "adpriority": 4,
            "adstate": "CREATED",
            "adtype": "GUARANTEED",
            "advertiserid": "A12345",
            "bidinfo": None,
            "budget": None,
            "campaignid": "C54321",
            "createdat": "Wed, 10 Apr 2024 16:22:38 GMT",
            "createdby": "kushal.1nagaraj.1@gmail.com",
            "creativeid": "CR12345",
            "enddate": "2024-03-17T21:05:56",
            "frequencycaps": None,
            "landingurl": "https://www.hotstar.com",
            "startdate": "2024-03-17T21:05:56",
            "targetinginfo": None,
            "updatedat": "",
            "updatedby": "aditihk@gmail.com"
        }

        created_ad = create_ad(json_data)
        ad_id = created_ad['adid']

        updated_json_data = {
            "adid": ad_id,
            "adname": "test1Aditi",
            "adpriority": 7,
            "adstate": "CREATED",
            "adtype": "GUARANTEED",
            "advertiserid": "A12345",
            "bidinfo": None,
            "budget": None,
            "campaignid": "C54321",
            "createdat": "Wed, 10 Apr 2024 16:22:38 GMT",
            "createdby": "kushal.1nagaraj.1@gmail.com",
            "creativeid": "CR12345",
            "enddate": "2024-03-17T21:05:56",
            "frequencycaps": None,
            "landingurl": "https://www.hotstar.com",
            "startdate": "2024-03-17T21:05:56",
            "targetinginfo": None,
            "updatedat": "",
            "updatedby": "aditihk@gmail.com"
        }

        update_ad(updated_json_data)
        updated_ad = get_ad_by_id(ad_id)
        self.assertIsNotNone(updated_ad)
        self.assertEqual(updated_ad['adpriority'], updated_json_data['adpriority'])


    def test_get_ad_by_state(self):
        state = "ACTIVE"
        ads = get_ad_by_state(state)
        self.assertIsNotNone(ads)
        self.assertIn("test1Aditi", [ad['adname'] for ad in ads])


if __name__ == '__main__':
    unittest.main()
