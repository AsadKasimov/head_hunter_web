## Проект UI автотестов hh.ru

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Python" src="./resourses/icons/Python-logo-notext.svg"></code>
  <code><img width="5%" title="PyCharm" src="./resourses/icons/pycharm.svg"></code>
  <code><img width="6%" title="PyCharm" src="./resourses/icons/pytest.png"></code>
  <code><img width="6%" title="PyCharm" src="./resourses/icons/selene.png"></code>
  <code><img width="5%" title="Allure Report" src="./resourses/icons/allure-Report-logo.svg"></code>
  <code><img width="5%" title="Allure TestOps" src="./resourses/icons/allure-ee-logo.svg"></code>
  <code><img width="5%" title="Github" src="./resourses/icons/git-logo.svg"></code>
  <code><img width="5%" title="Jenkins" src="./resourses/icons/jenkins-logo.svg"></code>
  <code><img width="5%" title="Jira" src="./resourses/icons/jira-logo.svg"></code>
  <code><img width="5%" title="Selenoid" src="./resourses/icons/selenoid-logo.svg"></code>
  <code><img width="5%" title="Telegram" src="./resourses/icons/Telegram.svg"></code>


</p>


<!-- Тест кейсы -->

### Что проверяем
* Добавление вакансий в Избранные и Черный список
* Вход и Выход из аккаунта
* Поиск профессии с параметрами
* Вход в аккаунт с помощью пароля
* Подписка на рассылку на почту


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="./resourses/icons/jenkins-logo.svg"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/003_python-edbeg1337-head-hunter-pip/)

##### При нажатии на "Собрать с параметрами" откроеться окно где надо выбрать тесты которые запустяться через виртуальную машину в Selenide.
![This is an image](resourses/icons/jenkins_job.png)
![This is an image](resourses/icons/jenkins_job1.png)
![This is an image](resourses/icons/jenkins_job2.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="./resourses/icons/allure-Report-logo.svg"> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](resourses/icons/allure1.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](resourses/icons/allure2.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](resourses/icons/allure3.png)

##### Видео прохождение теста
![This is an image](resourses/icons/allure4.gif)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="./resourses/icons/allure-ee-logo.svg"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/2012/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](resourses/icons/alluret1.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](resourses/icons/alluret2.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="./resourses/icons/jira-logo.svg"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](resourses/icons/alluret3.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="./resourses/icons/Telegram.svg"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](resourses/icons/alluret4.png)
