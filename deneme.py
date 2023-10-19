import base64
from PIL import Image
from io import BytesIO


with open("metin_dosyasi.txt", "r") as dosya:
    icerik = dosya.read()
# Örnek bir base64 verisi
base64_data = str(icerik)

# Base64 verisini bytes verisine dönüştür
image_bytes = base64.b64decode(base64_data)

# Bytes verisini bir resme dönüştür
image = Image.open(BytesIO(image_bytes))

# Resmi görüntüle
image.show()