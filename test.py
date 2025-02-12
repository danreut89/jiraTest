def greet():
    for _ in range(3):
        print("Hello, SonarCloud!")

def greet_duplicate():
    for _ in range(3):  # Duplicate block
        print("Hello, SonarCloud!")

def another_duplicate():
    for _ in range(3):  # Another duplicate block
        print("Hello, SonarCloud!")

if __name__ == "__main__":
    greet()
    greet_duplicate()
    another_duplicate()
