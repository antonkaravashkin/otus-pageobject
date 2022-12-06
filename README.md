# otus-pageobject

Перенес проект в отдельный репозиторий, дабы было удобнее ревьюить задачки.

# --------- allure-section ---------

# Отчет генерируется сам, параметр командной строки прописан в pytest.ini.
addopts = --alluredir allure-results -q

# Для генерации отчета прописать в терминале:
~/repositories/allure_report/allure/bin/allure generate ~/repositories/otus-pageobject/allure-results/ --clean

# Как запускать в локали:
На vscode перейти в папку ~/{PROJECTROOT}/allure-report/
В терминале набрать python3 -m http.server
На крайняк, если не сработает первый вариант: ~/repositories/allure_report/allure/bin/allure serve allure-results