from imported_admin_user import Admin

admin = Admin('ana', 'melo', 21, 'pink', ['make purchases', 'delete posts', 'delete profiles'])
admin.describe_user()
admin.privileges.show_privileges()