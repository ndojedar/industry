{
    'name': 'Hair Salon',
    'version': '1.1',
    'category': 'Services',
    'description': "",
    'depends': [
        'base_automation',
        'base_geolocalize',
        'calendar',
        'contacts',
        'hr',
        'knowledge',
        'pos_loyalty',
        'purchase_stock',
        'web_studio',
        'website_appointment',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_server.xml',
        'data/base_automation.xml',
        'data/pos_config.xml',
        'data/pos_category.xml',
        'data/product_template.xml',
        'data/product_pricelist.xml',
        'data/product_pricelist_item.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/appointment_type.xml',
        'data/ir_actions_actions.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/hr_employee.xml',
        'demo/res_users.xml',
        'demo/product_supplierinfo.xml',
        'demo/appointment_type.xml',
        'demo/calendar_event.xml',
        'demo/purchase_order.xml',
        'demo/website.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_rule.xml',
        'demo/loyalty_reward.xml',
        'demo/website_ir_attachment.xml',
        'demo/website_view.xml',
        'demo/website_builder.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
        'demo/delivery_confirm.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'hair_salon/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
    ],
    'images': ['images/main.png'],
}
