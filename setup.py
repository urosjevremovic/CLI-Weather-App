"""
Weather App
-------------

Script for fetching current weather conditions in your city.

You can get it by downloading it directly or by typing:

    $ pip install WeatherApp

After it is installed you can start it by simply typing in your terminal:

    $ current_weather

"""


from setuptools import setup

setup(name='WeatherApp',
      version='0.1',
      description='Fetches current weather conditions in your city',
      long_description=__doc__,
      long_description_content_type='text/markdown',
      url="https://github.com/urosjevremovic/CLI-Weather-App",
      license='MIT',
      author='Uros Jevremovic',
      author_email='jevremovic.uros91@gmail.com',
      packages=['WeatherApp'],
      entry_points={
          "console_scripts": ["current_weather=WeatherApp.CLI_weather_app:main"],
      },
      )

__author__ = 'Uros Jevremovic'
