import unittest

from http import HTTPStatus

from forex_miner_thor.api.error import ProblemDetails


class TestProblemDetails(unittest.TestCase):
    def test_init(self):
        # Arrange
        status_code = 400
        details = "This is the test error"

        # Act
        problem = ProblemDetails(status_code, details)

        # Assert
        self.assertEqual(problem.status, status_code)
        self.assertEqual(problem.title, HTTPStatus(status_code))
        self.assertEqual(problem.type, "https://httpstatuses.com/" + str(status_code))
        self.assertEqual(problem.details, details)


if __name__ == '__main__':
    unittest.main()

