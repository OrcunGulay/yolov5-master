from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import detect
from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
import base64
from pathlib import Path

app = FastAPI()

# CORS ayarları
origins = [
    "http://localhost:3000",  # Burayı kendi React uygulamanızın adresi ile değiştirin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],  # Sadece POST isteklerine izin verilmesini istiyoruz
    allow_headers=["*"]  # Tüm başlıklara izin veriyoruz, ancak ihtiyaca göre düzenleyebilirsiniz
)

class ImageData(BaseModel):
    base64_image: str

@app.post("/upload_image/")
def upload_image(image_data: ImageData):
    # Base64 verisini al
    base64_data = str(image_data.base64_image)
    with open("metin_dosyasi.txt", "w") as dosya:
        dosya.write(base64_data)
    
    # Base64 verisini bytes verisine dönüştür
    image_bytes = base64.b64decode(base64_data)

    # Bytes verisini bir resme dönüştür
    image = Image.open(BytesIO(image_bytes))

    # YOLOv5 betiğini çağır ve resmi işle
    result = detect.run(
        source=image,  # Giriş resmi
        # Diğer parametreleri buraya ekleyin
    )
    
    return {"result": result}
   