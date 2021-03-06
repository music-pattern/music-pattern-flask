""" scale """
from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from models.utils import Model, Wrapper


class Scale(Wrapper,
            Model):

    combinationIndex = Column(BigInteger())

    harmonyId = Column(BigInteger,
                       ForeignKey("harmony.id"),
                       nullable=True)

    harmony = relationship('Harmony',
                           foreign_keys=[harmonyId],
                           backref='scales')

    name = Column(String(30))

    size = Column(BigInteger())

    tags = Column(ARRAY(String(220)),
                  nullable=False,
                  default=[])
