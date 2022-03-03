import os
import sys
from setuptools import setup, find_packages

readme_file = os.path.join(os.path.dirname(__file__), "README.rst")
try:
    long_description = open(readme_file).read()
except IOError as err:
    sys.stderr.write(
        "[ERROR] Cannot find file specified as "
        f"``long_description`` ({readme_file})\n"
    )
    sys.exit(1)

setup(
    name="django-river",
    version="3.3.0",
    author="Ahmet DAL",
    author_email="ceahmetdal@gmail.com",
    packages=find_packages(),
    url="https://github.com/javrasya/django-river.git",
    description="Django Workflow Library",
    long_description=long_description,
    install_requires=[
        "Django",
        "django-mptt",
        "django-cte",
        "django-codemirror2",
    ],
    include_package_data=True,
    zip_safe=False,
    license="BSD",
    platforms=["any"],
)
