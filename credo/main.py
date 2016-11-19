import os
import yaml
from credo import __all_paths__ 
from toolz.itertoolz import concat
from toolz.itertoolz import groupby

def template(path):
    return [
        yaml.load(file(os.path.join(path, elem), "r"))
        for elem in os.listdir(path)
        if elem.endswith(".yaml")
        or elem.endswith(".yml")
    ]


def render_markdown(belief_group):
    _type = belief_group.get("type")
    beliefs = "\n\n".join(["""
## {0}

### Summary

{1}
    """.format(elem["title"], elem["summary"])
        for elem in belief_group["data"]
    ])
    print """
# {0}    

{1}
    """.format(_type.title(), beliefs)


def main():
    all_beliefs = groupby("belief", list(concat(concat(map(template, __all_paths__)))))
    by_type = sorted([dict(type=key, data=all_beliefs[key]) for key in all_beliefs])
    for belief in by_type:
        render_markdown(belief)


if __name__ == "__main__":
    main()


