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
router=APIRouter(tags=["Reports"])
@router.post("/get/my/team/report")
async def add_records(me:myteamre):
        date_only=me.date
        for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:

            try:
                dto=datetime.strptime(me.date,format)
                # dto1=datetime.strptime(dd,format).datetime()
                date_only = datetime.combine(dto, datetime.min.time())
            except ValueError:
                pass
        gg=Usercreate.objects(Reporting_Manager=me.reporting_manager).to_json()
        ggg=json.loads(gg)
        if ggg:
            data1={"Error":"False","Message":"Data found","Teamreports":[]}
            for ff in ggg:
                dan=ff["Employee_id"]
                dan2=ff["Reporting_Manager"]
                dan3=ff["User_name"]
                start_time1= datetime.combine(dto, time(0, 0))
                end_time1= datetime.combine(dto, time(16,00))
                start_time2= datetime.combine(dto, time(16, 1))
                end_time2= datetime.combine(dto, time(23, 59))
                start_time3= datetime.combine(dto, time(0, 0))
                end_time3= datetime.combine(dto, time(23, 59))
                rr=Callreport.objects(created_on__gte=start_time1,created_on__lte=end_time1,created_by=str(dan)).count()
                r=Callreport.objects(created_on__gte=start_time2,created_on__lte=end_time2,created_by=str(dan)).count()
                # pipeline = [{"$match": {"camp": {"$ne": "String","$ne":""}}},{"$group": {"_id": "$camp", "count": {"$sum": 1}}},{"$group": {"_id": None, "total_count": {"$sum": 1}}}]
                #call count ucid
                r1=Callreport.objects(created_on__gte=start_time3,created_on__lte=end_time3,created_by=str(dan),Ucid_id__ne="").count()
                r2=Callreport.objects(created_on__gte=start_time3,created_on__lte=end_time3,created_by=str(dan),camp__ne="").count()
                aaa={"EMP_id":dan,"Name":dan3,"Reporting_manager":dan2,"First_Half":rr,"Second_Half":r,"Callcount":r1,"Activitycount":r2}
                data1["Teamreports"].append(aaa)
            return data1
        else:
                a={"Error":"True","Message":"Data not found"}
                return JSONResponse(content=a, status_code=400)

        

@router.post("/get/Team/coverage")
def gf(me:getre):
    id=me.Reporting_manager_id
    for format in ["%Y-%m","%Y/%m","%m-%Y","%m.%Y","%m/%Y","%b-%Y","%Y-%b"]:

            try:
                dto1=datetime.strptime(me.month_year,format)
                dto2=datetime.strptime(me.month_year,format).year
                dto3=datetime.strptime(me.month_year,format).month
                # end_date = (datetime(dto2, dto3 + 1, 1) - timedelta(days=1))
                if dto3<=11:
                    end_date = (datetime(dto2, dto3 + 1, 1) - timedelta(days=1))
                else:
                    end_date = (datetime(dto2, 1, 1) - timedelta(days=1))

            except ValueError:
                pass
    a=Usercreate.objects(Reporting_Manager=str(id),Role_Code="Executive",Active_Status="Active").to_json()
    a1=json.loads(a)
    data2={"Error":"False","Message":"Data found","Teamreport":[]}
    if a1:
        for d in a1:
            dd=d["Employee_id"]
            dd1=d["User_name"]
            a=Callreport.objects(created_by=str(dd),created_on__gte=dto1,created_on__lte=end_date,Ucid_id__ne="").count()
            new1=AddMaster1.objects(created_by=str(dd),created_on__gte=dto1,created_on__lte=end_date,Ucid_id__ne="").count()
            new3=Callreport.objects(created_by=str(dd),created_on__gte=dto1,created_on__lte=end_date,Ucid_id__ne="").distinct('Ucid_id')
            call_count=len(new3)
            Not_visit=new1-call_count
            af={"Emp_id":dd,"Name":dd1,"call_count":a,"Master_count":new1,"unique_call_count_ucid":call_count,"Not_visit":Not_visit,"v1":a,"v2":0,"v3":0}
            data2["Teamreport"].append(af)
        return data2
    else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)

