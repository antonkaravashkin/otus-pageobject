# otus-pageobject

Перенес проект в отдельный репозиторий, дабы было удобнее ревьюить задачки.

# --------- <h1>allure-section</h1> ---------

# Отчет генерируется сам, параметр командной строки прописан в pytest.ini.
addopts = --alluredir allure-results -q

# Для генерации отчета прописать в терминале:
~/repositories/allure_report/allure/bin/allure generate ~/repositories/otus-pageobject/allure-results/ --clean

# Заметки для себя.
На vscode перейти в папку "~/{PROJECTROOT}/allure-results/"
В терминале набрать "python3 -m http.server"
