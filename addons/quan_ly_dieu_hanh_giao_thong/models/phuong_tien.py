from odoo import models, fields, api
class PhuongTien(models.Model):
    _name = 'phuong_tien'
    _description = 'Quản lý Phương Tiện'

    name = fields.Char(string='Tên phương tiện', required=True)
    license_plate = fields.Char(string='Biển số xe', required=True)
    vehicle_type = fields.Selection([
        ('truck', 'Xe tải'),
        ('bus', 'Xe buýt'),
        ('car', 'Xe con')
    ], string='Loại phương tiện', required=True)
    status = fields.Selection([
        ('available', 'Sẵn sàng'),
        ('in_use', 'Đang sử dụng'),
        ('maintenance', 'Bảo trì')
    ], string='Trạng thái', default='available')
    mileage = fields.Float(string='Số km đã đi')
    manufacture_year = fields.Integer(string='Năm sản xuất')
    manufacturer = fields.Char(string='Hãng sản xuất')
    image = fields.Binary(string='Hình ảnh phương tiện')
    driver_id = fields.Many2one('tai_xe', string='Tài xế phụ trách')