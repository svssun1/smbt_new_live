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
router=APIRouter(tags=["Add Call"])
@router.post("/call/submit/details")
async def call_sub(info:Request,me:callreport):
    in_tz = pytz.timezone('Asia/Kolkata')
    in_time = datetime.now(in_tz)
    in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
    a=await info.json()
    try:
        Lattitide=a["Lattitide"]
        Logitude=a["Logitude"]
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(Lattitide+","+Logitude)
        address = location.raw['address']
        city=address["city"]
        state=address["state"]
        pincode=address["postcode"]
        district=address["state_district"]
        location=address["city"]
    except ValueError:
        # return "please enter Lattitide and Logitude values"
        data1={"Error":"True","Message":"GPS Signal too Weak"}
        return JSONResponse(content=data1, status_code=400)
    now = datetime.now().date()
    start_time1= datetime.combine(now, time(0, 0))
    end_time1= datetime.combine(now, time(23,59))
    type=a["type"]
    change= type[:1].upper() + type[1:]
    u=me.Ucid_id
    g=Callreport.objects(Ucid_id=u,created_on__gte=start_time1,created_on__lte=end_time1).to_json()
    gg=json.loads(g)
    tt=None
    def ucid_valid():
        for f in gg:
            if f["Ucid_id"] is not None:
                tt =f["Ucid_id"]
            else:
                tt=None

            return tt
    check=ucid_valid()    
    if change=="Call":
        
        if all([me.Ucid_id, me.name,me.mobilenumber,me.Designation]):
            if me.Ucid_id!=check:
                fe=Callreport(sno=Callreport.objects.count()+1,Ucid_id=me.Ucid_id,name=me.name,Designation=me.Designation,mobilenumber=me.mobilenumber,catagery=me.catagery,remarks=me.remarks,groupcall=me.groupcall,branch=me.branch,camp=me.camp,campdetails=me.campdetails,Lattitide=Lattitide,Logitude=Logitude,city=city,pincode=pincode,district=district,state=state,location=location,station=me.station,created_by=me.created_by,status="Active",created_on=in_time_str)
                fe.save()
                a="Successfully Submitted"
                return {"Error":"False","Message":a}
            else:
                data1={"Error":"True","Message":"UCID is Already Existed"}
                return JSONResponse(content=data1, status_code=400)
        else:
            # return {"message": "UCID and Name and mobile number and Designation is empty"}
            data1={"Error":"True","Message":"UCID,Name,Mobile and Designation are Empty"}
            return JSONResponse(content=data1, status_code=400)
    elif change=="Camp":

        if all([me.camp,me.campdetails]):
            fe=Callreport(sno=Callreport.objects.count()+1,Ucid_id=me.Ucid_id,name=me.name,Designation=me.Designation,mobilenumber=me.mobilenumber,catagery=me.catagery,remarks=me.remarks,groupcall=me.groupcall,branch=me.branch,camp=me.camp,campdetails=me.campdetails,Lattitide=Lattitide,Logitude=Logitude,city=city,pincode=pincode,district=district,state=state,location=location,station=me.station,created_by=me.created_by,status="Active",created_on=in_time_str)
            fe.save()
            a="Successfully Submited"
            return {"Error":"False","Message":a}
        else:
            # return {"message": "Camp and Campdetails is empty"}
            data1={"Error":"True","Message":"Camp and Campdetails are Empty"}
            return JSONResponse(content=data1, status_code=400)
    else:
            data1={"Error":"True","Message":"Please Enter Type"}
            return JSONResponse(content=data1, status_code=400)
@router.post("/get_call_submit_details")
def get_call_submit(me:get_call_report):
    for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
        try:
            
            dto=datetime.strptime(me.date, format).date()
            start_time1= datetime.combine(dto, time(0, 0))
            end_time1= datetime.combine(dto, time(23,59))
            f=Callreport.objects(Q(created_on__gte=start_time1) & Q(created_on__lte=end_time1) & Q(created_by=me.emp_id)   & Q(status="Active") & Q(Ucid_id__ne="")  & Q(name__ne="")).order_by("-sno").to_json()
            # f=Callreport.objects(created_on=dto,status="Active").to_json()
            g=json.loads(f)
            data={"Error":"False","Message":"Data found","call_details":[]}
            if g:
                for ff in g:
                    k=ff["created_on"]
                    timestamp = k['$date']
                    date_object = datetime.fromtimestamp(timestamp/1000).date()
                    formatted_date = date_object.strftime('%Y-%b-%d')
                    a={"sno":ff["sno"],"Ucid_id":ff["Ucid_id"],"name":ff["name"],"Designation":ff["Designation"],"mobilenumber":ff["mobilenumber"],"city":ff["city"],"district":ff["district"],"state":ff["state"],"branch":ff["branch"],"station":ff["station"],"groupcall":ff["groupcall"],"catagery":ff["catagery"],"created_by":ff["created_by"],"created_on":formatted_date,"remarks":ff["remarks"]}
                    data["call_details"].append(a)
                return data
            else:
            # return {"Error":"True","Message":"Data not found"}
             data1={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=data1, status_code=400)
        except ValueError:
            pass
