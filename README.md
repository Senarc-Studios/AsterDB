<div align="center">
	<img src="https://user-images.githubusercontent.com/70798458/224541691-9ba48971-2ccb-497b-b123-8f89f1f57051.png"/>
	<p align="center">
		<em>HTTP API Wrapper built for MongoDB for the encryption of Data.</em>
	</p>
</div>

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

<p>
	<code>aster.db</code> is not its own Database, but rather runs on top of MongoDB.
	<br/>
	Aster adds encryption to your MongoDB Database.
	<br/>
	Therefore, if someone accesses your Database's contents, they can't
	decrypt the data in the Database.
	<br/>
	You can only decrypt the data if you have a Public Key.
	<br/>
	You can only make changes without breaking DB by encrypting the data with Private Key.
</p>

### Disclaimer
<p>
	(1) Losing both the Private Key and Public Key might result in redering the Database and it's contents useless;
	<br/>
	(2) If your Private Key is lost, you can still retrieve the data with your Public Key;
	<br/>
	(3) If your Public Key is lost, you can simply generate it with your Private Key.
</p>

**Keep in mind that this Project is not complete and still being developed.**
