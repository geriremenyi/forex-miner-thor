from http import HTTPStatus


class ProblemDetails(object):
    def __init__(self, status: int, details: str):
        self.status = status
        self.title = HTTPStatus(status)
        self.type = "https://httpstatuses.com/" + str(status)
        self.details = details

