# -*- coding: utf-8 -*-
from pip._vendor.distlib.util import cached_property
from sqlalchemy import Column, String, Integer, desc
from sqlalchemy.ext.declarative import declarative_base
from module.db.base import DBBaseMixin, CreateUpdateMixin
from utils.tls_property import cached_tls

Base = declarative_base()


class Site(DBBaseMixin, CreateUpdateMixin, Base):
    name = Column('name', String(50))
    short_name = Column('short_name', String(20))
    title = Column('title', String(10), index=True)
    url = Column('url', String(200))
    background_image_count = Column('background_image_count', Integer)
    ad_type = Column('ad_type', Integer, default=None, nullable=True)

    @classmethod
    @cached_tls
    def get(cls, pk):
        """
        :param pk: int
        :rtype: cls
        """
        return cls.objects().get(pk)

    @classmethod
    @cached_tls
    def get_all(cls):
        return cls.objects().filter().order_by(desc(cls.id)).all()

    @classmethod
    @cached_tls
    def get_title(cls, title):
        """
        :param title: int
        :rtype: cls
        """
        return cls.objects().filter(cls.title==title)[0]

    @cached_property
    def top_image_path(self):
        """
        /static/img/site/{title}/top.jpg
        :return:str
        """
        return '/static/img/site/{}/top.jpg'.format(self.title)

    @property
    def subjects_url(self):
        """
        http://anago.2ch.sc/applism/subject.txt
        :return:str
        """
        return '{}subject.txt'.format(self.url)

    @property
    def title_suffix(self):
        """
        - xxxx速報(肉)
        """
        return ' - {}'.format(self.name)

    @property
    def update_at(self):
        from module.site.page import Page
        import datetime
        import pytz
        pages = Page.get_new_history(self.id)
        new_list = sorted(pages, key=lambda x: x.id, reverse=True)
        now = datetime.datetime.now(pytz.utc)
        for page in new_list:
            if page.is_enable(now):
                return page.open_at
        raise ValueError

    def get_background_image_id(self, _id):
        return 1 + _id % self.background_image_count
