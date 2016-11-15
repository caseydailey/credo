import os
import yaml
from credo import __feelings__


def test_feelings_criteria():
    """
    Ensure feeling template syntax is valid
    """
    out = yaml.load(file(os.path.join(__feelings__, "template.yaml"), "r"))
    print out
    assert isinstance(out, list)
    assert all(isinstance(elem, dict) for elem in out)

    all_keys = ["topic", "summary", "caveats", "belief", "title"] 
    assert len(out[0]) == len(all_keys)

    for doc in out:
        for key in all_keys:
            assert key in doc

    assert out[0].get("belief") == "feeling"
