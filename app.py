from flask import Flask, request, Response, render_template
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/jpgtopng", methods=["GET"])
def jpg_to_png():
    return render_template("jpgtopng.html")

@app.route("/pngtojpg", methods=["GET"])
def png_to_jpg():
    return render_template("pngtojpg.html")

@app.route("/webptopng", methods=["GET"])
def webp_to_png():
    return render_template("webptopng.html")

@app.route("/bmptopng", methods=["GET"])
def bmp_to_png():
    return render_template("bmptopng.html")

@app.route("/pngtopdf", methods=["GET"])
def png_to_pdf():
    return render_template("pngtopdf.html")

@app.route("/api/jpgtopng", methods=["POST"])
def api_jpg_to_png():
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGBA")
    byte_io = io.BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    response = Response(byte_io.getvalue(), content_type="image/png")
    response.headers.set("Content-Disposition", "attachment", filename="converted_image.png")
    return response

@app.route("/api/pngtojpg", methods=["POST"])
def api_png_to_jpg():
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGB")
    byte_io = io.BytesIO()
    img.save(byte_io, 'JPEG')
    byte_io.seek(0)
    response = Response(byte_io.getvalue(), content_type="image/jpeg")
    response.headers.set("Content-Disposition", "attachment", filename="converted_image.jpeg")
    return response

@app.route("/api/webptopng", methods=["POST"])
def api_webp_to_png():
    image = request.files["image"]
    img = Image.open(image)
    img = img.convert("RGB")
    byte_io = io.BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    response = Response(byte_io.getvalue(), content_type="image/png")
    response.headers.set("Content-Disposition", "attachment", filename="converted_image.png")
    return response

@app.route("/api/bmptopng", methods=["POST"])
def api_bmp_to_png():
    image = request.files["image"]
    img = Image.open(image)
    byte_io = io.BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    response = Response(byte_io.getvalue(), content_type="image/png")
    response.headers.set("Content-Disposition", "attachment", filename="converted_image.png")
    return response

@app.route("/api/pngtopdf", methods=["POST"])
def api_png_to_pdf():
    image = request.files["image"]
    img = Image.open(image)
    byte_io = io.BytesIO()
    img.save(byte_io, 'PDF')
    byte_io.seek(0)
    response = Response(byte_io.getvalue(), content_type="application/pdf")
    response.headers.set("Content-Disposition", "attachment", filename="converted_file.pdf")
    return response

if __name__ == "__main__":
    app.run()
