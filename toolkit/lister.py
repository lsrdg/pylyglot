langs = ['svensk', 'dansk']

def add_lang():
    l = raw_input("Which language would you like to add? ")
    
    langs.append(l)

    print langs

    prompt_lang()


def del_lang():
    ul = raw_input("Which language would you like to remove? ")

    langs.remove(ul)

    print langs

    prompt_lang()


def prompt_lang():
    action = raw_input("Would you like to add a language? ")
    
    if action == 'yes':
        add_lang()
    elif action == 'no':
        del_lang()
    else:
        print "See you!"
        quit()


prompt_lang()
