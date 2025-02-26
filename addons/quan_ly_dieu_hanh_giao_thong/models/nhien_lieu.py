from odoo import models, fields, api
class NhienLieu(models.Model):
    _name = 'nhien_lieu'
    _description = 'Quản lý Nhiên Liệu'

    vehicle_id = fields.Many2one('phuong_tien', string='Phương tiện', required=True)
    date = fields.Date(string='Ngày đổ nhiên liệu', required=True)
    current_km = fields.Float(string='Số km hiện tại')
    fuel_liters = fields.Float(string='Số lít nhiên liệu')
    fuel_price = fields.Float(string='Giá nhiên liệu')
    fuel_efficiency = fields.Float(string='Tiêu hao nhiên liệu (lít/km)', compute='_compute_efficiency')

    @api.depends('current_km', 'fuel_liters')
    def _compute_efficiency(self):
        for record in self:
            if record.fuel_liters:
                record.fuel_efficiency = record.current_km / record.fuel_liters
            else:
                record.fuel_efficiency = 0.0