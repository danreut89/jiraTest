def greet():
    for _ in range(10):  # Increase the loop size
        print("Hello, SonarCloud!")
    print("This is a test function to check SonarCloud.")
    print("This is a test function to check SonarCloud.")  # Duplicate line
    print("This is a test function to check SonarCloud.")  # Duplicate line

def greet_duplicate():
    for _ in range(10):  # Exact same block as above
        print("Hello, SonarCloud!")
    print("This is a test function to check SonarCloud.")
    print("This is a test function to check SonarCloud.")  # Duplicate line
    print("This is a test function to check SonarCloud.")  # Duplicate line

if __name__ == "__main__":
    greet()
    greet_duplicate()
