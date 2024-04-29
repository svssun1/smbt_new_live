from pydantic import BaseModel,FilePath
from datetime import date
from datetime import datetime
class Don5(BaseModel):
    genus:str
    family:str
class Don6(BaseModel):
    User_name:str
    Mobile_number:int
    Desigination:str
    Email_id:str
    Branch:str
    Created_by:str
    Modified_by:str
    Modified_On:date
    Source:str
    # Last Login Date & Time
    # Last Location
    Country:str
    Country_code:str
    State:str
    State_code:str
    City:str
    Pincode:int
    Allowance_Per_Day:int
    Multi_Branch_Access:str
    Active_Status:str
    Department:str
    Reporting_Manager:str
    Bank_Account_No:int
    Bank_Name:str
    IFSC_Code:str
    PAN_Number:str
    ID_Proof_No:str
    Role_Code:str
    # Bank Attachment
    # PAN Attachment
    # ID Proof Attachment
    # Profile Image Path
# class test(BaseModel):
#     upload_bank_passbook_path:str
class role(BaseModel):
    Role:str
class change_password_em(BaseModel):
    Employee_id:str
    old_password:str
    new_password:str
    confirm_password:str
class update_user_master_list_using_emp_id(BaseModel):
    Employee_id:str
    User_name:str
    mobile_number:str
    Desigination:str
    Email_id:str
    Country:str
    State:str
    City:str
    Pincode:str
    Allowance_Per_Day:str
    Multi_Branch_Access:str
    Department:str
    Reporting_Manager:str
    Bank_Account_No:str
    Bank_Name:str
    IFSC_Code:str
    PAN_Number:str
    ID_Proof_No:str
    Role_Code:str
    Branch:str
class search_user_list(BaseModel):
    Employee_id:str
class get_userlist(BaseModel):
    emp_id:str
class get_delete(BaseModel):
    emp_id:str
    status:str
class add_depart(BaseModel):
    department_name:str
class add_designation(BaseModel):
    Designation_name:str
class don5(BaseModel):
    name:str
class don7(BaseModel):
    id:str
    state_name:str
    country_id:str
    country_code:str
    country_status:str
    country_name:str
    state_code:str
    state_status:str
class don8(BaseModel):
    unit_code:str
class user_id(BaseModel):
    employe_id:int
class state_list(BaseModel):
    country_code:str
class active(BaseModel):
    Activity_type:str
    created_by:str
class search_activity_report(BaseModel):
    sno:str
class update_activity_report(BaseModel):
    sno:str
    Activity_type:str
class delete_activity(BaseModel):
    sno:str
    status:str
class addunitmaster(BaseModel):
    unit_name:str
    cluster_name:str
    address:str
    file_name:str
    status:str
class addunitmaster_mobile(BaseModel):
    unit_name:str
    cluster_name:str
    address:str
    file_name:bytes
    status:str

class search_unit(BaseModel):
    unit_name:str
class update_unitmaster(BaseModel):
    unit_name:str
    cluster_name:str
    address:str
    file_name:str
class delete_unitmaster(BaseModel):
    unit_name:str
    status:str
class getaddmaster(BaseModel):
    emp_id:str
class search_master_list(BaseModel):
    sno:str
class update_addmaster(BaseModel):
    sno:str
    Agent_name:str
    mobile:str
    Qualification:str
    Designation:str
    Bank_Account_No:str
    Bank_Name:str
    IFSC_Code:str
    PAN_Number:str
    branch:str
    bank_attach_path:str
    pan_attach_path:str

class addmaster1(BaseModel):
    Agent_name:str
    mobile:str
    Qualification:str
    Designation:str
    Latitude:str
    Longitude:str
    Bank_Account_No:int
    Bank_Name:str
    IFSC_Code:str
    PAN_Number:str
    created_by:str
    branch:str
    source:str
    bank_attach_path:str
    pan_attach_path:str
class callreport(BaseModel):
    created_by:str
    name:str
    Ucid_id:str
    Designation:str
    mobilenumber:str
    catagery:str
    remarks:str
    groupcall:str
    branch:str
    source:str
    camp:str
    campdetails:str
    Lattitide:str
    Logitude:str
    station:str
    type:str
class get_call_report(BaseModel):
    date:str
    emp_id:str
class Se(BaseModel):
    search:str
    created_by:str
class adre(BaseModel):
    unit_name:str
    month_year:str
    target:str
    Incores:str
    Inlakhs:str
    Inthousands:str
    created_by:str
class adre11(BaseModel):
    unit_name:str
    month_year:str
    target:str
    Incores:str
    Inlakhs:str
    Inthousands:str
    created_by:str
class update_revenue_data(BaseModel):
    sno:str
    target:str
    Incores:str
    Inlakhs:str
    Inthousands:str
