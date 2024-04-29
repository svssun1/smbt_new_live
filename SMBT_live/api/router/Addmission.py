from fastapi import APIRouter
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta,datetime,time

router=APIRouter(tags=["Addimission"])
@router.post("/ADD/Addmission/Target")
def addmission(me:add_adimision_data):
    # in_tz = pytz.timezone('Asia/Kolkata')
    # in_time = datetime.now(in_tz)
    # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
    b=me.unit_name[:1].upper()+me.unit_name[1:]
    now = datetime.now()
    now1= datetime.now().date()
    k=str(now)
    ff=me.Date
    for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
        try:
            date_obj = datetime.strptime(ff, format)
            month_year_str = date_obj.strftime('%Y-%m-%d')
            khh=str(month_year_str)
            f=AddAD.objects(status="Active",Date=khh,unit_name=b).order_by("-sno").to_json()
            h=json.loads(f)
            if h:
                a={"Error":"True","Message":"Addmission Is Already Exist For This Day And Branch"}
                return JSONResponse(content=a, status_code=400)
            else:
                    if me.unit_name!=""and me.Date!="":
                        data=AddAD(sno=AddAD.objects.count()+1,unicode="UN{:002d}".format(AddAD.objects.count()+1),unit_name=b,Date=khh,target=int(me.target),created_by=me.created_by,modified_by="None",modified_on=k,status="Active",created_on=now1)
                        data.save()
                        b="Successfully Submitted"
                        if b:
                                return {"Error":"False","Message":b}
                        else:
                            # return {"Error":"True","Message":"Data not found"}
                            a={"Error":"True","Message":"Data not found"}
                            return JSONResponse(content=a, status_code=400)
                    else:
                        a={"Error":"True","Message":"please enter unit_name and Date"}
                        return JSONResponse(content=a, status_code=400)
        except ValueError:
            pass
@router.get("/get/Addmission/Target")
def get_adimission():
    f=AddAD.objects(status="Active").order_by("-sno").to_json()
    h=json.loads(f)
    data={"Error":"False","Message":"Data found","AddmissionTarget":[]}
    if h:
        for g in h:
            date=g["Date"]
            for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
                try:
                    dto=datetime.strptime(date, format).date()
                except ValueError:
                    pass
            ds=dto.strftime("%d-%b-%Y")
            b={"SNO":g["sno"],"UnitName":g["unit_name"],"Date":ds,"Target":str(g["target"]),"status":g["status"]}
            data["AddmissionTarget"].append(b)
        return data
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/search_admission_mobile")
def revenue_terget_search(me:search_adimission):
        result = AddAD.objects(unit_name__icontains=me.search,status="Active",created_by=me.created_by).order_by("-sno").to_json()
        result1=json.loads(result)
        data={"Error":"False","message":"Data found","AddmissionTarget":[]}
        if result1:
            for g in result1:
                date=g["Date"]
                for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
                    try:
                        dto=datetime.strptime(date, format).date()
                    except ValueError:
                        pass
                ds=dto.strftime("%d-%b-%Y")
                b={"SNO":g["sno"],"UnitName":g["unit_name"],"Date":ds,"Target":str(g["target"]),"status":g["status"]}
                data["AddmissionTarget"].append(b)
            return data
        else:
            # return {"Error":"True","Message":"Data not found"}
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
@router.post("/search/Addmission/Target/data")
def get_adimission_data(me:search_adimission_data):
    f=AddAD.objects(sno=me.sno,status="Active").to_json()
    h=json.loads(f)
    data={"Error":"False","Message":"Data found","AddmissionTarget":[]}
    if h:
        for g in h:
           for g in h:
            date=g["Date"]
            for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
                try:
                    dto=datetime.strptime(date, format).date()
                except ValueError:
                    pass
            ds=dto.strftime("%d-%b-%Y")
            b={"SNO":g["sno"],"UnitName":g["unit_name"],"Date":ds,"Target":str(g["target"]),"status":g["status"]}
            data["AddmissionTarget"].append(b)
        return data
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.put("/change/Addmission/target")
def update(me:update_adimission_data):
    try:
        new=AddAD.objects(sno=int(me.sno)).to_json()
        new1=json.loads(new)
        if new1:
            a= AddAD.objects(sno=int(me.sno)).update_one(set__target=float(me.target))
            b="Successfully Updated"
            if b:
                    return {"Error":"False","Message":b}
            else:
                # return {"Error":"True","Message":"Data nt found"}
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
        else :
            a={"Error":"True","Message":"please enter valid sno"}
            return JSONResponse(content=a, status_code=400)
    except ValueError:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)

@router.put("/change/Addmission/target/unit/status")
def update(me:adiupda):
    try:
        new=AddAD.objects(sno=int(me.sno)).to_json()
        new1=json.loads(new)
        if new1:
            a= AddAD.objects(sno=int(me.sno)).update_one(set__status=me.status)
            b="Successfully Updated"
            if b:
                    return {"Error":"False","Message":b}
            else:
                # return {"Error":"True","Message":"Data not found"}
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)
        else :
            a={"Error":"True","Message":"please enter valid sno"}
            return JSONResponse(content=a, status_code=400)
    except ValueError:
        a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)