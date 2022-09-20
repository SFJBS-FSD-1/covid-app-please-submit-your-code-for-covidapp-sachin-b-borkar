from passlib.hash import pbkdf2_sha256
password ="hello"
hased=  pbkdf2_sha256.hash(password)
print(hased)
if pbkdf2_sha256.verify("hello",hased):
    print("pasword encrypted verfied")
else:
    print("pasword encrypted not verfied")