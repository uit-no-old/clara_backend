# API documentation

## Student classes (studentkull)

- GET https://clara-backend.eastus.cloudapp.azure.com/student_classes
- POST https://clara-backend.eastus.cloudapp.azure.com/student_classes

Example JSON:
```
[
  {
    "student_classes": "KULL1_2018_HØST"
  }
]
```

## Reponse options

- GET https://clara-backend.eastus.cloudapp.azure.com/response_options?where={"language":"no"}
  - Possible values: no, en

## Clara items (the questions)

- GET https://clara-backend.eastus.cloudapp.azure.com/clara_items?where={"language":"no"}
  - Possible values: no, en

## Clara reponses (the filled out question forms)

- GET https://clara-backend.eastus.cloudapp.azure.com/clara_responses?embedded={"student_classes":1,"clara_items.clara_item":1,"clara_items.response_option":1}
- POST https://clara-backend.eastus.cloudapp.azure.com/clara_responses

Example JSON:
```
[
  {
    "student_classes": "5b86391868ddbf388c2d4e67",
    "clara_items": [
      {
        "clara_item": "5b74182f68ddbf7283f572cf",
        "response_option": "5b75344d68ddbf20c42563bc"
      },
      {
        "clara_item": "5b74182f68ddbf7283f572d0",
        "response_option": "5b75344d68ddbf20c42563be"
      },
      {
        "clara_item": "5b74226468ddbf754d744536",
        "response_option": "5b75344d68ddbf20c42563be"
      }
    ]
  }
]
```
