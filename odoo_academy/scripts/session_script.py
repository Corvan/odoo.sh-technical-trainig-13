import xmlrpc.client

url = ("https://corvan-odoo-sh-technical-training-13-"
       "13-0-dev-academ-5158857.dev.odoo.com")
db = "corvan-odoo-sh-technical-training-13-13-0-dev-academ-5158857"
username = "admin"
password = "AtxJ3jf6PiQXbkvjjsriKdS9RZytUB93LWwWhQ8VCRSYDJM2qYpNsxpvSeSwCLK4"

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/object")
check_access_rights = models.execute_kw(
    db,
    uid,
    password,
    "academy.session",
    "check_access_rights",
    [
        "write"
    ],
    {
        "raise_exception": False
    }
)

print(check_access_rights)

courses = models.execute_kw(
    db,
    uid,
    password,
    "academy.course",
    "search_read",
    [
        [("level", "in", ["intermediate", "beginner"])]
    ],
)

print(courses)

course = models.execute_kw(
    db,
    uid,
    password,
    "academy.course",
    "search",
    [
        [("name", "=", "Accounting 200")]
    ],
)

print(course)

session_fields = models.execute_kw(
    db,
    uid,
    password,
    "academy.session",
    "fields_get",
    [],
    {
        "attributes": ["string", "type", "required"]
    },
)

print(session_fields)
