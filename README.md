
# REST-API

![alt text](https://static.codingforentrepreneurs.com/media/cfe-blog/rest-api-basics-with-the-django-rest-framework/rest_api_basics_logo.jpg)

REST is a loosely defined protocol for listing, creating, changing, and deleting data on your server over HTTP. 
The Django REST framework (DRF) is a toolkit built on top of the Django web framework that reduces the amount of code you need to write to create REST interfaces.


Build a REST API by leveraging Django, Python and the Django Rest Framework.REST APIs are here to connect your web application to anything and everything.
Build microservices, connect to client-side technologies like Angular & Ionic,and connect to other apps too.


# 1. User Registration and Login

How to build a Python Rest Api Server using Django Rest Framework. Create new Django app, define a Django Model, migrate it to database, write the Views and define Url patterns for handling HTTP GET/POST/PUT/DELETE requests.

## Features

User Register API

User Login API

Token Authentication API

User update and delete API

Pagination and Search API


 
## Screenshot from the User Registration and Login

User GET details

![userudpateapi](https://user-images.githubusercontent.com/83909801/157364717-d01fc748-c242-4666-80ec-ad1304ae31a6.png)

User UPDATE 

![2api](https://user-images.githubusercontent.com/83909801/157365010-62570023-64ec-415a-a715-f75a4fa988b7.png)


![3api](https://user-images.githubusercontent.com/83909801/157365536-608d56d9-23ab-4fc9-8c81-e8378e98ba1a.png)

Pagination and Search API

![3pagination](https://user-images.githubusercontent.com/83909801/157376117-820fcfa2-4ad2-4b89-a6d8-e6017645df4c.png)


## Installation
Install using pip...

    pip install djangorestframework

Add 'rest_framework' to your INSTALLED_APPS setting.

    INSTALLED_APPS = [
    ...
    'rest_framework',
    ]

## Requirements
1.Python (3.7, 3.8, 3.9, 3.10)

2.Django (2.2, 3.2, 4.0)

3.Django REST framework (3.12, 3.13)


#### User Registration and Login for the project is available at

https://github.com/merinjo90/Django-REST-Framework/tree/master/1_UserRegister_API/restapi. 

#### Demo for the User Registration and Login REST Framework

https://github.com/merinjo90/Django-REST-Framework/blob/master/1_UserRegister_API/userReg_log.gif



# 2.Django-DRF-Quiz-API

Quiz API developed using Django  & DjangoRestFramework.

Created a project QuizAPI_Django  created an api . It created 4 models Category,Quizzes,Questions & Answers. created a model Updated to log change in time for updates in model (Question & Answer) created serializers for models Category,Quizzes,Questions & Answers. added 2 more serializers RandomQuestionSerializer And QuestionSerializer for taking quiz on a specific topic.Topic to be passed through str:topic via URL in urls.py Created a nested serializer in RandomQuestionSerializer And QuestionSerializer for displaying Category, Questions and Answers all together in the API to make it more presentable and unserstandable. A full-fledged working API On The Go.Communcation between Bot with Django Done through DRF Api.


quiz get api is working

go to api/quiz/ to get all quizes

go to api/quiz/q/(name of quiz) to get all questions and answers related to quiz

 
## Screenshot from the Django-DRF-Quiz-API

go to api/quiz/ to get all quizes

![2_quiz_select](https://user-images.githubusercontent.com/83909801/157634207-27015274-05d2-4e89-8b00-7c8f9551c9cc.png)

go to api/quiz/r/(name of quiz) to get all questions  related to quiz

![1_ranquestn](https://user-images.githubusercontent.com/83909801/157633893-cee26309-1cd2-4a87-ad3d-44a5abe80c56.png)

go to api/quiz/q/(name of quiz) to get all questions and answers related to quiz

![3_quizqustn](https://user-images.githubusercontent.com/83909801/157634214-df1b4f43-edaf-459b-9303-51f5f72ac85f.png)


#### Django-DRF-Quiz-API project is available at

https://github.com/merinjo90/Django-REST-Framework/tree/master/2_QuizAPI_Django

#### Demo for the Django-DRF-Quiz-API

https://github.com/merinjo90/Django-REST-Framework/blob/master/2_QuizAPI_Django/Quiz_API.gif


# 3.Django Rest Framework - Blog API

In this tutorial we will build the API for a blog app featuring CRUD (Create-Read-Update-Delete) functionality with Django Rest Framework.

## Screenshot from the Django-DRF- Blog API

list view at 

![1_blog](https://user-images.githubusercontent.com/83909801/157819976-59dd7d1a-1251-4e6f-8946-fb59be702f4e.png)

detail view at 

![2_blog](https://user-images.githubusercontent.com/83909801/157819989-abfb4cda-61b9-429a-9861-5ae855ebf2ad.png)



#### Django-DRF- Blog API project is available at

https://github.com/merinjo90/Django-REST-Framework/tree/master/3_Blog_API


#### Demo for the Django-DRF- Blog Project

https://github.com/merinjo90/Django-REST-Framework/blob/master/3_Blog_API/blogAPI.gif
