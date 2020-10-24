from typing import List

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from forex_miner_thor.model.candle import CandleSchema
from forex_miner_thor.model.instrument import Instrument, InstrumentSchema
from forex_miner_thor.model.trade import TradeSignalSchema, TradeSignal
from forex_miner_thor.api.error import ProblemDetailsSchema, ProblemDetails
from forex_miner_thor.utilities.add_instrument_data import add_instrument_data
from forex_miner_thor.strategies import apply_strategies


# Setup flask
api = Flask(__name__)


# Default endpoint just to report back 200
@api.route('/api/v1/engine', methods=['GET'])
def report_status():
    return '', 200


# Tick route
@api.route('/api/v1/engine/tick', methods=['POST'])
def tick():
    if not request.is_json:
        return (
            ProblemDetailsSchema().dump(ProblemDetails(415, "Only 'application/json' is a supported 'Content-Type'.")),
            415
        )

    try:
        # Empty trade signals
        trade_signals: List[TradeSignal] = []

        # Process instruments and apply strategy on them
        instruments: List[Instrument] = InstrumentSchema(many=True).load(request.get_json())
        for inst in instruments:
            candles = add_instrument_data(inst.instrument, inst.granularity, inst.candles)
            trade_signal = apply_strategies(inst.instrument, candles)
            if trade_signal is not None:
                trade_signals.append(trade_signal)

        # Return trade signals
        return jsonify(TradeSignalSchema(many=True).dump(trade_signals))
    except ValidationError as vex:
        return ProblemDetailsSchema().dump(ProblemDetails(422, vex.messages)), 422
    except Exception as ex:
        return ProblemDetailsSchema().dump(ProblemDetails(500, str(ex))), 500


# Add instrument data route
@api.route('/api/v1/engine/instruments/<instrument>/granularities/<granularity>', methods=['POST'])
def post_instrument_granularity_candles(instrument: str, granularity: str):
    # Error handling on non json data
    if not request.is_json:
        return (
            ProblemDetailsSchema().dump(ProblemDetails(415, "Only 'application/json' is a supported 'Content-Type'.")),
            415
        )

    try:
        # Parse incoming candles
        candles = CandleSchema(many=True).load(request.get_json())

        # Add data to csv files
        add_instrument_data(instrument, granularity, candles)

        # Return 201
        return '', 201
    except ValidationError as vex:
        return ProblemDetailsSchema().dump(ProblemDetails(422, vex.messages)), 422
    except Exception as ex:
        return ProblemDetailsSchema().dump(ProblemDetails(500, str(ex))), 500


# Run API
api.run(host='0.0.0.0', port=31001)

