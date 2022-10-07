from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'view_count']
        labels = {
        'title' : '리뷰 제목',
        'content' : '리뷰 내용',
        'movie_name' : '영화 제목',
        'grade' : '평점(0~10)',
        }