# Import all models so that Base has them registered before autogenerating migrations
from app.database.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.host import Host  # noqa
