class NotFoundError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

class BadRequestError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

class UnauthorizedError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

class ForbiddenError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

class InternalServerError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

def handle_error(error: Exception):
    if isinstance(error, NotFoundError):
        return {"status": 404, "detail": error.detail}
    elif isinstance(error, BadRequestError):
        return {"status": 400, "detail": error.detail}
    elif isinstance(error, UnauthorizedError):
        return {"status": 401, "detail": error.detail}
    elif isinstance(error, ForbiddenError):
        return {"status": 403, "detail": error.detail}
    elif isinstance(error, InternalServerError):
        return {"status": 500, "detail": error.detail}
    else:
        return {"status": 500, "detail": "An unexpected error occurred."}