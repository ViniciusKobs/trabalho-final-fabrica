from flask import jsonify

from ..exceptions.public_exception import PublicException
from ..http.request import Request

def dispatch(controller):
    try:
        response = controller(Request())
        return jsonify(response.body), response.status
    except PublicException as e:
        return jsonify({ "error": str(e) }), e.code
    except Exception as e:
        return jsonify({ "error": str(e) }), 500
        # return jsonify({ "error": "error.internal.unknown" }), 500
