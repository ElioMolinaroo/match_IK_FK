import sys
import os
from pathlib import Path

from ..ui import matchData_UI
from ..libs import match_utilities
from importlib import reload
reload(match_utilities)

sys.dont_write_bytecode = True  # Avoid writing .pyc files

# ----------------------------------------------------------------------
# Environment detection
# ----------------------------------------------------------------------

try:
    import maya.cmds as cmds
    MAYA = True
except ImportError:
    MAYA = False

STANDALONE = False
if not MAYA:
    STANDALONE = True


# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------

# Window title and object names
WINDOW_TITLE = 'Match IK FK 1.0'
WINDOW_OBJECT = 'matchIkFk'

# Maya-specific
DOCK_WITH_MAYA_UI = False

# Repository path
REPO_PATH = str(Path(__file__).parent)

# Palette filepath
PALETTE_FILEPATH = os.path.join(
    REPO_PATH, 'boilerdata', 'qpalette_maya2016.json')

# Full path to where .ui files are stored
UI_PATH = os.path.join(REPO_PATH, 'boilerdata')


# ----------------------------------------------------------------------
# Set up Python modules access
# ----------------------------------------------------------------------

# Enable access to boilerlib (Qt.py, mayapalette)
if REPO_PATH not in sys.path:
    sys.path.append(REPO_PATH)

# ----------------------------------------------------------------------
# Main script
# ----------------------------------------------------------------------

from boilerlib.Qt import QtWidgets
from boilerlib.Qt import QtCore
from boilerlib.Qt import QtGui
from boilerlib.Qt import QtCompat

from boilerlib import mayapalette


class mainUI(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)

        # Set object name and window title
        self.setObjectName(WINDOW_OBJECT)
        self.setWindowTitle(WINDOW_TITLE)

        # Window type
        self.setWindowFlags(QtCore.Qt.Window)

        # Window resizing
        self.setFixedSize(260, 145)

        if MAYA:
            # Makes Maya perform magic which makes the window stay
            # on top in OS X and Linux. As an added bonus, it'll
            # make Maya remember the window position
            #self.setProperty("saveWindowPref", True)
            pass

        # Filepaths
        main_window_file = os.path.join(UI_PATH, 'main.ui')

        # Load UIs
        self.main_widget = QtCompat.load_ui(main_window_file)  # Main window UI

        # Set the main widget
        self.setCentralWidget(self.main_widget)

        # Add the available rigs data to the combo box
        rigs_data_path = str(Path(__file__).parents[1] / 'rigs_data')
        data_files = os.listdir(rigs_data_path)
        rigs_data_list = [data.removesuffix('.json') for data in data_files]
        self.main_widget.limb_comboBox.addItems(rigs_data_list)

        # Signals
        self.main_widget.getData_button.clicked.connect(lambda: matchData_UI.run_maya())
        self.main_widget.match_button.clicked.connect(lambda: match_utilities._matchProcess(self.main_widget.limb_comboBox))


# ----------------------------------------------------------------------
# DCC application helper functions
# ----------------------------------------------------------------------

def _maya_delete_ui():
    """Delete existing UI in Maya"""
    if cmds.window(WINDOW_OBJECT, q=True, exists=True):
        cmds.deleteUI(WINDOW_OBJECT)  # Delete window
    if cmds.dockControl('MayaWindow|' + WINDOW_TITLE, q=True, ex=True):
        cmds.deleteUI('MayaWindow|' + WINDOW_TITLE)  # Delete docked window


def _maya_main_window():
    """Return Maya's main window"""
    for obj in QtWidgets.QApplication.topLevelWidgets():
        if obj.objectName() == 'MayaWindow':
            return obj
    raise RuntimeError('Could not find MayaWindow instance')


# ----------------------------------------------------------------------
# Run functions
# ----------------------------------------------------------------------

def run_maya():
    """Run in Maya"""
    _maya_delete_ui()  # Delete any existing existing UI
    boil = mainUI(parent=_maya_main_window())

    # Makes Maya perform magic which makes the window stay
    # on top in OS X and Linux. As an added bonus, it'll
    # make Maya remember the window position
    #boil.setProperty("saveWindowPref", True)

    if not DOCK_WITH_MAYA_UI:
        boil.show()  # Show the UI
    elif DOCK_WITH_MAYA_UI:
        allowed_areas = ['right', 'left']
        cmds.dockControl(WINDOW_TITLE, label=WINDOW_TITLE, area='right',
                         content=WINDOW_OBJECT, allowedArea=allowed_areas)
