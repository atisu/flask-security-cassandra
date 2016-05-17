from flask.ext.security import UserMixin
from cqlengine import columns
from cqlengine.models import Model
import uuid

class Users(Model, UserMixin):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    role_id = columns.UUID()
    address_id = columns.UUID()
    name = columns.Text()
    phone_num = columns.Text()
    email = columns.Text(index=True)
    password = columns.Text()
    confirmed_at = columns.DateTime()
    roles = columns.Set(columns.UUID)
    active = columns.Boolean()

