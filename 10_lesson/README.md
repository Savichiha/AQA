# Автотесты с использованием Allure для Windows

## Описание проекта

Этот проект включает в себя автоматические тесты, использующие **pytest** для выполнения тестов и **Allure** для генерации визуальных отчетов. В данном файле описан процесс запуска тестов для формирования отчета и просмотра отчета с помощью Allure.

---

## Установка зависимостей

Для того чтобы начать работу с проектом, необходимо установить все необходимые зависимости:

1. Установите библиотеку pytest для запуска тестов:

   pip install pytest

2. Установите библиотеку allure-pytest для интеграции pytest с Allure:

   pip install allure-pytest

3. Чтобы запустить тесты и сохранить результаты в формате, который будет использоваться для генерации отчета в Allure, выполните следующую команду:

   pytest Lesson10 -v --alluredir allure-result. После выполнения команды результаты тестов будут сохранены в папке allure-results.

4. После того как вы запустили тесты и сформировали результаты, для просмотра отчета выполните следующую команду:

   allure serve allure-results. Эта команда откроет сформированный отчет в браузере. Allure будет генерировать отчет в реальном времени.

5. Если вы хотите просто открыть уже сформированный отчет без повторной генерации, используйте команду:

   allure open allure-results

## Структура отчета
После открытия отчета в Allure вы сможете увидеть:

Общие статистики: количество успешных, неудачных и пропущенных тестов.

Детали каждого теста: время выполнения, скриншоты, логи и другие данные.

Графики и диаграммы: статистика по тестам и графики времени выполнения.