'''ESTE PROGRAMA TIENE COMO OBJETIVO FACILITAR EL RECOPILAR LA INFORMACION DE LIBRERIAS'''
import matplotlib as mat #MODULO
import matplotlib.pyplot as plt # MODULO
import numpy as np #MODULO
import time #MODULO
import requests #MODULO DE API REQUESTS
import sys
from PIL import ImageTk, Image, ImageDraw
import json
from src.api.altitude import get_altitude
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import simplekml