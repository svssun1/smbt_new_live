from fastapi import APIRouter
from starlette.responses import JSONResponse
from mongoengine import *
import json
from api.models import *
from mongoengine import *
from api.schema import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta,datetime,time
from geopy.geocoders import Nominatim
import base64
from pathlib import Path

router=APIRouter(tags=["ADD Master"])
@router.post("/Add/Master")
async def master(me:addmaster1):
    # in_tz = pytz.timezone('Asia/Kolkata')
    # in_time = datetime.now(in_tz)
    # in_time_str = in_time.strftime('%Y-%m-%d %H:%M')
    b=me.branch[:1].upper()+me.branch[1:]
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        Latitude =me.Latitude
        Longitude =me.Longitude
        location = geolocator.reverse(Latitude+","+Longitude)
        address = location.raw['address']
        city=address["city"]
        state=address["state"]
        pincode=address["postcode"]
        district=address["state_district"]
        location=address["state_district"]
    except ValueError:
        # return "please enter Latitude and Longitude values"
        data1={"Error":"True","Message":"GPS Singal Too Weak"}
        return JSONResponse(content=data1, status_code=400)
    now = datetime.now()
    try: 
        master=AddMaster1(sno=AddMaster1.objects.count()+1,Ucid_id="UC{:02d}".format(AddMaster1.objects.count()+1),Agent_name=me.Agent_name,mobile=me.mobile,Qualification=me.Qualification,Designation=me.Designation,Bank_Account_No=me.Bank_Account_No,Bank_Name=me.Bank_Name,IFSC_Code=me.IFSC_Code,PAN_Number=me.PAN_Number,Latitude=Latitude,Longitude=Longitude,area=location,city=city,district=district,state=state,pincode=pincode,created_by=me.created_by,status="Active",bank_attach_path=me.bank_attach_path,pan_attach_path=me.pan_attach_path,branch=b,created_on=now)
        master.save()
    except NotUniqueError:
#         # return "Mobile Number is alredy Existed"
        data1={"Error":"True","Message":"Mobile Number Already Existed"}
        return JSONResponse(content=data1, status_code=400)
    except  ValidationError:
        data1={"Error":"True","Message":"Please Check Mobile Number"}
        return JSONResponse(content=data1, status_code=400)
    b="Successfully Submitted"
    if b:
        return {"Error":"False","Message":b}
    else:
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/get/Master/List")
def list1(me:getaddmaster):
    data=AddMaster1.objects(created_by=me.emp_id,status="Active").order_by("-sno").to_json()
    g=json.loads(data)
    data1={"Error":"False","Message":"Data found","MasterList":[]}
    if g:
        for a in g:
            a1=a["bank_attach_path"]
            f = a["Agent_name"]
            f1=a["pan_attach_path"]
            a2=str.encode(a1)
            a3=str.encode(f1)
            FILEPATH="./api/static/{}_bank.jpg".format(f)
            filepath="./api/static/{}_bank.jpg".format(f)
            return_filepATH = "http://13.127.133.6"+filepath[5:]
            with open(FILEPATH,"wb") as fh:
                fh.write(base64.decodebytes(a2))
            FILEPATH="./api/static/{}pan.jpg".format(f)
            filepath="./api/static/{}pan.jpg".format(f)
            return_filepATH2 = "http://13.127.133.6"+filepath[5:]
            with open(FILEPATH,"wb") as fh:
                fh.write(base64.decodebytes(a3))
            g=a["created_on"]
            timestamp = g['$date']
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            formatted_date = date_object.strftime('%d-%b-%Y')
            gt={"sno":a["sno"],"UCID":a["Ucid_id"],"Agent_name":a["Agent_name"],"Mobile":a["mobile"],"Qualification":a["Qualification"],"Designation":a["Designation"],"Location":a["area"],"Bank_Name":a["Bank_Name"],"Bank_Account_No":str(a["Bank_Account_No"]),"IFSC_Code":a["IFSC_Code"],"Created_on":formatted_date,"Branch":a["branch"],"PAN_Number":a["PAN_Number"],"bank_path":return_filepATH,"pan_path":return_filepATH2}
            data1["MasterList"].append(gt)
        return data1
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.post("/search_master_list_mobile")
def master_list(me:search_masterlist):
    result = AddMaster1.objects(Q(Ucid_id__icontains=me.search) | Q(Agent_name__icontains=me.search) | Q(mobile__icontains=me.search),created_by=me.created_by).to_json()
    result1=json.loads(result)
    data1={"Error":"False","message":"Data found","MasterList":[]}
    for a in result1:
        a1=a["bank_attach_path"]
        f = a["Agent_name"]
        f1=a["pan_attach_path"]
        a2=str.encode(a1)
        a3=str.encode(f1)
        FILEPATH="./api/static/{}_bank.jpg".format(f)
        filepath="./api/static/{}_bank.jpg".format(f)
        return_filepATH = "http://13.127.133.6"+filepath[5:]
        with open(FILEPATH,"wb") as fh:
            fh.write(base64.decodebytes(a2))
        FILEPATH="./api/static/{}pan.jpg".format(f)
        filepath="./api/static/{}pan.jpg".format(f)
        return_filepATH2 = "http://13.127.133.6"+filepath[5:]
        with open(FILEPATH,"wb") as fh:
            fh.write(base64.decodebytes(a3))
        g=a["created_on"]
        timestamp = g['$date']
        date_object = datetime.fromtimestamp(timestamp/1000).date()
        formatted_date = date_object.strftime('%d-%b-%Y')
        gt={"sno":a["sno"],"UCID":a["Ucid_id"],"Agent_name":a["Agent_name"],"Qualification":a["Qualification"],"Designation":a["Designation"],"Location":a["area"],"Created_on":formatted_date,"Branch":a["branch"],"bank_path":return_filepATH,"pan_path":return_filepATH2}
        data1["MasterList"].append(gt)
    return data1
    
