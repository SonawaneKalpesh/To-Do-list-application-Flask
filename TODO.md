# TODO List for Fixing To-Do List Application Errors

- [x] Fix import in app/__init__.py: Change `from app.routes.auth import tasks_bp` to `from app.routes.tasks import tasks_bp`
- [x] Correct assignment operators in toggle_status function in app/routes/tasks.py: Change `==` to `=` for status assignments
- [x] Create app/templates/edit_task.html: Add a form to edit task title
- [x] Update app/templates/tasks.html: Add buttons/forms for toggle status, delete, edit, and clear tasks
- [x] Run the app to verify fixes
- [x] Remove invalid register link from base.html to fix BuildError
