import unittest

from main import call_api, get_mongodb_character_id, replace_pilots, upload_to_mongodb


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.main_starting_api = "https://swapi.dev/api/starships"
        self.testing_api_1 = "https://swapi.dev/api/people/13/"
        self.testing_api_2 = "https://swapi.dev/api/starships/5/"
        self.testing_ship_1 = [{'name': 'Jedi Interceptor', 'model': 'Eta-2 Actis-class light interceptor', 'manufacturer': 'Kuat Systems Engineering', 'cost_in_credits': '320000', 'length': '5.47', 'max_atmosphering_speed': '1500', 'crew': '1', 'passengers': '0', 'cargo_capacity': '60', 'consumables': '2 days', 'hyperdrive_rating': '1.0', 'MGLT': 'unknown', 'starship_class': 'starfighter', 'pilots': ['https://swapi.dev/api/people/10/', 'https://swapi.dev/api/people/11/'], 'films': ['https://swapi.dev/api/films/6/'], 'created': '2014-12-20T19:56:57.468000Z', 'edited': '2014-12-20T21:23:49.951000Z', 'url': 'https://swapi.dev/api/starships/65/'}]
        self.testing_ship_2 = [{
            "name": "CR90 corvette",
            "model": "CR90 corvette",
            "manufacturer": "Corellian Engineering Corporation",
            "cost_in_credits": "3500000",
            "length": "150",
            "max_atmosphering_speed": "950",
            "crew": "30-165",
            "passengers": "600",
            "cargo_capacity": "3000000",
            "consumables": "1 year",
            "hyperdrive_rating": "2.0",
            "MGLT": "60",
            "starship_class": "corvette",
            "pilots": [],
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-10T14:20:33.369000Z",
            "edited": "2014-12-20T21:23:49.867000Z",
            "url": "https://swapi.dev/api/starships/2/"
        }]
        self.testing_names_1 = "Anakin Skywalker"

    def test_call_api(self):
        actual = call_api(self.testing_api_2)
        expected = [{
            "name": "Sentinel-class landing craft",
            "model": "Sentinel-class landing craft",
            "manufacturer": "Sienar Fleet Systems, Cyngus Spaceworks",
            "cost_in_credits": "240000",
            "length": "38",
            "max_atmosphering_speed": "1000",
            "crew": "5",
            "passengers": "75",
            "cargo_capacity": "180000",
            "consumables": "1 month",
            "hyperdrive_rating": "1.0",
            "MGLT": "70",
            "starship_class": "landing craft",
            "pilots": [],
            "films": ["https://swapi.dev/api/films/1/"],
            "created": "2014-12-10T15:48:00.586000Z",
            "edited": "2014-12-20T21:23:49.873000Z",
            "url": "https://swapi.dev/api/starships/5/"
                }]
        self.assertEqual(
            expected, actual,
            "Expected `call_api` method to return a list of dict of api responses"
        )


    def test_get_mongodb_character_id(self):
        actual = str(get_mongodb_character_id(self.testing_names_1))
        expected = "61e58b4d1098a06001dc2ddf"
        self.assertEqual(
            expected, actual,
            "Expected `get_mongodb_character_id` method to return the id in type type bson.objectid.ObjectId \
                (but I don't know how to set that type so I converted it to a string) "
        )


    def test_replace_pilots(self):
        actual = replace_pilots(self.testing_ship_1)
        expected = [{'name': 'Jedi Interceptor', 'model': 'Eta-2 Actis-class light interceptor', 'manufacturer': 'Kuat Systems Engineering', 'cost_in_credits': '320000', 'length': '5.47', 'max_atmosphering_speed': '1500', 'crew': '1', 'passengers': '0', 'cargo_capacity': '60', 'consumables': '2 days', 'hyperdrive_rating': '1.0', 'MGLT': 'unknown', 'starship_class': 'starfighter', 'pilots': ['61e58b6d928a45949b85099b', '61e58b4d1098a06001dc2ddf'], 'films': ['https://swapi.dev/api/films/6/'], 'created': '2014-12-20T19:56:57.468000Z', 'edited': '2014-12-20T21:23:49.951000Z', 'url': 'https://swapi.dev/api/starships/65/'}]
        actual[0]["pilots"][0] = str(actual[0]["pilots"][0])
        actual[0]["pilots"][1] = str(actual[0]["pilots"][1])

        self.assertEqual(
            expected, actual,
            "Expected `replace_pilots` method to return the pilot dict with apis in 'pilot' replaced with id's type \
            bson.objectid.ObjectId (but I don't know how to set that type so I converted it to a string) "
        )


    def test_upload_to_mongodb(self):
        actual = upload_to_mongodb(self.testing_ship_2)
        expected = True
        self.assertEqual(
            expected, actual,
            "Expected `upload_to_mongodb` method to return true"
        )
