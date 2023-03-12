<div align="center">
	<img src="https://user-images.githubusercontent.com/70798458/224541691-9ba48971-2ccb-497b-b123-8f89f1f57051.png"/>

</div>

<p align="center">
<em>HTTP API Wrapper built for MongoDB for the encryption of Data.</em>
</p>

---
[![Package version](https://badge.fury.io/py/aster.db.svg)](https://pypi.python.org/pypi/aster.db)

This Database runs on top of any MongoDB instance, this can be
used on both cloud instances and local machine instances.
The SDK and Server is both included in this package.

**Note:** You would need to encrypt the MongoDB instance with `aster-db encrypt <MONGO-URI>` if you have data on the database.

**Requirements:** Python 3.7+ (For Python 3.6 support, install version 0.16.0.)

## Quickstart
Install SDK or Server using `pip`:

**SDK:**
```shell
$ pip install aster.db
```
**Server:**
```shell
$ pip install aster.db[srv]
```

---
## Why `aster.db`?

`aster.db` is not its own Database, but rather runs on top of MongoDB.
The one thing that Aster adds to your MongoDB Database is encryption.
If someone gets access to the Database, they can't see the contents or data in the Database.
You can only see the contents if you have a Public Key, and you can only make changes
that doesn't break the system by encrypting the data with Private Keys.

### Disclaimer
(1) Losing both the Private Key and Public Key might result in redering the Database and it's contents useless;
(2) If your Private Key is lost, you can still retrieve the data with your Public Key;
(3) If your Public Key is lost, you can simply generate it with your Private Key;

**Keep in mind that this Project is not complete and still being developed.**
