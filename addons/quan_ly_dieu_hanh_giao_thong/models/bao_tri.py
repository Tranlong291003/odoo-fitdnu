from odoo import models, fields, api
class BaoTri(models.Model):
    _name = 'bao_tri'
    _description = 'Quản lý Bảo Trì'

    vehicle_id = fields.Many2one('phuong_tien', string='Phương tiện', required=True)
    maintenance_date = fields.Date(string='Ngày bảo trì', required=True)
    maintenance_type = fields.Selection([
        ('repair', 'Sửa chữa'),
        ('replacement', 'Thay thế')
    ], string='Loại bảo trì', required=True)
    details = fields.Text(string='Chi tiết sửa chữa')
    service_provider = fields.Char(string='Nhà cung cấp dịch vụ')
    cost = fields.Float(string='Chi phí bảo trì')
    next_maintenance = fields.Date(string='Lịch bảo trì tiếp theo')