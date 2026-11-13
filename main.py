import unittest

if __name__ == "__main__":
    # print("Run test cases with `uv run python unittest -v`")
    print("Running unit tests...")
    # os.system("uv run python -m unittest -v")
    tests = unittest.TestLoader().discover(start_dir="tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)
