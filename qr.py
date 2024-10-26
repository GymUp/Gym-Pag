import qrcode
import os

# Lista de URLs de los videos
videos = [
    "http://tu_dominio.com/videos/Best_Fitness_BFCCO10_Cable_Crossover.mp4",
    "http://tu_dominio.com/videos/Como_hacer_SENTADILLA_HACK.mp4",
    "http://tu_dominio.com/videos/Como_realizar_el_ejercicio_de_Press_de_pierna.mp4",
    "http://tu_dominio.com/videos/GEMELO_EN_MAQUINA_DE_PIE.mp4",
    "http://tu_dominio.com/videos/Gluteos_Articulado_Elevacion_Pelvica.mp4",
    "http://tu_dominio.com/videos/GN_Sentadilla_maquina_smith.mp4",
    "http://tu_dominio.com/videos/Hammer_Strength_Select_Pectoral_Fly.mp4",
    "http://tu_dominio.com/videos/Pantorrilla_Sentado.mp4",
    "http://tu_dominio.com/videos/Press_de_banca_plano.mp4",
    "http://tu_dominio.com/videos/Remo_sentado_en_polea.mp4",
    "http://tu_dominio.com/videos/saveinsta_extensiones_de_cuadriceps.mp4",
    "http://tu_dominio.com/videos/saveinsta_patada_de_gluteo_en_maquina.mp4"
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
