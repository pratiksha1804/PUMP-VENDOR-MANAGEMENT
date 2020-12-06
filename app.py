import os
from config import app
from api import api
from api.vendorCreate import vendorCreation
from api.vendorDelete import vendorDeletion
from api.vendorList import vendorList
from api.updateVendor import vendorUpdate

api.add_resource(vendorCreation,"/api/vendorCreate")
api.add_resource(vendorDeletion,"/api/vendorDelete")
api.add_resource(vendorList,"/api/get_all_vendors")
api.add_resource(vendorUpdate,"/api/update_vendor")

if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5002, debug=True)