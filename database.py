from config import app
from config import mongo

def addVendor(vendor_name,vendor_initial,vendor_gmail,vendor_phone,vendor_location,vendor_gst,vendor_photo_url):
    comp_info={
     "company_name":vendor_name,
     "company_initial":vendor_initial,
     "company_gmail":vendor_gmail,
     "company_contact":vendor_phone,
     "company_location":vendor_location,
     "company_gst":vendor_gst,
     "company_photo":vendor_photo_url
    }
    return mongo.db.PUMP_VENDOR_INVENTORY.insert_one(comp_info)

def deleteVendor(vendor_name):
    comp_info={
        "company_name":vendor_name
    }
    return mongo.db.PUMP_VENDOR_INVENTORY.delete_one(comp_info)

def getVendors():
    vendors = mongo.db.PUMP_VENDOR_INVENTORY.find({}, {'_id': False})
    vendor_list = []
    if vendors:
        for vendor in vendors:
            vendor_list.append(vendor)
        return vendor_list
    return None

def getParticularVendor(vendor_name):
    vendors = mongo.db.PUMP_VENDOR_INVENTORY.find_one({"company_name":vendor_name}, {'_id': False})
    if vendors:
        return vendors
    return None

def updateVendor(vendor_name,updated_initial,updated_gmail,updated_phone,updated_location,updated_gst,updated_photo_url):
        my_query = {"company_name": vendor_name}
        new_values = {"$set": {"company_gmail":updated_gmail,"company_initial":updated_initial,"company_phone":updated_phone,"company_location":updated_location
                               ,"company_gst":updated_gst,"company_photo":updated_photo_url}}
        return mongo.db.PUMP_VENDOR_INVENTORY.update(my_query, new_values)
