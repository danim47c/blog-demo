from django.db.models.base import ModelBase
from django.contrib import admin


from . import models

for name, model in models.__dict__.items():
    if issubclass(type(model), ModelBase):
        admin.site.register(model)
