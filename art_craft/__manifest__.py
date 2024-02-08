{
    'name': 'The Arts & Crafts Shop',
    'version': '1.0',
    'category': 'Retail',
    'description': """
        This modules provide a colourful array of paints, brushes, paper, beads, tools, colourful trays and other crafting (Handmade) essentials.
        They are a treasure trove for anyone seeking to express their creativity, explore new hobbies, or create beautiful handmade items.
    """,
    'depends': [
        'hr_hourly_cost',
        'knowledge',
        'pos_sale',
        'pos_discount',
        'product_email_template',
        'purchase_stock',
        'sale_service',
        'stock_delivery',
        'web_studio',
        'website_crm',
        'website_sale_autocomplete',
        'website_sale_comparison',
        'website_sale_loyalty',
        'website_sale_picking',
        'website_sale_wishlist',
        'theme_artists',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/base_automation.xml',
        'data/ir_actions_server.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/product_public_category.xml',
        'data/product_category.xml',
        'data/uom_uom.xml',
        'data/pos_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/product_pricelist_item.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/pos_payment_method.xml',
        'data/pos_config.xml',
        'data/ir_model_data.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
        'demo/crm_lead.xml',
        'demo/product_supplierinfo.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_rule.xml',
        'demo/loyalty_reward.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_post.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_post.xml',
        'demo/website_views.xml',
        'demo/website_ir_attachment.xml',
        'demo/website.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
