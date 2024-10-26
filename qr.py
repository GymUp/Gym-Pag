import qrcode
import os

# Lista de URLs de los videos
videos = [
    "https://drive.google.com/file/d/1tQuZmJLTQeNVxJMitMnU3_XkPgSXZMgC/view?usp=sharing",
    "https://drive.google.com/file/d/1tf6jWnDsujS_qyaPmmtDsHyKv0w7QEXL/view?usp=sharing",
    "https://drive.google.com/file/d/1YVTkGdTf5vUqFoQKiExpm9O56p1ufzRf/view?usp=sharing",
    "https://drive.google.com/file/d/1n7j6LYRYWViokcOM3dxRs7g5JZ6mPL6U/view?usp=sharing",
    "https://drive.google.com/file/d/1n7j6LYRYWViokcOM3dxRs7g5JZ6mPL6U/view?usp=sharing",
    "https://drive.google.com/file/d/1rOeaB9HolEG8_9UxEmRNsrVGI4MhzcCt/view?usp=sharing",
    "https://drive.google.com/file/d/1rOeaB9HolEG8_9UxEmRNsrVGI4MhzcCt/view?usp=sharing",
    "https://drive.google.com/file/d/1SV9AbQNbWK2uZmYjK8NK6Sda0uL2ekBe/view?usp=sharing",
    "https://drive.google.com/file/d/1-PO2apkqda1LoWJ65QGL7m68ZlUQFqKb/view?usp=sharing",
    "https://drive.google.com/file/d/1TXAZ7fvt0N_ga1wvFCvo4XzEe9Vjkbpo/view?usp=sharing",
    "https://drive.google.com/file/d/1HdEah7OmF0LkX5b2o-2lz-v2rb5QWUt8/view?usp=sharing",
    "https://drive.google.com/file/d/1HdEah7OmF0LkX5b2o-2lz-v2rb5QWUt8/view?usp=sharing"
]

# Crear una carpeta para guardar los códigos QR
carpeta_qr = "codigos_qr"
os.makedirs(carpeta_qr, exist_ok=True)

# Generar un código QR para cada video
for i, video_url in enumerate(videos):
    # Nombre del archivo de imagen del código QR
    nombre_archivo = os.path.join(carpeta_qr, f"codigo_qr_video_{i + 1}.png")
    
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(video_url)
    qr.make(fit=True)

    # Crear imagen del código QR
    imagen = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen en un archivo
    imagen.save(nombre_archivo)

    print(f"Código QR para video {i + 1} generado y guardado como '{nombre_archivo}'")
