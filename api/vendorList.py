from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import constant
import json
@swagger.model
class vendorList(Resource):
    @swagger.operation(
        description="vendor list",
        nickname="vendor list",
        parameters=[
            {
                "name": "vendor_name",
                "dataType": "String",
                "description": "vendor details",
                "required": False,
                "allowMultiple": False,
                "paramType": "query"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Vendors fetched successfully"},
            {"code": 400, "message": "Bad Request: Error on fetching vendor list"}
        ],
    )
    def get(self):
        try:
            vendor_name = request.args.get(constant.VENDOR_NAME)
            if vendor_name:
                vendors=database.getParticularVendor(vendor_name)
            else:
                vendors=database.getVendors()
            return make_response(jsonify(
                {
                    "title": "Vendors Details Fetched Successfully",
                    "status": HTTPStatus.OK,
                    "data": vendors,
                }
            ),
                HTTPStatus.OK
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from fetching vendors",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )