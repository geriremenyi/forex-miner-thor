import unittest

from marshmallow import fields

from forex_miner_thor.api.error import ProblemDetailsSchema


class TestProblemDetailSchema(unittest.TestCase):
    def test_init(self):
        # Arrange
        # Act
        problem_schema = ProblemDetailsSchema()

        # Assert
        self.assertEqual(type(problem_schema.fields["status"]), fields.Integer)
        self.assertEqual(type(problem_schema.fields["title"]), fields.String)
        self.assertEqual(type(problem_schema.fields["type"]), fields.String)
        self.assertEqual(type(problem_schema.fields["details"]), fields.String)


if __name__ == '__main__':
    unittest.main()

