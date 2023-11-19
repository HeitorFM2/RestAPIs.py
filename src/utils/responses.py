from datetime import datetime
from flask import make_response, jsonify

"""
    This class is used to create a standard response for the API.
"""


class Response:
    def Ok(data, message="Successfuly request!"):
        return make_response(
            jsonify(
                code=200,
                success=True,
                timestamp=datetime.now(),
                message=message,
                data=data,
            ),
            200,
        )

    def Created(data, message="Successfuly created!"):
        return make_response(
            jsonify(
                code=201,
                success=True,
                timestamp=datetime.now(),
                message=message,
                data=data,
            ),
            201,
        )

    def Error(message="Internal Server Error"):
        return make_response(
            jsonify(
                code=500,
                success=False,
                timestamp=datetime.now(),
                message=message,
            ),
            500,
        )

    def BadRequest(message="Bad Request"):
        return make_response(
            jsonify(
                code=400,
                success=False,
                timestamp=datetime.now(),
                message=message,
            ),
            400,
        )

    def NotFound(message="Not Found"):
        return make_response(
            jsonify(
                code=404,
                success=False,
                timestamp=datetime.now(),
                message=message,
            ),
            404,
        )
