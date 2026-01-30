'''imports: argparse'''
import argparse
import sys

 def greet_user(args):
    """Function to handle the 'greet' command."""
    print(f"Hello, {args.name}!")

def show_status(args):
    """Function to handle the 'status' command."""
    # In a real application, you might run a system command using subprocess here
    print("System status: All systems go!")

"""def command_extra(args)
print("")"""

def main():
    parser = argparse.ArgumentParser(description="A custom CLI tool with multiple commands.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # --- Create the 'greet' command ---
    greet_parser = subparsers.add_parser('greet', help='Greet the specified user')
    greet_parser.add_argument('name', type=str, help='Name of the user to greet')
    greet_parser.set_defaults(func=greet_user) # Set a default function to call

    # --- Create the 'status' command ---
    status_parser = subparsers.add_parser('status', help='Show system status')
    status_parser.set_defaults(func=show_status) # Set a default function to call

    # If no command is provided, show help
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Call the function associated with the command
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

