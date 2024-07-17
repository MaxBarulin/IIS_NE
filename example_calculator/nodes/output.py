from qtpy.QtWidgets import QLabel
from qtpy.QtCore import Qt
from example_calculator.calc_conf import register_node, OP_NODE_OUTPUT
from example_calculator.calc_node_base import CalcNode, CalcGraphicsNode, CalcNodeResult
from nodeeditor.node_content_widget import QDMNodeContentWidget
import os

open_img_out = "output_1.ico"

put = os.path.dirname(__file__)

path_img_out = f'{put}\icons\{open_img_out}'



class CalcOutputContent(QDMNodeContentWidget):
    def initUI(self):
        self.lbl = QLabel("", self)
        self.lbl.setAlignment(Qt.AlignLeft)
        self.lbl.setObjectName(self.node.content_label_objname)


@register_node(OP_NODE_OUTPUT)
class CalcNode_Output(CalcNodeResult):
    icon = path_img_out
    op_code = OP_NODE_OUTPUT
    op_title = "Результат"
    content_label_objname = "calc_node_output"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        self.content = CalcOutputContent(self)
        self.grNode = CalcGraphicsNode(self)

    def evalImplementation(self):
        input_node = self.getInput(0)
        if not input_node:
            self.grNode.setToolTip("Input is not connected")
            self.markInvalid()
            return

        val = input_node.eval()

        if val is None:
            self.grNode.setToolTip("Input is NaN")
            self.markInvalid()
            return
        try:
            self.content.lbl.setText(str(round(val, 4)))
        except:
            self.content.lbl.setText(val)

        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return val
