from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from homework_20.declarative_base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship(
        "Course", secondary="student_course_association", back_populates="students"
    )
