from odoo import models, fields, api


class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Bảng chứa thông tin phòng ban'

    ma_phong_ban = fields.Char("Mã phòng bàn", required=True)
    ten_phong_ban = fields.Char("Tên phòng ban")

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.ten_phong_ban))
        return result