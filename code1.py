# password_demo.py
# pip install argon2-cffi

from argon2 import PasswordHasher, exceptions
import time, secrets, string, hashlib

ph = PasswordHasher(time_cost=2, memory_cost=102400, parallelism=2)  # параметры можно регулировать

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(hash: str, password: str) -> bool:
    try:
        return ph.verify(hash, password)
    except exceptions.VerifyMismatchError:
        return False

if __name__ == "__main__":
    # выбор пароля - для демонстрации
    passwd = "CorrectHorseBatteryStaple!123"
    h = hash_password(passwd)
    print("Hash:", h)

    # проверка (успешно)
    print("Проверка верного пароля:", verify_password(h, passwd))

    # эмуляция грубой атаки: перебираем словарь коротких паролей и измеряем время
    wordlist = ["123456", "password", "letmein", "CorrectHorseBatteryStaple!123"]
    start = time.perf_counter()
    found = None
    for w in wordlist:
        if verify_password(h, w):
            found = w
            break
    t = time.perf_counter() - start
    print("Bruteforce simulated: found=", found, "time=", t)
    # В реальном брутфорсе перебор дорог из-за аргоновских затрат времени/памяти
