from seleniumbase import BaseCase

class CartPage(BaseCase):
    converse_add_to_cart_btn = "a[aria-label='Add “Branded Converse” to your cart']"
    cart_count_text = "ul[id='primary-menu'] span[class='count']"
    subtotal_text = "td[class='product-subtotal']"
    product_quantity_input = "input[id^='quantity']"
    update_cart_btn = "button[name='update_cart']"
    loading_overlay = ".woocommerce-cart-form div[class*='blockOverlay']"

    def open_page(self):
        self.open("https://practice.automationbro.com/cart")
