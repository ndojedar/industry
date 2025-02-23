{
    'name': 'IT Hardware & Support',
    'version': '1.0',
    'category': 'Services',
    'description': """
We offer IT sales, installation, and repair services for a wide range of products, including laptops, RAM, accessories, and CCTV cameras.
""",
    'depends': [
        'account_followup',
        'helpdesk_stock',
        'knowledge',
        'purchase_stock',
        'industry_fsm_sale',
        'repair',
        'sale_crm',
        'sale_purchase',
        'web_studio',
        'website_crm',
        'website_helpdesk',
        'website_sale_comparison',
        'website_sale_stock',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/base_automation.xml',
        'data/ir_actions_server.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/stock_picking_type.xml',
        'data/ir_ui_view.xml',
        'data/project_task_type.xml',
        'data/product_category.xml',
        'data/project_project.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/sale_order_template.xml',
        'data/sale_order_template_line.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/website_view.xml',
        'data/website_theme_apply.xml',
        'data/ir_model_data.xml',
    ],
    'demo': [
        'demo/website.xml',
        'demo/res_partner.xml',
        'demo/product_supplierinfo.xml',
        'demo/product_template.xml',
        'demo/stock_lot.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/helpdesk_ticket.xml',
        'demo/website_attachment.xml',
        'demo/website_view.xml',
        'demo/website_theme_apply.xml',
        'demo/payment_provider_demo_post.xml',
    ],
    'license': 'OPL-1',
    'author': 'Odoo S.A.',
    'images': ['images/main.png'],
}
