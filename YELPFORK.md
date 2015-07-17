Warning
=======
This branch (yelp) is rebased and force-pushed as necessary when upstream pulls
in pull requests. Do not base your work on this branch.

Yelps Hacheck Fork
==================
We maintain a few commits on top of stock hacheck. This is mostly to support
our needs in Smartstack, and if these changes manage to make it upstream
we will no longer need this fork.

This git repo only contains our changes to hacheck, it under no circumstances
should contain code specific to packaging, testing, or distributing hacheck.

How to Maintain the Fork
========================
Because this repo only contains our changes to stock hacheck, pulling in
upstream is relatively easy. Just do:

Initial setup
-------------
```
git clone git@github.com:Yelp/hacheck
cd hacheck
git remote add upstream git@github.com:uber/hacheck
```

Pulling in upstream
-------------------
```
git fetch upstream
git rebase -i upstream/master
```

Fix any merge conflicts, update the Changelog below, and push

This next step will screw up history, but we want to do that so that we can
maintain as clean of a fork as possible

```
git push origin HEAD --force
```

Changelog
=========

2015-01-21
~~~~~~~~~~
* Accept periods in service names (https://github.com/uber/hacheck/pull/26)

2015-01-16
~~~~~~~~~~
* Extract port from X-Haproxy-Server-State header if present (https://github.com/uber/hacheck/pull/20)
* Initial fork, includes this YELPFORK file for how to maintain the fork

2015-07-16
~~~~~~~~~~
* Recreate fork.
* Allow remote control of spool state (https://github.com/uber/hacheck/pull/25)
* Added support for multiple headers via config list (https://github.com/uber/hacheck/pull/24)
