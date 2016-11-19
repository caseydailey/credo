import os
__author__ = "Jon Staples"
__version__ = "0.0.1"
__project_root__ = os.path.dirname(os.path.abspath(__file__))
__beliefs__ = os.path.join(__project_root__, "beliefs")
__feelings__ = os.path.join(__beliefs__, "feelings")
__opinions__ = os.path.join(__beliefs__, "opinions")
__stances__ = os.path.join(__beliefs__, "stances")
__all_paths__ = [
    os.path.join(__beliefs__, dirname)
    for dirname in os.listdir(__beliefs__)
]
