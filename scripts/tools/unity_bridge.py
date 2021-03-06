#!/usr/bin/env python
from .udp_link import UDPLink
import numpy as np
from copy import deepcopy


class UnityBridge(object):
    def __init__(self, ip="BAXTERFLOWERS.local", port=5005):
        self.udp = UDPLink(ip, port)
        self.corresp_dict = {}
        self.base_vector = np.zeros(92)
        self.init_dict()

    def init_dict(self):
        # create the base vector that contains all the offsets
        self.base_vector[18] = 0.16
        self.base_vector[20] = 0.02
        self.base_vector[21] = 0.44
        self.base_vector[22] = -0.03
        self.base_vector[23] = 0.01

        self.base_vector[26] = 0.16
        self.base_vector[28] = 0.02
        self.base_vector[29] = 0.44
        self.base_vector[30] = -0.03
        self.base_vector[31] = 0.01

        self.base_vector[36] = 0.22
        self.base_vector[37] = 0.16
        self.base_vector[38] = -0.09
        self.base_vector[39] = 0.48
        self.base_vector[40] = 0.06
        self.base_vector[41] = 0.02

        self.base_vector[45] = 0.22
        self.base_vector[46] = 0.16
        self.base_vector[47] = -0.09
        self.base_vector[48] = 0.48
        self.base_vector[49] = 0.06
        self.base_vector[50] = 0.02

        self.base_vector[52] = -1.33
        self.base_vector[53] = -0.29
        self.base_vector[54] = 0.64
        self.base_vector[55] = 0.64
        self.base_vector[56] = 0.67
        self.base_vector[57] = -0.46
        self.base_vector[58] = 0.81
        self.base_vector[59] = 0.81
        self.base_vector[60] = 0.67
        self.base_vector[61] = -0.61
        self.base_vector[62] = 0.81
        self.base_vector[63] = 0.81
        self.base_vector[64] = 0.67
        self.base_vector[65] = -0.61
        self.base_vector[66] = 0.81
        self.base_vector[67] = 0.81
        self.base_vector[68] = 0.67
        self.base_vector[69] = -0.46
        self.base_vector[70] = 0.81
        self.base_vector[71] = 0.81
        self.base_vector[72] = -1.33
        self.base_vector[73] = -0.29
        self.base_vector[74] = 0.64
        self.base_vector[75] = 0.64
        self.base_vector[76] = 0.67
        self.base_vector[77] = -0.46
        self.base_vector[78] = 0.81
        self.base_vector[79] = 0.81
        self.base_vector[80] = 0.67
        self.base_vector[81] = -0.61
        self.base_vector[82] = 0.81
        self.base_vector[83] = 0.81
        self.base_vector[84] = 0.67
        self.base_vector[85] = -0.61
        self.base_vector[86] = 0.81
        self.base_vector[87] = 0.81
        self.base_vector[88] = 0.67
        self.base_vector[89] = -0.46
        self.base_vector[90] = 0.81
        self.base_vector[91] = 0.81
        # create the dict for each joints with change of sign and vector index
        joints_dict = {}
        joints_dict['spine_0'] = [1, 1]
        joints_dict['spine_1'] = [0, -1]
        joints_dict['spine_2'] = [2, -1]

        joints_dict['neck_0'] = [7, 1]
        joints_dict['neck_1'] = [6, -1]
        joints_dict['neck_2'] = [8, -1]

        joints_dict['left_knee_0'] = [21, 1]
        joints_dict['right_knee_0'] = [29, 1]

        joints_dict['left_shoulder_0'] = [36, -1]
        joints_dict['left_shoulder_1'] = [37, 1]
        joints_dict['left_shoulder_2'] = [38, -1]

        joints_dict['left_elbow_0'] = [39, 1]

        joints_dict['left_wrist_0'] = [42, 1]
        joints_dict['left_wrist_1'] = [41, -1]
        joints_dict['left_wrist_2'] = [40, -1]

        joints_dict['right_shoulder_0'] = [45, -1]
        joints_dict['right_shoulder_1'] = [46, -1]
        joints_dict['right_shoulder_2'] = [47, 1]

        joints_dict['right_elbow_0'] = [48, -1]

        joints_dict['right_wrist_0'] = [51, -1]
        joints_dict['right_wrist_1'] = [50, -1]
        joints_dict['right_wrist_2'] = [49, 1]

        self.corresp_dict['joints'] = joints_dict

        # create the dict for correspondance link
        self.corresp_dict['links'] = ['spine', 'neck', 'left_shoulder', 'right_shoulder',
                                      'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist']

        # create the dict for channel correspondances
        channel_dict = {}
        channel_dict['/posture'] = 1
        channel_dict['/camera'] = 2
        channel_dict['/model'] = 3
        channel_dict['/risk'] = 4

        self.corresp_dict['channels'] = channel_dict

    def send_joint_values(self, joint_names, values):
        if type(joint_names) is str:
            joint_names = [joint_names]
        if type(values) in [float, int]:
            values = [values]
        assert len(joint_names) == len(values)

        vect = deepcopy(self.base_vector)
        for i in range(len(joint_names)):
            try:
                params = self.corresp_dict['joints'][joint_names[i]]
                vect[params[0]] += (params[1] * values[i]) / (np.pi + vect[params[0]])
            except:
                continue
        chan = self.corresp_dict['channels']['/posture']
        self.udp.send_float_vector(chan, vect.tolist())

    def send_state(self, joint_state):
        self.send_joint_values(joint_state['name'], joint_state['position'])

    def activate_camera(self, cam_id):
        chan = self.corresp_dict['channels']['/camera']
        self.udp.send_int(chan, cam_id)

    def activate_model(self, model_id):
        chan = self.corresp_dict['channels']['/model']
        self.udp.send_int(chan, model_id)

    def send_risk_values(self, risk_dict):
        sent_vect = [risk_dict[f] for f in self.corresp_dict['links']]
        chan = self.corresp_dict['channels']['/risk']
        self.udp.send_float_vector(chan, sent_vect)
