import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as candidates:
        res = json.load(candidates)
    return res


def load_candidates_from_json():
    return [i['name'] for i in load_candidates()]


def get_candidate_by_id(candidate_id):
    return load_candidates()[candidate_id-1]


def get_candidates_by_name(candidate_name):
    return [i for i in load_candidates() if candidate_name.lower() in i['name'].lower()]


def get_candidates_by_skill(skill_name):
    return [i for i in load_candidates() if skill_name.lower() in i['skills']]
