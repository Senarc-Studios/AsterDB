from setuptools import setup

requirements = []
README = ""

with open("requirements.txt") as f:
	requirements = f.read().splitlines()

with open("README.md") as f:
	README = f.read()

extra_require = {
	"srv": [
		"fastapi",
		"uvicorn",
		"pydantic",
		"dnspython",
		"motor",
		"pymongo[srv]"
	]
}

packages = [
	"aster"
]

setup(
	name="aster.db",
	author="BenitzCoding",
	author_email="beni@senarc.net",
	url="https://github.com/Senarc-Studios/AsterDB",
	project_urls={
		"Documentation": "https://coming-soon.senarc.net",
		"Issue tracker": "https://github.com/Senarc-Studios/AsterDB/issues",
		"Github": "https://github.com/Senarc-Studios/AsterDB"
	},
	version="0.0.1",
	packages=packages,
	license="MIT",
	description="HTTP API Wrapper built for MongoDB for the encryption of Data.",
	long_description=README,
	long_description_content_type="text/markdown",
	include_package_data=True,
	install_requires=requirements,
	extras_require=extra_require,
	python_requires=">=3.7.0",
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: MIT License",
		"Intended Audience :: Developers",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"Topic :: Internet",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Utilities",
	]
)