from fastapi import APIRouter
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta,datetime,time
router=APIRouter(tags=["Enrol"])
@router.post("/Create/Enroll/Registration")
def enroll(me:enrol):
    
    now = datetime.now()
   
    a=Camp.objects(TransID=me.TransID,status="Start").to_json()
    b=json.loads(a)
    
    try:
        for mn in b:
            de=mn["status"]
        if de=="Start":
            if me.Patient_name!="" and me.Age!=0:
                en=Enrol(sno=Enrol.objects.count()+1,TransID=me.TransID,Patient_name=me.Patient_name,Age=int(me.Age),mobile=me.mobile,Remarks=me.Remarks,created_by=me.created_by,status="Active",created_on=now)
                en.save()
                b="Successfully Submitted"
                return {"Error":"False","Message":b}
            else:
                b="please enter patient_name and age"
                return {"Error":"False","Message":b}
        elif de=="Stop":
            # return {"Error":"True","Message":"Data not found"}
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
            
    except:ValueError
    # return {"Error":"True","Message":"Campclosed"}
    a={"Error":"True","Message":"Campclosed"}
    return JSONResponse(content=a, status_code=400)
@router.post("/get/Enroll/Registration")
def Enroll(me:enrolme):
    data={"Error":"False","Message":"Data found","Enroll":[]}
    g=Enrol.objects(TransID=me.TransID,status="Active").order_by("-sno").to_json()
    f=json.loads(g)
    if f :
        for fd in f:
            # g=fd["created_on"]
            # timestamp = g['$date']
            # date_object = datetime.fromtimestamp(timestamp/1000).date()
            # formatted_date = date_object.strftime('%Y-%b-%d')
            a2=fd["mobile"]
            g=fd["created_on"]
            timestamp = g['$date']
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            formatted_date = date_object.strftime('%d-%b-%Y')
            formatted_number = a2[:1] + "*******" + a2[-2:]
            a={"SNO":fd["sno"],"TransID":fd["TransID"],"Patientname":fd["Patient_name"],"Age":fd["Age"],"Mobile":formatted_number,"Remarks":fd["Remarks"],"created_by":fd["created_by"],"created_on":formatted_date}
            data["Enroll"].append(a)
        return data
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/search/Enroll/Registration")
def Search_enrol_data(me:search_enrol_dta):
    data={"Error":"False","Message":"Data found","Enroll":[]}
    g=Enrol.objects(sno=me.sno).to_json()
    f=json.loads(g)
    if f :
        for fd in f:
            g=fd["created_on"]
            timestamp = g['$date']
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            formatted_date = date_object.strftime('%d-%b-%Y')
            a2=fd["mobile"]
            formatted_number = a2[:1] + "*******" + a2[-2:]
            a={"SNO":fd["sno"],"TransID":fd["TransID"],"Patientname":fd["Patient_name"],"Age":fd["Age"],"Mobile":formatted_number,"Remarks":fd["Remarks"],"created_by":fd["created_by"],"created_on":formatted_date}
            data["Enroll"].append(a)
        return data
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.put("/update_enrol_registration")
def change_enrol_reg(me:update_enrol_data):
    try:
        new=Enrol.objects(sno=int(me.sno)).to_json()
        new1=json.loads(new)
        if new1:
            data=Enrol.objects(sno=int(me.sno)).update_one(set__Patient_name=me.Patient_name,set__mobile=me.mobile,set__Age=int(me.age),set__Remarks=me.Remarks)
            b="Successfully Updated"
            if b:
                    return {"Error":"False","Message":b}
            else:
                # return {"Error":"True","Message":"Data not found"}
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
        else:
            a={"Error":"True","Message":"please enter valid sno"}
            return JSONResponse(content=a, status_code=400)
    except ValueError:
         a={"Error":"True","Message":"please enter valid sno"}
         return JSONResponse(content=a, status_code=400)
@router.put("/update_enrol_registration_status")
def change_enrol_reg(me:update_enrol_status):
    try:
        new=Enrol.objects(sno=me.sno).to_json()
        new1=json.loads(new)
        if new1:
            data=Enrol.objects(sno=me.sno).update_one(set__status=me.status)
            b="Successfully Updated"
            if b:
                    return {"Error":"False","Message":b}
            else:
                # return {"Error":"True","Message":"Data not found"}
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
        else:
            a={"Error":"True","Message":"please enter valid sno"}
            return JSONResponse(content=a, status_code=400)
    except ValueError:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)
