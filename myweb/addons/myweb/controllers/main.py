from odoo import http
from odoo.http import request

class WsController(http.Controller):
    @http.route([
        'mywebsite',
        ], type='http', auth='public', website=True, cors='*')
    def main(self):

        return request.render('myweb.website',{})
