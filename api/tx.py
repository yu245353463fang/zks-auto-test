import os
from base.rest_client import RestClient
from common.read_data import data
from zksync_sdk import zksync_signer



BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]

class transfer(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(transfer, self).__init__(api_root_url, **kwargs)

    def change_pubkey(self, **kwargs):
        return self.post('/api/app/v1/tx', **kwargs)

    def Transfer(self, **kwargs):
        return self.request('/api/app/v1/tx',data='',**kwargs)


class withdraw(RestClient):
    def __init__(self, api_root_yrl, **kwargs):
        super(withdraw, self).__init__(api_root_url, **kwargs)

    def info(self, **kwargs):
        return self.get('/api/app/v1/tx', **kwargs)

    def Withdraw(self, **kwargs):
        return self.request('')
