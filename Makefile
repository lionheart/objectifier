all: pyc version push

init:
	virtualenv .
	. bin/activate && python setup.py develop

pyc:
	find . -name "*.pyc" -exec rm '{}' ';'

version: pyc
	echo "Packaging version ${MAJ}.${MIN}"
	sed -i '' 's/\(__version__ = \).*/\1"${MAJ}.${MIN}"/g' objectifier/metadata.py
	sed -i '' 's/\(version = \).*/\1"${MAJ}"/g' docs/conf.py
	sed -i '' 's/\(release = \).*/\1"${MAJ}.${MIN}"/g' docs/conf.py
	git add objectifier/metadata.py
	git add docs/conf.py
	git commit -m "bump version to ${MAJ}.${MIN}"
	python setup.py sdist upload --sign
	s3cmd put dist/objectifier-${MAJ}.${MIN}.tar.gz s3://packages.elmcitylabs.com/ -P

documentation:
	cp docs/index.rst README.rst
	sed -i '' 's/:ref://g' README.rst
	cd docs && make html && cd _build/html && git add . && git commit -m "doc update" && git push
	python setup.py upload_docs
	cd ../../..
	git add README.rst
	git add docs
	git commit -m "doc update"

push:
	git push github master
	git push origin master


