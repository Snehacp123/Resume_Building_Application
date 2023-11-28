from sqlalchemy import String, Column, Date, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from database import engine

# base class from which all mapped classes should inherit.
Base = declarative_base()


# create model for applicants details
class ApplicantPersonalInfo(Base):
    __tablename__ = "applicant_details"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    phone_number = Column(String(13), nullable=False)
    image_url = Column(String(300), nullable=True)
    summary = Column(String(1000), nullable=False)


# create model for address details
class ApplicantAddressInfo(Base):
    __tablename__ = "applicant_address"

    id = Column(Integer, primary_key=True)
    applicant_id = Column(Integer, ForeignKey("applicant_details.id", ondelete="CASCADE"))
    address_line = Column(String(500), nullable=False)
    street_name = Column(String(200), nullable=False)
    city = Column(String(200), nullable=False)
    state = Column(String(200), nullable=False)
    country = Column(String(200), nullable=False)
    zipcode = Column(String(200), nullable=False)
	# relationship between parent child class
    applicant = relationship(
        "ApplicantPersonalInfo",
        backref=backref("applicant_address", passive_deletes=True),
    )

# create model for education details
class ApplicantEducationInfo(Base):
    __tablename__ = "applicant_education"

    id = Column(Integer, primary_key=True)
    applicant_id = Column(Integer, ForeignKey("applicant_details.id", ondelete="CASCADE"))
    qualification = Column(String(200), nullable=False)
    course_name = Column(String(200), nullable=False)
    institute = Column(String(200), nullable=False)
    institute_location = Column(String(200), nullable=False)
    academic_start_date = Column(Date, nullable=False)
    academic_end_date = Column(Date, nullable=False)
    # relationship between parent child class
    applicant = relationship(
        "ApplicantPersonalInfo",
        backref=backref("applicant_education", passive_deletes=True),
    )

# create model for work experience details
class ApplicantWorkExperienceInfo(Base):
    __tablename__ = "applicant_work_experience"

    id = Column(Integer, primary_key=True)
    applicant_id = Column(Integer, ForeignKey("applicant_details.id", ondelete="CASCADE"))
    job_title = Column(String(200), nullable=True)
    organization = Column(String(200), nullable=True)
    key_roles = Column(String(200), nullable=True)
    job_location = Column(String(200), nullable=True)
    job_start_date = Column(Date, nullable=True)
    job_end_date = Column(Date, nullable=True)
    # relationship between parent child class
    applicant = relationship(
        "ApplicantPersonalInfo",
        backref=backref("applicant_work_experience", passive_deletes=True),
    )

# create model for skills details
class ApplicantSkillsInfo(Base):
    __tablename__ = "applicant_skills"

    id = Column(Integer, primary_key=True)
    applicant_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    skill_name = Column(String(200), nullable=True)
    skill_level = Column(String(200), nullable=True)
    # relationship between parent child class
    applicant = relationship(
        "ApplicantPersonalInfo",
        backref=backref("applicant_skills", passive_deletes=True),
    )

# create model for socialmedia details
class ApplicantSocialMediaInfo(Base):
    __tablename__ = "applicant_socialmedia"

    id = Column(Integer, primary_key=True)
    applicant_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    network = Column(String(200), nullable=True)
    username = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    # relationship between parent child class
    applicant = relationship(
        "ApplicantPersonalInfo",
        backref=backref("applicant_socialmedia", passive_deletes=True),
    )

# create model for language details
class ApplicantLanguageInfo(Base):
    __tablename__ = "applicant_language"

    id = Column(Integer, primary_key=True)
    applicant_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    language = Column(String(200), nullable=True)
    proficiency = Column(String(200), nullable=True)
    # relationship between parent child class
    applicant = relationship(
        "ApplicantPersonalInfo",
        backref=backref("applicant_language", passive_deletes=True),
    )

# create model for project details
class ApplicantProjectDetailsInfo(Base):
    __tablename__ = "applicant_projectdetails"

    id = Column(Integer, primary_key=True)
    applicant_id = Column(
        Integer, ForeignKey("applicant_details.id", ondelete="CASCADE")
    )
    project_name = Column(String(200), nullable=True)
    skills_earned = Column(String(200), nullable=True)
    project_description = Column(String(700), nullable=True)
    # relationship between parent child class
    applicant = relationship(
        "ApplicantPersonalInfo",
        backref=backref("applicant_projectdetails", passive_deletes=True),
    )

# Create the tables in the database
Base.metadata.create_all(bind=engine, checkfirst=True)
