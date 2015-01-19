def main():
    # read in CLI arguments
    args = parse_cli()
    print args.numLevels
    print args.outputFile

def parse_cli():
    import argparse as ap

    par = ap.ArgumentParser(description="Generate rectilinear 3D mesh as "
                            "specified on the command line.",
                            formatter_class=ap.ArgumentDefaultsHelpFormatter)
    par.add_argument("--levels",
                     dest="numLevels",
                     help="number of tree levels that should be generated. should be a positive integer.",
                     type=int,
                     default=4)
    par.add_argument("--output",
                     dest="outputFile",
                     help="name of text file where the generated tree will be written",
                     default="tree.txt")

    args = par.parse_args()

    return args

main()