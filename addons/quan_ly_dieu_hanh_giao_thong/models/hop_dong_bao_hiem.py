from odoo import models, fields, api
class HopDongBaoHiem(models.Model):
    _name = 'hop_dong_bao_hiem'
    _description = 'Quản lý Hợp Đồng & Bảo Hiểm'

    vehicle_id = fields.Many2one('phuong_tien', string='Phương tiện', required=True)
    contract_start = fields.Date(string='Ngày bắt đầu')
    contract_end = fields.Date(string='Ngày kết thúc')
    rental_company = fields.Char(string='Công ty thuê hoặc cho thuê')
    rental_price = fields.Float(string='Giá thuê')
    insurance_company = fields.Char(string='Công ty bảo hiểm')
    insurance_package = fields.Char(string='Gói bảo hiểm')
    insurance_price = fields.Float(string='Số tiền bảo hiểm')