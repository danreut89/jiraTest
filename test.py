def greet():
    print("Hello, SonarCloud!")

def greet_duplicate():
    print("Hello, SonarCloud!")  # This is a duplicate function

if __name__ == "__main__":
    greet()
    greet_duplicate()
