def validate_user(name, age):
    """Return True when the supplied user details are valid."""
    if not isinstance(name, str) or not name.strip():
        return False
    if not isinstance(age, int) or age < 18:
        return False
    return True


if __name__ == "__main__":
    print("DVP Week 12 CI/CD validation app")
    print("Sample validation:", validate_user("Shalini", 24))
