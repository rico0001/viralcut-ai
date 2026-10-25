from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services.api.db.models import User, Project, Job, Clip, Media

DATABASE_URL = "postgresql://user:password@localhost/dbname"

def seed_database():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Seed Users
    user1 = User(username='user1', email='user1@example.com', password='hashed_password1')
    user2 = User(username='user2', email='user2@example.com', password='hashed_password2')
    
    session.add(user1)
    session.add(user2)

    # Seed Projects
    project1 = Project(name='Project 1', user_id=user1.id)
    project2 = Project(name='Project 2', user_id=user2.id)

    session.add(project1)
    session.add(project2)

    # Seed Jobs
    job1 = Job(name='Job 1', project_id=project1.id)
    job2 = Job(name='Job 2', project_id=project2.id)

    session.add(job1)
    session.add(job2)

    # Seed Clips
    clip1 = Clip(title='Clip 1', job_id=job1.id)
    clip2 = Clip(title='Clip 2', job_id=job2.id)

    session.add(clip1)
    session.add(clip2)

    # Seed Media
    media1 = Media(file_path='path/to/media1.mp4', clip_id=clip1.id)
    media2 = Media(file_path='path/to/media2.mp4', clip_id=clip2.id)

    session.add(media1)
    session.add(media2)

    session.commit()
    session.close()

if __name__ == "__main__":
    seed_database()