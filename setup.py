import setuptools


setuptools.setup(
    name="ozon3",
    author="Milind Sharma",
    author_email="milindsharma8@gmail.com",
    keywords=["aqi", "air quality", "world air quality", "api", "open source"],
    description="A package to get air quality data using the WAQI API",
    license="GPLv3+",
    url="https://github.com/Milind220/Ozone",
    version="1.1.0",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy; python_version>='3'",
        "pandas; python_version>='3'",
        "requests; python_version>='3'",
        "openpyxl; python_version>='3'",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
