from fastapi import FastAPI, Response
import qrcode
import io

app = FastAPI()

@app.get("/")
@app.get("/api/generate")
def generate_qr(text: str = "https://github.com"):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        return Response(content=img_bytes, media_type="image/png")

    except Exception as e:
        return Response(content=f"Error interno: {str(e)}", status_code=500)