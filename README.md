# 장고 프로젝트

## 목차

1. 프로젝트 배경

2. 프로젝트 팀 구성 및 역할

3. 프로젝트 수행절차 및 방법

4. 프로젝트 수행 결과

## 1. 프로젝트 배경

주제 : 서초구 음식점 추천 사이트(소비자가 음식점을 고르는데에 도움을 주기위한 사이트)

목적 : 음식점 결정시간을  최소화하기 위한 추천 서비스 시스템 구축

개요 : request - django - MariaDB

<img width="%100" alt='contribute' src='https://user-images.githubusercontent.com/73889507/156279545-b7737c3b-ecc1-41e3-9d18-0626b5139e5e.jpg'>

구축된 DB와 함께 연결하여 파이썬 애니웨어를 통하여 웹상에 배포됩니다.

배포 주소 : https://sawwell.pythonanywhere.com/

구조 

: 로그인-일반회원 로그인/ceo로그인, 마이페이지, 개인정보 업데이트, 계정삭제

: 카테고리-음식점리스트-음식점 정보/메뉴-리뷰 달기

기대효과 : 저장된 DB와 UI를 통해 음식점의 정보를 얻어 결정에 도움을 줄 수 있다.

## 역할

팀 : 잘했조

프로젝트 명 : saw well

팀장: SQL 및 데이터분석 및 django orm 및 전체적 설계 

팀원: 이채림: reivew orm 구축 및 review page 구현

노현진: login orm 구축 및 login page 구현

강민성: html readable Code 및 데이터 조사

## 코드 컨베이션

## 파이썬 코딩 스타일 가이드를 참고해서 

## 1. Code lay-out

- 인덴트(Indent): 공백으로 4칸 들여쓰기

인덴트가 권장사항인 다른 언어들에 비해 파이썬에게 인덴트는 지켜야만 하는 대표적인 특징이라고 할 수 있다.

PEP8에서는 공백 4칸으로 들여쓰기 하는 것을 원칙으로 하고 있으며 탭 사용은 이미 탭으로 들여쓰기 된 코드와 일관성 유지를 위해서만 사용하는 것을 권장한다.

- Blank Lines: 함수 및 클래스 정의 위에는 빈 2줄

두개의 빈 줄로 함수 및 클래스 정의를 구분한다. 또한 클래스 내의 메소드 정의에는 1줄씩 빈 줄을 넣어 쓴다.

## 2. Whitespace in Expressions and Statements

- 불필요한 공백 넣지 않기

대괄호[], 소괄호() 안

쉼표(,), 쌍점(:)과 쌍반점(;) 앞

## 3. Comments

- 코드와 맞지 않는 주석 없도록 하기

코드 내용과 달라 내용이 맞지 않는 주석은 헷갈리지않도록 항상 최신의 코드내용 상태로 유지하도록 한다.

- 불필요한 주석 달지 않기

가독성을 오히려 떨어트린다.

- 명령문과 같은줄에 있는 인라인 주석은 많지 않도록 하기

명백한 내용을 적음으로써 더 가독성을 떨어트린다. 하지만 이해력과 가독성을 높여줄 수도 있음으로 남발하지 않도록 한다.

## 4. Naming Conventions

- 피해야 하는 이름

'l'(소문자), 'O'(대문자) 또는 'I'(대문자) 문자를 단일 문자 변수 이름으로 사용하지 않도록 한다.(숫자 1, 0과 구별하기가 어렵기 때문)

- 이름 정하기

모듈 명은 짧은 소문자로

클래스 명은 카멜케이스(CamelCase)로 작성

함수명은 소문자로

인스턴스 메소드의 첫 번째 인수는 항상 self

클래스 메소드의 첫 번째 인수는 항상 cls

상수(Constant)는 모듈 단위에서만 정의, 스네이크케이스(Snake Case)로 작성


### 4. 프로젝트 환경 및 사용된 툴


| 개발 도구 | 데이터베이스 | 협업 도구       |
| --------- | ------------ | -------------- |
|  pycharm  | MariaDB      | Zoom  & Github |

### 일정

3/2~ 3/2: 주제 선정 및 일정 수립

3/3 ~ 3/4: 데이터 수집과 전처리

3/3 ~ 3/5: 데이터 분석 및 SQL(mariadb)

3/5 ~ 3/6: 데이터 시각화 및 Django 업로드

3/6 ~ 3/7 : login page 완료

3/7 ~ 3/10 : marmaket page 완료

3/10 ~ 3/16 : review page 완료

3/17 ~ 3/18 : 프로젝트 고도화 및 보고서 & ppt 작성

3/18: 최종 마무리 및 발표

## 프로젝트 수행 결과 목차

1.  Database 구조, 크롤링, 템플릿 분할

2. Login Page(cust, ceo) 구조 및 프로세스

3. Main Page(category,popular,search,chart)

4. Sub Page (markets, menu, review & reply)

## 1.  Database 구조

Register를 통해 회원 등록시 회원 레코드 생성

회원정보와 가게정보를 받아 리뷰 작성

<img width="%100" alt='erd' src='https://user-images.githubusercontent.com/73889507/159175770-fd478540-0dea-4e16-8a6d-0ab1318ee529.png'>

## 2. Data 크롤링

가계 대표 이미지를 크롤링(가게 이미지라 맞지 않은것은 직접 수정)

<img width="%100" alt='crawing2' src='https://user-images.githubusercontent.com/73889507/159176383-6fd1ba9d-0e15-42aa-8884-0f1417ff8216.gif'>

## 3. 데이터 등록 마켓 갯수와 동일한 test 쿼리 만들기

데이터 등록 마켓 갯수와 동일한 test 쿼리 만들기

<img width="%100" alt='test' src='https://user-images.githubusercontent.com/73889507/159176490-c18cb5ae-fb2f-484a-9f6c-8bb46bd0a86a.png'>

## 4. csv 데이터

csv 데이터 Hide sql에서 데이터 저장

<img width="%100" alt='crawing2' src='https://user-images.githubusercontent.com/73889507/159176551-82333ea0-71d4-480f-95c4-661c4ba99ac2.png'>












