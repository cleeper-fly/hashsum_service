from sqlmodel import create_engine, SQLModel, Session

from app.apps.file_hash.models import *
from app.core.config import get_settings

settings = get_settings()


engine = create_engine(settings.DB_URL)


CHECK_TABLE_EXISTS_STATEMENT = "SELECT EXISTS ( " \
                               "SELECT from information_schema.tables WHERE table_schema = 'public' " \
                               "AND table_name = 'result');"


def check_table_exists_and_create():
    with Session(engine) as session:
        query_result = session.exec(CHECK_TABLE_EXISTS_STATEMENT)
        if not query_result.one()[0]:
            SQLModel.metadata.create_all(engine)

