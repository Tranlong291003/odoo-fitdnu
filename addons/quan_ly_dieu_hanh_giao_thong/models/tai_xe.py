from odoo import models, fields, api

class TaiXe(models.Model):
    _name = 'tai_xe'
    _description = 'Quản lý Tài Xế'

    name = fields.Char(string='Họ tên', required=True)
    phone = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    license_number = fields.Char(string='Số bằng lái')
    license_issue_date = fields.Date(string='Ngày cấp')
    license_expiry_date = fields.Date(string='Ngày hết hạn')
    experience = fields.Integer(string='Kinh nghiệm lái xe (năm)')
    rating = fields.Float(string='Đánh giá tài xế')
    image = fields.Binary(string='Ảnh tài xế')
    vehicle_id = fields.Many2one('phuong_tien', string='Phương tiện phụ trách')