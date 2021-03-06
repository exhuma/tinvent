from sqlalchemy import *
import tinvent.model
from migrate import *
from migrate.changeset import *
meta = MetaData(migrate_engine)

tg_user = Table('tg_user', meta,
 Column('user_id', Integer(), primary_key=True, nullable=False),
 Column('user_name', Unicode(length=16), nullable=False),
 Column('email_address', Unicode(length=255), nullable=False),
 Column('display_name', Unicode(length=255)),
 Column('password', Unicode(length=80)),
 Column('created', DateTime(timezone=False)),
)

category = Table( 'category', meta,
      Column( 'category_id', Integer, nullable=False, primary_key=True ),
      Column( 'label', Unicode(32) )
      )

contact = Table( 'contact', meta,
      Column( 'user_id', Integer, ForeignKey('tg_user.user_id',
         onupdate="CASCADE", ondelete="CASCADE")),
      Column( 'label', Unicode(64), nullable=False ),
      Column( 'other_user_id', Integer, ForeignKey('tg_user.user_id',
         onupdate="CASCADE", ondelete="SET NULL"), default=None),
      PrimaryKeyConstraint( 'user_id', 'label' )
)

picture = Table( 'picture', meta,
      Column( 'picture_id', Integer, primary_key=True ),
      Column( 'mime_type', String(24), default="application/octet-stream" ),
      Column( 'filename', Unicode(255), nullable=False ),
      Column( 'md5', String(32), default="" ),
      Column( 'data', Binary, default="" )
      )

item = Table( 'item', meta,
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

def upgrade():
   picture.create()
   category.create()
   contact.create()
   item.create()

def downgrade():
   item.drop()
   contact.drop()
   category.drop()
   picture.drop()

