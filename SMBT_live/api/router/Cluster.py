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
router=APIRouter(tags=["Cluster"])
@router.post("/create/cluster/data")
def clusters(me:cluster):
    b = me.cluster_name[:1].upper() + me.cluster_name[1:]
    alr= Cluster1.objects(cluster_name=b).first()
    if alr:
        if alr.status == 'Inactive':
            alr.status = 'Active'
            alr.save()
        elif alr.status == "Active":
            data = {"Error":"True", "Message":"Cluster name already exists."}
            return JSONResponse(content=data, status_code=400)
    else:
        new=Cluster1(sno=Cluster1.objects.count()+1,cluster_code="CLU{:002d}".format(Cluster1.objects.count()+1),cluster_name=b,address=me.address,status="Active")
        new.save()
    b="Successfully Created"
    if b:
        return {"Error":"False","Message":b}
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.get("/get/cluster/data")
def clusters():
    clu=Cluster1.objects(status="Active").order_by("-sno").to_json()
    clus=json.loads(clu)
    data={"Error":"False","Message":"Data found","Clusters":[]}
    if clus:
        for cl in clus:
            a={"Sno":cl["sno"],"cluster_code":cl["cluster_code"],"cluster_name":cl["cluster_name"],"address":cl["address"],"status":cl["status"]}
            data["Clusters"].append(a)
        return data
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
    return JSONResponse(content=a, status_code=400)
@router.post("/search_cluster_mobile")
def search_cluster_data(me:cluster_search_mobile):
        result = Cluster1.objects(cluster_name__icontains=me.search,status="Active").to_json()
        result1=json.loads(result)
        data={"Error":"False","message":"Data found","Clusters":[]}
        for cl in result1:
            a={"Sno":cl["sno"],"cluster_code":cl["cluster_code"],"cluster_name":cl["cluster_name"],"address":cl["address"],"status":cl["status"]}
            data["Clusters"].append(a)
        return data
@router.post("/search/cluster/data")
def search_cluster_data(me:search_cluster):
    clu=Cluster1.objects(sno=me.sno,status="Active").to_json()
    clus=json.loads(clu)
    data={"Error":"False","Message":"Data found","Clusters":[]}
    if clus:
        for cl in clus:
            a={"Sno":cl["sno"],"cluster_code":cl["cluster_code"],"cluster_name":cl["cluster_name"],"address":cl["address"],"status":cl["status"]}
            data["Clusters"].append(a)
        return data
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.put("/update_cluster_data")
def update_cluster(me:update_cluster_data):
    try:
        a= Cluster1.objects(sno=me.sno).update_one(set__cluster_name=me.cluster_name,set__address=me.address)
        b="Successfully Updated"
        if b:
                return {"Error":"False","Message":b}
        else:
            # return {"Error":"True","Message":"Data not found"}
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    except:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)

@router.put("/delete_cluster_unit")
def delete_cluster(me:delete_cluster_data):
    new=Cluster1.objects(cluster_code=me.cluster_code).to_json()
    new1=json.loads(new)
    if new1:
        a= Cluster1.objects(cluster_code=me.cluster_code).update_one(set__status=me.status)
        b="Successfully Updated"
        if b:
                return {"Error":"False","Message":b}
        else:
            # return {"Error":"True","Message":"Data not found"}
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    else:
        a={"Error":"True","Message":"please enter valid code"}
        return JSONResponse(content=a, status_code=400)

@router.get("/get_cluster_counts")
def get_cluster():
     u=Cluster1.objects().count()
     v=Cluster1.objects(status="Active").count()
     w=Cluster1.objects(status="Inactive").count()
     a={"Total_clusters":u,"Active_clusters":v,"Inactive_clusters":w}
     if a:
         data1={"Error":"False","Message":"Data found","Counts":[]}
         data1["Counts"].append(a)
         return data1
     else:
        n={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=n, status_code=400)
