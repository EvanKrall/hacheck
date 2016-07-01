
all: itest_trusty

DATE := $(shell date +'%Y-%m-%d')
HACHECKVERSION := $(shell sed 's/.*(\(.*\)).*/\1/;q' debian/changelog)
bintray.json: bintray.json.in
	sed -e 's/@DATE@/$(DATE)/g' -e 's/@HACHECKVERSION@/$(HACHECKVERSION)/g' $< > $@

setup:
	echo "Go"
	# mkdir src && cp -R hacheck src && cp -R debian src

package_lucid: setup
	[ -d dist ] || mkdir dist
	tox -e package_lucid

itest_lucid: package_lucid dockerfiles/itest/itest_lucid/Dockerfile
	tox -e itest_lucid

package_trusty: setup
	[ -d dist ] || mkdir dist
	tox -e package_trusty

itest_trusty: package_trusty bintray.json
	tox -e itest_trusty

clean:
	git clean -Xfd