import argparse

parser = argparse.ArgumentParser(description='Run pypefitter to generate a concrete pipeline from the abstract form.')
parser.add_argument('-s', '--src', dest='src', action='store',
                   default='pipeline.pf',
                   help='The source file containing the pipeline declaration. Defaults to \'pipeline.pf\'.')
parser.add_argument('-p', '--provider', dest='provider', action='store',
                   default='jenkins', choices=['jenkins', 'aws'],
                   help='The name of the provider for which the pipeline should be generated. Defaults to \'jenkins\'.')
parser.add_argument('-v', dest='verbosity', action='count',
                   default='-vv',
                   help='The verbosity level of the logging.')
parser.add_argument('-c', '--config', dest='config', action='store',
                   help='The file containing provider-specific configuration. This is used during the transformation of the abstract pipeline into its concrete form for the specified provider.')
args = parser.parse_args()

print(args.src)
print(args.provider)
print(args.verbosity)
print(args.config)
