## 10월 7일, Django를 활용하여 개발한 영화리뷰게시판입니다.



## 목표

- ModelForm 활용 CRUD 구현
- Staticfiles 활용 서비스 로고 표시

## 요구 사항

### 모델 Model

- 모델 이름 : Movie

  모델 필드

  | 이름       | 역할          | 필드     | 속성                                                         |
  | ---------- | ------------- | -------- | ------------------------------------------------------------ |
  | title      | 리뷰 제목     | Char     | max_length=20                                                |
  | content    | 리뷰 내용     | Text     |                                                              |
  | movie_name | 영화 이름     | Char     | max_length=20                                                |
  | grade      | 영화 평점     | Integer  | default=10,validators=[MinValueValidator(0),MaxValueValidator(10)] |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True                                            |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True                                              |
  | view_count | 리뷰 조회 수  | Integer  | default=0                                                    |

---

### 기능 View

생성 및 수정은 ModelForm을 사용하여 구현.

- 데이터 목록 조회

  - `GET` http://127.0.0.1:8000/reviews/

- 데이터 정보 조회

  - `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/

- 데이터 생성

  - `POST` http://127.0.0.1:8000/reviews/create/

  - 사용자에게 받을 데이터
    - 리뷰 제목(title)
    - 리뷰 내용(content)
    - 영화 이름(movie_name)
    - 영화 평점(grade)

- 데이터 수정

  - `POST` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/update/

- 데이터 삭제

  - `POST` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/delete/

---

### 화면 Template

**네비게이션바, Bootstrap <nav>**

- 서비스 로고
  - Django Staticfiles 활용
  - 클릭 시 메인 페이지로 이동
- 리뷰 목록 버튼
  - 클릭 시 목록 페이지로 이동
- 리뷰 작성 버튼
  - 클릭 시 작성 페이지로 이동

**메인 페이지**

- `GET` http://127.0.0.1:8000/reviews/
- 자유 디자인

목록 페이지

- `GET` http://127.0.0.1:8000/reviews/index/

- 리뷰 목록 출력

  - 리뷰 제목
  - 영화 이름

- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

- 리뷰 조회 수 구현(view_count)

  ~~~python
  # views.py
  def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    cnt = movie.view_count	# pk로 선택한 movie객체의 view_point값을 변수에 할당
    cnt += 1					# 1증가
    movie.view_count = cnt	# 증가한 값 다시 재할당
    movie.save()				# 저장 후 context로 전달
    context={
      'movie':movie,
    }
    return render(request, 'movies/detail.html', context)
  ~~~

  

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/
- 해당 리뷰 정보 출력
- 수정 / 삭제 버튼
  - 삭제 버튼 클릭 시 Bootstrap Modal 기능을 활용하여 사용자에게 다시 한 번 삭제 의사를 묻도록 구현.

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/update/
- 리뷰 수정 폼