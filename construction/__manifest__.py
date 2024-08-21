{
    'name': 'Construction',
    'version': '1.0',
    'category': 'Construction',
    'description': """
This industry is ideal for construction businesses proficient in managing projects from conception to completion,
focusing on accurate quoting, efficient planning, seamless execution, and excellent customer service, ...
""",
    'depends': [
        'crm_enterprise',
        'documents',
        'helpdesk',
        'hr_fleet',
        'industry_fsm',
        'industry_fsm_stock',
        'knowledge',
        'maintenance',
        'purchase_stock',
        'sale_crm',
        'sale_margin',
        'sale_project_forecast',
        'sign',
    ],
    'data': [
        'data/account_analytic_account.xml',
        'data/documents_folder.xml',
        'data/res_config_settings.xml',
        'data/product_category.xml',
        'data/project_task_type.xml',
        'data/project_project.xml',
        'data/ir_attachment_pre.xml',
        'data/uom_uom.xml',
        'data/product_product.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_favorite.xml',
        'data/mail_message.xml',
        'data/mail_activity_type.xml',
        'data/hr_job.xml',
    ],
    'demo': [
        'demo/documents_folder.xml',
        'demo/res_partner.xml',
        'demo/account_analytic_account.xml',
        'demo/project_project.xml',
        'demo/product_product.xml',
        'demo/documents_document.xml',
        'demo/helpdesk_ticket.xml',
        'demo/hr_employee.xml',
        'demo/fleet_cars_data.xml',
        'demo/fleet_vehicle.xml',
        'demo/crm_lead.xml',
        'demo/product_supplierinfo.xml',
        'demo/stock_quant.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/project_task.xml',
        'demo/account_analytic_line.xml',
        'demo/project_update.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
        'demo/planning_recurrency.xml',
        'demo/planning_slot.xml',
    ],
    'license': 'OPL-1',
    'author': 'Odoo S.A.',
    'images': ['images/main.png'],
}
