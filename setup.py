from setuptools import setup, find_packages


setup(name='mgapi',
	version='1.0',
	description='Python wrapper for the MailiGen API',
	classifiers = [
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	keywords = 'email mail mailinglist newsletter',
	author='Juris',
	author_email='suppport@mailigen.com',
	url = 'http://admin.mailigen.lv/settings/api',
	license = 'New BSD License',
	packages=find_packages(),
)
