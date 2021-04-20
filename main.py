from app_factories import make_root,make_display,make_label,make_buttons
from app_class import Assistente


def main():
    root = make_root()
    display = make_display(root)
    label = make_label(root)
    buttons = make_buttons(root,starting_row=3)
    assistente = Assistente(root,label,display,buttons)
    assistente.start()


if __name__ == '__main__':
    main()