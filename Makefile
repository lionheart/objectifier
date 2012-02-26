all: version commit upload

version:
	@echo "Packaging version ${VERSION}"
	@sed -i '' 's/\(__version__ = \).*/\1${VERSION}/g' objectifier/__init__.py
	@sed -i '' 's/\(version = \).*/\1"${VERSION}",/g' setup.py

commit:
	@git add .
	@git cim "bump version to ${VERSION}"

upload: version
	@python setup.py sdist
	@s3cmd put dist/objectifier-${VERSION}.tar.gz s3://packages.elmcitylabs.com/ -P

