#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import requests as req
from os.path import exists


def get_filename(qid, url, category="algorithms"):
    return "./_leetcode/{}-{}.md".format(qid, url)

def format_item(item):
    mapping = {
        "frontend_question_id": "id",
        "question__title": "title",
        "question__title_slug": "url",
        "question_id": "qid",
        "total_acs": "acs",
        "total_submitted": "sbs",
    }
    res = {mapping[key]: item["stat"][key] for key in mapping}
    res["difficulty"] = ["", "Easy", "Medium", "Hard"][item["difficulty"]["level"]]
    res["acceptance"] = "{:.1f}%".format(res["acs"] * 100.0 / res["sbs"])
    res["editorial"] = item["status"] == "ac"
    res["editorial"] = "true" if exists(get_filename(res["qid"], res["url"])) else "false"
    if item.get("paid_only", False):
        res["editorial"] = "locked"
    return res


def output_item(item):
    keys = ["id", "title", "acceptance", "difficulty", "editorial", "url"]
    return "  - " + "\n    ".join(
        [
            "{}: {}".format(
                key, item[key] if ":" not in str(item[key]) else '"{}"'.format(item[key])
            ) for key in keys
        ]
    )


def get_string(category="algorithms"):
    base_url = "https://leetcode.com/api/problems/{}/"
    keys = ["all", "algorithms", "shell", "database"]
    url_mapping = {key: base_url.format(key) for key in keys}
    all_datas = req.get(url_mapping[category]).json()
    out_data = [format_item(item) for item in all_datas["stat_status_pairs"]]
    out_string = "{}:\n".format(category) + "\n\n".join([output_item(item) for item in out_data][::-1])
    return out_string

if __name__ == "__main__":
    categories = ["algorithms", "shell", "database"]
    for cate in categories:
        print(get_string(cate) + "\n\n")
