# ========================
# %%%% MAIN FUNCTION %%%%%
# ========================
def prepare_packages():
    try:
        import nltk
        print(">You have an nltk package install under {} version.".format(nltk.__version__))
        if nltk.__version__ != "3.4.5":
            print("\t>>It is recommended to switch to the 3.4.5 version, as under it the original build took place.")
    except:
        print("You are missing an nltk package.")

    try:
        import kivy
        print(">You have a kivy package install under {} version.".format(kivy.__version__))
        if kivy.__version__ != "1.11.1":
            print("\t>>It is recommended to switch to the 1.11.1 version, as under it the original build took place.")
    except:
        print("You are missing a kivy package.")

# ======================
# %%%% IF __NAME__ %%%%%
# ======================

if __name__ == "__main__":
    prepare_packages()