from django.contrib import admin
from .models import User
from .models import Movie
from .models import Rating

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Rating)
