from src.common_methods import CommonMethods


class TestCurencySwitch:
    def test_switch_currency(self, driver):
        base = CommonMethods(driver)
        base.click_currency_dropdown()
        base.select_drop_option("£ Pound Sterling")
        base.assert_currency_mark("£ Currency")
