import hashlib

h = hashlib.new("SHA256")
correct_password = "MyPassword123567"
h.update(correct_password.encode())

password_hash = h.hexdigest()
print(password_hash)

user_input = "MyPassword123567"
h = hashlib.new("SHA256")
h.update(user_input.encode())
input_hash = h.hexdigest()
print(input_hash)

print(input_hash == password_hash)

CORRECT_HASH = 'b546098aacd168cc02404d7b0073726aa161aa8e8c1e5dea8f06758100fa1857'

with open("Everything-1.4.1.1022.x86.en-US-Setup.exe", "rb") as f:
    file_bytes = f.read()
    h = hashlib.sha256()
    h.update(file_bytes)
    file_hash = h.hexdigest()
    # or 3.11 alternative
    digest = hashlib.file_digest(f, 'SHA256').hexdigest()
    print(digest)


print(file_hash == CORRECT_HASH)
print(digest == CORRECT_HASH)
