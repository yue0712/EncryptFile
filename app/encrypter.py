import gnupg

class Encrypter:
    def __init__(self) -> None:
        self.gpg = gnupg.GPG()

    def generate_key(self, key_length=2048, key_type="RSA", passphrase=None):
        """
        生成 OpenPGP 密钥对
        """
        input_data = self.gpg.gen_key_input(
            key_type=key_type,
            key_length=key_length,
            passphrase=passphrase
        )
        key = self.gpg.gen_key(input_data)
        return key.fingerprint

    def encrypt(self, input_data, output_path, passphrase):
        """
        使用 OpenPGP 加密文件
        """
        encrypted_data = self.gpg.encrypt(input_data, passphrase=passphrase, symmetric=True, recipients=None)

        with open(output_path, 'wb') as file:
            file.write(encrypted_data.data)

    def decrypt(self, encrypted_file_path, passphrase) -> bytes:
        """
        使用 OpenPGP 解密文件
        """
        with open(encrypted_file_path, 'rb') as input_file:
            encrypted_data = input_file.read()

        decrypted_data = self.gpg.decrypt(encrypted_data, passphrase=passphrase)

        return decrypted_data.data

    def encrypt_file(self, input_path, output_path, passphrase):
        self.gpg.encrypt_file(input_path, output=output_path, passphrase=passphrase, symmetric=True, recipients=None)

    def decrypt_file(self, encrypted_file_path, output_path, passphrase):
        self.gpg.decrypt_file(encrypted_file_path, output=output_path, passphrase=passphrase)

