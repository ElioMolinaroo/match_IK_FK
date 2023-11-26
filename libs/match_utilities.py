import json
from pathlib import Path
from maya import cmds

from ..ui import matchData_UI


class Match():

    def __init__(self, 
                 blend_attribute: str, 
                 fk_blend_value: int,
                 ik_blend_value: int,
                 ik_controls: tuple,
                 ik_joints: tuple,
                 fk_controls: tuple,
                 fk_joints: tuple,):

        # Declare variables
        self.blend_attribute = blend_attribute
        self.fk_blend_value = fk_blend_value
        self.ik_blend_value = ik_blend_value
        self.ik_controls = ik_controls
        self.ik_joints = ik_joints
        self.fk_controls = fk_controls
        self.fk_joints = fk_joints


    def IKtoFK(self):

        """Turns the IK limb into an FK"""

        # Create the temp pc list
        parent_constraints = []
        # Iterate over controls to match them
        for i, ctrl in enumerate(self.ik_joints):
            temp_pc = cmds.parentConstraint(ctrl, self.fk_controls[i])[0]
            parent_constraints.append(temp_pc)

        # delete the temp parent constraints
        for pc in parent_constraints:
            cmds.delete(pc)

        # Switch the attribute
        cmds.setAttr(self.blend_attribute, self.fk_blend_value)


    def FKtoIK(self):

        """Turns the FK limb into an IK"""

        # Create the temp pc list
        parent_constraints = []
        # Iterate over controls to match them
        for i, ctrl in enumerate(self.fk_joints):
            temp_pc = cmds.parentConstraint(ctrl, self.ik_controls[i])[0]
            parent_constraints.append(temp_pc)

        # delete the temp parent constraints
        for pc in parent_constraints:
            cmds.delete(pc)

        # Switch the attribute
        cmds.setAttr(self.blend_attribute, self.ik_blend_value)


class MatchData():

    """Ingests some data and spits out a database dictionary."""

    def __init__(self,
                 data):
        self.data = data

        # Create database dict
        self.createDatabaseDict()


    def createDatabaseDict(self):
        # get the blend attribute and the blend values
        blend_attr = "%s.%s" % (self.data[0], self.data[1])
        fk_blend_value = cmds.addAttr(blend_attr, q=1,min=1)
        ik_blend_value = cmds.addAttr(blend_attr, q=1, max=1)

        # Create the dictionary
        self.data_dict = {"blend_attr": blend_attr,
                          "fk_blend_value": fk_blend_value,
                          "ik_blend_value": ik_blend_value,
                          "ik_controls": (self.data[5], self.data[6], self.data[7]), 
                          "ik_joints": (self.data[2], self.data[3], self.data[4]), 
                          "fk_controls": (self.data[11], self.data[12], self.data[13]),
                          "fk_joints": (self.data[8], self.data[9], self.data[10])}

    
    def writeToDatabase(self):
        self.file_name = self.data[0].split('|')[-1] + '.json'
        database_path = Path(Path(__file__).parents[1] / "rigs_data", self.file_name)
        
        json_data = json.dumps(self.data_dict)
        with open(database_path, "w") as file:
            file.write(json_data)
        file.close()


def _databaseProcess(raw_data_list):
        # Process data
        data = []
        for i in raw_data_list:
            data.append(i.text())
        
        # Create class data
        match_data = MatchData(data)

        # Check if any piece of data is empty
        for data in match_data.data:
            if len(data) == 0:
                cmds.error("Missing piece(s) of info")

        # Write the content to the database
        match_data.writeToDatabase()
        # Close the window
        matchData_UI._maya_delete_ui()


def _matchProcess(combo_box):
    # Get the limb
    combo_item = combo_box.currentText() + '.json'
    data_path = Path(Path(__file__).parents[1]) / 'rigs_data' / combo_item

    if len(combo_box.currentText()) == 0:
        cmds.error("No Limb selected, run the Get Data function first")

    # Query limb data
    with open(data_path, "r") as file:
        data = json.load(file)
    file.close()

    # Get current blend value
    current_blend_value = cmds.getAttr(data['blend_attr'])

    # Create matcher object
    matcher = Match(data['blend_attr'], data['fk_blend_value'], data['ik_blend_value'], data['ik_controls'], data['ik_joints'], data['fk_controls'], data['fk_joints'])

    # Figure out which way it should go
    if current_blend_value == data['fk_blend_value']:
        matcher.FKtoIK()
    elif current_blend_value == data['ik_blend_value']:
        matcher.IKtoFK()
    else:
        pass