@router.post("/search/Master/List")
def search_master_list(me:search_master_list):
    data=AddMaster1.objects(sno=int(me.sno),status="Active").to_json()
    g=json.loads(data)
    data1={"Error":"False","Message":"Data found","MasterList":[]}
    if g:
        for a in g:
            g=a["created_on"]
            timestamp = g['$date']
            a1=a["bank_attach_path"]
            f = a["Agent_name"]
            f1=a["pan_attach_path"]
            a2=str.encode(a1)
            a3=str.encode(f1)
            FILEPATH="./api/static/{}_bank.jpg".format(f)
            filepath="./api/static/{}_bank.jpg".format(f)
            return_filepATH = "http://13.127.133.6"+filepath[5:]
            with open(FILEPATH,"wb") as fh:
                fh.write(base64.decodebytes(a2))
            FILEPATH="./api/static/{}pan.jpg".format(f)
            filepath="./api/static/{}pan.jpg".format(f)
            return_filepATH2 = "http://13.127.133.6"+filepath[5:]
            with open(FILEPATH,"wb") as fh:
                fh.write(base64.decodebytes(a3))
            date_object = datetime.fromtimestamp(timestamp/1000).date()
            formatted_date = date_object.strftime('%Y-%b-%d')
            gt={"sno":a["sno"],"UCID":a["Ucid_id"],"Agent_name":a["Agent_name"],"Qualification":a["Qualification"],"Designation":a["Designation"],"Location":a["area"],"Created_on":formatted_date,"bank_path":return_filepATH,"pan_path":return_filepATH2}
            data1["MasterList"].append(gt)
        return data1
    else:
        # return {"Error":"True","Message":"Data not found"}
        a={"Error":"True","Message":"Data not found"}
        return JSONResponse(content=a, status_code=400)
@router.put("/update_add_master_data")
def update_master(me:update_addmaster):
    try:
        new=AddMaster1.objects(sno=me.sno).to_json()
        new1=json.loads(new)
        if new1:
            if me.bank_attach_path !="" and me.pan_attach_path !="" :
                a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch,set__bank_attach_path=me.bank_attach_path,set__pan_attach_path=me.pan_attach_path)
            elif me.bank_attach_path !="":
                a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch,set__bank_attach_path=me.bank_attach_path)
            elif me.pan_attach_path !="":
                a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch,set__pan_attach_path=me.pan_attach_path)
            elif me.bank_attach_path=="" and me.pan_attach_path =="":
                a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch)
            # elif me.pan_attach_path=="string" or me.bank_attach_path=="string":
            #     a= AddMaster1.objects(sno=me.sno).update_one(set__Agent_name=me.Agent_name,set__mobile=me.mobile,set__Qualification=me.Qualification,set__Designation=me.Designation,set__Bank_Account_No=int(me.Bank_Account_No),set__Bank_Name=me.Bank_Name,set__IFSC_Code=me.IFSC_Code,set__PAN_Number=me.PAN_Number,set__branch=me.branch)

            b="Successfully Submited"
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