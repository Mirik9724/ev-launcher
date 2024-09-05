from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import os


# Проверка наличия ключей и их создание, если они отсутствуют
def create_keys_if_not_exists():
    if not os.path.exists("private_key.pem") or not os.path.exists("public_key.pem"):
        print("Ключи не найдены. Генерация новых ключей...")

        # Генерация приватного ключа
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        # Сохранение приватного ключа в файл
        with open("private_key.pem", "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Генерация публичного ключа
        public_key = private_key.public_key()

        # Сохранение публичного ключа в файл
        with open("public_key.pem", "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

        print("Ключи успешно сгенерированы и сохранены в файлы.")
    else:
        print("Ключи уже существуют.")


# Чтение приватного ключа из файла
def load_private_key():
    try:
        with open("private_key.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
        return private_key
    except FileNotFoundError:
        print("Ошибка: Файл 'private_key.pem' не найден.")
        raise
    except Exception as e:
        print(f"Ошибка при загрузке приватного ключа: {e}")
        raise


# Хеширование файла
def hash_file(file_path):
    hasher = hashes.Hash(hashes.SHA256())
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.finalize()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return None


# Подпись файла и хеширование
def sign_and_hash_file(private_key, file_path, combined_file):
    hash_value = hash_file(file_path)
    if hash_value is not None:
        # Создание подписи
        signature = private_key.sign(
            hash_value,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Сохранение хеша и подписи в один файл
        with open(combined_file, "a") as f:
            f.write(f"{file_path}:\n")
            f.write(f"  Хеш: {hash_value.hex()}\n")
            f.write(f"  Подпись: {signature.hex()}\n")

        print(f"Файл '{file_path}' подписан и хеш сохранен в '{combined_file}'.")


# Подпись всех файлов в директории
def sign_multiple_files(file_paths):
    try:
        private_key = load_private_key()
        combined_file = "combined_signatures.txt"
        # Очистка файла с хешами и подписями перед записью
        with open(combined_file, "w") as f:
            f.write("Подписи и хеши файлов:\n")

        for file_path in file_paths:
            sign_and_hash_file(private_key, file_path, combined_file)
    except Exception as e:
        print(f"Ошибка при подписании файлов: {e}")


if __name__ == "__main__":
    create_keys_if_not_exists()
    files_to_sign = [
        "evl_start.py",
        "evl_check_libs.py",
        "evl_env_file.py",
        "evl_latest_log.py",
        "evl_license.py",
        "evl_main.py",
        "evl_settings.py",
        "evl_hash.py"
    ]
    sign_multiple_files(files_to_sign)
