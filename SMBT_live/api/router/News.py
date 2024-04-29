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
import pytz
import io
import webbrowser
router=APIRouter(tags=["News"])
@router.post("/News/upload")
def add_news(me:news):
    # in_tz = pytz.timezone('Asia/Kolkata')
    # in_time = datetime.now(in_tz)
    # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
    now = datetime.now()
    k=str(now)
    now1= datetime.now().date()
    dum=str(now1)
    if me.title!="" and me.message!="":
        mat=News(sno=News.objects.count()+1,news_id="NEW{:002d}".format(Greet.objects.count()+1),title=me.title,message=me.message,Attachment=me.Attachment,share=me.share,status="Active",created_by=me.created_by,created_on=now,modified_by="head",modified_on=k)
        f=mat.Attachment_name="attach"+str(mat.sno)+str(dum)
        mat.save()
        a={"Error":"False","Message":"Successfully Submitted"}
        if a:
            return JSONResponse(content=a, status_code=200)
        else:
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
    else:
        a={"Error":"True","Message":"please enter details"}
        return JSONResponse(content=a, status_code=400)
@router.get("/get/new/data")
def get_news():
    ff=News.objects(status="Active").order_by("-sno").to_json()
    f1=json.loads(ff)
    data1={"Error":"False","Message":"Data found","news":[]}
    if f1:
        for d in f1:
            m=d["created_on"]
            f1=d["news_id"]
            timestamp = m['$date']
            f=d["Attachment"]
            a2=str.encode(f)
            FILEPATH="./api/static/{}_news.jpg".format(f1)
            filepath="./api/static/{}_news.jpg".format(f1)
            return_filepATH = "http://13.127.133.6"+filepath[5:]
            with open(FILEPATH,"wb") as fh:
                fh.write(base64.decodebytes(a2))
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            d1={"Sno":d["sno"],"News_id":d["news_id"],"Title":d["title"],"Message":d["message"],"Attach_name":d["Attachment_name"],"Share":d["share"],"Status":d["status"],"Created_by":d["created_by"],"Created_on":date_object,"Image_path":return_filepATH}
            data1["news"].append(d1)
        return data1
    else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
@router.post("/search/get/news/data")
def search_get_news(me:search_news_data):
    ff=News.objects(news_id=me.News_id,status="Active").order_by("-sno").to_json()
    f1=json.loads(ff)
    data1={"Error":"False","Message":"Data found","news":[]}
    if f1:
        for d in f1:
            m=d["created_on"]
            f1=d["news_id"]
            timestamp = m['$date']
            f=d["Attachment"]
            a2=str.encode(f)
            FILEPATH="./api/static/{}_news.jpg".format(f1)
            filepath="./api/static/{}_news.jpg".format(f1)
            return_filepATH = "http://13.127.133.6"+filepath[5:]
            with open(FILEPATH,"wb") as fh:
                fh.write(base64.decodebytes(a2))
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            d1={"Sno":d["sno"],"News_id":d["news_id"],"Title":d["title"],"Message":d["message"],"Attach_name":d["Attachment_name"],"Share":d["share"],"Status":d["status"],"Created_by":d["created_by"],"Created_on":date_object,"Image_path":return_filepATH}
            data1["news"].append(d1)
        return data1
    else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
@router.put("/update/news/status")
def update(me:newupd):
    try:      
        new=News.objects(sno=int(me.sno)).to_json()
        new1=json.loads(new)
        if new1:
            b1= me.status[:1].upper() + me.status[1:]
            a= News.objects(sno=int(me.sno)).update_one(set__status=b1)
            b="Successfully Updated"
            if b:
                    return {"Error":"False","Message":b}
            else:
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
    except:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)
@router.put("/update_news_details")
def update(me:update_news):
    try:
        new=News.objects(sno=me.sno).to_json()
        new1=json.loads(new)
        if new1:
            if me.image not in ["", "string"]:
                a= News.objects(sno=me.sno).update_one(set__title=me.title,set__message=me.message,set__share=me.share,set__Attachment=me.Attachment)
            elif me.Attachment=="":
                a= News.objects(sno=me.sno).update_one(set__title=me.title,set__message=me.message,set__share=me.share)
            elif me.Attachment=="string":
                a= News.objects(sno=me.sno).update_one(set__title=me.title,set__message=me.message,set__share=me.share)
            b="Successfully Updated"
            if b:
                    return {"Error":"False","Message":b}
            else:
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
    except:
         a={"Error":"True","Message":"please enter valid sno"}
         return JSONResponse(content=a, status_code=400)
