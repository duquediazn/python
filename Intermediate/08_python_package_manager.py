### Python Package Manager ###

# PIP https://pypi.org

# Instalación de PIP y paquetes desde consola: 

# pip install pip # Windows:  py -m pip install
# pip --version # Windows: py -m pip --version

# pip install numpy # Windows: py -m pip install numpy

# pip install pandas # Windows: py -m pip install pandas

# pip list # Windows: py -m pip lsit
# pip uninstall pandas # Windows: py -m pip uninstall pandas
# pip show numpy # Windows: py -m pip show numpy

# pip install requests # Windows: py -m pip install requests

import pandas #https://pandas.pydata.org/
#from mypackage import arithmetics
import requests
import numpy #https://numpy.org/

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array)) # <class 'numpy.ndarray'>

print(numpy_array * 2) # [ 70  48 124 104  60  60  34]



response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response) # <Response [200]>
print(response.status_code) # 200
print(response.json())

# Arithmetics Package


#print(arithmetics.sum_two_values(1, 4))