from flask_admin.contrib import sqla


class StudentsAdminView(sqla.ModelView):
    """
        Configure different properties of the view
    """
    page_size = 10
    edit_template = 'student_edit.html'
    column_filters = ('name', 'address')
