from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
@swagger.model
class vendorUpdate(Resource):
    @swagger.operation(
        description="vendor update",
        nickname="vendor update",
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
            {"code": 200, "message": "Vendor updated succesfully"},
            {"code": 400, "message": "Bad Request: Error on updating vendor"}
        ],
    )
    def put(self):
        try:
            payload = json.loads(request.data.decode())
            vendor_name = payload["vendor_name"]
	    vendor_initial = payload["vendor_initial"]
            vendor_gmail = payload["vendor_gmail"]
            vendor_phone = payload["vendor_phone"]
            vendor_location = payload["vendor_location"]
            vendor_gst = payload["vendor_gst"]
            vendor_photo_url = payload["vendor_photo_url"]

            database.updateVendor(vendor_name,vendor_initial,vendor_gmail,vendor_phone,vendor_location,vendor_gst,vendor_photo_url)
            return make_response(jsonify(
                {
                    'title': "Vendor updated Successfully",
                    "status": HTTPStatus.OK
                }
            ),
                HTTPStatus.OK,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from vendor updation",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )
