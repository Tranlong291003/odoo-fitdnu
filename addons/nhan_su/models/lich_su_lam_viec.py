from odoo import models, fields

class LichSuLamViec(models.Model):
    _name = 'lich_su_lam_viec'
    _description = 'Bảng chứa lịch sử làm việc của nhân viên'

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True)
    phong_ban_id = fields.Many2one('phong_ban', string="Phòng ban", required=True)
    chuc_vu_id = fields.Many2one('chuc_vu', string="Chức vụ", required=True)
    
    loai_chuc_vu = fields.Selection(
        [
            ('Chính', 'Chính'),
            ('Kiêm nhiệm', 'Kiêm nhiệm')
        ],
        string="Loại chức vụ",
        default='Chính'
    )
