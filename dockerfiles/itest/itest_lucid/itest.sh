#!/bin/bash
set -eu

dpkg -i /work/dist/hacheck_*_amd64.deb

/usr/bin/hacheck --help
/usr/bin/hadown --help
/usr/bin/halist --help
/usr/bin/hashowdowned --help
/usr/bin/hastatus --help
/usr/bin/haup --help
