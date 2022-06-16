{
    "name": "Odoo Academy",
    "summary": """Academy App to manage training""",
    "description": """
        Academy module to manage training:
        - Courses
        - Sessions
        - Attendees
    """,
    "author": "Lars Liedtke",
    "website": "https://www.odoo.com",
    "category": "Training",
    "version": "0.1",
    "depends": ["sale_management"],
    "data": [
        "security/academy_security.xml",
        "security/ir.model.access.csv",
        "views/academy_menuitems.xml",
        "views/course_views.xml",
        "views/session_views.xml",
        "views/sale_views_inherit.xml",
        "views/product_views_inherit.xml",
        "wizard/sale_wizard_view.xml",
        "report/session_report_templates.xml"
    ],
    "demo": [
        "demo/academy_demo.xml",
    ]
}
