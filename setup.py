import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.txt")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "pyjwt",
    "plaster_pastedeploy",
    "pyramid",
    "pyramid_chameleon",
    "pyramid_debugtoolbar",
    "waitress",
    "PyMySQL",
    "bcrypt",
    "alembic",
    "pyramid_retry",
    "pyramid_tm",
    "pyramid-jwt",
    "SQLAlchemy",
    "transaction",
    "zope.sqlalchemy",
]

tests_require = [
    "WebTest",
    "pytest",
    "pytest-cov",
]

setup(
    name="uts_pwl_2023_backend",
    version="0.0",
    description="UTS_PWL_2023_Backend",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="",
    author_email="",
    url="",
    keywords="web pyramid pylons",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        "testing": tests_require,
    },
    install_requires=requires,
    entry_points={
        "paste.app_factory": [
            "main = uts_pwl_2023_backend:main",
        ],
        "console_scripts": [
            "initialize_uts_pwl_2023_backend_db=uts_pwl_2023_backend.scripts.initialize_db:main",
        ],
    },
)
