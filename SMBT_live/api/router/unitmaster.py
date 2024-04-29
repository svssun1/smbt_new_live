from fastapi import APIRouter,Depends
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import base64
import os
router=APIRouter(tags=["Unit Master"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.post("/ADD/USER/MASTER/NEW_UNIT")
async def new_unit(me:addunitmaster_mobile,token:str=Depends(oauth2_scheme)):
    b=me.unit_name[:1].upper()+me.unit_name[1:]
    alr_unit = Addunitmaster_mobile.objects(unit_name=b).first()
    if alr_unit:
        if alr_unit.status == 'Inactive':
            sno = alr_unit.sno
            alr_unit.delete()
            Addunitmaster_mobile.objects(sno__gt=sno).update(dec__sno=1)    
        else:
            data = {"Error":"True", "Message":"Unit name already exists."}
            return JSONResponse(content=data, status_code=400)
    img = Addunitmaster_mobile(sno=Addunitmaster_mobile.objects.count()+1,unit_name=b,cluster_name=me.cluster_name,address=me.address,status=me.status,file_name=me.file_name)
    img.save()
    b = "Successfully Submitted"
    if b:
        return {"Error":"False", "Message":b}
    else:
        a = {"Error":"True", "Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
# @router.post("/ADD/USER/MASTER/NEW_UNIT")
# async def new_unit(me:addunitmaster,token:str=Depends(oauth2_scheme)):
#     b=me.unit_name[:1].upper()+me.unit_name[1:]
#     alr_unit = Addunitmaster.objects(unit_name=b).first()
#     if alr_unit:
#         if alr_unit.status == 'Inactive':
#             sno = alr_unit.sno
#             alr_unit.delete()
#             Addunitmaster.objects(sno__gt=sno).update(dec__sno=1)    
#         else:
#             data = {"Error":"True", "Message":"Unit name already exists."}
#             return JSONResponse(content=data, status_code=400)
#     img = Addunitmaster(sno=Addunitmaster.objects.count()+1,unit_name=b,cluster_name=me.cluster_name,address=me.address,status=me.status,file_name=me.file_name)
#     img.save()
#     b = "Successfully Submitted"
#     if b:
#         return {"Error":"False", "Message":b}
#     else:
#         a = {"Error":"True", "Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)



# @router.get("/get/UnitMaster/Data")
# async def get_images(token:str=Depends(oauth2_scheme)):
#     images = Addunitmaster_mobile.objects(status="Active")
#     data1={"Error":"False","Message":"Data found","Unitmaster":[]}
#     if images:
#         for image in images:
#             sno=image.sno
#             unit_name=image.unit_name
#             unit_code=image.unit_code
#             address=image.address
#             status=image.status
#             unit_code = image.unit_code
#             cluster_name=image.cluster_name
#             FILEPATH = os.path.join("./api/static/{}_unit.jpg".format(unit_code))
#             filepath = os.path.join("./api/static/{}_unit.jpg".format(unit_code))
#             return_filepath = "http://13.127.133.6" + filepath[5:]
#             with open(FILEPATH, "wb") as f:
#                 f.write(image.file_name)
#                 k={"SNO":sno,"Unit_Code":unit_code,"Unit_Name":unit_name,"Cluster_Name":cluster_name,"Address":address,"Status":status,"Image_path":return_filepath}
#             # m={"sno":sno,"unit_name":unit_name,"unit_code":unit_code,"address":address,"status":status,"path":return_filepath}
#             data1["Unitmaster"].append(k)
#         return data1
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
@router.get("/get/UnitMaster/Data")
async def get_image(token:str=Depends(oauth2_scheme)):
    data1={"Error":"False","Message":"Data found","Unitmaster":[]}
    images=Addunitmaster_mobile.objects(status="Active")
    if images:
           for unit_pic in images:
                sno=unit_pic.sno
                unit_name=unit_pic.unit_name
                image_data=unit_pic.file_name
                unit_code=unit_pic.unit_code
                cluster_name=unit_pic.cluster_name
                address=unit_pic.address
                status=unit_pic.status
                FILEPATH="./api/static/{}_unit.jpg".format(unit_code)
                filepath="./api/static/{}_unit.jpg".format(unit_code)
                return_filepATH = "http://13.127.133.6"+filepath[5:]
                with open(FILEPATH, "wb") as f:
                    decoded_image = base64.b64decode(image_data)
                    f.write(decoded_image)
                    k={"SNO":sno,"Unit_Code":unit_code,"Unit_Name":unit_name,"Cluster_Name":cluster_name,"Address":address,"Status":status,"Image_path":return_filepATH}
                    data1["Unitmaster"].append(k)
           return data1
                
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
# import base64
# from fastapi import FastAPI, Depends

# app = FastAPI()

# class ImageCache:
#     def __init__(self):
#         self.cache = {}

# image_cache = ImageCache()

# class UnitMaster:
#     def __init__(self, sno, unit_code, unit_name, cluster_name, address, status, image_path):
#         self.sno = sno
#         self.unit_code = unit_code
#         self.unit_name = unit_name
#         self.cluster_name = cluster_name
#         self.address = address
#         self.status = status
#         self.image_path = image_path

# def decode_image(image_data, file_path):
#     with open(file_path, "wb") as f:
#         decoded_image = base64.b64decode(image_data)
#         f.write(decoded_image)

# @router.get("/get/UnitMaster/Data")
# async def get_image():
#     data1 = {"Error": "False", "Message": "Data found", "Unitmaster": []}
#     images = Addunitmaster_mobile.objects(status="Active")  # Assuming Addunitmaster_mobile is your model
#     if images:
#         for unit_pic in images:
#             sno = unit_pic.sno
#             unit_name = unit_pic.unit_name
#             image_data = unit_pic.file_name
#             unit_code = unit_pic.unit_code
#             cluster_name = unit_pic.cluster_name
#             address = unit_pic.address
#             status = unit_pic.status
#             file_path = "./api/static/{}_unit.jpg".format(unit_code)
#             return_file_path = "http://13.127.133.6" + file_path[5:]

#             if unit_code in image_cache.cache:
#                 # Use cached image path
#                 cached_image_path = image_cache.cache[unit_code]
#                 k = UnitMaster(sno, unit_code, unit_name, cluster_name, address, status, cached_image_path)
#             else:
#                 # Cache the image path and write the image to the disk
#                 decode_image(image_data, file_path)
#                 image_cache.cache[unit_code] = return_file_path
#                 k = UnitMaster(sno, unit_code, unit_name, cluster_name, address, status, return_file_path)
#             data1["Unitmaster"].append(k.__dict__)

#     return data1


@router.post("/search/UnitMaster/Data")
def search_data(me:search_unit):
    # a=Addunitmaster.objects(unit_name=me.unit_name,status="Active").to_json() 
    data1={"Error":"False","Message":"Data found","Unitmaster":[]}
    images=Addunitmaster_mobile.objects(unit_name=me.unit_name,status="Active")
    if images:
           for unit_pic in images:
                sno=unit_pic.sno
                unit_name=unit_pic.unit_name
                image_data=unit_pic.file_name
                unit_code=unit_pic.unit_code
                cluster_name=unit_pic.cluster_name
                address=unit_pic.address
                status=unit_pic.status
                FILEPATH="./api/static/{}_unit.jpg".format(unit_code)
                filepath="./api/static/{}_unit.jpg".format(unit_code)
                return_filepATH = "http://13.127.133.6"+filepath[5:]
                print(return_filepATH)
                with open(FILEPATH, "wb") as f:
                    decoded_image = base64.b64decode(image_data)
                    f.write(decoded_image)
                    k={"SNO":sno,"Unit_Code":unit_code,"Unit_Name":unit_name,"Cluster_Name":cluster_name,"Address":address,"Status":status,"Image_path":return_filepATH}
                    data1["Unitmaster"].append(k)
           return data1
                
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
            
@router.get("/get/Unitmaster/Counts")
def counts(token:str=Depends(oauth2_scheme)):
     u=Addunitmaster_mobile.objects().count()
     v=Addunitmaster_mobile.objects(status="Active").count()
     w=Addunitmaster_mobile.objects(status="Inactive").count()
     a={"Total_Units":u,"Active_Units":v,"Inactive_Units":w}
     if a:
         data1={"Error":"False","Message":"Data found","Counts":[]}
         data1["Counts"].append(a)
         return data1
     else:
        n={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=n, status_code=400)

@router.put("/Update_unitmaster_data")
def update_image(me:update_unitmaster):
    b=me.unit_name[:1].upper()+me.unit_name[1:]
    new=Addunitmaster_mobile.objects(unit_name=me.unit_name).to_json()
    new1=json.loads(new)
    
    if new1:
        if me.file_name not in ["", "string"]:
            a= Addunitmaster_mobile.objects(unit_name=me.unit_name).update_one(set__unit_name=b,set__cluster_name=me.cluster_name,set__address=me.address,set__file_name=me.file_name)
        elif me.file_name == "":
            a= Addunitmaster_mobile.objects(unit_name=me.unit_name).update_one(set__unit_name=b,set__cluster_name=me.cluster_name,set__address=me.address)
        elif me.file_name=="string":
            a= Addunitmaster_mobile.objects(unit_name=me.unit_name).update_one(set__unit_name=b,set__cluster_name=me.cluster_name,set__address=me.address)

        b="Successfully Updated"
        if b:
                return {"Error":"False","Message":b}
        else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    else:
            a={"Error":"True","Message":"please enter valid unit_name"}
            return JSONResponse(content=a, status_code=400)
@router.put("/Delete_unitmaster_data")
def get_delete_data(me:delete_unitmaster):
    new=Addunitmaster_mobile.objects(unit_name=me.unit_name).to_json()
    new1=json.loads(new)
    if new1:
        a= Addunitmaster_mobile.objects(unit_name=me.unit_name).update_one(set__status=me.status)
        b="Successfully Updated"
        if b:
                return {"Error":"False","Message":b}
        else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    else:
         a={"Error":"True","Message":"please enter valid unit_name"}
         return JSONResponse(content=a, status_code=400)