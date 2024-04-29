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
router=APIRouter(tags=["Patient"])
@router.post("/create/refer/patient")
def refer(me:referpatient):
    # in_tz = pytz.timezone('Asia/Kolkata')
    # in_time = datetime.now(in_tz)
    # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
    try:
        id=int(me.emp_id)
    except ValueError:
        a={"Error":"True","Message":"Please Check Employe_id"}
        return JSONResponse(content=a, status_code=400)

    uc_id=me.Ucid
    now = datetime.now().date()
    k=str(now)
    user=Usercreate.objects(Employee_id=id).to_json()
    master=AddMaster1.objects(Ucid_id=uc_id).to_json()
    ma1=json.loads(master)
    user1=json.loads(user)
    if user1 and ma1:
        for u,v in zip(user1,ma1):
            d=u["User_name"]
            f1=u["mobile_number"]
            f2=u["Branch"]
            e=v["Agent_name"]
            f=v["mobile"]
            new=Referpatient(sno=Referpatient.objects.count()+1,patient_name=me.patient_name,patient_mobile=me.patient_mobile,executive_name=d,Ucid=me.Ucid,Ucid_name=e,conslutant=me.conslutant,speciality=me.speciality,remarks=me.remarks,Ipno="none",mapped_by="none",mapped_on="none",status="Pending",created_by=me.created_by,branch=f2,agent_mobile=f,executive_mobile=f1,created_on=now)
            new.save()
        a={"Error":"False","Message":"Successfully Submitted"}
        return JSONResponse(content=a, status_code=200)
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Please Check Entered Ucid"}
        return JSONResponse(content=a, status_code=400)
