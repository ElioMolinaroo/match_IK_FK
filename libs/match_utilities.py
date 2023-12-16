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

    """Ingests some data and spits out a database node (based on maya network node)."""

    def __init__(self,
                 data):
        self.data = data

        # Create database dict
        self.createDatabaseNode()


    def createDatabaseNode(self):
        # get the blend attribute and the blend values
        blend_attr = "%s.%s" % (self.data[0], self.data[1])
        fk_blend_value = cmds.addAttr(blend_attr, q=1,min=1)
        ik_blend_value = cmds.addAttr(blend_attr, q=1, max=1)

        # Create the dictionary
        self.data_dict = {"blend_attr": blend_attr,
                          "fk_blend_value": fk_blend_value,
                          "ik_blend_value": ik_blend_value,
                          "ik_control_01": self.data[5],
                          "ik_control_02": self.data[6], 
                          "ik_control_03": self.data[7], 
                          "ik_joint_01": self.data[2],
                          "ik_joint_02": self.data[3], 
                          "ik_joint_03": self.data[4], 
                          "fk_control_01": self.data[11],
                          "fk_control_02": self.data[12], 
                          "fk_control_03": self.data[13], 
                          "fk_joint_01": self.data[8],
                          "fk_joint_02": self.data[9], 
                          "fk_joint_03": self.data[10]}

        # Create the node
        self.data_node = cmds.createNode('network', n=self.data[0]+'_DATA')

        # Add the attributes to the node
        for i in self.data_dict:
            data_attr = cmds.addAttr(self.data_node, sn=i, dt='string')
            cmds.setAttr("%s.%s"%(self.data_node, i), str(self.data_dict[i]), type='string')


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

        # Close the window
        matchData_UI._maya_delete_ui()


def _matchProcess(combo_box):
    # Get the limb
    combo_item = combo_box.currentText() + '_DATA'
    #data_path = Path(Path(__file__).parents[1]) / 'rigs_data' / combo_item

    if len(combo_box.currentText()) == 0:
        cmds.error("No Limb selected, run the Get Data function first")

    # Query limb data
    data_query = {"blend_attr": cmds.getAttr(combo_item+'.blend_attr'),
                          "fk_blend_value": float(cmds.getAttr(combo_item+'.fk_blend_value')),
                          "ik_blend_value": float(cmds.getAttr(combo_item+'.ik_blend_value')),
                          "ik_controls": (cmds.getAttr(combo_item+'.ik_control_01'), cmds.getAttr(combo_item+'.ik_control_02'), cmds.getAttr(combo_item+'.ik_control_03')), 
                          "ik_joints": (cmds.getAttr(combo_item+'.ik_joint_01'), cmds.getAttr(combo_item+'.ik_joint_02'), cmds.getAttr(combo_item+'.ik_joint_03')), 
                          "fk_controls": (cmds.getAttr(combo_item+'.fk_control_01'), cmds.getAttr(combo_item+'.fk_control_02'), cmds.getAttr(combo_item+'.fk_control_03')),
                          "fk_joints": (cmds.getAttr(combo_item+'.fk_joint_01'), cmds.getAttr(combo_item+'.fk_joint_02'), cmds.getAttr(combo_item+'.fk_joint_03'))}

    # Get current blend value
    current_blend_value = cmds.getAttr(data_query['blend_attr'])

    # Create matcher object
    matcher = Match(data_query['blend_attr'], data_query['fk_blend_value'], data_query['ik_blend_value'], data_query['ik_controls'], data_query['ik_joints'], data_query['fk_controls'], data_query['fk_joints'])

    # Figure out which way it should go
    if current_blend_value == data_query['fk_blend_value']:
        matcher.FKtoIK()
    elif current_blend_value == data_query['ik_blend_value']:
        matcher.IKtoFK()
    else:
        pass