class search_revenue_web(BaseModel):
    sno:str
class update_call(BaseModel):
    sno:str
    name:str
    Designation:str
    mobilenumber:str
    remarks:str
    station:str
    Ucid_id:str
class update_status(BaseModel):
    sno:str
    status:str
class upd(BaseModel):
    sno:str
    target:float
    Incores:float
    Inlakhs:float
    Inthousands:float
class upda(BaseModel):
    sno:str
    status:str
class add_adimision_data(BaseModel):
    unit_name:str
    Date:str
    target:str
    created_by:str
class search_adimission_data(BaseModel):
    sno:str
class search_revenue(BaseModel):
    sno:str
class update_adimission_data(BaseModel):
    sno:str
    target:str
class adiupda(BaseModel):
    sno:str
    status:str
# class adiupda(BaseModel):
#     sno:int
#     status:str
class camp(BaseModel):
    state:str
    city:str
    Area:str
    location:str
    campname:str
    created_by:str
class campdate(BaseModel):
    emp_id:str
    from_date:str
    to_date:str
class updatecamp(BaseModel):
    emp_id:str
    TransID:str
    status:str
class enrol(BaseModel):
    TransID:str
    Patient_name:str
    Age:str
    mobile:str
    Remarks:str
    created_by:str
class update_enrol_data(BaseModel):
    sno:str
    Patient_name:str
    mobile:str
    age:str
    Remarks:str
class update_enrol_status(BaseModel):
    sno:str
    status:str
class enrolme(BaseModel):
    TransID:str
class search_enrol_dta(BaseModel):
    sno:str
class area(BaseModel):
    Location:str
    Pincode:int
    State:str
    District:str
    areacode:str
class Location(BaseModel):
    city:str
class Location1(BaseModel):
    city:str
    
class cluster(BaseModel):
    cluster_name:str
    address:str
class cluster1(BaseModel):
    cluster_name:str
    address:str
class search_cluster(BaseModel):
    sno:str
class update_cluster_data(BaseModel):
    sno:str
    cluster_name:str
    address:str
class delete_cluster_data(BaseModel):
    cluster_code:str
    status:str
class referpatient(BaseModel):
    patient_name:str
    patient_mobile:str
    emp_id:str
    Ucid:str
    conslutant:str
    speciality:str
    remarks:str
    created_by:str
class update_patient_data(BaseModel):
    sno:str
    patient_name:str
    patient_mobile:str
    conslutant:str
    speciality:str
    remarks:str
class update_refer_patient_status(BaseModel):
    sno:str
    status:str
class reget(BaseModel):
    emp_id:str
    from_date:str
    to_date:str
class search_refer_patient(BaseModel):
    sno:str
class city(BaseModel):
    State:str
    City:str
    city_code:str
class state(BaseModel):
    state:str
class consultant(BaseModel):
    consultant:str
    department:str
class department(BaseModel):
    department_name:str
class myteamre(BaseModel):
    reporting_manager:str
    date:str
class get_reports(BaseModel):
    date:str
    emp_id:str
class getre(BaseModel):
    month_year:str
    Reporting_manager_id:str
class marketing(BaseModel):
    Branch:str
    from_date:str
    to_date:str
class marketing1(BaseModel):
    emp_id:str
    from_date:str
    to_date:str
class greet(BaseModel):
    title:str
    message:str
    catagory:str
    image:str
    target_link:str
    share:str
    employe_name:str
    desigation:str
    created_by:str
class update_greet(BaseModel):
    Greet_id:str
    title:str
    message:str
    employe_name:str
    desigation:str
    image:str
class search_greet_id(BaseModel):
    Greet_id:str

class upgre(BaseModel):
    sno:str
    status:str
class news(BaseModel):
    title:str
    message:str
    Attachment:str
    share:str
    # employe_name:str
    # desigation:str
    created_by:str
class search_news_data(BaseModel):
    News_id:str
class newupd(BaseModel):
    sno:str
    status:str
class update_news(BaseModel):
    sno:str
    title:str
    message:str
    share:str
    Attachment:str

class Cordi(BaseModel):
    emp_id:str
    coordinates:str
class loccoverage(BaseModel):
    Branch:str
class emp_id_status(BaseModel):
    emp_id:str
class get_location_cov(BaseModel):
    emp_id:str
class search_revenue1(BaseModel):
    search:str
    created_by:str
class search_adimission(BaseModel):
    search:str
    created_by:str
class search_masterlist(BaseModel):
    search:str
    created_by:str
class cluster_search_mobile(BaseModel):
    search:str
class search_patient(BaseModel):
    search:str
    created_by:str

class del_call_reort(BaseModel):
    sno:str
class mobile_image_data(BaseModel):
    name:str
    file:bytes
class update_image_data(BaseModel):
    name:str
    change_name:str
    path_image:bytes

