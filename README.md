# Django 과제 - User와 Post 앱 개발  

## 📌 프로젝트 개요  
이 프로젝트는 Django 및 Django Rest Framework(DRF)에 익숙해지기 위한 개인 과제입니다.  
MTV 패턴을 기반으로 `User`와 `Post` 앱을 개발하며, 추가적으로 도전 과제를 통해 프로젝트를 확장할 수 있습니다.  

---

## ✅ 필수 과제  
### 1. User 앱  
- **사용자 모델 확장**: 기본 Django User 모델을 확장하여 `CustomUser` 구현 (프로필 이미지, 소개글 필드 추가).  
- **기능 구현**:
  1. **회원가입**  
      - 뷰: `signup` or `SignUpView`  
      - 템플릿: `user/signup.html`  
  2. **로그인**  
      - 뷰: `login` or `LoginView`  
      - 템플릿: `user/login.html`  
  3. **로그아웃**  
      - 뷰: `logout` or `LogoutView`  
  4. **프로필 페이지**  
      - 뷰: `user_profile` or `UserProfileView`  
      - 템플릿: `user/profile.html`  

### 2. Post 앱 (CRUD 기능)  
- **Post 모델**: 제목, 내용, 작성자, 작성일, 수정일 필드 구현.  
- **게시판 기능**:
  1. **게시글 목록 보기 (List)**  
      - 뷰: `post_list` or `PostListView`  
      - 템플릿: `post/post_list.html`  
  2. **게시글 상세 보기 (Detail)**  
      - 뷰: `post_detail` or `PostDetailView`  
      - 템플릿: `post/post_detail.html`  
  3. **게시글 작성 (Create)**  
      - 뷰: `post_create` or `PostCreateView`  
      - 템플릿: `post/post_form.html`  
  4. **게시글 수정 (Update)**  
      - 뷰: `post_update` or `PostUpdateView`  
      - 템플릿: `post/post_form.html`  
  5. **게시글 삭제 (Delete)**  
      - 뷰: `post_delete` or `PostDeleteView`  
      - 템플릿: `post/post_confirm_delete.html`  

---

## 🚀 도전 과제  
1. **DRF(Django Rest Framework)로 변환**  
    - User와 Post 앱 API 구현.  
    - Serializer 작성 (`UserSerializer`, `PostSerializer`).  
    - APIView를 사용한 CRUD 기능 구현 및 URL 라우팅 설정.  
2. **좋아요 기능**  
    - Post 모델에 좋아요 필드 추가 및 좋아요 개수 표시.  
3. **댓글 기능**  
    - Comment 모델 생성 및 CRUD 기능 구현.  
    - 게시글 상세 페이지에 댓글 목록 표시.  
4. **데이터베이스 변경**  
    - SQLite3에서 PostgreSQL 또는 MySQL로 마이그레이션.  

---

## ⚙️ 기술 스택 및 설정  
- **프레임워크**: Django  
- **템플릿 엔진**: Django Template  
- **데이터베이스**: SQLite3  
- **추가 라이브러리**: Django Rest Framework (도전 과제 시 사용).  

---

## 📂 프로젝트 구조  

project/  
 ├── user/  
 │ ├── templates/user/  
 │ │ ├── signup.html  
 │ │ ├── login.html  
 │ │ └── profile.html  
 │ ├── views.py  
 │ ├── models.py  
 │ └── ...   
 ├── post/  
 │ ├── templates/post/  
 │ │ ├── post_list.html  
 │ │ ├── post_detail.html  
 │ │ ├── post_form.html  
 │ │ └── post_confirm_delete.html  
 │ ├── views.py  
 │ ├── models.py  
 │ └── ...   
 ├── templates/   
 │ ├── base.html   
 │ ├── navbar.html   
 │ └── footer.html   
 └── ...  

---

## 🗂️ Git 커밋 및 브랜치 관리  
1. **커밋**: 각 기능별로 세부적인 커밋 메시지를 작성하세요.  
   - 예: `feat(user): 회원가입 기능 추가`  
2. **브랜치**: 각 기능별 브랜치를 생성하여 개발 후 `main` 브랜치에 병합하세요.  
   - 예: `feature/user-signup`  

---

## ⏰ 제출  
- **마감 기한**: 2024년 1월 23일 목요일 14:00:00  
- **제출 방법**: GitHub Repository URL 제출  
- [제출 페이지](https://nbcamp.spartacodingclub.kr/mypage/assignments) 참고.  

---

## 📝 트러블슈팅  
- 프로젝트 진행 중 발생했던 문제와 해결 과정을 여기에 기록하세요.  
  - 예: "회원가입 시 비밀번호 검증 오류 발생 → Custom Validator 추가로 해결".  

---

## 📊 평가 기준  
1. 코드 구조 및 가독성  
2. MTV 패턴 준수 여부  
3. 구현 기능의 정확성  
4. 에러 처리 방식  
5. 코드 재사용성  
6. RESTful API 설계 원칙 준수 (DRF 도전 과제 시)  
