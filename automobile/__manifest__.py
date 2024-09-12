{
    'name': 'Automobile Spareparts',
    'version': '1.0',
    'category': 'Retail',
    'description': """
This set-up is for the automobile trading companies selling to the customers.
The Automobile spare parts business have the more number of items for the various car brands and the parts for the Engine,
Maintenance and accessorises etc.
    """,
    'depends': [
        'base_automation',
        'account_check_printing',
        'account_followup',
        'calendar',
        'knowledge',
        'pos_sale',
        'product_expiry',
        'purchase_product_matrix',
        'purchase_stock',
        'sale_planning',
        'sale_product_matrix',
        'sale_stock',
        'web_studio',
        ],
    'data': [
        'data/ir_attachment_pre.xml',
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window.xml',
        'data/base_automation.xml',
        'data/ir_actions_server.xml',
        'data/ir_ui_menu.xml',
        'data/ir_model_access.xml',
        'data/ir_default.xml',
        'data/product_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/product_pricelist_item.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/knowledge_cover.xml',
        'data/res_config_settings.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/stock_lot.xml',
        'demo/product_supplierinfo.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_post.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_post.xml',
    ],
    'license': 'OPL-1',
    'author': 'Odoo S.A.',
    'images': ['images/main.png'],
}
