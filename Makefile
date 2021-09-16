# To create the venv easily

VENV_NAME = venv
VIRTUALIZER = virtualenv
VIRTBIN = venv/bin/
ACT = $(VIRTBIN)activate
REQUIREMENTS = requirements.txt

PY_DIR = airisgie
PY = $(VIRTBIN)python
PY_PM = $(VIRTBIN)pip
PY_FL = flake8
PY_INS = $(PY_PM) install -r
PY_UPD = $(PY_PM) install --upgrade -r

build:
	. $(ACT);\
	$(PY_FL)

virtual: venv
	$(PY_INS) $(REQUIREMENTS)

updlib:
	$(PY_UPD) $(REQUIREMENTS)

venv:
	cd ..;\
	$(VIRT) $(VENV_NAME);\

git_quick:
	git add -u
	echo "After ADD"
	git status
	sleep 5
	git commit
	git push origin HEAD
	git status
