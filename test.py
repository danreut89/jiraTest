# test.py - new

def greet():
    for _ in range(10):  # Increase duplicate block size
        print("Hello, SonarCloud!")
    print("Testing SonarCloud duplication detection.")
    print("Testing SonarCloud duplication detection.")  # Duplicate line
    print("Testing SonarCloud duplication detection.")  # Duplicate line

if __name__ == "__main__":
    greet()
