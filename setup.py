from distutils.core import setup

setup(
    name = 'pyautonium',
    packages = ['pyautonium',
                'pyautonium.webdriver',
                'pyautonium.webdriver.chrome',
                'pyautonium.webdriver.firefox',
                ],
    version = '0.0.0',
    description = 'pyautogui + selenium (+ pyocr + google cloud vision)',
    author = 'nabehide',
    author_email = 'temp@temp.com',
    url = 'https://github.com/nabehide/pyautonium',
)
