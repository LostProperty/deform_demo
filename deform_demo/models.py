from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
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


# TODO: move to it's own file utils
class ColanderModelMixin(object):

    def set_values(self, app_struct):
        """
        Used to update/add the values of the model
        """
        for key, value in app_struct.items():
            if isinstance(value, list) == False:
                setattr(self, key, value)


class Ingredient(Base, ColanderModelMixin):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    recipe_id = Column(Integer, ForeignKey('recipe.id'), nullable=False)
    quantity = Column(Float)


class Recipe(Base, ColanderModelMixin):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(Text) # TODO: force unique here colander or both?
    description = Column(String(2550))

    ingredients = relationship(Ingredient, backref='recipe', cascade='all,delete')
