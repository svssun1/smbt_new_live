from fastapi import APIRouter,FastAPI,Depends,File,UploadFile,Form,Request,Query,status,Response
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from passlib.context import CryptContext
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
router=APIRouter(tags=["Location_Update_mobile"])
@router.put("/location-update-api")
def loc(me:Cordi):
    try:
        coordinates = me.coordinates
        add=[]
        latitude,longitude = map(float, coordinates.split(","))
        Lattitide=str(latitude)
        Logitude=str(longitude)
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(Lattitide+","+Logitude)
        address = location.raw['address']
        g=address["state_district"]
        add.append(g)
        f=address["city"]
        add.append(f)
        h=address["state"]
        add.append(h)
        i=address["postcode"]
        add.append(i)
        i=address["country"]
        add.append(i)
        # da=str(address)
        # print(type(address))
        a= Usercreate.objects(Employee_id=int(me.emp_id)).update_one(set__Location=str(coordinates),set__Location_address=str(add))
        b="Successfully Updated"
        if b:
                return {"Error":"False","Message":b}
        else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    except:
         a={"Error":"True","Message":"please enter valid emp_id and coordinates"}
         return JSONResponse(content=a, status_code=400)
