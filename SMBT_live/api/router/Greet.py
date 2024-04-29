from fastapi import APIRouter
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta,datetime,time
from jose import jwt
from geopy.geocoders import Nominatim
from fastapi.staticfiles import StaticFiles
import base64
from pathlib import Path
from fastapi.responses import FileResponse
from typing import Dict
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import pytz
import io
import webbrowser
router=APIRouter(tags=["Greetings"])
@router.post("/creating/personlized/greetings")
def gree(me:greet):
    # in_tz = pytz.timezone('Asia/Kolkata')
    # in_time = datetime.now(in_tz)
    # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
    now = datetime.now()
    k=str(now)
    now1= datetime.now().date()
    dum=str(now1)
    type1=me.catagory
    cat=type1[:1].upper()+type1[1:]
    if cat=="Video":
        if all([me.image,me.target_link]):
            d=Greet(sno=Greet.objects.count()+1,Greet_id="GRT{:002d}".format(Greet.objects.count()+1),title=me.title,message=me.message,catagory=me.catagory,image=me.image,target_link=me.target_link,share=me.share,employe_name=me.employe_name,desigation=me.desigation,status="Active",created_by=me.created_by,created_on=now,modified_by="head",modified_on=k)
            f=d.image_name="image"+str(d.sno)+str(dum)
            d.save()
            a={"Error":"False","Message":"Successfully Submitted"}
            if a:
             return JSONResponse(content=a, status_code=200)
        else:
            a={"Error":"True","Message":"please import image and video link"}
            return JSONResponse(content=a, status_code=400)
    elif cat=="Image":
        if all([me.image]):
                d=Greet(sno=Greet.objects.count()+1,Greet_id="GRT{:002d}".format(Greet.objects.count()+1),title=me.title,message=me.message,catagory=me.catagory,image=me.image,target_link=me.target_link,share=me.share,employe_name=me.employe_name,desigation=me.desigation,status="Active",created_by=me.created_by,created_on=now,modified_by="head",modified_on=k)
                f=d.image_name="image"+str(d.sno)+str(dum)
                d.save()
                a={"Error":"False","Message":"Successfully Submitted"}
                if a:
                    return JSONResponse(content=a, status_code=200)
        else :
                a={"Error":"True","Message":"please upload image"}
                return JSONResponse(content=a, status_code=400)
    else:
        a={"Error":"True","Message":"Please enter category"}
        return JSONResponse(content=a, status_code=400)

# def save_image_from_base64(file_path, image_data):
#     with open(file_path, "wb") as f:
#         decoded_image = base64.b64decode(image_data)
#         f.write(decoded_image)

@router.get("/get/personlized/greetings/data")
def greets():
    d=Greet.objects(status='Active').order_by("-sno").to_json()
    dd=json.loads(d)

    data1={"Error":"False","Message":"Data found","Greet":[]}
    if dd:
        
        for g in dd:
            m=g["created_on"]
            f1=g["Greet_id"]
            timestamp = m['$date']
            f=g["image"]
            a2=str.encode(f)
            FILEPATH="./api/static/{}_greet.jpg".format(f1)
            filepath="./api/static/{}_greet.jpg".format(f1)
            return_filepATH = "http://13.127.133.6"+filepath[5:]
            # save_image_from_base64(FILEPATH, a2)
            with open(FILEPATH,"wb") as fh:
                fh.write(base64.decodebytes(a2))
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            a={"SNO":g["sno"],"Greet_id":g["Greet_id"],"Title":g["title"],"Message":g["message"],"Image_name":g["image_name"],"Target_link":g["target_link"],"Catagory":g["catagory"],"Status":g["status"],"Created_by":g["created_by"],"Created_on":date_object,"Share":g["share"],"Employe_name":g["employe_name"],"Desigation":g["desigation"],"Image_path":return_filepATH}
            data1["Greet"].append(a)
        return data1
    else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
@router.post("/search/get/personlized/greetings/data")
def search_greet(me:search_greet_id):
    d=Greet.objects(Greet_id=me.Greet_id,status='Active').order_by("-sno").to_json()
    # return json.loads(d)
    dd=json.loads(d)
    data1={"Error":"False","Message":"Data found","Greet":[]}
    if dd:
        for g in dd:
            m=g["created_on"]
            f1=g["Greet_id"]
            timestamp = m['$date']
            f=g["image"]
            a2=str.encode(f)
            FILEPATH="./api/static/{}_greet.jpg".format(f1)
            filepath="./api/static/{}_greet.jpg".format(f1)
            return_filepATH = "http://13.127.133.6"+filepath[5:]
            with open(FILEPATH,"wb") as fh:
                fh.write(base64.decodebytes(a2))
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            a={"SNO":g["sno"],"Greet_id":g["Greet_id"],"Title":g["title"],"Message":g["message"],"Image_name":g["image_name"],"Target_link":g["target_link"],"Catagory":g["catagory"],"Status":g["status"],"Created_by":g["created_by"],"Created_on":date_object,"Share":g["share"],"Employe_name":g["employe_name"],"Desigation":g["desigation"],"Image_path":return_filepATH}
            data1["Greet"].append(a)
        return data1
    else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
@router.put("/update_greeting_data")
def update_greet_data(me:update_greet):
    new=Greet.objects(Greet_id=me.Greet_id).to_json()
    new1=json.loads(new)
    if new1:
        if me.image not in ["", "string"]:
            data=Greet.objects(Greet_id=me.Greet_id).update_one(set__title=me.title,set__message=me.message,set__employe_name=me.employe_name,set__desigation=me.desigation,set__image=me.image)
        elif me.image=="":
            data=Greet.objects(Greet_id=me.Greet_id).update_one(set__title=me.title,set__message=me.message,set__employe_name=me.employe_name,set__desigation=me.desigation)
        elif me.image=="string":
            data=Greet.objects(Greet_id=me.Greet_id).update_one(set__title=me.title,set__message=me.message,set__employe_name=me.employe_name,set__desigation=me.desigation)

        a={"Error":"False","Message":"Successfully Updated"}
        return JSONResponse(content=a, status_code=200)

    else:
        a={"Error":"True","Message":"please enter valid Greet_id"}
        return JSONResponse(content=a, status_code=400)

@router.put("/update/creating/personlized/status")
def update(me:upgre):
    try:
        new=Greet.objects(sno=int(me.sno)).to_json()
        new1=json.loads(new)
        if new1:
            b1= me.status[:1].upper() + me.status[1:]
            a= Greet.objects(sno=int(me.sno)).update_one(set__status=b1)
            b="Successfully Updated"
            if b:
                    return {"Error":"False","Message":b}
            else:
                # return {"Error":"True","Message":"Data not found"}
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
    except ValueError:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)