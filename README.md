# 장고 프로젝트

팀 : 잘했조

프로젝트 명 : saw well

팀원 : 강민성, 김진우, 노현진, 이채림

## 역할

팀장: 김진우: SQL 및 데이터 분석 및 django 

팀원: 이채림: reivew orm 구축 및 review page 구현

노현진: login orm 구축 및 login page 구현

강민성: html readable Code 및 데이터 조사

## 프로젝트 정보 

### 1.프로젝트 주제

서울 음식점 추천 사이트

### 프로젝트 목적 

음식점 결정시간을 최소화하기 위한 추천 서비스 시스템 구축

### 2.프로젝트 배경

음식점 결정시간을 최소화하기 위한 추천 서비스 시스템 구축

### 3. 프로젝트 개요

가게 선택후 후기와 별점을 남길 수 있고, 음식 추천 서비스을 이용해 음식 메뉴를 고를 수도 있습니다.

### 4. 프로젝트 환경 및 사용된 툴


| 개발 도구 | 데이터베이스 | 협업 도구                      | 
| --------- | ------------ | ---------------------------  |
|  pycharm  | MariaDB      | Zoom  & Github & google docs |

## 5. 일정

### 사전 기획

3.2 ~ 3.4 : 주제 선정 및 일정 수립, 기획서 작성, 데이터 수집과 잔처리

3.7 : 프로젝트 주제 및 아이디어 발표

### 개발

3.3 ~ 3.7 : 데이터 분석 및 sql, 데이터 시각화 및 django 업로드

3.6 ~ 3.16 : Login Page 완료, Ceo Page 완료, Market Page 완료, Review page 완료

## 수정 및 보안

3.17 ~ 3.18 : 프로젝트 고도화 및 보고서 및 ppt 작성

### 목차

1. Database 구조, 크롤링, 템플릿 분할

2. Login Page(cust, ceo) 구조 및 프로세스

3. Main Page(category, popular, search, chart)

4. Sub Page (markets, menu, review & reply)

## 기획

<img width="%100" alt='contribute' src='https://user-images.githubusercontent.com/73889507/156279545-b7737c3b-ecc1-41e3-9d18-0626b5139e5e.jpg'>

### ERD

<img width="%100" alt='erd' src='https://user-images.githubusercontent.com/73889507/159135823-3fd2d2cf-c9c9-4bb9-9406-9795dcc707c0.png'>

### 주요화면 기획

bootstrampmade.com 템플릿을 이용 (https://bootstrapmade.com/demo/Tempo)

<img width="%100" alt='erd' src='https://user-images.githubusercontent.com/73889507/157559811-f0419800-8c63-4c13-b098-573d9b099077.png'>

## 코드 컨베이션

### 1. Code lay-out

#### 인덴트(Indent): 공백으로 4칸 들여쓰기

인덴트가 권장사항인 다른 언어들에 비해 파이썬에게 인덴트는 지켜야만 하는 대표적인 특징이라고 할 수 있다.

PEP8에서는 공백 4칸으로 들여쓰기 하는 것을 원칙으로 하고 있으며 탭 사용은 이미 탭으로 들여쓰기 된 코드와 일관성 유지를 위해서만 사용하는 것을 권장한다.

#### Blank Lines: 함수 및 클래스 정의 위에는 빈 2줄

두개의 빈 줄로 함수 및 클래스 정의를 구분한다. 또한 클래스 내의 메소드 정의에는 1줄씩 빈 줄을 넣어 쓴다.

### 2. Whitespace in Expressions and Statements

#### 불필요한 공백 넣지 않기

대괄호[], 소괄호() 안

쉼표(,), 쌍점(:)과 쌍반점(;) 앞

### 3. Comments

#### 코드와 맞지 않는 주석 없도록 하기

코드 내용과 달라 내용이 맞지 않는 주석은 헷갈리지않도록 항상 최신의 코드내용 상태로 유지하도록 한다.

#### 불필요한 주석 달지 않기

가독성을 오히려 떨어트린다.

#### 명령문과 같은줄에 있는 인라인 주석은 많지 않도록 하기

명백한 내용을 적음으로써 더 가독성을 떨어트린다. 하지만 이해력과 가독성을 높여줄 수도 있음으로 남발하지 않도록 한다.

### 4. Naming Conventions

#### 피해야 하는 이름

'l'(소문자), 'O'(대문자) 또는 'I'(대문자) 문자를 단일 문자 변수 이름으로 사용하지 않도록 한다.(숫자 1, 0과 구별하기가 어렵기 때문)

#### 이름 정하기

모듈 명은 짧은 소문자로

클래스 명은 카멜케이스(CamelCase)로 작성

함수명은 소문자로

인스턴스 메소드의 첫 번째 인수는 항상 self

클래스 메소드의 첫 번째 인수는 항상 cls

상수(Constant)는 모듈 단위에서만 정의, 스네이크케이스(Snake Case)로 작성
