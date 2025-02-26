from odoo import models, fields, api
class ViPham(models.Model):
    _name = 'vi_pham'
    _description = 'Quản lý Vi Phạm Giao Thông'

    driver_id = fields.Many2one('tai_xe', string='Tài xế', required=True)
    vehicle_id = fields.Many2one('phuong_tien', string='Phương tiện', required=True)
    violation_type = fields.Selection([
        ('speeding', 'Vượt tốc độ'),
        ('wrong_lane', 'Đi sai làn'),
        ('lights_off', 'Không bật đèn')
    ], string='Loại vi phạm', required=True)
    violation_date = fields.Date(string='Ngày vi phạm', required=True)
    fine_amount = fields.Float(string='Số tiền phạt')
    status = fields.Selection([
        ('pending', 'Chưa đóng phạt'),
        ('paid', 'Đã đóng phạt')
    ], string='Trạng thái', default='pending')
