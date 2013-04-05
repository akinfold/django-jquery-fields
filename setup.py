from distutils.core import setup

version = '0.0.1'

setup(
    name='django-jquery-fields',
    version=version,
    packages=['jquery_fields'],
    url='https://bitbucket.org/Akinfold/django-jquery-fields',
    license='MIT License',
    author='Roman Akinfold',
    author_email='akinfold@gmail.com',
    description='Small collection of Django form fields and widgets using JQuery.',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
