def test_app_running():
    """Test that the app runs successfully"""
    import app  # This will run print statement
    assert True  # If app.py runs without error, test passes

def test_sample():
    """Simple mathematical test"""
    assert 1 + 1 == 2

if __name__ == "__main__":
    print("Running tests...")
    test_app_running()
    test_sample()
    print("All tests passed!")
