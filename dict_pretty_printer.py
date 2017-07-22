_INDENT_CHAR = ' '
_KEY_VALUE_SEPERATOR_CHAR = ':'


class DictPrettyPrinter:
    def __init__(self):
        pass

    def printItems(self, dictObj, indent):
        it = dictObj.iteritems()
        for k,v in it:
            if isinstance(v, dict):
                print _INDENT_CHAR*indent , k, _KEY_VALUE_SEPERATOR_CHAR
                self.printItems(v, indent+indent)
            else:
                print _INDENT_CHAR*indent , k, _KEY_VALUE_SEPERATOR_CHAR, v

class ListPrettyPrinter:
    def printItems(self, listObj, indent):
        for item in listObj:
            if isinstance(item, list):
                self.printItems(item, indent+indent)
            else:
                print _INDENT_CHAR*indent, item

if __name__ == "__main__":
    indent = 3

    test_dict = {'data':{'id':1,'title':'home','address':{'street':'some road','city':'anycity','postal':'somepostal', 'telephone':{'home':'xxx','offie':'yyy'}}}}

    test_list = ['data', ['id', 'title','address', ['street', ' road', 'city','postal', 'telephone', ['home','offie']]]]

    print "Testing DictPrettyPrinter:\n", "-"*80
    dpp = DictPrettyPrinter()
    dpp.printItems(test_dict, indent)

    print "\n\nTesting ListPrettyPrinter:\n", "-"*80
    dpp = ListPrettyPrinter()
    dpp.printItems(test_list ,indent)
