
"""
The command-line interface for the downloader
"""
import argparse
from .bootstrapper import bootstrap


def main():
    parser = argparse.ArgumentParser(
        description=("A problem bootstrapper for working on projecteuler "
                     "problems in a jupyter notebook.")
    )
    parser.add_argument(
        "problem", type=str,
        help="The number of the problem you'd like to work on."
    )
    parser.add_argument(
        "--output", "-o",
        help=("Destination local file path. If not set, the resource "
                "will be downloaded to the current working directory, with filename "
                "same as the basename of the URL")
    )
    args = parser.parse_args()
    bootstrap(args.problem, file_path=args.output)
    print("Problem ready to solve!")

if __name__ == "__main__":
    main()