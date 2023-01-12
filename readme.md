# Authz

## Curl

```bash
export JWT_TOKEN=....
curl -v -H "Authorization: Bearer ${JWT_TOKEN}"  http://127.0.0.1:5000/role_needed
curl -v -H "Authorization: Bearer ${JWT_TOKEN}"  http://127.0.0.1:5000/personal_data/1234
curl -v -H "Authorization: Bearer ${JWT_TOKEN}"  http://127.0.0.1:5000/org/1111/data
curl -v -H 'Content-Type: application/json' -d '{"state":"true"}' -H "Authorization: Bearer ${JWT_TOKEN}"  http://127.0.0.1:5000/cant_change_status_self
```

## Users

Generated with <https://jwt.io/>

### User one

```json
{
  "sub": "1234",
  "name": "John Doe",
  "org": "1111",
  "group": "ADMIN_X",
  "iat": 15162390
}
```

```jwt
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0IiwibmFtZSI6IkpvaG4gRG9lIiwib3JnIjoiMTExMSIsImdyb3VwIjoiQURNSU5fWCIsImlhdCI6MTUxNjIzOTB9.tp3iNrro4kcNOKOIflzOTDwYMHGuBhu7lmmy2xnrLfc
```

### User two

```json
{
  "sub": "5678",
  "name": "Ruby Hans",
  "org": "1111",
  "group": "USER_X",
  "iat": 15162390
}
```

```jwt
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1Njc4IiwibmFtZSI6IkpvaG4gRG9lIiwib3JnIjoiMTExMSIsImdyb3VwIjoiVVNFUl9YIiwiaWF0IjoxNTE2MjM5MH0.hT0rKb6UwjRZocFBpGAEna-6g09M9nA08IiJshgr5k0
```

### User three

```json
{
  "sub": "8989",
  "name": "Jule Mee",
  "org": "2222",
  "group": "USER_K",
  "iat": 15162390
}
```

```jwt
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4OTg5IiwibmFtZSI6Ikp1bGUgTWVlIiwib3JnIjoiMjIyMiIsImdyb3VwIjoiVVNFUl9LIiwiaWF0IjoxNTE2MjM5MH0.cztOSkZVuMfOBTEEikp8oWn9YYxW7tK5IHCWSOrenjg
```
