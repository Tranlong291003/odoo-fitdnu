from odoo import models, fields, api
class LichTrinh(models.Model):
    _name = 'lich_trinh'
    _description = 'Quản lý Lịch Trình'

    vehicle_id = fields.Many2one('phuong_tien', string='Phương tiện', required=True)
    driver_id = fields.Many2one('tai_xe', string='Tài xế', required=True)
    start_time = fields.Datetime(string='Thời gian xuất phát', required=True)
    end_time = fields.Datetime(string='Thời gian về')
    start_location = fields.Char(string='Địa điểm xuất phát', required=True)
    end_location = fields.Char(string='Đích đến', required=True)
    status = fields.Selection([
        ('pending', 'Chưa bắt đầu'),
        ('in_progress', 'Đang thực hiện'),
        ('completed', 'Đã hoàn thành')
    ], string='Trạng thái', default='pending')
    notes = fields.Text(string='Ghi chú hành trình')