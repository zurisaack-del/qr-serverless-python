from fastapi import FastAPI, Response
import qrcode
import io

app = FastAPI()

@app.get("/api/generate")
def generate_qr(text: str = "https://github.com"):
    try:
        # Generar la imagen del código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen en un buffer de memoria en bytes
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        # Devolver la imagen PNG directamente
        return Response(content=img_bytes, media_type="image/png")

    except Exception as e:
        return Response(content=f"Error interno: {str(e)}", status_code=500)