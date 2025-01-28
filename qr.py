import qrcode
from PIL import Image

# URL que deseas convertir en un código QR
url = 'https://lissbakeryweb.netlify.app/tableprice'

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mejor corrección de errores para incluir una imagen
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear una imagen del código QR
img_qr = qr.make_image(fill='black', back_color='white')

# Abrir el icono del pastel
icon_path = 'lisslogo.png'  # Asegúrate de tener esta imagen en tu directorio
icon = Image.open(icon_path)

# Calcular el tamaño del icono para que se ajuste al centro del código QR
img_qr_width, img_qr_height = img_qr.size
icon_size = int(img_qr_width / 5)
icon = icon.resize((icon_size, icon_size), Image.LANCZOS)

# Calcular la posición para pegar el icono
pos = ((img_qr_width - icon_size) // 2, (img_qr_height - icon_size) // 2)
img_qr.paste(icon, pos, mask=icon)

# Guardar la imagen final del código QR
img_qr.save('codigo_qr_con_pastel.png')
