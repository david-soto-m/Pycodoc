VIRTUALIZER = virtualenv
VENV_NAME = venv
SRC_DIR = src
TARGET = main.py
REQUIREMENTS = requirements.txt

VIRTBIN = $(VENV_NAME)/bin
ACT = $(VIRTBIN)/activate
PY = $(VIRTBIN)/python
PY_PM = $(VIRTBIN)/pip

PY_FL = flake8
PY_UPD = $(PY_PM) install --upgrade -r

build:
	. $(ACT);\
	$(PY_FL)

run:
	cd $(SRC_DIR);\
	../$(PY) $(TARGET)

updlib: $(VIRTBIN)
	$(PY_UPD) $(REQUIREMENTS)

virt $(VIRTBIN):
	cd ..;\
	$(VIRTUALIZER) $(VENV_NAME);\
