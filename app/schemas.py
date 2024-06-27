from pydantic import BaseModel
from typing import Optional
from datetime import time
from enum import Enum

class SemesterEnum(str, Enum):
    fall_2022 = 'Fall 2022'
    spring_2023 = 'Spring 2023'
    fall_2023 = 'Fall 2023'
    spring_2024 = 'Spring 2024'

class StudentCreate(BaseModel):
    name: str
    email: str
    phone: int
    address: str
    profile_picture: str

class GradeCreate(BaseModel):
    student_id: int
    subject_id: int
    grade: float
    semester: SemesterEnum

class GroupCreate(BaseModel):
    name: str
    section: str
    teacher_id: int

class SubjectCreate(BaseModel):
    name: str
    code: str

class TeacherCreate(BaseModel):
    name: str
    email: str
    phone: int
    address: str
    profile_picture: str

class TimetableCreate(BaseModel):
    group_id: int
    weekday: str
    period: time
    subject_id: int
