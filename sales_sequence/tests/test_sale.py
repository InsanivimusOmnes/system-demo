from odoo.tests.common import TransactionCase


class SomethingCase(TransactionCase):
    def setUp(self):
        super(SomethingCase, self).setUp()
        ResPartner = self.env["res.partner"]

        # Create test partner
        self.test_partner = ResPartner.create({"name": "Test Partner"})

        # Create products
        ProductProduct = self.env["product.product"]
        SaleOrderLine = self.env["sale.order.line"]

        self.product_1 = ProductProduct.create({"name": "Product 1"})
        self.product_2 = ProductProduct.create({"name": "Product 2"})
        self.product_3 = ProductProduct.create({"name": "Product 3"})

        # Create Sale Order
        SaleOrder = self.env["sale.order"]

        self.sale_order_1 = SaleOrder.create(
            {"name": "Sale Order 1", "partner_id": self.test_partner.id}
        )

        # Create Order Lines
        self.sale_order_line_1 = SaleOrderLine.create(
            {
                "product_id": self.product_1.id,
                "order_id": self.sale_order_1.id,
                "name": self.product_1.name,
                "product_uom_qty": 1,
                "price_unit": 1,
            }
        )

        self.sale_order_line_2 = SaleOrderLine.create(
            {
                "product_id": self.product_2.id,
                "order_id": self.sale_order_1.id,
                "name": self.product_2.name,
                "product_uom_qty": 1,
                "price_unit": 1,
            }
        )

        self.sale_order_line_3 = SaleOrderLine.create(
            {
                "product_id": self.product_3.id,
                "order_id": self.sale_order_1.id,
                "name": self.product_3.name,
                "product_uom_qty": 1,
                "price_unit": 1,
            }
        )

    def test_default_sequence(self):
        """test default sequence"""
        self.assertEqual(
            self.sale_order_line_1.number,
            "1",
            msg="Line number of the first line must be equal to 1",
        )
        self.assertEqual(
            self.sale_order_line_2.number,
            "2",
            msg="Line number of the second line must be equal to 2",
        )
        self.assertEqual(
            self.sale_order_line_3.number,
            "3",
            msg="Line number of the third line must be equal to 3",
        )

    def test_change_line(self):
        """test line sequence change"""
        self.sale_order_line_3.sequence = 1
        self.sale_order_line_1.sequence = 2
        self.sale_order_line_2.sequence = 3
        self.assertEqual(
            self.sale_order_line_1.number,
            "2",
            msg="Line number of the second line must be equal to 2",
        )
        self.assertEqual(
            self.sale_order_line_2.number,
            "3",
            msg="Line number of the third line must be equal to 3",
        )
        self.assertEqual(
            self.sale_order_line_3.number,
            "1",
            msg="Line number of the first line must be equal to 1",
        )

    def test_add_line(self):
        """Add new order line and check sequence"""
        # MOve TO SETUP
        self.product_4 = self.env["product.product"].create({"name": "Product 4"})
        # -------------
        self.sale_order_line_4 = self.env["sale.order.line"].create(
            {
                "product_id": self.product_4.id,
                "order_id": self.sale_order_1.id,
                "name": self.product_4.name,
                "product_uom_qty": 1,
                "price_unit": 1,
            }
        )
        self.assertEqual(
            self.sale_order_line_4.number,
            "4",
            msg="Line number of the four line must be equal to 4",
        )

    def test_delete_line(self):
        """Delete one of line and check their sequence"""
        self.sale_order_line_3.unlink()

        self.assertEqual(
            self.sale_order_line_1.number,
            "1",
            msg="Line number of the first line must be equal to 1",
        )
