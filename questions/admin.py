from django.contrib import admin
from .models import Question
from reversion.admin import VersionAdmin

@admin.register(Question)
class QuestionModelAdmin(VersionAdmin):
      pass
