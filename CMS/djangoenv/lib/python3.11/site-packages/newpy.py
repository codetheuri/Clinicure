""" newpy, created by Edward """

import argparse
from os import makedirs
import os.path
from shutil import rmtree
import pkg_resources
try:
    # Python 2
    from cStringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO

DIST_LOCATION = pkg_resources.resource_filename(__name__, "")
PROJECT_LOCATION = ""
PROJECT_NAME = ""
RESOURCES = os.path.join(DIST_LOCATION, "resources", "")
SETUP_PY = "setup.py"
README = "README.md"
LOGGER = None

def generate_project_dir(force):
    """ if this fails there is no point continuing. Fail fast."""
    print("generating project dir")
    try:
        # attempt to remove it, but don't worry if its not there
        if force:
            try:
                rmtree(PROJECT_LOCATION)
            except IOError:
                pass
        # makedirs exist_ok flag was not used as it isn't
        # python 2.x compatible
        makedirs(PROJECT_LOCATION)
    except OSError:
        print("Could not create project directory, directory "
              "may already exist, please use -f to force or "
              "specify another location")
        exit()

def generate_gitignore():
    print("generating gitignore")
    with open(PROJECT_LOCATION + ".gitignore", "w") as f:
        f.write("*.pyc\n")
        f.write("*.pyo\n")
        f.write("__pycache__\n")

def generate_py(replacements):
    if LOGGER:
        skeleton_file = RESOURCES + "py_skeleton_with_logger.py"
        generate_logger(replacements)
    else:
        skeleton_file = RESOURCES + "py_skeleton.py"

    with open(PROJECT_LOCATION + PROJECT_NAME + ".py", "w") as outfile:
        outfile.write(make_replacements(skeleton_file, replacements))

def generate_logger(replacements):
    """ TODO: The logger format is just a placeholder currently and needs
        improving. Must include name of file that made the log
    """
    logger_file = RESOURCES + "Logger.py"
    with open(PROJECT_LOCATION + "Logger.py", "w") as outfile:
        outfile.write(make_replacements(logger_file, replacements))

def generate_setup_py(replacements):
    with open(PROJECT_LOCATION + SETUP_PY, "w") as outfile:
        outfile.write(make_replacements(RESOURCES + SETUP_PY, replacements))

def generate_init_with_version(replacements):
    with open(PROJECT_LOCATION + "__init__.py", "w") as outfile:
        outfile.write("__version__ = 0.0.1\n")

def generate_readme(replacements):
    with open(PROJECT_LOCATION + README, "w") as outfile:
        outfile.write(make_replacements(RESOURCES + README, replacements))

def make_replacements(infile, replacements):
    with open(infile, "r") as f:
        infile_contents = StringIO(f.read())

    # TODO: could this be more elegant?
    out_buffer = StringIO()
    for out_line in infile_contents:
        for k, v in replacements.items():
            out_line = out_line.replace(k, v)
        out_buffer.write(out_line)
    return out_buffer.getvalue()

def main(args):
    # TODO: significantly improve
    # All fields should be passed to each function as an object or collection
    global PROJECT_LOCATION
    global PROJECT_NAME
    global LOGGER
    PROJECT_LOCATION = os.path.normpath(args.project_location) + os.path.sep
    PROJECT_NAME = os.path.basename(os.path.normpath(PROJECT_LOCATION))
    LOGGER = args.logger

    replacements = {
        "$DESCRIPTION": args.description,
        "$AUTHOR": args.author,
        "$PROJECT_NAME": PROJECT_NAME
    }

    generate_project_dir(args.force)
    generate_gitignore()
    generate_py(replacements)
    generate_setup_py(replacements)
    generate_init_with_version(replacements)
    generate_readme(replacements)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="newpy - for creating new python projects.")
    parser.add_argument("project_location", help="Please supply a directory for your new project. For example just `project_name` if you want it created in the current directory, or `/home/user/project_name` to create it in your home directory")
    parser.add_argument("-f", "--force", help="Force the creation of a new project, overwritting the directory if it exists already.", action="store_true")
    parser.add_argument("-d", "--description", help="Describe your new project", default="sample description")
    parser.add_argument("-a", "--author", help="What's your name?", default="")
    parser.add_argument("-l", "--logger", help="Do you want to create a logger?", action="store_true")
    args = parser.parse_args()

    exit(main(args))
else:
    print("example usage: python -m newpy PROJECT")
