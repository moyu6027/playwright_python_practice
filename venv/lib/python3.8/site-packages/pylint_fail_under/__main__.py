"""Command line interface for pylint-fail-under."""

import logging
import sys

from pylint.lint import Run

SUCCESS = 0
SCORE_TOO_LOW = 1
NO_SCORE_PARSED = 0


def main():
    """Perform command line operations.

    Parse command line arguments for a fail-under value, execute Pylint, and determine if the
    resulting score is greater than or equal to the fail-under value.

    """
    exit_code = SUCCESS
    cmd_line_args = list(sys.argv[1:])

    logger = logging.getLogger(__name__)

    if cmd_line_args:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

        if "--fail_under" in cmd_line_args:
            # If "--fail_under" appears in command line arguments, extract the value and remove the
            # argument/value elements from the argument list that is passed to Pylint.
            fail_under_index = cmd_line_args.index("--fail_under")
            fail_under_value = float(cmd_line_args[fail_under_index + 1])
            del cmd_line_args[fail_under_index:fail_under_index + 2]
        else:
            logger.warning("no fail_under argument provided, defaulting to 10.0")
            fail_under_value = 10.0

        results = Run(args=cmd_line_args, do_exit=False)
        sys.stdout.flush()

        try:
            score = results.linter.stats["global_note"]
        except KeyError:
            logger.warning("no score parsed from Pylint output")
            exit_code = NO_SCORE_PARSED
        else:
            if score < fail_under_value:
                logger.error("score %s is less than fail-under value %s", score, fail_under_value)
                exit_code = SCORE_TOO_LOW

    else:
        print("usage: pylint-fail-under [--fail_under SCORE] [Pylint Command Line Arguments]")

    return exit_code


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
