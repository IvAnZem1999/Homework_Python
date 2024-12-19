import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import psycopg2
from sqlalchemy.orm.session import Session


DATABASE_URL = "postgresql://postgres:dfytr1977@localhost:5432/PostgreSQL_16"




engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Subject(Base):
    __tablename__ = "subjects" 
    subject_id = Column(Integer, primary_key=True, index=True)
    subject_title = Column(String)



def create_subject(session: Session, subject_id, subject_title):
    subject = Subject(subject_id=subject_id, subject_title=subject_title)
    session.add(subject)
    session.commit()
    return subject


def get_subject_by_id(session: Session, subject_id):
    subject = session.query(Subject).filter(Subject.subject_id == subject_id).first()
    return subject


def update_subject(session: Session, subject_id, new_subject_title):
    subject = session.query(Subject).filter(Subject.subject_id == subject_id).first()
    if subject:
        subject.subject_title = new_subject_title
        session.add(subject)
        session.commit()
        return subject
    else:
        return None


def delete_subject(session: Session, subject_id):
    subject = session.query(Subject).filter(Subject.subject_id == subject_id).first()
    if subject:
        session.delete(subject)
        session.commit()
        return True
    else:
        return False


@pytest.fixture
def session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.rollback()


def test_create_subject(session: Session):
    subject = create_subject(session, 1, "Биология") 
    assert subject.subject_title == "Биология"

def test_update_subject(session: Session):
    subject = create_subject(session, 2, "Химия")
    updated_subject = update_subject(session, subject.subject_id, "Физика")
    assert updated_subject.subject_title == "Физика"

def test_delete_subject(session: Session):
    subject = create_subject(session, 3, "Математика")
    success = delete_subject(session, subject.subject_id)
    assert success is True
    deleted_subject = get_subject_by_id(session, subject.subject_id)
    assert deleted_subject is None

