from setuptools import setup, find_packages

setup(
    name="shapes-calculator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "py-circle-circle=py_circle.main:circle",
            "py-circle-rectangle=py_circle.main:rectangle",
            "py-circle-square=py_circle.main:square",
            "py-circle-triangle=py_circle.main:triangle",
        ],
    },
)
