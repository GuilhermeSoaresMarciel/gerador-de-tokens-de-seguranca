import time
import base58

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

class SessionGenerator:
    CURVE = ec.SECP256R1()

    ALPHABET = b"MfoqFNBUnJ4l7DWedPvLs-YtVz8wK15rZc90Rm3EbiCSjhaApkxOHIy2XQ"

    def generate(self):
        private_key = ec.generate_private_key(self.CURVE, default_backend())

        public_bytes = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.X962,
            format=serialization.PublicFormat.UncompressedPoint,
        )

        payload = public_bytes + int(time.time()).to_bytes(
            8,
            "little",
            signed=True,
        )

        return base58.b58encode(
            payload,
            alphabet=self.ALPHABET,
        ).decode("utf-8")


generator = SessionGenerator()

print(generator.generate())