@router.post("/get/the/refer/patient/data")
def get_refer(me:reget):
    da = me.from_date
    da1 = me.to_date
    date_formats = ["%Y-%m-%d","%Y/%m/%d","%d/%m/%Y","%d-%m-%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]
    valid_date = None

    for format in date_formats:
        try:
            from_date = datetime.strptime(da, format)
            to_date = datetime.strptime(da1, format)
            valid_date = format
            break
        except ValueError:
            pass

    if valid_date:
        if from_date != to_date:
            f = Referpatient.objects(Q(created_on__gte=from_date) & Q(created_on__lte=to_date) & Q(created_by=str(me.emp_id)) & Q(status="Pending")).order_by("-sno").to_json()
            g = json.loads(f)
        else:
            dto22 = to_date + timedelta(days=1)
            f = Referpatient.objects(Q(created_on__gte=from_date) & Q(created_on__lt=dto22) & Q(status="Pending") & Q(created_by=str(me.emp_id))).order_by("-sno").to_json()
            g = json.loads(f)
        if g:
            data1={"Error":"False","Message":"Data found","patient":[[{"sno":ff["sno"],"patient_name":ff["patient_name"],"patient_mobile":ff["patient_mobile"],"executive_name":ff["executive_name"],"Agent_name":ff["Ucid_name"],"Ucid":ff["Ucid"],"conslutant":ff["conslutant"],"speciality":ff["speciality"],"remarks":ff["remarks"],"emp_id":ff["created_by"],"branch":ff["branch"],"executive_mobile":str(ff["executive_mobile"]),"agent_mobile":ff["agent_mobile"],"Ipno":ff["Ipno"],"mapped_by":ff["mapped_by"],"mapped_on":ff["mapped_on"],"created_by":ff["created_by"],"created_on":datetime.fromtimestamp(ff["created_on"]["$date"]//1000).strftime('%d-%b-%Y'),"status":ff["status"]} for ff in g]]}
            return data1
        else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    else:
        a={"Error":"True","Message":"Invalid date format"}
        return JSONResponse(content=a, status_code=400)
   
@router.post("/search/the/refer/patient/data")
def get_refer(me:search_refer_patient):
    f=Referpatient.objects(sno=me.sno).to_json()
    g=json.loads(f)
    data1={"Error":"False","Message":"Data found","patient":[]}
    if g:
        for ff in g:
            g=ff["created_on"]
            timestamp = g['$date']
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            formatted_date = date_object.strftime('%d-%b-%Y')
            a={"sno":ff["sno"],"patient_name":ff["patient_name"],"patient_mobile":ff["patient_mobile"],"executive_name":ff["executive_name"],"Agent_name":ff["Ucid_name"],"Ucid":ff["Ucid"],"conslutant":ff["conslutant"],"speciality":ff["speciality"],"remarks":ff["remarks"],"emp_id":ff["created_by"],"branch":ff["branch"],"executive_mobile":str(ff["executive_mobile"]),"agent_mobile":ff["agent_mobile"],"Ipno":ff["Ipno"],"mapped_by":ff["mapped_by"],"mapped_on":ff["mapped_on"],"created_by":ff["created_by"],"created_on":formatted_date,"status":ff["status"]}
            data1["patient"].append(a)
        return data1
    else:
     a={"Error":"True","Message":"Data not found"}
    return JSONResponse(content=a, status_code=400)
@router.post("/search_patient_data_mobile")
def search_patient_data(me:search_patient):
    result = Referpatient.objects(Q(patient_name__icontains=me.search) | Q(patient_mobile__icontains=me.search) | Q(Ucid__icontains=me.search),created_by=me.created_by).order_by("-sno").to_json()
    result1=json.loads(result)
    data1={"Error":"False","Message":"Data found","patient":[]}
    if result1:
        for ff in result1:
            g=ff["created_on"]
            timestamp = g['$date']
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            formatted_date = date_object.strftime('%d-%b-%Y')
            a={"sno":ff["sno"],"patient_name":ff["patient_name"],"patient_mobile":str(ff["patient_mobile"]),"executive_name":ff["executive_name"],"Agent_name":ff["Ucid_name"],"Ucid":ff["Ucid"],"conslutant":ff["conslutant"],"speciality":ff["speciality"],"remarks":ff["remarks"],"branch":ff["branch"],"executive_mobile":str(ff["executive_mobile"]),"agent_mobile":ff["agent_mobile"],"Ipno":ff["Ipno"],"mapped_by":ff["mapped_by"],"mapped_on":ff["mapped_on"],"created_by":ff["created_by"],"created_on":formatted_date,"status":ff["status"]}
            data1["patient"].append(a)
        return data1
    
    else:
             
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)

@router.put("/update_patient/data")
def update_patient_data1(me:update_patient_data):
        try:
        # Update the Referpatient object with the given sno
            a = Referpatient.objects(sno=int(me.sno)).update_one(
                set__patient_name=me.patient_name,
                set__patient_mobile=me.patient_mobile,
                set__conslutant=me.conslutant,
                set__speciality=me.speciality,
                set__remarks=me.remarks
            )
        # Check if the object was updated
            if a:
                return {"Error": "False", "Message": "Successfully Updated"}
            else:
                return {"Error": "True", "Message": "Data not found"}
        except Exception as e:
        # Handle all possible exceptions in one block
            a = {"Error": "True", "Message": str(e)}
            return JSONResponse(content=a, status_code=400)

    # try:
    #     new=Referpatient.objects(sno=int(me.sno)).to_json()
    #     new1=json.loads(new)
    #     if new1:
    #         a= Referpatient.objects(sno=int(me.sno)).update_one(set__patient_name=me.patient_name,set__patient_mobile=me.patient_mobile,set__conslutant=me.conslutant,set__speciality=me.speciality,set__remarks=me.remarks)
    #         b="Successfully Updated"
    #         if b:
    #                 return {"Error":"False","Message":b}
    #         else:
    #             # return {"Error":"True","Message":"Data nt found"}
    #             a={"Error":"True","Message":"Data not found"}
    #             return JSONResponse(content=a, status_code=400)
    #     else:
    #         a={"Error":"True","Message":"please enter valid sno"}
    #         return JSONResponse(content=a, status_code=400)
    # except ValueError:
    #     a={"Error":"True","Message":"please enter valid sno"}
    #     return JSONResponse(content=a, status_code=400)
@router.put("/update_patient_status")
def update_patient_data(me:update_refer_patient_status):
    try:
        new=Referpatient.objects(sno=me.sno).to_json()
        new1=json.loads(new)
        if new1:
            a= Referpatient.objects(sno=me.sno).update_one(set__status=me.status)
            b="Successfully Updated"
            if b:
                    return {"Error":"False","Message":b}
            else:
                # return {"Error":"True","Message":"Data nt found"}
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
        else:
            a={"Error":"True","Message":"please enter valid sno"}
            return JSONResponse(content=a, status_code=400)
    except ValueError:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)

@router.get("/get/department")
def consul():
   data1={"Error":"False","Message":"Data found","Department":[]}
   consultants = Consultant.objects().distinct('department')
   unique_consultants = list(set(consultants))
   if unique_consultants:
        for i in unique_consultants:
            d={"department":i}
            data1["Department"].append(d)
        return data1
   else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/ADD/consultant/")
def consul(me:consultant):
    b=me.consultant[0].upper()+me.consultant[1:]
    c=me.department[0].upper()+me.department[1:]
    new=Consultant(sno=Consultant.objects.count()+1,consultant=b,department=c)
    new.save()
    a={"Error":"False","Message":"Successfully Submitted"}
    if a:
        return JSONResponse(content=a, status_code=200)
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/get/consultant")
def consul(me:department):
    a=Consultant.objects(department=me.department_name).to_json()
    b=json.loads(a)
    data1={"Error":"False","Message":"Data found","Consultant":[]}
    if b:
        for ff in b:
            a1={"consultant":ff["consultant"]}
            data1["Consultant"].append(a1)
        return data1
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
