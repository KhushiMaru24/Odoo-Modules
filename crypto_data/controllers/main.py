from odoo import http
from odoo.http import request
import requests

class CryptoController(http.Controller):

    @http.route('/fetch_crypto_data', type='http', auth='none')
    def fetch_crypto_data(self, **kwargs):
        # crypto_id = '1'
        api_key = '16a5e132-5f6c-4263-be6a-604912b272e6'
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(data)
            request.env['crypto.data'].sudo().search([]).unlink()
            for crypto in data['data']:
                name = crypto['name']
                symbol = crypto['symbol']
                price_usd = crypto['quote']['USD']['price']

                request.env['crypto.data'].sudo().create({
                    'name': name,
                    'symbol': symbol,
                    'price_usd': price_usd,
                })
            return 'Cryptocurrency data fetched and stored successfully'
        else:
            return 'Failed to fetch cryptocurrency data'
