from pemi import __path__ as mod_path
import os


def get_abs_ui_path(ui_file: str):
    return os.path.join(os.path.abspath(mod_path[0]), f"ui/{ui_file}")


MON_VARS = {
    "FBP": "load_current",
    "FBP_DCLink": "dclink_voltage",
    "FAP": "load_current",
    "FAP_4P": "load_current",
    "FAP_2P2S": "load_current",
    "FAP_225A": "load_current",
    "FAC_2P_ACDC_IMAS": "rectifier_current",
    "FAC_2P_DCDC_IMAS": "load_current",
}

BASIC_UI = get_abs_ui_path("basic.ui")
LOCK_UI = get_abs_ui_path("lock.ui")
MAIN_UI = get_abs_ui_path("main.ui")
PARAM_DIALOG_UI = get_abs_ui_path("param_dialog.ui")
PARAM_UI = get_abs_ui_path("param.ui")

CLOSE_CIRCLE_RES = get_abs_ui_path("res/close-circle.png")

CLOSE_BTN_STYLE = "QTabBar::close-button {image: url(" + CLOSE_CIRCLE_RES + ")}"