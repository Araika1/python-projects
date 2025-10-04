import pyotp, segno, time

secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)
url = totp.provisioning_uri(name="student@example.com", issuer_name="MyUniversity")
print("Secret:", secret)
print("otpauth URL:", url)
segno.make(url).save("totp_qr.png", scale=8)
print("QR saved as totp_qr.png")

# Показать текущий и соседние коды (для отладки)
print("Код сейчас:    ", totp.now())
print("Код -1 шаг:    ", totp.at(int(time.time()) - 30))
print("Код +1 шаг:    ", totp.at(int(time.time()) + 30))

code = input("Введите код из приложения (только 6 цифр): ").strip().replace(" ", "")
# проверка с окном ±1 шага
ok = totp.verify(code, valid_window=1)
print("Проверка:", ok)
