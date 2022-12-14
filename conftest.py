import pytest
import logging
import datetime

from selenium import webdriver
from src.common_methods import CommonMethods
from src.catalog.catalog_page import CatalogPage
from src.admin_panel.admin_panel import AdminPanel
from data.product_card import GALAXY
from data.admin_panel import LOGIN, PASSWORD


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "safari"],
        help="args - --browser=chrome, firefox, safari"
    )

    parser.addoption(
        "--url",
        default="http://192.168.88.81:8081",
        help="default is opencart demo_page. put '/admin' in url if u need to run admin tests."
    )

    parser.addoption(
        "--executor",
        action="store",
        default="192.168.88.81"
    )
    parser.addoption("--bv")


@pytest.fixture
def driver(request):
    """Считается, что драйвер добавлен в переменные сред ОС win, либо назначен исполняемым под unix\linux системы"""
    browser = request.config.getoption("--browser")
    target_link = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")

    logger = logging.getLogger(request.node.name)
    file = logging.FileHandler(f"logs/{request.node.name}.log")
    file.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(message)s"))
    logger.addHandler(file)
    logger.setLevel("DEBUG")

    logger.info(
        f"Начинаем тест: '{request.node.name}' в браузере: {browser}, в {datetime.datetime.now()}")

    if executor == "local":
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "safari":
            driver = webdriver.Safari()
        else:
            logger.info(f"Не удалось создать драйвер!")
            raise Exception(
                "Unknown browser, please check --browser help for supported options"
            )
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "name": "AntonK.",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False,
                "enableLog": True
            },
            "acceptSslCerts": True,
            "acceptInsecureCerts": True,
            "timeZone": "Europe/Moscow"
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities
        )
    driver.log_level = logging.DEBUG
    driver.logger = logger
    driver.test_name = request.node.name
    driver.maximize_window()
    driver.get(target_link)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    logger.info(
        f"Тест: '{request.node.name}' в браузере: {browser} закончен в {datetime.datetime.now()}")


@pytest.fixture
def open_product_card(driver):
    base = CommonMethods(driver)
    base.open_catalog_with_single_section("Tablets")
    catalog = CatalogPage(driver)
    catalog.click_product_card(GALAXY)


@pytest.fixture
def tablets_catalog(driver):
    base = CommonMethods(driver)
    base.open_catalog_with_single_section("Tablets")


@pytest.fixture
def my_account_registration(driver):
    registration = CommonMethods(driver)
    registration.click_my_account_button()
    registration.select_drop_option("Register")


@pytest.fixture
def admin_panel_login(driver):
    admin = AdminPanel(driver)
    admin.input_name(LOGIN)
    admin.input_password(PASSWORD)
    admin.click_login_button()