@router.post("/get_my_team_report_mkh")
def mar(me:marketing):
    for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:

            try:
                dto=datetime.strptime(me.from_date,format).date()
                dto1=datetime.strptime(me.to_date,format).date()
                date_only = datetime.combine(dto, datetime.min.time())
                start_time1= datetime.combine(dto, time(0, 0))
                end_time1= datetime.combine(dto, time(16,00))
            except ValueError:
                pass
    bre=me.Branch
    change= bre[:1].upper() + bre[1:]
    a=Usercreate.objects(Branch=change,Role_Code__in=["Manager", "Executive"],Active_Status="Active").to_json()
    b=json.loads(a)
    if b :
        data1={"Error":"False","Message":"Data found","Marketing":[]}
        for c in b:
            h=c["Employee_id"]
            gg=c["User_name"]
            mm=c["Reporting_Manager"]
            rc=c["Role_Code"]
            if dto!=dto1:
                vv=Camp.objects(created_by=str(h),created_on__gte=dto,created_on__lte=dto1).count()
                uu=Enrol.objects(created_by=str(h),created_on__gte=str(dto),created_on__lte=str(dto1)).count()
            else:
                vv=Camp.objects(created_by=str(h),created_on__gte=start_time1,created_on__lte=end_time1).count()
                uu=Enrol.objects(created_by=str(h),created_on__gte=str(start_time1),created_on__lte=str(end_time1)).count()
            aaa={"Emp_id":h,"Name":gg,"Camp_counts":vv,"Reporting_Manager":mm,"Enrol_counts":uu,"Role":rc}
            data1["Marketing"].append(aaa)
        return data1
    else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)
# @app.post("/get_my_team_report_mkh_list")
# def mar(me:marketing):
#     dto = datetime.strptime(me.from_date, "%Y-%m-%d")
#     dto1 = datetime.strptime(me.to_date, "%Y-%m-%d") + timedelta(days=1)
#     bre = me.Branch
#     change = bre[:1].upper() + bre[1:]
#     manager_data = Usercreate.objects(Branch=change, Role_Code__in=["Manager", "Executive"], Active_Status="Active").as_pymongo()
#     if not manager_data:
#         return {"Error": "True", "Message": "No data found"}
#     result = {"Error": "False", "Message": "Data found", "Marketing": []}
#     for manager in manager_data:
#         employee_id = manager["Employee_id"]
#         User_name=manager["User_name"]
#         camp_data = Camp.objects(created_by=str(employee_id), created_on__gte=dto, created_on__lt=dto1).order_by("-sno").as_pymongo()
#         enrol_data = Enrol.objects(created_by=str(employee_id), created_on__gte=dto, created_on__lt=dto1).order_by("-sno").as_pymongo()
#         for camp in camp_data:
            
#             for enrol in enrol_data:
#                 if camp and enrol_data:
#                     camps_str = camp["TransID"]
#                     camp_names_str = camp["campname"]
#                     Enroll = enrol["Patient_name"]
#                 else:
#                     camps_str = "Null"
#                     camp_names_str = "Null"
#                     Enroll = "Null"
#                 result["Marketing"].append({
#                     "Employee_id": employee_id,
#                     "User_name": User_name,
#                     "camps": camps_str,
#                     "Date": camp["created_on"],
#                     "camp_names": camp_names_str,
#                     "patients": Enroll
#                 })

#     if not result["Marketing"]:
#         a={"Error":"True","Message":"Data not found"}
#         return JSONResponse(content=a,status_code=400)
#     else:
#         return result





