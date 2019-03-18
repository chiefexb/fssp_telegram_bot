# init_db.py
from sqlalchemy import create_engine, MetaData

from settings import config
from models import user_session, fact


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[fact, user_session])

#def upgrade(migrate_engine):
#    meta = MetaData(bind=migrate_engine)
#    account = Table('account', meta, autoload=True)
#    emailc = Column('email', String(128))
#    emailc.create(account)


#def downgrade(migrate_engine):
#    meta = MetaData(bind=migrate_engine)
#    account = Table('account', meta, autoload=True)
#    account.c.email.drop()

# def sample_data(engine):
#    conn = engine.connect()
#    conn.execute(question.insert(), [
#        {'question_text': 'What\'s new?',
#         'pub_date': '2015-12-15 17:17:49.629+02'}
#    ])
#
#    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
   # sample_data(engine)
