from flask import Flask, request, jsonify
from marshmallow import ValidationError


from forex_miner_thor.api.error import ProblemDetailsSchema, ProblemDetails
from forex_miner_thor.api.tick import TickInstrumentSchema

# Setup flask
api = Flask(__name__)


# Tick route
@api.route('/api/v1/engine/tick', methods=['POST'])
def tick():
    if not request.is_json:
        return ProblemDetailsSchema().dump(ProblemDetails(
            415, "Only 'application/json' is a supported 'Content-Type'."
        )), 415

    try:
        instruments = TickInstrumentSchema(many=True).load(request.get_json())
        return jsonify(TickInstrumentSchema(many=True).dump(instruments))
    except ValidationError as ex:
        return ProblemDetailsSchema().dump(ProblemDetails(
            422, ex.messages
        )), 422


# Run API
api.run()

