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
    "depends": ["base"],
    "data": [
        "security/academy_security.xml",
        "security/ir.model.access.csv",
        "views/academy_menuitems.xml",
        "views/course_views.xml",
        "views/session_views.xml"
    ],
    "demo": [
        "demo/academy_demo.xml",
    ]
}
