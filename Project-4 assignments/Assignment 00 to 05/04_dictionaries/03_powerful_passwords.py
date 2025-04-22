print("03_powerful_passwords\n")

import hashlib

def hashed_password(password):
   return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
   "user@example.com": hashed_password("password123"),
   "admin@example.com": hashed_password("adminpass"),
}

def login(email, password):
   if email in stored_logins:
      return stored_logins[email] == hashed_password(password)
   return False

if __name__ == '__main__':
   email = input("Enter your email: ")
   password = input("Enter your password: ")

   if login(email, password):
      print("Login successfully!")
   else:
      print("Invalid email or password.")