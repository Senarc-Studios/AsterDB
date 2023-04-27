import os
import json
import click # type: ignore

from pathlib import Path
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

@click.group()
def aster():
    pass

@aster.command()
@click.option('--host', default='127.0.0.1', help='Host to bind to (defaults to 127.0.0.1)')
@click.option('--port', default=80, help='Port to bind to (defaults to 80)')
@click.option('--key', default=None, help='Load a SSH Key from a file.')
@click.option('--mongo', help='MongoDB connection string.')
@click.option('--encrypt', help='Encrypt existing data in the database.')
def install(host, port, key, mongo, encrypt):
    click.echo('Installing AsterDB API...')

    if key is None:
        key = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=2048
        )

        private_key = (key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption()
        )).decode("utf-8")

        public_key = (key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH
        )).decode("utf-8")

        home_directory = Path.home().replace("\\", "/")
        try:
            os.makedirs(home_directory + "/.ssh/aster.db", exist_ok = True)
        except:
            pass

        with open(home_directory + "/aster", "x") as file:
            file.write(private_key)
            click.echo('Private key created.')

        with open(home_directory + "/aster.pub", "x") as file:
            file.write(public_key)
            click.echo('Public key created.')

        private_key, public_key = home_directory + "/aster", home_directory + "/aster.pub"

    else:
        with open(key, "r") as file:
            private_key = file.read()
            click.echo('Private key loaded.')

        with open(key + ".pub", "r") as file:
            public_key = 
            click.echo('Public key loaded.')

    config_payload = {
        "host": host,
        "port": port,
        "mongo": mongo,
        "private_key": private_key,
        "public_key": public_key
    }
    with open("./config.json", "x") as file:
        file.write(json.dumps(config_payload, indent = 4))
        click.echo('Config file created.')