from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    print(parser.read(filename))
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        print(params)
        for param in params:
            print(param[0], param[1])
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


print(config())
