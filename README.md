[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)


## Coupon Service

Coupon service project has been created for Neshef.co.il .

### Features

* End-to-end coupon service including api
* Coupon will be emailed on submit (Mailjet is the only email platform supported right now)
* Email message can be modified
* QR Code can be attached to email
* Manage vendors and create custom password for every coupon
* Admin page


### Quick Start

Starting the project with hot-reloading enabled (the first time it will take a while):

```docker-compose up -d```

To run the alembic migrations (for the users table):

```docker-compose run --rm backend alembic upgrade head```

And navigate to http://localhost:8000/api/docs

### Frontend

```npm install && npm run build``` //For dev server: ```npm start```

```yarn && yarn build``` //For dev server: ```yarn start```


### Tests

```docker-compose run backend pytest```

or use ```scripts/test_backend.sh ```

Project created with the help of BuunTu project https://github.com/Buuntu/fastapi-react
