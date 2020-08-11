from config import dsn
from flask_sqlalchemy import SQLAlchemy

class DBworker:
    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = dsn
        db = SQLAlchemy(app)
        self.db = db

        person_to_url = db.Table('personal_to_urls',
                                            db.Column('url_id', db.Integer, db.ForeignKey('urls.id')),
                                            db.Column('personal_id', db.Integer, db.ForeignKey('personal.id'))
                                            )

        self.Personal = type(
                    'Personal', 
                    (db.Model,),
                    {
                       "id":db.Column(db.Integer, primary_key=True),
                       "type":db.Column(db.String),
                       "data":db.Column(db.String),
                       "url_list":db.relationship('Urls', secondary=person_to_url, lazy='subquery',
                                                   backref=db.backref('personal', lazy=True))
                    }
                )

        self.Urls = type('Urls',(db.Model,),
            {
                "id": db.Column(db.Integer, primary_key=True),
                "url": db.Column(db.String)
            })


    def save_to_db(self, result, url):
        Urls = self.Urls
        Personal = self.Personal
        if result:
            if not Urls.query.filter_by(url=url).first():
                urls_db = Urls(url=url)
                self.db.session.add(urls_db)
                self.db.session.commit()
            else:
                urls_db = Urls.query.filter_by(url=url).first()
        for key, value in result.items():
            pers = Personal.query.filter_by(type=value, data=key).first()
            if not pers:
                pers = Personal(type=value, data=key)
                pers.url_list.append(urls_db)
                self.db.session.add(pers)
                self.db.session.commit()
            else:
                if urls_db not in pers.url_list:
                    pers.url_list.append(urls_db)
                    self.db.session.add(pers)
                    self.db.session.commit()


        



