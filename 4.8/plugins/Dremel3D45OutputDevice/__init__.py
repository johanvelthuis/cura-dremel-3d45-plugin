# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the LGPLv3 or higher.

from . import Dremel3D45OutputDevicePlugin


def getMetaData():
    return {
    }

def register(app):
    return { "output_device": Dremel3D45OutputDevicePlugin.Dremel3D45OutputDevicePlugin() }
