import argparse
from LoginSystem import *
import sys

def main():
    parser = argparse.ArgumentParser(prog="LoginSystem.py", description="Kullanıcı Giriş Sistemi")
    subparsers = parser.add_subparsers(dest="command")
    register_parser = subparsers.add_parser("register", help="Yeni Kullanıcı Ekle")
    register_parser.add_argument("--username", required=True)
    register_parser.add_argument("--password", required=True)
    register_parser.set_defaults(func=handle_register)

    login_parser = subparsers.add_parser("login", help="Kullanıcı Giriş Yap")
    login_parser.add_argument("--username", required=True)
    login_parser.add_argument("--password", required=True)
    login_parser.set_defaults(func=handle_login)

    args = parser.parse_args()
    if hasattr(args, "func"):
        try:
            args.func(args)
        except Exception as e:
            print(f"Hata: {e}")
            sys.exit(1)
    else:
            parser.print_help()
def handle_register(args):
    username = args.username
    password = args.password
    register(username, password)

def handle_login(args):
    username = args.username
    password = args.password
    login(username, password)

    
if __name__ == "__main__":
    main()