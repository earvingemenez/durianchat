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



## Messages

#### Create Message

- URL : `<domain.com>/messages/
- RESPONSE : `{"id":1,"sender":1,"recipient":7,"content":"test"}`
- SAMPLE : `curl -X POST -d "sender=1&recipient=7&content=test" <domain.com>/messages` -H 'Authorization: Token 2a2e6749688f8556ed56b6f4a72f1d70184ofae5'`


#### Get Message list

- URL : `<domain.com>/messages/`
- RESPONSE :
```
[
    {
        "id": 1,
        "sender": 1,
        "recipient": 1,
        "content": "test"
    },
    {
        "id": 2,
        "sender": 1,
        "recipient": 7,
        "content": "asdasda"
    }
]
```
SAMPLE: `curl <domain.com>/messages -H 'Authorization: Token 2a2e6749688f8556ed56b6f4a72f1d70184ofae5'`


#### Get specific message

- URL : `<domain.com>/messages/<id>`
- RESPONSE : `{"id":1,"sender":1,"recipient":7,"content":"test"}`
- SAMPLE : `curl <domain.com>/messages/1 -H 'Authorization: Token 2a2e6749688f8556ed56b6f4a72f1d70184ofae5'`

#### Update specific message

- URL : `<domain.com>/messages/<id>
- TYPE : PUT
- RESPONSE : `{"id":1,"sender":1,"recipient":7,"content":"updated"}`
- SAMPLE : `curl -X PUT -d "sender=1&recipient=7&content=updated" <domain.com>/messages` -H 'Authorization: Token 2a2e6749688f8556ed56b6f4a72f1d70184ofae5'`

#### Delete specific message

- URL : `<domain.com>/messages/<id>
- TYPE : DELETE
- RESPONSE : "http204: No content"
- SAMPLE : - SAMPLE : `curl -X DELETE <domain.com>/messages/<id>` -H 'Authorization: Token 2a2e6749688f8556ed56b6f4a72f1d70184ofae5'`