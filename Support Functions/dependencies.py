# ============================
# %%%% PREPARE ARGUMENTS %%%%%
# ============================
import argparse
from argparse import RawTextHelpFormatter
parser = argparse.ArgumentParser(description = "\t\t\t\tDescription:\n"
                                "--------------------------------------------------------------------------\n"
                                "Use this file to prepare your environment if it is missing certain packages"
                                "in an automated way."
                                "--------------------------------------------------------------------------"
                                formatter_class = RawTextHelpFormatter)

parser.add_arugment("-i", "--install",
                    type = str,
                    metavar = "",
                    help = "Indicate [y] or [yes] if you want to have all needed packages installed in your"
                           "environment for the project to work.")

parser.add_argument("-c", "--check",
                    type = str,
                    metavar = "",
                    help = "Indicate [y] or [yes] if you would like to check whether you have needed packages"
                           "for the project to work on your side.")
args = parser.parse_args()

# ============================
# %%%% PREPARE FUNCTIONS %%%%%
# ============================

def prepare_packages(install = None, check = None):
    """

    :param install: Decides if there is a need to install missing packages
    :param check:  Checks if all the needed packages are present to work with the project
    :return: void
    """
    pass

# ======================
# %%%% IF __NAME__ %%%%%
# ======================

if __name__ == "__main__":
    prepare_packages(args.install, args.check)