from setuptools import setup, find_packages

version = "1.0"

setup(name="css.fontawesome",
      version=version,
      description="fanstatic font awesome",
      long_description=open("README.rst").read(),
      classifiers=[],
      keywords="fanstatic bootstrap font-awesome fontawesome",
      author="Jason K\xc3\xb6lker",
      author_email="jason@koelker.net",
      url="https://github.com/jkoelker/css.fontawesome",
      license="CC BY 3.0",
      packages=find_packages(),
      namespace_packages=["css"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "fanstatic",
          "js.bootstrap"
      ],
      entry_points={
          "fanstatic.libraries": [
              "fontawesome = css.fontawesome:library"
              ],
          },
      )
