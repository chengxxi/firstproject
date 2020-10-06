from django.contrib import admin
from .models import Choice, Question

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # 개별 필드를 표시하기 위한 튜플 (객체의 변경 목록 페이지에서 열로 표시됨)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Question 변경 목록 페이지에 개선점 추가
    list_filter = ['pub_date']
    # 검색 기능 추가
    search_fields = ['question_text']
    

admin.site.register(Question, QuestionAdmin)