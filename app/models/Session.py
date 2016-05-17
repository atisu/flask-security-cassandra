from cqlengine import columns
from cqlengine.models import Model
import uuid

class Session(Model):
    sid = columns.UUID(primary_key=True, default=uuid.uuid4)
    data = columns.Text()
    expiration = columns.DateTime()

