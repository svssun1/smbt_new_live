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
router=APIRouter(tags=["Camp"])
@router.post("/Create/Camp/Data")
def cam(me:camp):
    now = datetime.now()
    k=str(now)
    # in_tz = pytz.timezone('Asia/Kolkata')
    # in_time = datetime.now(in_tz)
    # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
    f=Camp.objects(Q(status="Start")  & Q(created_by=me.created_by)).to_json()
    g=json.loads(f)
    if g:
        a={"Error":"True","Message":"Please Stop Already Existed Camp"}
        return JSONResponse(content=a, status_code=400)
    else :
        da=Camp(sno=Camp.objects.count()+1,TransID="CAMP{:002d}".format(Camp.objects.count()+1),state=me.state,city=me.city,Area=me.Area,location=me.location,campname=me.campname,created_by=me.created_by,modified_by="head",modified_on=k,status="Start",created_on=now)
        da.save()
        ad=da.TransID
        b="Successfully Created"
        if b:
            return {"Error":"False","Message":b,"CAMPID":ad}
        else:
            # return {"Error":"True","Message":"Data not found"}
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)

    
@router.post("/Get/Camp")
def empn(me:campdate):
    da=me.from_date
    da1=me.to_date
    for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
            try:
                dto=datetime.strptime(da, format)
                dto1=str(dto)
                d=datetime.strptime(da1, format)
                # d22=datetime.strptime(da1, format)
                # d1=str(d)
                dto22=datetime.strptime(me.to_date,format)+timedelta(days=1)
                # dto221=str(dto22)
                start_time1= datetime.combine(dto, time(0, 0))
                end_time1= datetime.combine(dto, time(23,59))
                if dto1!=dto22:
                    f=Camp.objects(created_by=me.emp_id,created_on__gte=dto1,created_on__lte=dto22).order_by("-sno").to_json()
                    g=json.loads(f)
                else:
                     f=Camp.objects(created_by=me.emp_id,created_on__gte=start_time1,created_on__lte=end_time1).order_by("-sno").to_json()
                     g=json.loads(f)
                
                data={"Error":"False","Message":"Data found","Campdetails":[]}
                if g:
                    for k in g:
                        g=k["created_on"]
                        timestamp = g['$date']
                        date_object = datetime.fromtimestamp(timestamp/1000).date()
                        formatted_date = date_object.strftime('%d-%b-%Y')
                        ds={"SNO":k["sno"],"CampID":k["TransID"],"State":k["state"],"City":k["city"],"Area":k["Area"],"Campname":k["campname"],"Date":formatted_date,"Status":k["status"]}
                        data["Campdetails"].append(ds)
                    return data
                else:
                    # return {"Error":"True","Message":"Data not found"}
                    a={"Error":"True","Message":"Data not found"}
                    return JSONResponse(content=a, status_code=400)
            except ValueError:
                pass

@router.put("/update/Camp/status")
def update(me:updatecamp):
    b1= me.status[:1].upper() + me.status[1:]
    f=Camp.objects(created_by=me.emp_id,TransID=me.TransID).to_json()
    g=json.loads(f)
    if g:
        a= Camp.objects(created_by=me.emp_id,TransID=me.TransID).update_one(set__status=b1)
        b="Successfully Updated"
        if b:
                return {"Error":"False","Message":b}
        else:
            # return {"Error":"True","Message":"Data not found"}
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
    else:
        a={"Error":"True","Message":"Please check Details"}
        return JSONResponse(content=a, status_code=400)