@router.post("/get_activity_submit_details")
def get_call_submit(me:get_call_report):
    for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:
        try:
            dto=datetime.strptime(me.date, format).date()
            start_time1= datetime.combine(dto, time(0, 0))
            end_time1= datetime.combine(dto, time(23,59))
            # f=Callreport.objects(Q(created_on__gte=start_time1) & Q(created_on__lte=end_time1)   & Q(status="Active")).order_by("-sno").to_json()
            f=Callreport.objects(created_on__gte=start_time1,created_on__lte=end_time1,status="Active",camp__ne="",campdetails__ne="",created_by=me.emp_id).order_by("-sno").to_json()
            # f=Callreport.objects(created_on=dto,status="Active").to_json()
            g=json.loads(f)
            data={"Error":"False","Message":"Data found","call_details":[]}
            if g:
                for ff in g:
                     ddd=ff["camp"]
                     ddd4=ff["campdetails"]
                     k=ff["created_on"]
                     timestamp = k['$date']
                     date_object = datetime.fromtimestamp(timestamp/1000).date()
                     formatted_date = date_object.strftime('%Y-%b-%d')
                     a={"sno":ff["sno"],"camp":ddd,"campdetails":ddd4,"created_by":ff["created_by"],"created_on":formatted_date,"remarks":ff["remarks"]}
                     data["call_details"].append(a)
                return data
            else:
            # return {"Error":"True","Message":"Data not found"}
             data1={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=data1, status_code=400)
        except ValueError:
            pass

@router.post("/Search/call/report")
def call(me:Se):
        result = AddMaster1.objects(Q(mobile__icontains=me.search) | Q(Ucid_id__icontains=me.search) | Q(Agent_name__icontains=me.search) ,created_by=me.created_by)
        if result:
            data={"Error":"False","message":"Data found","callreport":[{"UCID":result1.Ucid_id,"Name":result1.Agent_name,"Designation":result1.Designation,"Mobilenumber":result1.mobile,"created_by":result1.created_by} for result1 in result]}
            return data
        else:
            data1={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=data1, status_code=400)
# def call(me:Se):
        
#         result = AddMaster1.objects(Q(mobile__icontains=me.search) | 
#                                     Q(Ucid_id__icontains=me.search) | 
#                                     Q(Agent_name__icontains=me.search) ,created_by=me.created_by).to_json()
    
#         m=json.loads(result)
#         data={"Error":"False","message":"Data found","callreport":[]}
#         if m:
#             for f in m:
#                 de={"UCID":f["Ucid_id"],"Name":f["Agent_name"],"Designation":f["Designation"],"Mobilenumber":f["mobile"],"created_by":f["created_by"]}
#                 data["callreport"].append(de)
#             return data
#         else:
#             # return {"Error":"True","Message":"Data not found"}
#             data1={"Error":"True","Message":"Data not found"}
#             return JSONResponse(content=data1, status_code=400)
@router.put("/update_call_submit_details")
def update_call_sub(me:update_call):
    new=Callreport.objects(sno=me.sno).to_json()
    new1=json.loads(new)
    if new1:
        new=Callreport.objects(sno=me.sno).update_one(set__name=me.name,set__Designation=me.Designation,set__mobilenumber=me.mobilenumber,set__remarks=me.remarks,set__station=me.station,set__Ucid_id=me.Ucid_id)
        b="Successfully Submitted"
        if b:
                return {"Error":"False","Message":b}
        else:
            a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
    else:
            a={"Error":"True","Message":"please enter valid sno"}
    return JSONResponse(content=a, status_code=400)

@router.put("/update_call_status")
def update_call_sub(me:update_status):
    try:
        new=Callreport.objects(sno=me.sno).to_json()
        new1=json.loads(new)
        if new1:
            new2=Callreport.objects(sno=me.sno).update_one(set__status=me.status)
            b="Successfully Deleted"
            if b:
                    return {"Error":"False","Message":b}
            else:
                a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
        else:
                a={"Error":"True","Message":"please enter valid sno"}
        return JSONResponse(content=a, status_code=400)
    except ValueError:
         a={"Error":"True","Message":"please enter valid sno"}
         return JSONResponse(content=a, status_code=400)

@router.post("/Delete_call_report_data_{sno}")
def delete_userdetails(call_re:del_call_reort):
    userdetail = Callreport.objects(sno=int(call_re.sno)).first()
    if userdetail is None:
        return {"Error": "True", "Message": "User not found"}
    userdetail.delete()
    Callreport.objects(sno__gt=call_re.sno).update(dec__sno=1)
    return {"Error": "False", "Message":"Successfully Deleted"}
