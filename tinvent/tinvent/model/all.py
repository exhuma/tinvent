# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from tinvent.model import DeclarativeBase, metadata, DBSession, User
category = Table( 'category', metadata,
      Column( 'category_id', Integer, nullable=False, primary_key=True ),
      Column( 'label', Unicode(32) )
      )

contact = Table( 'contact', metadata,
      Column( 'user_id', Integer, ForeignKey('tg_user.user_id',
         onupdate="CASCADE", ondelete="CASCADE")),
      Column( 'label', Unicode(64), nullable=False ),
      Column( 'other_user_id', Integer, ForeignKey('tg_user.user_id',
         onupdate="CASCADE", ondelete="SET NULL"), default=None),
      PrimaryKeyConstraint( 'user_id', 'label' )
)

picture = Table( 'picture', metadata,
      Column( 'picture_id', Integer, primary_key=True ),
      Column( 'mime_type', String(24), default="application/octet-stream" ),
      Column( 'filename', Unicode(255), nullable=False ),
      Column( 'md5', String(32), default="" ),
      Column( 'data', Binary, default="" )
      )

item = Table( 'item', metadata,
      Column( 'item_id', Integer, nullable=False, primary_key=True ),
      Column( 'label', Unicode(64) ),
      Column( 'barcode', String(64) ),
      Column( 'comment', UnicodeText() ),
      Column( 'category_id', Integer, ForeignKey('category.category_id',
         onupdate="CASCADE", ondelete="SET NULL"), default=None),
      Column( 'owner_id', Integer, ForeignKey('tg_user.user_id',
         onupdate="CASCADE", ondelete="CASCADE"), nullable=False),
      Column( 'holder_id', Integer, ForeignKey('tg_user.user_id',
         onupdate="CASCADE", ondelete="SET NULL"), nullable=True),
      Column( 'picture_id', Integer, ForeignKey( 'picture.picture_id',
         ondelete='CASCADE', onupdate='CASCADE'), default=None )
      )

class Category(object):
   pass

class Contact(object):
   pass

class Picture(object):
   pass

class Item(object):
   pass

mapper( Category, category )
mapper( Contact, contact )
mapper( Picture, picture )
mapper( Item, item, properties={
   #'category': relation( Category, backref='items' ),
   #'picture': relation( Picture, uselist=False, backref='item', lazy=True ),
   'owner': relation( User, backref='owned_items', primaryjoin=item.c.owner_id==User.user_id ),
   'user': relation( User, backref='all_items', primaryjoin=or_(
         item.c.owner_id==User.user_id,
         item.c.holder_id==User.user_id
      ))
   } )
