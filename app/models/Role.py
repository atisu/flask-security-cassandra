from flask.ext.security import RoleMixin
from cqlengine import columns
from cqlengine.models import Model
import uuid

class Role(Model, RoleMixin):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text()
    description = columns.Text()

