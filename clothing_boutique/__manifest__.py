{
    'name': 'Clothing Store',
    'version': '1.0',
    'category': 'Retail',
    'description': """
This setup if for Clothing Store companies selling female clothing.""",
    'depends': [
        'knowledge',
        'pos_sale',
        'purchase_stock',
        'sale_product_matrix',
        'sale_purchase',
        'website_sale_comparison',
        'website_sale_loyalty',
        'website_sale_stock',
        'website_sale_wishlist',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/pos_payment_method.xml',
        'data/pos_config.xml',
        'data/product_public_category.xml',
        'data/product_category.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_template.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/product_image.xml',
        'data/ir_attachment.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/knowledge_tour.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/product_supplierinfo.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_generate_wizard.xml',
        'demo/loyalty_reward.xml',
        'demo/loyalty_rule.xml',
        'demo/product_template.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/website.xml',
        'demo/purchase_order_confirm.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/website_attachments.xml',
        'demo/website_view.xml',
        'demo/website_theme_apply.xml',
        'demo/payment_provider_demo_post.xml',
    ],
    'license': 'OPL-1',
    'assets': {
        'web.assets_backend': [
            'clothing_boutique/static/src/js/my_tour.js',
        ]
    },
    'author': 'Odoo S.A.',
    "cloc_exclude": [
        "data/knowledge_article.xml",
        "static/src/js/my_tour.js",
        "demo/website_view.xml",
    ],
    'images': ['images/main.png'],
}
