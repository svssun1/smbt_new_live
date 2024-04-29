from fastapi import APIRouter
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta,datetime,time
router=APIRouter(tags=["Revenue"])
@router.post("/ADD/Revenue/Target")
def revenue(me:adre11):
    now = datetime.now()
    change= me.unit_name[:1].upper() + me.unit_name[1:]
    # month_now=datetime.now().month
    # year_now=datetime.now().year
    k2=str(now)
    # start_date = datetime(year_now, month_now, 1)
    # end_date = datetime(year_now, month_now + 1, 1)
    b=me.month_year[0].upper()+me.month_year[1:]
    ff=me.month_year
    for format in ["%Y-%m","%Y-%b","%b-%Y","%m-%Y"]:
        try:
            date_obj = datetime.strptime(ff, format)
            month_year_str = date_obj.strftime('%b-%Y')
            sss=str(month_year_str)
            f=AddRe11.objects(status="Active",month_year=sss,unit_name=change).order_by("-sno").to_json()
            h=json.loads(f)
            if h:
                a={"Error":"True","Message":"Target Is Already Exist For This Month And Branch"}
                return JSONResponse(content=a, status_code=400)
            else:
                data=AddRe11(sno=AddRe11.objects.count()+1,unicode="UN{:002d}".format(AddRe11.objects.count()+1),unit_name=change,month_year=sss,target=float(me.target),Incroces=float(me.Incores),Inlaks=float(me.Inlakhs),Inthousands=float(me.Inthousands),created_by=me.created_by,modified_by="None",modified_on=k2,status="Active",created_on=now)
                data.save()
                b="Successfully Submitted"
                if b:
                    return {"Error":"False","Message":b}
                else:
                    a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)

        except:
            pass
        
@router.get("/get/revenue/Target")
def get_rev():
    f=AddRe11.objects(status="Active").order_by("-sno").to_json()
    h=json.loads(f)
    data={"Error":"False","message":"Data found","RevenueTarget":[]}
    if h:
        for g in h:
            ff=g["month_year"]
            month_year_str = ""
            for format in ["%Y-%m","%Y-%b","%b-%Y","%m-%Y"]:
                try:
                    date_obj = datetime.strptime(ff, format)
                    month_year_str = date_obj.strftime('%b-%Y')
                    break
                except ValueError:
                    pass
            b={"SNO":g["sno"],"UnitName":g["unit_name"],"Month_Year":month_year_str,"Target":str(g["target"]),"Incroces":str(g["Incroces"]),"Inlaks":str(g["Inlaks"]),"Inthousands":str(g["Inthousands"]),"status":g["status"]}
            data["RevenueTarget"].append(b)
        return data
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/search/revenue/Target")
def get_revenue(me:search_revenue_web):
    f=AddRe11.objects(sno=me.sno,status="Active").to_json()
    h=json.loads(f)
    data={"Error":"False","message":"Data found","RevenueTarget":[]}
    if h:
        for g in h:
            ff=g["month_year"]
            for format in ["%Y-%m","%Y-%b","%b-%Y","%m-%Y"]:
                try:
                    date_obj = datetime.strptime(ff, format)
                    month_year_str = date_obj.strftime('%b-%Y')
                except ValueError:
                    pass
            b={"SNO":g["sno"],"UnitName":g["unit_name"],"Month_Year":month_year_str,"Target":str(g["target"]),"Incroces":str(g["Incroces"]),"Inlaks":str(g["Inlaks"]),"Inthousands":str(g["Inthousands"])}
            data["RevenueTarget"].append(b)
        return data
    else:
             
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)

@router.post("/search_revenue_taget_mobile")
def revenue_terget_search(me:search_revenue1):
    result = AddRe11.objects(unit_name__icontains=me.search,status="Active",created_by=me.created_by).order_by("-sno").to_json()
    result1=json.loads(result)
    print("result1")
    data={"Error":"False","message":"Data found","RevenueTarget":[]}
    if result1:
        for g in result1:
            ff=g["month_year"]
            for format in ["%Y-%m","%Y-%b","%b-%Y","%m-%Y"]:
                try:
                    date_obj = datetime.strptime(ff, format)
                    month_year_str = date_obj.strftime('%b-%Y')
                except ValueError:
                    pass
            b={"SNO":g["sno"],"UnitName":g["unit_name"],"Month_Year":month_year_str,"Target":str(g["target"]),"Incroces":str(g["Incroces"]),"Inlaks":str(g["Inlaks"]),"Inthousands":str(g["Inthousands"]),"status":g["status"]}
            data["RevenueTarget"].append(b)
    return data


@router.put("/change/Revenue/target")
def update(me:update_revenue_data):
    try:
        new=AddRe11.objects(sno=int(me.sno)).to_json()
        new1=json.loads(new)
        if new1:
            a= AddRe11.objects(sno=int(me.sno)).update_one(set__target=float(me.target),set__Incroces=float(me.Incores),set__Inlaks=float(me.Inlakhs),set__Inthousands=float(me.Inthousands))
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
@router.put("/change/Revenue/target/unit/status")
def update(me:upda):
    try:
        new=AddRe11.objects(sno=int(me.sno)).to_json()
        new1=json.loads(new)
        if new1:
            a= AddRe11.objects(sno=int(me.sno)).update_one(set__status=me.status)
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