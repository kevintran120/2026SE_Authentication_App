# Feedback

### **Strengths**
1. **Basic Functionality**:
   - The code implements login, registration, and password change functionality, which are essential for a user management system.
   - It uses file I/O to persist user data, ensuring that data is retained across program runs.

2. **Use of `match` Statements**:
   - The use of `match` statements for handling user choices is clean and improves readability.

3. **Separation of Concerns**:
   - Functions like `login`, `register`, and `logged_in` are separated, which is a good practice for modularity.

---

### **Issues and Suggestions for Improvement**

#### 1. **Insecure Password Storage**
   - Passwords are stored in plaintext in `plain_text.txt`, which is a major security risk.
   - **Fix**: Use a library like `bcrypt` to hash passwords before storing them and verify the hash during login.

   Example:
   ```python
   import bcrypt

   salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

   # Hashing a password
   hashed_password = bcrypt.hashpw(password.encode(), salt=salt)

   # Verifying a password
   if bcrypt.checkpw(input_password.encode(), hashed_password):
       print("Login successful!")
   ```

---

#### 2. **Error Handling**
   - **File Not Found**:
     - The program assumes that `plain_text.txt` exists, which can cause a `FileNotFoundError` if the file is missing.
     - **Fix**: Add error handling to check if the file exists and create it if necessary.

   Example:
   ```python
   import os

   if not os.path.exists("plain_text.txt"):
       with open("plain_text.txt", "w") as file:
           pass  # Create an empty file
   ```

   - **Input Validation**:
     - The program does not validate user inputs properly, which can lead to unexpected behavior or crashes.
     - **Fix**: Add input validation for all user inputs.

---

#### 3. **Code Logic Issues**
   - **Login Logic**:
     - The `login` function uses a `found` flag, but the logic is convoluted and could be simplified.
     - The `line` variable is reused incorrectly in the password check, which can lead to undefined behavior.
     - **Fix**: Refactor the login logic to avoid reusing variables and simplify the flow.

   Example:
   ```python
   def login():
       username = input("Username: ")
       password = input("Password: ")

       with open("plain_text.txt", "r") as file:
           for line in file:
               stored_username, stored_password = line.strip().split(",")
               if stored_username == username and stored_password == password:
                   print("Login successful!")
                   return
       print("Invalid username or password")
   ```

   - **Password Change**:
     - The `change_password` function is incomplete and does not implement the required functionality.
     - **Fix**: Implement logic to update the password in the file.

   Example:
   ```python
   def change_password(username):
       new_password = input("Enter your new password: ")
       lines = []

       with open("plain_text.txt", "r") as file:
           for line in file:
               stored_username, stored_password = line.strip().split(",")
               if stored_username == username:
                   lines.append(f"{stored_username},{new_password}\n")
               else:
                   lines.append(line)

       with open("plain_text.txt", "w") as file:
           file.writelines(lines)

       print("Password changed successfully!")
   ```

   - **Registration Logic**:
     - The `register` function does not handle edge cases like empty usernames or passwords.
     - **Fix**: Add validation for username and password inputs.

---

#### 4. **Code Readability**
   - The code lacks comments explaining the purpose of each block, making it harder to understand.
   - Variable names like `line[1]` and `line[0]` are not descriptive.
   - **Fix**: Use meaningful variable names and add comments to explain the logic.

---

#### 5. **File Handling**
   - The program opens the file multiple times in different places, which is inefficient.
   - **Fix**: Load the file content into memory once and reuse it where needed.