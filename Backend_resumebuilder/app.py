from litestar import Litestar, get, post, put, delete, Request
from litestar.config.cors import CORSConfig
from database import session
from typing import Any
import json
import re
import smtplib
from models import (
    ApplicantPersonalInfo,
    ApplicantAddressInfo,
    ApplicantEducationInfo,
    ApplicantWorkExperienceInfo,
    ApplicantProjectDetailsInfo,
    ApplicantSkillsInfo,
    ApplicantSocialMediaInfo,
    ApplicantLanguageInfo,
)

def clean_record(record):
    """
       Removes unnecessary keys and values
       from a record,then returns the modified record.
    """
    for key in ["_sa_instance_state", "applicant_id", "id"]:
        record.pop(key)
    return record


def final_records(records):
    """
       This method returns the data as a dictionary
       if there is only one record in the table for a given
       ID, or as a list of dictionaries if there are multiple records.
    """
    record_list = []
    # If there is only one record in the collection
    if records.count() == 1:
        record = records.first().__dict__
        record = clean_record(record)
        new_record = {}
        if record:
            for key, value in record.items():
                new_record[key] = str(value)
            record_list.append(new_record)
        return record_list
    # If there are multiple records in the collection
    elif records.count() > 1:
        for record in records.all():
            record = clean_record(record.__dict__)
            for key, value in record.items():
                record[key] = str(value)
            record_list.append(record)
        return record_list
    
def send_form_creation_email(data):
    """
       Sends an email notification when a form is created,
       Connect to the email server using the provided credentials
    """
    # Connect to the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('snehamohan6282@gmail.com', 'pwwp dpmz pzrm zpbn')
    From = 'snehamohan6282@gmail.com'
    To = 'snehac@alokin.in'
    subject = "Test mail"
    body = f'Resume created successfully by {data["personalDetails"]["full_name"]}'
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail(From, To, message)
    # print("Mail sent")


@get("/resumes/", name = "fetch_resumes")
async def fetch_records() -> json:
    """
        This function retrieves all resumes from the ApplicantPersonalInfo table in the database and
        returns them as a JSON string.
    """
    records = session.query(ApplicantPersonalInfo).all()
    # Create an empty dictionary to store all records
    all_records = {}
    for record in records:
        record_id = record.id
        # Convert the record object to a dictionary and remove the '_sa_instance_state' key
        data = record.__dict__
        data.pop("_sa_instance_state", None)
        # Create a key-value pair for the record
        key = f"record_{record_id}"
        value = data
        # Add the key-value pair to the dictionary of all records
        all_records[key] = value
        # Convert the dictionary of records to a JSON string
        json_data = json.dumps(all_records)
    return json_data


@get("/resume/{val_id: int}", name = "fetch_record_by_id")
async def fetch_record_by_id(val_id : int) -> json:
    """
    This function retrieve resume according to their id from the database and
    returns them as a JSON string.
    """
    all_data = {}
    applicant_basic_record = (session.query(ApplicantPersonalInfo).filter_by(id = val_id).first().__dict__)
    applicant_basic_record.pop("_sa_instance_state", None)
    all_data["personalDetails"] = applicant_basic_record

    applicant_address_record = (session.query(ApplicantAddressInfo).filter_by(applicant_id = val_id).first().__dict__)
    all_data["addressDetails"] = clean_record(applicant_address_record)

    applicant_education_record = session.query(ApplicantEducationInfo).filter_by(applicant_id = val_id)
    all_data["educationDetails"] = final_records(applicant_education_record)

    applicant_skills_record = session.query(ApplicantSkillsInfo).filter_by(applicant_id = val_id)
    all_data["skillDetails"] = final_records(applicant_skills_record)

    applicant_projects_record = session.query(ApplicantProjectDetailsInfo).filter_by(applicant_id = val_id)
    all_data["projectDetails"] = final_records(applicant_projects_record)

    applicant_socialmedia_record = session.query(ApplicantSocialMediaInfo).filter_by(applicant_id = val_id)
    all_data["socialMediaDetails"] = final_records(applicant_socialmedia_record)

    applicant_workexperience_record = session.query(ApplicantWorkExperienceInfo).filter_by(applicant_id = val_id)
    all_data["workExperienceDetails"] = final_records(applicant_workexperience_record)
    
    applicant_language_record = session.query(ApplicantLanguageInfo).filter_by(applicant_id = val_id)
    all_data["languageDetails"] = final_records(applicant_language_record)

    json_data = json.dumps(all_data)
    return json_data

