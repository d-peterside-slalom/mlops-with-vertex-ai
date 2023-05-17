import setuptools

REQUIRED_PACKAGES = [
    "google-cloud-aiplatform==1.13.1",
    "tensorflow-transform==1.13.0",
    "tensorflow-data-validation==1.13.0",
    "cloudml-hypertune==0.1.0.dev6"
]

setuptools.setup(
    name="executor",
    version="0.0.1",
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"src": ["raw_schema/schema.pbtxt"]},
)
