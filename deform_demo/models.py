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


# TODO: move to it's own file
class ColanderModelMixin(object):

    def set_values(self, app_struct):
        """
        Used to update/add the values of the model
        """
        for key, value in app_struct.items():
            # TODO: if it's a dict can we do some clever mapping and saving here?
            if isinstance(value, list) == False:
                try:
                    setattr(self, key, value)
                except:
                    import pdb; pdb.set_trace()


class Ingredient(Base, ColanderModelMixin):
    # TODO: check if we should be using plurals
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
