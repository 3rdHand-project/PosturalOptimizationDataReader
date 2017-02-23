from time import sleep
from .unity_bridge import UnityBridge
import json
from os.path import join


class DataPlayer(object):
    def __init__(self, id_user, ip_interface, port):
        self.bridge = UnityBridge(ip=ip_interface, port=port)
        # get the gender from the survey to set the correct model
        self.set_model(id_user)
        self.score_range = {}
        self.score_range['spine'] = [0, 7]
        self.score_range['neck'] = [0, 4]
        self.score_range['left_shoulder'] = [0, 8]
        self.score_range['right_shoulder'] = [0, 8]
        self.score_range['left_elbow'] = [0, 5]
        self.score_range['right_elbow'] = [0, 5]
        self.score_range['left_wrist'] = [0, 5]
        self.score_range['right_wrist'] = [0, 5]
        self.offset_min = 0.
        self.offset_max = 0.6

    def set_model(self, id_user):
        with open(join('..', 'results', 'user_study_dataset', 'survey.json')) as datafile:
            survey_data = json.load(datafile)
        i = 0
        while i < len(survey_data):
            if str(survey_data[i]['id']) == id_user:
                user_gender = survey_data[i]['Gender']
                break
            i += 1
        if user_gender == "M":
            id_model = 0
        else:
            id_model = 1
        self.bridge.activate_model(id_model)

    def replay_data(self, data):
        for i, state in enumerate(data['states']):
            # send the posture state
            self.bridge.send_state(state)
            # get the posture score
            reba_values = {}
            for key, value in self.score_range.iteritems():
                s_range = self.score_range[key][1]
                pourcent_reba = min((data["posture_score"][key][i] - self.offset_min * s_range) /
                                    ((self.offset_max - self.offset_min) * s_range), 1.)
                reba_values[key] = pourcent_reba
            # send the posture score
            self.bridge.send_risk_values(reba_values)
            sleep(0.05)
        return 0
