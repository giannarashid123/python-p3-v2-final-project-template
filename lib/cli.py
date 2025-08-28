from helpers import (
    create_user,
    login_user,
    exit_program
)

def main():
    while True:
        print("\nLanguage Learning CLI App")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("> ")

        if choice == "1":
            create_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
