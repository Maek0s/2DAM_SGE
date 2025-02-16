import base64
import io
import random
from PIL import Image
from odoo import http
from odoo.http import request

class RandomImageController(http.Controller):

    @http.route('/random_image', type='http', auth='public', methods=['GET'], cors="*")
    def generate_random_image(self, width=100, height=100):
        """Genera una imagen aleatoria y la devuelve en base64."""
        try:
            width = int(width)
            height = int(height)
        except ValueError:
            return "Invalid width or height", 400

        # Crear una imagen RGB con píxeles aleatorios
        image = Image.new("RGB", (width, height))
        pixels = [(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ) for _ in range(width * height)]
        image.putdata(pixels)

        # Guardar la imagen en un buffer de memoria
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # Responder con la imagen en base64
        return request.make_response(
            f'<img src="data:image/png;base64,{image_base64}" />',
            headers=[('Content-Type', 'text/html')]
        )
