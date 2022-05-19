# Testing 101

Time to test our app!

## Steps

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Masterclass-M3-Testing).
2. Create a virtual environment and activate it.
3. Install the requirements using `pip install -r dev-requirements.lock`.
4. Add a **unit** test for `get_operator` and validate different inputs return the correct `operator` (have a look at `operator` functions [here](https://docs.python.org/3/library/operator.html)).
5. Add another **unit** test for `get_operator` and validate that **incorrect** inputs return `None`.
6. Run the tests using `pytest --cov=app tests`, you should **fail**.
7. Add another **unit** test for `get_arithmetic_result`, and validate the correct outputs.
   - You are **NOT** allowed to have the `get_operator` function completed yet, instead you must `mock` your `get_operator` function. Have a look at `mocking` [here](https://docs.python.org/3/library/unittest.mock.html) and [here](https://realpython.com/python-mock-library/).
   - If you do not mock the `get_operator` function, then this would be considered an integration test.
8. Add logic for `get_operator` in `utils.py`.
9. Add an integration test for the `main` function:
   - Your test should validate the return code (`0` is successful exits and `1` is error exits).
   - If the CLI was successful (and you expected it to be successful), then validate the answer is correct using `capsys` and the `in` operator for the captured output.
   - If the CLI was unsuccessful and you expected it to be unsuccessful, then no further assertions are required (hint: successful tests assertions should be in separate testing function than the error test assertions).

## Bonus

Add GitHub actions to run your tests when pushing/opening a PR.
