from fastapi import APIRouter
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from datetime import timedelta,datetime,time
router=APIRouter(tags=["Activity"])
@router.post("/Create/Activity/Report")
def act(me:active):
    now = datetime.now()
    k=str(now)
    alr_unit = Active11.objects(camp=me.Activity_type).first()
    if alr_unit:
        if alr_unit.status == 'Inactive':
            sno = alr_unit.sno
            alr_unit.delete()
            Active11.objects(sno__gt=sno).update(dec__sno=1)    
        else:
            data = {"Error":"True", "Message":"Unit name already exists."}
            return JSONResponse(content=data, status_code=400)
    try:
        if me.Activity_type!=""and me.created_by!="":
            data=Active11(sno=Active11.objects.count()+1,camp=me.Activity_type,status="Active",created_by=me.created_by,Modified_by=" ",Modified_on=k,created_on=now)
            data.save()
            a="Successfully Submitted"
            if a:
                    return {"Error":"False","Message":a}
            else:
                # return {"Error":"True","Message":"Data not found"}
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
        else:
            a={"Error":"True","Message":"please enter fileds"}
            return JSONResponse(content=a, status_code=400)
    except Exception:
        a={"Error":"True","Message":"please enter correct fileds"}
        return JSONResponse(content=a, status_code=400)
@router.get("/get/Activity/Report")
def Report():
    d=Active11.objects(status="Active").order_by("-sno").to_json()
    f=json.loads(d)
    data={"Error":"False","Message":"Data found","ActivityReports":[]}
    if f:
        for c in f:
            k=c["created_on"]
            timestamp = k['$date']
            date_object = datetime.fromtimestamp(timestamp/1000)
            formatted_date = date_object.strftime('%d-%b-%Y')
            re={"sno":c["sno"],"Camp":c["camp"],"Status":c["status"],"Created_on":formatted_date}
            data["ActivityReports"].append(re)
        return data
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/search/Activity/Report")
def Report(me:search_activity_report):
    d=Active11.objects(sno=int(me.sno),status="Active").to_json()
    f=json.loads(d)
    data={"Error":"False","Message":"Data found","ActivityReports":[]}
    if f:
        for c in f:
            k=c["created_on"]
            timestamp = k['$date']
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            formatted_date = date_object.strftime('%Y-%b-%d')
            re={"sno":c["sno"],"Camp":c["camp"],"Status":c["status"],"Created_on":formatted_date}
            data["ActivityReports"].append(re)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.put("/update_activity_Report_data")
def update_activity_report(me:update_activity_report):
    try:
        new=Active11.objects(sno=me.sno).to_json()
        new2=json.loads(new)
        if new2:
                a= Active11.objects(sno=me.sno).update_one(set__camp=me.Activity_type)
                a="Successfully Updated"
                if a:
                 return {"Error":"False","Message":a}
                else:    
                        a={"Error":"True","Message":"Data not found"}
                        return JSONResponse(content=a, status_code=400)
        else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    except ValueError:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)

@router.put("/delete_Activity_Report")
def get_delete_activity_report(me:delete_activity):
    try:
        a= Active11.objects(sno=me.sno).update_one(set__status=me.status)
        b="Successfully Deleted"
        if a:
            return {"Error":"False","Message":b}
        else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    except ValueError:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)