# lib/helpers.py
from models import Session, User

def create_user():
    session = Session()
    username = input("Enter username: ")
    email = input("Enter email: ")
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print("User already exists!")
        return
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print(f"User '{username}' created!")

def login_user():
    session = Session()
    username = input("Enter your username: ")
    user = session.query(User).filter_by(username=username).first()
    if user:
        print(f"Welcome back, {user.username}!")
        # You can now build user dashboard here
    else:
        print("User not found. Please sign up.")

def exit_program():
    print("Goodbye!")
    exit()
