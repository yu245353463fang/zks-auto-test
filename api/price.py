import os
from base.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Price(RestClient):
    def __init__(self, api_root_url,**kwargs):
        super(Price, self).__init__(api_root_url, **kwargs)

    def list_price(self, **kwargs):
        return self.get('/api/app/v1/tokens/price', **kwargs)

    def list_pairs_summary(self, **kwargs):
        return self.get('api/explorer/v1/pairs/summary', **kwargs)


price = Price(api_root_url)