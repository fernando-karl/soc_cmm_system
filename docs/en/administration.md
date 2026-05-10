# Administration

## Features
- Dashboard at `/admin` with statistics (users, customers, assessments,
  in-progress work)
- Charts (Chart.js): assessment status and monthly growth
- User list at `/admin/users` with search, edit and delete
- Pages for: edit user, new user, change password

## Backend
- Admin routes (web pages + API) defined in `main.py`
- `database.py` exposes methods to fetch/update/delete users and aggregate
  statistics
- `auth.py` exposes methods to update user data and change passwords

## Security
- Authentication required for every admin page
- Password complexity requirements and input validation
- Users cannot delete themselves

## Future improvements
- Role-based access control (RBAC)
- Action audit log
- Bulk operations and export
