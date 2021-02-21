from page_objects.shop_page import ShopPage
from selenium.common.exceptions import NoSuchElementException


class ShopTest(ShopPage):
    def test_search_products(self):
        # open page
        self.open_page()

        # search for product
        self.send_keys(self.search_input, "Toys")
        self.click(self.search_btn)

        # assert product image
        try:
            print("Within Try Block")
            self.assert_element(self.product_img)
        except NoSuchElementException:
            print("Exception Block")
            self.assert_text("No products were found matching your selection.", self.no_products_txt)
