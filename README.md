# Durianchat API
- A sample project that shows the functionalities of `Django Rest Framework (DRF)`

## Accounts

#### Creating user account

- URL : `<domain.com>/accounts/create`
- RESPONSE (JSON) : `{"id":4,"username":"admin2","email":"","is_staff":false}`
- SAMPLE: `curl -X POST -d "username=admin1&password=1234"  <domain.com>/accounts/create`


#### Log-in user

- URL : `<domain.com>/accounts/authenticate`
- RESPONSE (JSON) : `{"token":"2a2e6749688f8556ed56b6f4a72f1d70184ofae5"}`
- SAMPLE: `curl -X POST -d "username=admin&password=1234"  <domain.com>/accounts/authenticate`


#### Get User info (logged-in user)

- URL :  `<domain.com>/accounts/me`
- RESPONSE (JSON) : `{"id":1,"username":"admin","email":"","is_staff":true}`
- SAMPLE : `curl <domain.com>/accounts/me -H 'Authorization: Token 2a2e6749688f8556ed56b6f4a72f1d70184ofae5'`