# fetch resume by mail ,name and phone number
@get("/search-resume/{value:str}", name="search_resume")
async def fetch_data(value: str) -> json:
    """
        This function searches and retrieves resumes based on the specified value.
        It takes a value as input and returns a JSON string containing the matching applicant's resume data if found.
    """
    if re.match(r'^[a-zA-Z\s]+$', value):
        # Search by name
        records = session.query(ApplicantPersonalInfo).filter(ApplicantPersonalInfo.full_name.like(f"%{value}%")).all()
    elif re.match(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$', value):
        # Search by email
        records = session.query(ApplicantPersonalInfo).filter(ApplicantPersonalInfo.email.like(f"%{value}%")).all()

    elif re.match(r'^[0-9]+$', value):
        # Search by phone number
        records = session.query(ApplicantPersonalInfo).filter(ApplicantPersonalInfo.phone_number.like(f"%{value}%")).all()
    else:
        return json.dumps([])  # Invalid search value

    data = [record.__dict__ for record in records]
    for record in data:
        record.pop("_sa_instance_state", None)

    json_data = json.dumps(data)
    return json_data


@post("/add-resume")
async def add_data(request: Request, data : dict[str, Any]) -> json:
    """
    This function adds a new resume record to the database. It takes a JSON object containing the applicant's personal details,
    address information, education details, work experience, skills, project details, language proficiency, and social media links as input.
    It then creates the corresponding database records and commits the changes to the database.
    """

    applicant_details = ApplicantPersonalInfo(
        full_name = data["personalDetails"].get("full_name"),
        email = data["personalDetails"].get("email"),
        phone_number = data["personalDetails"].get("phone_number"),
        image_url = data["personalDetails"].get("image_url"),
        summary = data["personalDetails"].get("summary"),
    )
    # Add the applicant basic details details record to the database
    flag = False
    if applicant_details:
        session.add(applicant_details)
        session.commit()
        flag = True

    if flag:
        all_details = session.query(ApplicantPersonalInfo).all()
        records = [record.__dict__ for record in all_details]
        *_, applicant_rec = records

    applicant_address = ApplicantAddressInfo(
        applicant_id = applicant_rec["id"],
        address_line = data["addressDetails"].get("address_line"),
        street_name = data["addressDetails"].get("street_name"),
        city = data["addressDetails"].get("city"),
        state = data["addressDetails"].get("state"),
        country = data["addressDetails"].get("country"),
        zipcode = data["addressDetails"].get("zipcode"),
    )
    if applicant_address:
        session.add(applicant_address)

    if data["educationDetails"]:
        education_levels = len(data["educationDetails"])
        for item in range(education_levels):
            applicant_education = ApplicantEducationInfo(
                applicant_id = applicant_rec["id"],
                qualification = data["educationDetails"][item].get("qualification"),
                course_name = data["educationDetails"][item].get("course_name"),
                institute = data["educationDetails"][item].get("institute"),
                institute_location = data["educationDetails"][item].get("institute_location"),
                academic_start_date = data["educationDetails"][item].get("academic_start_date"),
                academic_end_date = data["educationDetails"][item].get("academic_end_date"),
            )
            # Add the applicant education details record to the database
            if applicant_education:
                session.add(applicant_education)

    if data["workExperienceDetails"]:
        experience_in_work = len(data["workExperienceDetails"])
        for item in range(experience_in_work):
            if(data["workExperienceDetails"][item].get("job_start_date") != "" and data["workExperienceDetails"][item].get("job_end_date") != ""):

                applicant_work_experience = ApplicantWorkExperienceInfo(
                    applicant_id = applicant_rec["id"],
                    job_title = data["workExperienceDetails"][item].get("job_title"),
                    organization = data["workExperienceDetails"][item].get("organization"),
                    key_roles = data["workExperienceDetails"][item].get("key_roles"),
                    job_location = data["workExperienceDetails"][item].get("job_location"),
                    job_start_date = data["workExperienceDetails"][item].get("job_start_date"),
                    job_end_date = data["workExperienceDetails"][item].get("job_end_date"),
                )
                if applicant_work_experience:
                    session.add(applicant_work_experience)
            else:
                applicant_work_experience = ApplicantWorkExperienceInfo(
                    applicant_id = applicant_rec["id"],
                    job_title = data["workExperienceDetails"][item].get("job_title"),
                    organization = data["workExperienceDetails"][item].get("organization"),
                    key_roles = data["workExperienceDetails"][item].get("key_roles"),
                    job_location = data["workExperienceDetails"][item].get("job_location")
                )
                if applicant_work_experience:
                    session.add(applicant_work_experience)

            
    if data["skillDetails"]:
        number_of_skills = len(data["skillDetails"])
        for item in range(number_of_skills):
            applicant_skills = ApplicantSkillsInfo(
                applicant_id = applicant_rec["id"],
                skill_name = data["skillDetails"][item].get("skill_name"),
                skill_level = data["skillDetails"][item].get("skill_level"),
            )
            if applicant_skills:
                session.add(applicant_skills)

    if data["projectDetails"]:
        number_of_projects = len(data["projectDetails"])
        for item in range(number_of_projects):
            applicant_projectdetails = ApplicantProjectDetailsInfo(
                applicant_id = applicant_rec["id"],
                project_name = data["projectDetails"][item].get("project_name"),
                skills_earned = data["projectDetails"][item].get("skills_earned"),
                project_description = data["projectDetails"][item].get("project_description"),
            )
            if applicant_projectdetails:
                session.add(applicant_projectdetails)

    if data["languageDetails"]:
        number_of_languages = len(data["languageDetails"])
        for item in range(number_of_languages):
            applicant_language = ApplicantLanguageInfo(
                applicant_id = applicant_rec["id"],
                language = data["languageDetails"][item].get("language"),
                proficiency = data["languageDetails"][item].get("proficiency"),
            )
            if applicant_language:
                session.add(applicant_language)

    if data["socialMediaDetails"]:
        number_of_socialmedia = len(data["socialMediaDetails"])
        for item in range(number_of_socialmedia):
            applicant_socialmedia = ApplicantSocialMediaInfo(
                applicant_id = applicant_rec["id"],
                network = data["socialMediaDetails"][item].get("network"),
                username = data["socialMediaDetails"][item].get("username"),
                url = data["socialMediaDetails"][item].get("url"),
            )
            if applicant_socialmedia:
                session.add(applicant_socialmedia)

    session.commit()
    session.close()
    send_form_creation_email(data)
    return data


@put("/update-resume/{applicant_id: int}")

async def update_data(applicant_id: int, data: dict[str, Any]) -> json:
    applicant_detail_record = session.query(ApplicantPersonalInfo).filter_by(id = applicant_id).first()
    
    if applicant_detail_record:
        record = applicant_detail_record
        applicant_data = data.get("personalDetails")
        record.full_name = applicant_data.get("full_name")
        record.email = applicant_data.get("email")
        record.phone_number = applicant_data.get("phone_number")
        record.image_url = applicant_data.get("image_url")
        record.summary = applicant_data.get("summary")
        session.add(record)

    address_detail_record = session.query(ApplicantAddressInfo).filter_by(applicant_id = applicant_id).first()
    if address_detail_record:
        record = address_detail_record
        address_data = data.get("addressDetails")
        record.address_line = address_data.get("address_line")
        record.street_name = address_data.get("street_name")
        record.city = address_data.get("city")
        record.state = address_data.get("state")
        record.country = address_data.get("country")
        record.zipcode = address_data.get("zipcode")
        session.add(address_detail_record)
    session.add(applicant_detail_record)

    education_detail_record = session.query(ApplicantEducationInfo).filter_by(applicant_id = applicant_id).all()
    if education_detail_record:
        item = 0
        for entry in education_detail_record:
            education_data = data.get("educationDetails")[item]
            entry.qualification = education_data.get("qualification")
            entry.course_name = education_data.get("course_name")
            entry.institute = education_data.get("institute")
            entry.institute_location = education_data.get("institute_location")
            entry.academic_start_date = education_data.get("academic_start_date")
            entry.academic_end_date = education_data.get("academic_end_date")
            session.add(entry)
            item += 1

    skills_record = session.query(ApplicantSkillsInfo).filter_by(applicant_id = applicant_id).all()
    if skills_record:
        item = 0
        for entry in skills_record:
            skills_data = data.get("skillDetails")[item]
            entry.skill_name = skills_data.get("skill_name")
            entry.skill_level = skills_data.get("skill_level")
            session.add(entry)
            item += 1

    projects_record = session.query(ApplicantProjectDetailsInfo).filter_by(applicant_id = applicant_id).all()
    if projects_record:
        item = 0
        for entry in projects_record:
            projects_data = data.get("projectDetails")[item]
            entry.project_name = projects_data.get("project_name")
            entry.skills_earned = projects_data.get("skills_earned")
            entry.project_description = projects_data.get("project_description")
            session.add(entry)
            item += 1


    social_media_record = session.query(ApplicantSocialMediaInfo).filter_by(applicant_id = applicant_id).all()
    if social_media_record:
        item = 0
        for entry in social_media_record:
            media_data = data.get("socialMediaDetails")[item]
            entry.network = media_data.get("network")
            entry.username = media_data.get("username")
            entry.url = media_data.get("url")
            session.add(entry)
            item += 1


    work_experience_record = session.query(ApplicantWorkExperienceInfo).filter_by(applicant_id = applicant_id).all()
    if work_experience_record:
        item = 0
        for entry in work_experience_record:
            work_data = data.get("workExperienceDetails")[item]
            print(work_data.get("job_start_date"))
            if(work_data.get("job_start_date") == "None" and work_data.get("job_end_date") == "None"):
                entry.job_title = work_data.get("job_title")
                entry.organization = work_data.get("organization")
                entry.key_roles = work_data.get("key_roles")
                entry.job_location = work_data.get("job_location")
               
                session.add(entry)
                item += 1
            else:
                entry.job_title = work_data.get("job_title")
                entry.organization = work_data.get("organization")
                entry.key_roles = work_data.get("key_roles")
                entry.job_location = work_data.get("job_location")
                entry.job_start_date = work_data.get("job_start_date")
                entry.job_end_date = work_data.get("job_end_date")
                session.add(entry)
                item += 1


    languages_record = session.query(ApplicantLanguageInfo).filter_by(applicant_id = applicant_id).all()
    if languages_record:
        item = 0
        for entry in languages_record:
            languages_data = data.get("languageDetails")[item]
            entry.language = languages_data.get("language")
            entry.proficiency = languages_data.get("proficiency")
            session.add(entry)
            item += 1

    session.commit()
    session.close()
    return json.dumps("updated")


@delete("/delete-resume/{applicant_id: int}")
async def delete_data(applicant_id: int) -> None:
    """
    This function deletes a resume record from the database based on the provided applicant ID.
    It takes an applicant ID as input and removes the corresponding record from the ApplicantPersonalInfo table.
    If the record exists, it deletes it and commits the changes to the database.
    """
    query = session.query(ApplicantPersonalInfo).filter_by(id = applicant_id).first()
    if query:
        session.delete(query)
        session.commit()
        session.close()
        return None


cors_config = CORSConfig(allow_origins=["*"])

# creates an app instance of the Litestar application
app = Litestar(
    # root handler
    [
        fetch_records,
        fetch_record_by_id,
        delete_data,
        update_data,
        fetch_data,
        add_data,
    ],
    cors_config = cors_config,
    debug = True,
)
