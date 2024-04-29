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
import re 
router=APIRouter(tags=["Location"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.get("/get/Country/List")
def list2(token:str=Depends(oauth2_scheme)):
    new=country_state3.objects(status="Active").to_json()
    new1=json.loads(new)
    data={"Error":"False","Message":"Data found","Country_List":[]}
    for i in new1:
        a={"Country_Name":i["Capital"],"Country_Code":i["Capital_code"],"status":i["status"]}
        data["Country_List"].append(a)
#             # data.append(de)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
# @app.get("/get/Country/List")
# def list2(token:str=Depends(oauth2_scheme)):
#     # data={"Error":"False","message":"Data found","Country List":}
    
#     # r=country_state.objects(country_name="North-East District").distinct()
#     r=country_state.objects(country_status="Active").distinct(field="country_name")
#     d=country_state.objects(country_status="Active").to_json()
#     data_list=json.loads(d)
#     if data_list:
#         data={"Error":"False","Message":"Data found","Country_List":[]}
#         for i,j in zip(r,data_list):
#             de={"Country_Name":i,"Country_Code":j["country_code"],"Country_Status":j["country_status"],"id":j["id"]}
#             data["Country_List"].append(de)
#             # data.append(de)
#         return data
#     else:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a, status_code=400)
@router.get("/get/State/List")
def list1(token:str=Depends(oauth2_scheme)):
    r=country_state2.objects(status="Active").to_json()
    data_list=json.loads(r)
    data={"Error":"False","Message":"Data found","State_List":[]}
    if data_list:
        for g in data_list:
            ji={"State":g["StateName"],"Statecode":g["Statecode"],"Status":g["status"]}
            data["State_List"].append(ji)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/Create/area/names")
def areas(me:area):
    a=Areas(Location=me.Location,Pincode=me.Pincode,State=me.State,District=me.District,areacode=me.areacode)
    a.save()
    b="Successfully Updated"
    return {"Error":"False","Message":b}

@router.post("/get/area/lists")
def area_list(me:Location):
    if type(me.city) == str:
        b = me.city[:1].upper() + me.city[1:]
    d=Areas.objects.filter(Q(District=b)).to_json()
    g=json.loads(d)
    data={"Error":"False","Message":"Data found","Areas":[]}
    if g:
        for s in g:
            a={"Area":s["Location"],"areacode":s["areacode"]}
            data["Areas"].append(a)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/add/city/names")
def citys(me:city):
    s=Cityes2(sno=Cityes2.objects.count()+1,State=me.State,City=me.City,city_code=me.city_code)
    s.save()
    b="Successfully Created"
    if b:
            return {"Error":"False","Message":b}
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/get/city")
def cites(me:state):
    a=Cityes2.objects(State=me.state).to_json()
    f=json.loads(a)
    data={"Error":"False","Message":"Data found","city":[]}
    if f:
        for g in f:
            a=g["City"]
            # data["city"].append(a)
            a={"city":g["City"],"Citycode":g["city_code"]}
            data["city"].append(a)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)