from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    #Index,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Ingredient(Base):
    # TODO: check if we should be using plurals
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    recipe_id = Column(Integer, ForeignKey('recipe.id'), nullable=False)
    quantity = Column(Float)


class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(Text) # TODO: force unique here colander or both?
    description = Column(String(2550))

    ingredients = relationship(Ingredient, backref='recipe', cascade='all,delete')

#Index('my_index', MyModel.name, unique=True, mysql_length=255)
