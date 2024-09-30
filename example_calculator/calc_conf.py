LISTBOX_MIMETYPE = "application/x-item"

OP_NODE_INPUT = 1
OP_NODE_OUTPUT = 2
OP_NODE_ADD = 3
OP_NODE_GROUP = 4
OP_NODE_SUB = 5
OP_NODE_MUL = 6
OP_NODE_GROUP1 = 7
OP_NODE_DIV = 8
OP_NODE_TABLE_1 = 9
OP_NODE_INPUT_1 = 10
OP_NODE_INPUT_2 = 11
OP_NODE_TABLE_4 = 12
OP_NODE_TABLE_6 = 13
OP_NODE_TABLE_7 = 14
OP_NODE_TABLE_3 = 15
OP_NODE_TABLE_2 = 16
OP_NODE_TABLE_5 = 17
OP_NODE_TABLE_8 = 18
OP_NODE_TABLE_9 = 19
OP_NODE_INPUT_TEXT = 20
OP_NODE_INPUT_3 = 21
OP_NODE_TABLE_T1 = 22
OP_NODE_INPUT_5 = 23
OP_NODE_FORMULA = 24
OP_NODE_PEREMEN = 25
OP_NODE_TURN1 = 26
OP_NODE_TEST = 27

CALC_NODES = {
}

class ConfException(Exception): pass
class InvalidNodeRegistration(ConfException): pass
class OpCodeNotRegistered(ConfException): pass


def register_node_now(op_code, class_reference):
    if op_code in CALC_NODES:
        raise InvalidNodeRegistration("Duplicate node registration of '%s'. There is already %s" %(
            op_code, CALC_NODES[op_code]
        ))
    CALC_NODES[op_code] = class_reference


def register_node(op_code):
    def decorator(original_class):
        register_node_now(op_code, original_class)
        return original_class
    return decorator

def get_class_from_opcode(op_code):
    if op_code not in CALC_NODES: raise OpCodeNotRegistered("OpCode '%d' is not registered" % op_code)
    return CALC_NODES[op_code]



# import all nodes and register them
from example_calculator.nodes import *