from setuptools import setup

version = '1.0.1'

setup(name='google_chat_handler',
      version=version,
      description="Log data in google chat",
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Google Chat Handler, google chat logging',
      author='Anand Tripathi',
      author_email='anand.tripathi507@gmail.com',
      url='https://github.com/anandtripathi5/google-chat-handler.git',
      packages=['google_chat_handler'],
      install_requires=[
          'httplib2',
      ],
      zip_safe=True
      )
