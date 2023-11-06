{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Services',
    'description': """
Manage your long term or mid long term rental properties
Manage your properties, create and manage rental contracts, and streamline your entire rental process. Efficient property management.
""",
    'author': 'Odoo S.A.',
    'depends': [
        'crm_enterprise',
        'crm_iap_enrich',
        'crm_iap_mine',
        'knowledge',
        'sale_crm',
        'sale_product_configurator',
        'sale_subscription',
        'website_crm',
        'website_studio',
        'theme_treehouse',
    ],
    'data': [
        'data/account_analytic_plan.xml',
        'models/meter_reading.xml',
        'models/account_analytic_account.xml',
        'models/sale_order.xml',
        'data/crm_stages.xml',
        'models/crm_lead.xml',
        'data/res_config_setting.xml',
        'data/ir_attachment_pre.xml',
        'data/account_tags.xml',
        'data/account_analytic_account.xml',
        'data/product_product.xml',
        'data/sale_order_template.xml',
        'data/knowledge_article.xml',
        'data/ir_attachment_post.xml',
        'security/ir_model_access.xml',
        'security/ir_rule.xml',
        'views/account_analytic_account_views.xml',
        'views/sale_order_views.xml',
        'views/crm_lead_views.xml',
        'views/industry_real_estate_views.xml',
        'views/website.xml',
        'data/website_menu.xml',
        'data/ir_filters.xml',
    ],
    'demo': [
        'demo/website.xml',
        'demo/res_partner.xml',
        'demo/crm_tag.xml',
        'demo/crm_lead.xml',
        'demo/crm_lead_action.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/account_move.xml',
        'demo/account_move_line.xml',
        'demo/account_move_confirm.xml',
        'demo/website_attachment.xml',
        'demo/website_views.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
    ],
    'application': False,
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
