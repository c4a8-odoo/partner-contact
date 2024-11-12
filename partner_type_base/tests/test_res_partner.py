from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):
    def setUp(self):
        super().setUp()
        self.ResPartner = self.env["res.partner"]

        self.Partner_company = self.ResPartner.create(
            {"name": "Company Partner", "is_company": True, "type": "contact"}
        )
        self.Partner_contact = self.ResPartner.create(
            {"name": "Individual Partner", "is_company": False, "type": "contact"}
        )
        self.Partner_child = self.ResPartner.create(
            {
                "name": "Child Partner",
                "is_company": False,
                "type": "contact",
                "parent_id": self.Partner_company.id,
            }
        )
        self.Partner_other = self.ResPartner.create(
            {"name": "Other Partner", "is_company": False, "type": "other"}
        )
        self.Partner_invoice = self.ResPartner.create(
            {"name": "Invoice Partner", "is_company": False, "type": "invoice"}
        )
        self.Partner_delivery = self.ResPartner.create(
            {"name": "Shipping Partner", "is_company": False, "type": "delivery"}
        )

    def test_is_address_readonly(self):
        self.assertFalse(self.Partner_company.is_address_readonly)
        self.assertFalse(self.Partner_contact.is_address_readonly)
        self.assertTrue(self.Partner_child.is_address_readonly)
        self.assertFalse(self.Partner_invoice.is_address_readonly)
        self.assertFalse(self.Partner_delivery.is_address_readonly)

    def test_is_individual_types(self):
        self.assertFalse(self.Partner_company.is_individual)
        self.assertTrue(self.Partner_contact.is_individual)
        self.assertTrue(self.Partner_other.is_individual)
        self.assertFalse(self.Partner_invoice.is_individual)
        self.assertFalse(self.Partner_delivery.is_individual)

    def test_can_be_parent(self):
        self.assertTrue(self.Partner_company.can_be_parent)
        self.assertFalse(self.Partner_contact.can_be_parent)
        self.assertFalse(self.Partner_other.can_be_parent)
        self.assertFalse(self.Partner_invoice.can_be_parent)
        self.assertFalse(self.Partner_delivery.can_be_parent)

    def test_can_be_child(self):
        self.assertFalse(self.Partner_company.can_be_child)
        self.assertTrue(self.Partner_contact.can_be_child)
        self.assertTrue(self.Partner_other.can_be_child)
        self.assertTrue(self.Partner_invoice.can_be_child)
        self.assertTrue(self.Partner_delivery.can_be_child)
