import qrcode
import os

# Directorio de videos y qrcodes
base_url = "http://localhost:8000/videos"
video_folder = "videos"
qr_folder = "qrcodes"

# Crear carpeta qrcodes si no existe
os.makedirs(qr_folder, exist_ok=True)

# Generar un QR para cada video
for i in range(1, 21):
    video_url = f"{base_url}/video{i}.mp4"
    qr = qrcode.make(video_url)
    qr_path = os.path.join(qr_folder, f"video{i}.png")
    qr.save(qr_path)
    print(f"QR generado para {video_url}")
