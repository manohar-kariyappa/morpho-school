# custom_app/api/student.py

import frappe


# ===============================
# GET TOTAL STUDENT COUNT
# ===============================
@frappe.whitelist(allow_guest=True)
def get_student_count(
    from_date=None,
    to_date=None
):

    filters = []

    # FROM DATE
    if from_date:

        filters.append([
            "creation",
            ">=",
            from_date
        ])

    # TO DATE
    if to_date:

        filters.append([
            "creation",
            "<=",
            to_date + " 23:59:59"
        ])

    count = frappe.db.count(
        "Student",
        filters=filters
    )

    return {
        "status": "success",
        "count": count
    }


# ===============================
# GET ALL STUDENT LIST
# ===============================
@frappe.whitelist(allow_guest=True)
def get_student_list(
    from_date=None,
    to_date=None
):

    filters = []

    if from_date:

        filters.append([
            "creation",
            ">=",
            from_date
        ])

    if to_date:

        filters.append([
            "creation",
            "<=",
            to_date + " 23:59:59"
        ])

    students = frappe.get_all(
        "Student",
        filters=filters,
        fields=[
            "name",
            "student_name",
            "joining_date",
            "enabled",
            "creation"
        ],
        order_by="creation desc"
    )

    return {
        "status": "success",
        "count": len(students),
        "data": students
    }


# ===============================
# GET RECENT 5 STUDENTS
# ===============================
@frappe.whitelist(allow_guest=True)
def get_recent_students(
    from_date=None,
    to_date=None
):

    filters = []

    if from_date:

        filters.append([
            "creation",
            ">=",
            from_date
        ])

    if to_date:

        filters.append([
            "creation",
            "<=",
            to_date + " 23:59:59"
        ])

    students = frappe.get_all(
        "Student",
        filters=filters,
        fields=[
            "name",
            "student_name",
            "joining_date",
            "enabled",
            "creation"
        ],
        order_by="creation desc",
        limit_page_length=5
    )

    return {
        "status": "success",
        "data": students
    }


# ===============================
# DASHBOARD DATA
# ===============================
@frappe.whitelist(allow_guest=True)
def get_students_dashboard(
    from_date=None,
    to_date=None
):

    filters = []

    if from_date:

        filters.append([
            "creation",
            ">=",
            from_date
        ])

    if to_date:

        filters.append([
            "creation",
            "<=",
            to_date + " 23:59:59"
        ])

    total = frappe.db.count(
        "Student",
        filters=filters
    )

    recent_students = frappe.get_all(
        "Student",
        filters=filters,
        fields=[
            "name",
            "student_name",
            "joining_date",
            "enabled"
        ],
        order_by="joining_date desc",
        limit_page_length=5
    )

    return {
        "status": "success",
        "total_students": total,
        "recent_students": recent_students
    }


# ======================================================
# STUDENTS BY PROGRAM
# ======================================================
@frappe.whitelist(allow_guest=True)
def get_students_by_program(
    from_date=None,
    to_date=None
):

    conditions = ""

    # FROM DATE
    if from_date:

        conditions += f"""
            AND s.creation >= '{from_date}'
        """

    # TO DATE
    if to_date:

        conditions += f"""
            AND s.creation <= '{to_date} 23:59:59'
        """

    data = frappe.db.sql(f"""
        SELECT
            sg.program AS label,
            COUNT(sgs.student) AS total

        FROM `tabStudent Group` sg

        LEFT JOIN `tabStudent Group Student` sgs
            ON sgs.parent = sg.name

        LEFT JOIN `tabStudent` s
            ON s.name = sgs.student

        WHERE IFNULL(sg.program,'') != ''

        {conditions}

        GROUP BY sg.program

        ORDER BY sg.program ASC
    """, as_dict=True)

    return {
        "status": "success",
        "data": data
    }


# ======================================================
# FEE COLLECTION
# ======================================================
@frappe.whitelist(allow_guest=True)
def get_fee_collection(
    from_date=None,
    to_date=None
):

    conditions = ""

    if from_date:

        conditions += f"""
            AND posting_date >= '{from_date}'
        """

    if to_date:

        conditions += f"""
            AND posting_date <= '{to_date}'
        """

    paid = frappe.db.sql(f"""
        SELECT
            IFNULL(SUM(grand_total),0) as total

        FROM `tabSales Invoice`

        WHERE status='Paid'

        {conditions}
    """, as_dict=True)[0].total

    unpaid = frappe.db.sql(f"""
        SELECT
            IFNULL(SUM(grand_total),0) as total

        FROM `tabSales Invoice`

        WHERE status='Unpaid'

        {conditions}
    """, as_dict=True)[0].total

    monthly = frappe.db.sql(f"""
        SELECT
            MONTHNAME(posting_date) as month,
            IFNULL(SUM(grand_total),0) as total

        FROM `tabSales Invoice`

        WHERE docstatus < 2

        {conditions}

        GROUP BY MONTH(posting_date)

        ORDER BY MONTH(posting_date)
    """, as_dict=True)

    return {
        "status": "success",
        "paid_total": paid,
        "unpaid_total": unpaid,
        "chart": monthly
    }