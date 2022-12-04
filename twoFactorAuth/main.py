import pyotp
import qrcode

# key = pyotp.random_base32()
# print(key)

# time.sleep(30)
# print(totp.now())

key = "H5VJTEIN6HU6H4D2LZNGJ5WAQ7RIIQOL"

"""
totp = pyotp.TOTP(key)
print(totp.now())
input_code = input("Enter 2FA Code:")
print(totp.verify(input_code))

counter = 0

hotp = pyotp.HOTP(key)

print(hotp.at(0))

for _ in range(5):
    print(hotp.verify(input("Enter Code: "), counter))
    counter += 1

"""

# uri = pyotp.totp.TOTP(key).provisioning_uri(name="paulthomas",
  #                                          issuer_name="Pauls App")

# print(uri)

# otpauth://totp/Pauls%20App:paulthomas?secret=H5VJTEIN6HU6H4D2LZNGJ5WAQ7RIIQOL&issuer=Pauls%20App

# qrcode.make(uri).save("paul.png")

totp = pyotp.TOTP(key)
while True:
    print(totp.verify(input("Enter Code: ")))
