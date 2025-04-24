import qrcode
from io import BytesIO
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


MAP_LINKS = {
    "Cosmo Park": "https://2gis.kg/bishkek/firm/70000001019320032",
    "Bishkek Park" : "https://2gis.kg/bishkek/search/%D0%B1%D0%B8%D1%88%D0%BA%D0%B5%D0%BA%20%D0%BF%D0%B0%D1%80%D0%BA/firm/70000001019343641/74.590311%2C42.874854?m=74.590311%2C42.874854%2F15.69",
    "Tsum" : "https://2gis.kg/bishkek/branches/70000001019367293/firm/70000001039842673/74.61453%2C42.876625?m=74.595518%2C42.874855%2F14.32"
}

def hall_to_link(hall: str) -> str | None:
    return MAP_LINKS.get(hall)

def make_qr_pixmap(link: str, size: int = 220) -> QPixmap:
    qr = qrcode.QRCode(border=1, box_size=8)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    pix = QPixmap()
    pix.loadFromData(buf.getvalue(), "PNG")
    return pix.scaled(size, size,
                      Qt.AspectRatioMode.KeepAspectRatio,
                      Qt.TransformationMode.SmoothTransformation)
