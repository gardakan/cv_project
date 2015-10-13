from distutils import setup

setup(
    name='db_handler',
    version='0.0.1',
    description='Database and currency conversion tools for cv_project',
    url='http://github.com/gardakan/cv_project',
    author='John Tamm-Buckle'
    author_email='jtammbuckle@gmail.com'
    license='none that I\'m aware of...',
    packages=['db_handler'],
    py_modules=['db_handler', 'currency_converter']
    zip_safe=False
    )
