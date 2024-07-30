from odoo import models, fields, api
import requests

class CryptoData(models.Model):
    _name = 'crypto.data'
    _description = 'Crypto Data'

    name = fields.Char(string='Cryptocurrency Name')
    symbol = fields.Char(string='Symbol')
    price_usd = fields.Float(string='Price in USD')

    # @api.model
    # def fetch_crypto_data(self):
    #     crypto_id = '1'
    #     api_key = '16a5e132-5f6c-4263-be6a-604912b272e6'
    #     url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?id={crypto_id}'
    #     headers = {
    #         'Accepts': 'application/json',
    #         'X-CMC_PRO_API_KEY': api_key,
    #     }
    #     response = requests.get(url, headers=headers)
    #     if response.status_code == 200:
    #         data = response.json()
    #         print(data)
    #         for crypto in data['data']:
    #             name = crypto['name']
    #             symbol = crypto['symbol']
    #             price_usd = crypto['quote']['USD']['price']
    #
    #             self.create({
    #                 'name': name,
    #                 'symbol': symbol,
    #                 'price_usd': price_usd,
    #             })
