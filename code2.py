import pyotp, segno

# 1. Генерация секрета (ключа)
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)

# 2. Формируем otpauth URL (используется для QR)
otpauth_url = totp.provisioning_uri(name="student@example.com", issuer_name="MyUniversity")
print("Secret:", secret)
print("otpauth URL:", otpauth_url)

# 3. Создаём QR-код и сохраняем как файл
segno.make(otpauth_url).save('totp_qr.png', scale=8)
print("QR saved as totp_qr.png")

# 4. Выводим текущий код (сервер вычисляет)
print("Текущий код (пример):", totp.now())

# 5. Проверка кода, введённого пользователем
code_from_phone = input("Введите код из приложения (6 цифр): ").strip()
print("Проверка:", totp.verify(code_from_phone))

