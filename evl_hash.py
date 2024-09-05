from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from dotenv import load_dotenv, set_key

env_file = '.env'
load_dotenv()

# Чтение публичного ключа из файла
def load_public_key():
    try:
        with open("public_key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read()
            )
        return public_key
    except FileNotFoundError:
        print("Ошибка: Файл 'public_key.pem' не найден.")
        raise
    except Exception as e:
        print(f"Ошибка при загрузке публичного ключа: {e}")
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


# Проверка подписи
def verify_signature(public_key, file_path, signature):
    hash_value = hash_file(file_path)
    if hash_value is not None:
        try:
            public_key.verify(
                bytes.fromhex(signature),
                hash_value,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
    return False


# Проверка всех подписанных файлов
def verify_signed_files(combined_file):
    public_key = load_public_key()
    with open(combined_file, "r") as f:
        lines = f.readlines()

    for i in range(1, len(lines), 3):  # Пропускаем заголовок
        file_path = lines[i].strip()[:-1]  # Убираем ":"
        hash_value = lines[i + 1].strip().split(": ")[1]
        signature = lines[i + 2].strip().split(": ")[1]

        is_valid = verify_signature(public_key, file_path, signature)
        if is_valid:
            print(f"Подпись для файла '{file_path}' верна.")
        else:
            print(f"Подпись для файла '{file_path}' неверна.")
            print("Остановка выполнения программы из-за неверной подписи!")
            set_key(env_file, 'evlstop', '0')
            return  # Прерываем выполнение, если подпись неверна


if __name__ == "__main__":
    combined_file = "combined_signatures.txt"
    verify_signed_files(combined_file)
