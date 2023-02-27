from app import index
import os

def set_action_output(output_name, value) :
    """Sets the GitHub Action output.

    Keyword arguments:
    output_name - The name of the output
    value - The value of the output
    """
    if "GITHUB_OUTPUT" in os.environ :
        with open(os.environ["GITHUB_OUTPUT"], "a") as f :
            print("{0}={1}".format(output_name, value), file=f)

def test_index():
    assert index() == "Hello, world!"
