# Copyright (c) 2018 Ultimaker B.V.
# Uranium is released under the terms of the LGPLv3 or higher.

from UM.Application import Application
from UM.OutputDevice.OutputDevicePlugin import OutputDevicePlugin
from UM.i18n import i18nCatalog
from .Dremel3D45OutputDevice import Dremel3D45OutputDevice

catalog = i18nCatalog("uranium")


class Dremel3D45OutputDevicePlugin(OutputDevicePlugin):
    """Implements an OutputDevicePlugin that provides a single instance of Dremel3D45OutputDevice"""

    def __init__(self):
        super().__init__()

        Application.getInstance().getPreferences().addPreference("dremel3d45_network/last_used_type", "")
        Application.getInstance().getPreferences().addPreference("dremel3d45_network/dialog_save_path", "")

    def start(self):
        self.getOutputDeviceManager().addOutputDevice(Dremel3D45OutputDevice())

    def stop(self):
        self.getOutputDeviceManager().removeOutputDevice("dremel_3d45")