@router.post("/get/Team/camp/registration/list")
def mar(me:marketing1):
    for format in ["%Y-%m-%d","%Y/%m/%d","%Y.%m.%d","%d/%m/%Y","%d-%m-%Y","%d.%m.%Y","%m/%d/%Y","%m-%d-%Y","%m.%d.%Y","%d-%b-%Y","%Y-%b-%d"]:

            try:
                dto=datetime.strptime(me.from_date,format)
                dto1=datetime.strptime(me.to_date,format)
                start_time1= datetime.combine(dto, time(0, 00))
                end_time1= datetime.combine(dto, time(23,59))
                date_only = datetime.combine(dto, datetime.min.time())
            except ValueError:
                pass
    
    if dto!=dto1:
        uu=Enrol.objects(created_by=me.emp_id,created_on__gte=str(dto),created_on__lte=str(dto1)).to_json()
        vv=json.loads(uu)
    else:
         uu=Enrol.objects(created_by=me.emp_id,created_on__gte=str(start_time1),created_on__lte=str(end_time1)).to_json()
         vv=json.loads(uu)
    data1={"Error":"False","Message":"Data found","Registration_list":[]}
    if vv:
        for v in vv:
            a22=v["mobile"]
            formatted_number = a22[:1] + "*******" + a22[-2:]
            m={"Patient_name":v["Patient_name"],"Age":v["Age"],"Mobile":formatted_number}
            data1["Registration_list"].append(m)
        return data1       
    else:
            a={"Error":"True","Message":"Data not found"}
            return JSONResponse(content=a, status_code=400)   
@router.post("/location_coverage_report")
def coverage(me:loccoverage):
    now = datetime.now().date()
    k=now
    b1= me.Branch[:1].upper() + me.Branch[1:]
    data1={"Error":"False","Message":"Data found","location_coverage":[]}
    new=Usercreate.objects(Branch=b1,Active_Status="Active",Role_Code__in=["Manager", "Executive"]).to_json()
    new1=json.loads(new)
    if new1:
        for n in new1:
            id=n["Employee_id"]
            na=n["User_name"]
            loc=n["Location"]
            loca=n["Location_address"]
            phone=n["mobile_number"]
            role=n["Role_Code"]
            data=Callreport.objects(created_on__gt=k,created_by=str(id)).to_json()
            dss=json.loads(data)
            if dss:
                status="present"
            else:
                status="absent"
            r1=Callreport.objects(created_on__gt=k,created_by=str(id),Ucid_id__ne="").count()
            r2=Callreport.objects(created_on__gt=k,created_by=str(id),camp__ne="").count()
            a={"emp_id":id,"emp_name":na,"status":status,"Role_code":role,"calls":r1,"activites":r2,"location":loc,"location_address":loca,"phonenumber":phone}
            data1["location_coverage"].append(a)
        return data1
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)

@router.post("/get_location_emp_coverage_report")
def get_location_emp(me:get_location_cov):
    now = datetime.now().date()
    k=now
    start_time1= datetime.combine(now, time(0, 00))
    end_time1= datetime.combine(now, time(23,59))
    data1={"Error":"False","Message":"Data found","emp_coverage":[]}
    new=AddMaster1.objects(created_by=me.emp_id,created_on__gte=start_time1,created_on__lte=end_time1).count()
    new1=len(Callreport.objects(created_by=me.emp_id,created_on__gte=start_time1,created_on__lte=end_time1,Ucid_id__ne='').distinct(field="Ucid_id"))
    total=new+new1
    new5=Callreport.objects(created_by=me.emp_id,created_on__gte=start_time1,created_on__lte=end_time1).to_json()
    new6=json.loads(new5)
    if new6:
        for data in new6:
            a=data["Ucid_id"]
        nn=len(new6)
        if nn==1:
            v1=nn
        elif nn>1:
            v2=nn
        elif nn>3:
            v3=nn
        a={"total_counts":total,"meet":new1,"not_meet":new,"v1":v1,"v2":0,"v3":0}
        data1["emp_coverage"].append(a)
        return data1
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)     