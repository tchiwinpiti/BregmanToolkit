import os, sys, glob
from matplotlib import pylab
import bregman
import os.path

from bregman.features import *
from bregman.segment import *
from bregman.audiodb import *
from bregman.testsignal import *
from bregman.psychoacoustics import *
from bregman.tuning import *
from bregman.sound import *
from bregman.plca import *
from bregman.distance import *
from bregman.classifier import *
from bregman.error import *
from bregman.beat import *

from bregman import features
from bregman import segment
from bregman import testsignal
from bregman import psychoacoustics
from bregman import tuning
from bregman import sound
from bregman import plca
from bregman import distance
from bregman import classifier
from bregman import error
from bregman import beat

sep = os.path.sep
bregman_data_root = os.path.split(bregman.__file__)[0]
examples_dir = os.path.join(bregman_data_root, "examples" + sep)
audio_dir = os.path.join(bregman_data_root, "audio" + sep)
sys.path.append(examples_dir)


def get_tutorials():
    """
    print and return a list of tutorials in the bregman/examples folder
    """
    tlist = glob.glob(os.path.join(examples_dir, "*.py"))
    tlist.sort()
    return tlist
