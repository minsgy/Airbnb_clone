# 🥇AirBnb Clone project  
  
## 💪Project Informations
+ 해당 프로젝트는 NomadCoder에서 제공하는 **에어비엔비 클론 강의** 입니다.  
+ 백 엔드와 프론트 엔드를 둘다 접할 수 있는 **풀스택 과정**입니다.  
+ CRUD, UI/UX, AWS EB 배포 등 많은 기술을 접할 수 있는 Clone Project 입니다.  


## ⚙ Installation   
+ 🛠 Django release: 2.2.5 
+ 🛠 Python 3.8.4    
+ 🛠 HTML5, CSS3  
+ 🎨TailWind  

## ☹ 이 프로젝트를 사용하기 위한 과정 
1. pipenv 설치
```python
pip install pipenv
```
2. 가상환경 생성
```python
pipenv --three # python3 을 사용할 수 있는 가상 환경 생성
pipenv shell # 가상 환경 활성화
```
3. Django Project 시작
```python
django-admin startproject projectname . 
# 이 방식은 협업에 좋은 구조화 방식을 만듬. 불필요한 폴더 생성X 
```

4. django app 생성
```python
django-admin startapp appname 
# pip와 달리 django-admin 을 통해 생성함.
```  