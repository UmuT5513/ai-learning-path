import argparse, sys
from program import *

mng = TodoManager() # bu mng günlük olarak kullanılabilir. Mesela yarın başka bir mng oluşturup yarının taskları orada saklanır.
def handle_add(args):
    mng.add(task_text=args.text)

def handle_remove(args):
    mng.remove(task_id=args.taskid)

def handle_list(args):
    mng.list()

def mark_done(args):
    mng.mark_done(task_id=args.taskid)

def main():
    parser = argparse.ArgumentParser(prog="program.py", description="Todo System")
    subparsers = parser.add_subparsers(dest='command')
    add_parser = subparsers.add_parser('add', help="Yeni görev ekle")
    add_parser.add_argument("-t", "--text", required=True, type=str, help="taskın açıklaması/içeriği")
    add_parser.add_argument("-d", "--done", default=False, type=bool, help="taskın tamamlanma durumunu belirtir!")
    add_parser.set_defaults(func=handle_add)
    
    remove_parser = subparsers.add_parser('remove', help="Görevler listesinden görev siler.")
    remove_parser.add_argument("-ti", "--taskid", required=True, type=int, help="Silinecek görevin id sini alır.")
    remove_parser.set_defaults(func=handle_remove)
    
    list_parser = subparsers.add_parser('list', help="Görev listesinin güncel durumunu gösterir. Tamamlanmış ise 'tick' tamamlanmamış ise 'cross'.")
    list_parser.set_defaults(func=handle_list)

    done_parser = subparsers.add_parser('done', help="Görevi tamamlandı olarak işaretler.")
    done_parser.add_argument("-ti", "--taskid", required=True, type=int, help="İşaretlenecek görevin ID sini alır.")
    done_parser.set_defaults(func=mark_done)


    args = parser.parse_args()
    if hasattr(args, "func"):
        try:
            args.func(args)
        except Exception as e:
            print(f"Hata: {e}")
            sys.exit(1)
    else:
            parser.print_help()



if __name__=="__main__":
     main()

    