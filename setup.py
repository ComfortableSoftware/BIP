

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CF.setup.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  description="Batch image processor for some special needs we have."
  license="GPLv3",
  name="BIP",
  url="https://github.com/ComfortableSoftware/BIP",
  version="0.1.0-0",
  package_dir={"BIP": "BIP"},
  package_data={
      "BIP": [
          "../doc/*",
      ],
  },
  packages=["BIP"],
  install_requires=[
      "CF",
  ],
  scripts=[
    "scripts/BIC",
    "scripts/respread",
    "scripts/spread",
    "scripts/spreadinator",
  ],
)


#
