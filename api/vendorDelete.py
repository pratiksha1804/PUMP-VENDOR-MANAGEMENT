from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
@swagger.model
class vendorDeletion(Resource):
    @swagger.operation(
        description="vendor deletion",
        nickname="vendor deletion",
        parameters=[
            {
                "name": "body",
                "dataType": "string",

                "required": True,
                "allowMultiple": False,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Vendor deleted succesfully"},
            {"code": 400, "message": "Bad Request: Error on deleting vendor"}
        ],
    )
    def delete(self):
        try:
            payload = json.loads(request.data.decode())
            vendor_name=payload["vendor_name"]

            database.deleteVendor(vendor_name)
            return make_response(jsonify(
                {
                    'title': "Vendor Deleted Successfully",
                    "status": HTTPStatus.OK
                }
            ),
                HTTPStatus.OK,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from vendor deletion",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )