# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tfnev_codeepneat_mainwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_genome_analysis = QtWidgets.QWidget(self.centralwidget)
        self.widget_genome_analysis.setGeometry(QtCore.QRect(60, 10, 930, 660))
        self.widget_genome_analysis.setObjectName("widget_genome_analysis")
        self.ga_vline_1 = QtWidgets.QFrame(self.widget_genome_analysis)
        self.ga_vline_1.setGeometry(QtCore.QRect(450, 0, 20, 660))
        self.ga_vline_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.ga_vline_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ga_vline_1.setObjectName("ga_vline_1")
        self.ga_hline_1 = QtWidgets.QFrame(self.widget_genome_analysis)
        self.ga_hline_1.setGeometry(QtCore.QRect(0, 320, 460, 20))
        self.ga_hline_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.ga_hline_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ga_hline_1.setObjectName("ga_hline_1")
        self.ga_list_generations = QtWidgets.QListWidget(self.widget_genome_analysis)
        self.ga_list_generations.setGeometry(QtCore.QRect(10, 370, 440, 290))
        self.ga_list_generations.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ga_list_generations.setObjectName("ga_list_generations")
        self.ga_lbl_list_heading = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_list_heading.setGeometry(QtCore.QRect(60, 340, 340, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ga_lbl_list_heading.setFont(font)
        self.ga_lbl_list_heading.setObjectName("ga_lbl_list_heading")
        self.ga_widget_genome_visualization = QtWidgets.QWidget(self.widget_genome_analysis)
        self.ga_widget_genome_visualization.setGeometry(QtCore.QRect(470, 0, 460, 460))
        self.ga_widget_genome_visualization.setObjectName("ga_widget_genome_visualization")
        self.ga_lbl_genome_id = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_id.setGeometry(QtCore.QRect(470, 465, 460, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ga_lbl_genome_id.setFont(font)
        self.ga_lbl_genome_id.setAlignment(QtCore.Qt.AlignCenter)
        self.ga_lbl_genome_id.setObjectName("ga_lbl_genome_id")
        self.ga_lbl_genome_fitness = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_fitness.setGeometry(QtCore.QRect(470, 490, 170, 20))
        self.ga_lbl_genome_fitness.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_fitness.setObjectName("ga_lbl_genome_fitness")
        self.ga_lbl_genome_bp_id = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_bp_id.setGeometry(QtCore.QRect(470, 515, 170, 20))
        self.ga_lbl_genome_bp_id.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_bp_id.setObjectName("ga_lbl_genome_bp_id")
        self.ga_lbl_genome_assign_mod = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_assign_mod.setGeometry(QtCore.QRect(470, 540, 170, 20))
        self.ga_lbl_genome_assign_mod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_assign_mod.setObjectName("ga_lbl_genome_assign_mod")
        self.ga_lbl_genome_out_layers = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_out_layers.setGeometry(QtCore.QRect(470, 565, 170, 20))
        self.ga_lbl_genome_out_layers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_out_layers.setObjectName("ga_lbl_genome_out_layers")
        self.ga_lbl_genome_input_shape = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_input_shape.setGeometry(QtCore.QRect(470, 590, 170, 20))
        self.ga_lbl_genome_input_shape.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_input_shape.setObjectName("ga_lbl_genome_input_shape")
        self.ga_lbl_genome_dtype = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_dtype.setGeometry(QtCore.QRect(470, 615, 170, 20))
        self.ga_lbl_genome_dtype.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_dtype.setObjectName("ga_lbl_genome_dtype")
        self.ga_lbl_genome_orig_gen = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_orig_gen.setGeometry(QtCore.QRect(470, 640, 170, 20))
        self.ga_lbl_genome_orig_gen.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_orig_gen.setObjectName("ga_lbl_genome_orig_gen")
        self.ga_lbl_genome_fitness_value = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_fitness_value.setGeometry(QtCore.QRect(640, 490, 290, 20))
        self.ga_lbl_genome_fitness_value.setText("")
        self.ga_lbl_genome_fitness_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_fitness_value.setObjectName("ga_lbl_genome_fitness_value")
        self.ga_lbl_genome_assign_mod_area = QtWidgets.QScrollArea(self.widget_genome_analysis)
        self.ga_lbl_genome_assign_mod_area.setGeometry(QtCore.QRect(640, 540, 290, 25))
        self.ga_lbl_genome_assign_mod_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ga_lbl_genome_assign_mod_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ga_lbl_genome_assign_mod_area.setWidgetResizable(True)
        self.ga_lbl_genome_assign_mod_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ga_lbl_genome_assign_mod_area.setObjectName("ga_lbl_genome_assign_mod_area")
        self.ga_lbl_genome_assign_mod_widget = QtWidgets.QWidget()
        self.ga_lbl_genome_assign_mod_widget.setGeometry(QtCore.QRect(0, 0, 290, 25))
        self.ga_lbl_genome_assign_mod_widget.setObjectName("ga_lbl_genome_assign_mod_widget")
        self.ga_lbl_genome_assign_mod_layout = QtWidgets.QVBoxLayout(self.ga_lbl_genome_assign_mod_widget)
        self.ga_lbl_genome_assign_mod_layout.setContentsMargins(0, 2, 10, 0)
        self.ga_lbl_genome_assign_mod_layout.setObjectName("ga_lbl_genome_assign_mod_layout")
        self.ga_lbl_genome_assign_mod_value = QtWidgets.QLabel(self.ga_lbl_genome_assign_mod_widget)
        self.ga_lbl_genome_assign_mod_value.setText("")
        self.ga_lbl_genome_assign_mod_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ga_lbl_genome_assign_mod_value.setWordWrap(True)
        self.ga_lbl_genome_assign_mod_value.setObjectName("ga_lbl_genome_assign_mod_value")
        self.ga_lbl_genome_assign_mod_layout.addWidget(self.ga_lbl_genome_assign_mod_value)
        self.ga_lbl_genome_assign_mod_area.setWidget(self.ga_lbl_genome_assign_mod_widget)
        self.ga_lbl_genome_bp_id_value = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_bp_id_value.setGeometry(QtCore.QRect(640, 515, 290, 20))
        self.ga_lbl_genome_bp_id_value.setText("")
        self.ga_lbl_genome_bp_id_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_bp_id_value.setObjectName("ga_lbl_genome_bp_id_value")
        self.ga_lbl_genome_out_layers_area = QtWidgets.QScrollArea(self.widget_genome_analysis)
        self.ga_lbl_genome_out_layers_area.setGeometry(QtCore.QRect(640, 565, 290, 25))
        self.ga_lbl_genome_out_layers_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ga_lbl_genome_out_layers_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ga_lbl_genome_out_layers_area.setWidgetResizable(True)
        self.ga_lbl_genome_out_layers_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ga_lbl_genome_out_layers_area.setObjectName("ga_lbl_genome_out_layers_area")
        self.ga_lbl_genome_out_layers_widget = QtWidgets.QWidget()
        self.ga_lbl_genome_out_layers_widget.setGeometry(QtCore.QRect(0, 0, 290, 25))
        self.ga_lbl_genome_out_layers_widget.setObjectName("ga_lbl_genome_out_layers_widget")
        self.ga_lbl_genome_out_layers_layout = QtWidgets.QVBoxLayout(self.ga_lbl_genome_out_layers_widget)
        self.ga_lbl_genome_out_layers_layout.setContentsMargins(0, 3, 10, 0)
        self.ga_lbl_genome_out_layers_layout.setObjectName("ga_lbl_genome_out_layers_layout")
        self.ga_lbl_genome_out_layers_value = QtWidgets.QLabel(self.ga_lbl_genome_out_layers_widget)
        self.ga_lbl_genome_out_layers_value.setText("")
        self.ga_lbl_genome_out_layers_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ga_lbl_genome_out_layers_value.setWordWrap(True)
        self.ga_lbl_genome_out_layers_value.setObjectName("ga_lbl_genome_out_layers_value")
        self.ga_lbl_genome_out_layers_layout.addWidget(self.ga_lbl_genome_out_layers_value)
        self.ga_lbl_genome_out_layers_area.setWidget(self.ga_lbl_genome_out_layers_widget)
        self.ga_lbl_genome_input_shape_value = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_input_shape_value.setGeometry(QtCore.QRect(640, 590, 290, 20))
        self.ga_lbl_genome_input_shape_value.setText("")
        self.ga_lbl_genome_input_shape_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_input_shape_value.setObjectName("ga_lbl_genome_input_shape_value")
        self.ga_lbl_genome_dtype_value = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_dtype_value.setGeometry(QtCore.QRect(640, 615, 290, 20))
        self.ga_lbl_genome_dtype_value.setText("")
        self.ga_lbl_genome_dtype_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_dtype_value.setObjectName("ga_lbl_genome_dtype_value")
        self.ga_lbl_genome_orig_gen_value = QtWidgets.QLabel(self.widget_genome_analysis)
        self.ga_lbl_genome_orig_gen_value.setGeometry(QtCore.QRect(640, 640, 290, 20))
        self.ga_lbl_genome_orig_gen_value.setText("")
        self.ga_lbl_genome_orig_gen_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ga_lbl_genome_orig_gen_value.setObjectName("ga_lbl_genome_orig_gen_value")
        self.widget_mod_bp_analysis = QtWidgets.QWidget(self.centralwidget)
        self.widget_mod_bp_analysis.setGeometry(QtCore.QRect(60, 10, 930, 660))
        self.widget_mod_bp_analysis.setObjectName("widget_mod_bp_analysis")
        self.mba_hline_1 = QtWidgets.QFrame(self.widget_mod_bp_analysis)
        self.mba_hline_1.setGeometry(QtCore.QRect(0, 300, 460, 20))
        self.mba_hline_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.mba_hline_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mba_hline_1.setObjectName("mba_hline_1")
        self.mba_vline_1 = QtWidgets.QFrame(self.widget_mod_bp_analysis)
        self.mba_vline_1.setGeometry(QtCore.QRect(450, 0, 20, 660))
        self.mba_vline_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.mba_vline_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mba_vline_1.setObjectName("mba_vline_1")
        self.mba_list_generations = QtWidgets.QListWidget(self.widget_mod_bp_analysis)
        self.mba_list_generations.setGeometry(QtCore.QRect(10, 30, 215, 270))
        self.mba_list_generations.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.mba_list_generations.setObjectName("mba_list_generations")
        self.mba_list_members = QtWidgets.QListWidget(self.widget_mod_bp_analysis)
        self.mba_list_members.setGeometry(QtCore.QRect(235, 30, 215, 270))
        self.mba_list_members.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.mba_list_members.setObjectName("mba_list_members")
        self.mba_lbl_heading_generations = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_heading_generations.setGeometry(QtCore.QRect(10, 0, 215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mba_lbl_heading_generations.setFont(font)
        self.mba_lbl_heading_generations.setObjectName("mba_lbl_heading_generations")
        self.mba_lbl_heading_members = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_heading_members.setGeometry(QtCore.QRect(235, 0, 215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mba_lbl_heading_members.setFont(font)
        self.mba_lbl_heading_members.setObjectName("mba_lbl_heading_members")
        self.mba_widget_module = QtWidgets.QWidget(self.widget_mod_bp_analysis)
        self.mba_widget_module.setGeometry(QtCore.QRect(470, 0, 460, 660))
        self.mba_widget_module.setObjectName("mba_widget_module")
        self.mba_widget_blueprint = QtWidgets.QWidget(self.widget_mod_bp_analysis)
        self.mba_widget_blueprint.setGeometry(QtCore.QRect(470, 0, 460, 660))
        self.mba_widget_blueprint.setObjectName("mba_widget_blueprint")
        self.mba_widget_blueprint_visualization = QtWidgets.QWidget(self.mba_widget_blueprint)
        self.mba_widget_blueprint_visualization.setGeometry(QtCore.QRect(0, 0, 460, 460))
        self.mba_widget_blueprint_visualization.setObjectName("mba_widget_blueprint_visualization")
        self.mba_lbl_gen_summary_heading = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_summary_heading.setGeometry(QtCore.QRect(10, 320, 440, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mba_lbl_gen_summary_heading.setFont(font)
        self.mba_lbl_gen_summary_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.mba_lbl_gen_summary_heading.setObjectName("mba_lbl_gen_summary_heading")
        self.mba_lbl_gen_mod_spec = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_mod_spec.setGeometry(QtCore.QRect(10, 350, 160, 20))
        self.mba_lbl_gen_mod_spec.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mba_lbl_gen_mod_spec.setObjectName("mba_lbl_gen_mod_spec")
        self.mba_lbl_gen_mod_spec_repr = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_mod_spec_repr.setGeometry(QtCore.QRect(10, 400, 160, 20))
        self.mba_lbl_gen_mod_spec_repr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mba_lbl_gen_mod_spec_repr.setObjectName("mba_lbl_gen_mod_spec_repr")
        self.mba_lbl_gen_mod_spec_fit_hist = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_mod_spec_fit_hist.setGeometry(QtCore.QRect(10, 450, 160, 20))
        self.mba_lbl_gen_mod_spec_fit_hist.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mba_lbl_gen_mod_spec_fit_hist.setObjectName("mba_lbl_gen_mod_spec_fit_hist")
        self.mba_lbl_gen_bp_spec_fit_hist = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_bp_spec_fit_hist.setGeometry(QtCore.QRect(10, 600, 160, 20))
        self.mba_lbl_gen_bp_spec_fit_hist.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mba_lbl_gen_bp_spec_fit_hist.setObjectName("mba_lbl_gen_bp_spec_fit_hist")
        self.mba_lbl_gen_bp_spec_repr = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_bp_spec_repr.setGeometry(QtCore.QRect(10, 550, 160, 20))
        self.mba_lbl_gen_bp_spec_repr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mba_lbl_gen_bp_spec_repr.setObjectName("mba_lbl_gen_bp_spec_repr")
        self.mba_lbl_gen_bp_spec = QtWidgets.QLabel(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_bp_spec.setGeometry(QtCore.QRect(10, 500, 160, 20))
        self.mba_lbl_gen_bp_spec.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mba_lbl_gen_bp_spec.setObjectName("mba_lbl_gen_bp_spec")
        self.mba_lbl_gen_mod_spec_area = QtWidgets.QScrollArea(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_mod_spec_area.setGeometry(QtCore.QRect(170, 350, 280, 45))
        self.mba_lbl_gen_mod_spec_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mba_lbl_gen_mod_spec_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mba_lbl_gen_mod_spec_area.setWidgetResizable(True)
        self.mba_lbl_gen_mod_spec_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_mod_spec_area.setObjectName("mba_lbl_gen_mod_spec_area")
        self.mba_lbl_gen_mod_spec_widget = QtWidgets.QWidget()
        self.mba_lbl_gen_mod_spec_widget.setGeometry(QtCore.QRect(0, 0, 280, 45))
        self.mba_lbl_gen_mod_spec_widget.setObjectName("mba_lbl_gen_mod_spec_widget")
        self.mba_lbl_gen_mod_spec_layout = QtWidgets.QVBoxLayout(self.mba_lbl_gen_mod_spec_widget)
        self.mba_lbl_gen_mod_spec_layout.setContentsMargins(0, 3, 10, 0)
        self.mba_lbl_gen_mod_spec_layout.setObjectName("mba_lbl_gen_mod_spec_layout")
        self.mba_lbl_gen_mod_spec_value = QtWidgets.QLabel(self.mba_lbl_gen_mod_spec_widget)
        self.mba_lbl_gen_mod_spec_value.setText("")
        self.mba_lbl_gen_mod_spec_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_mod_spec_value.setWordWrap(True)
        self.mba_lbl_gen_mod_spec_value.setObjectName("mba_lbl_gen_mod_spec_value")
        self.mba_lbl_gen_mod_spec_layout.addWidget(self.mba_lbl_gen_mod_spec_value)
        self.mba_lbl_gen_mod_spec_area.setWidget(self.mba_lbl_gen_mod_spec_widget)
        self.mba_lbl_gen_mod_spec_repr_area = QtWidgets.QScrollArea(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_mod_spec_repr_area.setGeometry(QtCore.QRect(170, 400, 280, 45))
        self.mba_lbl_gen_mod_spec_repr_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mba_lbl_gen_mod_spec_repr_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mba_lbl_gen_mod_spec_repr_area.setWidgetResizable(True)
        self.mba_lbl_gen_mod_spec_repr_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_mod_spec_repr_area.setObjectName("mba_lbl_gen_mod_spec_repr_area")
        self.mba_lbl_gen_mod_spec_repr_widget = QtWidgets.QWidget()
        self.mba_lbl_gen_mod_spec_repr_widget.setGeometry(QtCore.QRect(0, 0, 280, 45))
        self.mba_lbl_gen_mod_spec_repr_widget.setObjectName("mba_lbl_gen_mod_spec_repr_widget")
        self.mba_lbl_gen_mod_spec_repr_layout = QtWidgets.QVBoxLayout(self.mba_lbl_gen_mod_spec_repr_widget)
        self.mba_lbl_gen_mod_spec_repr_layout.setContentsMargins(0, 3, 10, 0)
        self.mba_lbl_gen_mod_spec_repr_layout.setObjectName("mba_lbl_gen_mod_spec_repr_layout")
        self.mba_lbl_gen_mod_spec_repr_value = QtWidgets.QLabel(self.mba_lbl_gen_mod_spec_repr_widget)
        self.mba_lbl_gen_mod_spec_repr_value.setText("")
        self.mba_lbl_gen_mod_spec_repr_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_mod_spec_repr_value.setWordWrap(True)
        self.mba_lbl_gen_mod_spec_repr_value.setObjectName("mba_lbl_gen_mod_spec_repr_value")
        self.mba_lbl_gen_mod_spec_repr_layout.addWidget(self.mba_lbl_gen_mod_spec_repr_value)
        self.mba_lbl_gen_mod_spec_repr_area.setWidget(self.mba_lbl_gen_mod_spec_repr_widget)
        self.mba_lbl_gen_mod_spec_fit_hist_area = QtWidgets.QScrollArea(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_mod_spec_fit_hist_area.setGeometry(QtCore.QRect(170, 450, 280, 45))
        self.mba_lbl_gen_mod_spec_fit_hist_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mba_lbl_gen_mod_spec_fit_hist_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mba_lbl_gen_mod_spec_fit_hist_area.setWidgetResizable(True)
        self.mba_lbl_gen_mod_spec_fit_hist_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_mod_spec_fit_hist_area.setObjectName("mba_lbl_gen_mod_spec_fit_hist_area")
        self.mba_lbl_gen_mod_spec_fit_hist_widget = QtWidgets.QWidget()
        self.mba_lbl_gen_mod_spec_fit_hist_widget.setGeometry(QtCore.QRect(0, 0, 280, 45))
        self.mba_lbl_gen_mod_spec_fit_hist_widget.setObjectName("mba_lbl_gen_mod_spec_fit_hist_widget")
        self.mba_lbl_gen_mod_spec_fit_hist_layout = QtWidgets.QVBoxLayout(self.mba_lbl_gen_mod_spec_fit_hist_widget)
        self.mba_lbl_gen_mod_spec_fit_hist_layout.setContentsMargins(0, 3, 10, 0)
        self.mba_lbl_gen_mod_spec_fit_hist_layout.setObjectName("mba_lbl_gen_mod_spec_fit_hist_layout")
        self.mba_lbl_gen_mod_spec_fit_hist_value = QtWidgets.QLabel(self.mba_lbl_gen_mod_spec_fit_hist_widget)
        self.mba_lbl_gen_mod_spec_fit_hist_value.setText("")
        self.mba_lbl_gen_mod_spec_fit_hist_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_mod_spec_fit_hist_value.setWordWrap(True)
        self.mba_lbl_gen_mod_spec_fit_hist_value.setObjectName("mba_lbl_gen_mod_spec_fit_hist_value")
        self.mba_lbl_gen_mod_spec_fit_hist_layout.addWidget(self.mba_lbl_gen_mod_spec_fit_hist_value)
        self.mba_lbl_gen_mod_spec_fit_hist_area.setWidget(self.mba_lbl_gen_mod_spec_fit_hist_widget)
        self.mba_lbl_gen_bp_spec_area = QtWidgets.QScrollArea(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_bp_spec_area.setGeometry(QtCore.QRect(170, 500, 280, 45))
        self.mba_lbl_gen_bp_spec_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mba_lbl_gen_bp_spec_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mba_lbl_gen_bp_spec_area.setWidgetResizable(True)
        self.mba_lbl_gen_bp_spec_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_bp_spec_area.setObjectName("mba_lbl_gen_bp_spec_area")
        self.mba_lbl_gen_bp_spec_widget = QtWidgets.QWidget()
        self.mba_lbl_gen_bp_spec_widget.setGeometry(QtCore.QRect(0, 0, 280, 45))
        self.mba_lbl_gen_bp_spec_widget.setObjectName("mba_lbl_gen_bp_spec_widget")
        self.mba_lbl_gen_bp_spec_layout = QtWidgets.QVBoxLayout(self.mba_lbl_gen_bp_spec_widget)
        self.mba_lbl_gen_bp_spec_layout.setContentsMargins(0, 3, 10, 0)
        self.mba_lbl_gen_bp_spec_layout.setObjectName("mba_lbl_gen_bp_spec_layout")
        self.mba_lbl_gen_bp_spec_value = QtWidgets.QLabel(self.mba_lbl_gen_bp_spec_widget)
        self.mba_lbl_gen_bp_spec_value.setText("")
        self.mba_lbl_gen_bp_spec_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_bp_spec_value.setWordWrap(True)
        self.mba_lbl_gen_bp_spec_value.setObjectName("mba_lbl_gen_bp_spec_value")
        self.mba_lbl_gen_bp_spec_layout.addWidget(self.mba_lbl_gen_bp_spec_value)
        self.mba_lbl_gen_bp_spec_area.setWidget(self.mba_lbl_gen_bp_spec_widget)
        self.mba_lbl_gen_bp_spec_repr_area = QtWidgets.QScrollArea(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_bp_spec_repr_area.setGeometry(QtCore.QRect(170, 550, 280, 45))
        self.mba_lbl_gen_bp_spec_repr_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mba_lbl_gen_bp_spec_repr_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mba_lbl_gen_bp_spec_repr_area.setWidgetResizable(True)
        self.mba_lbl_gen_bp_spec_repr_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_bp_spec_repr_area.setObjectName("mba_lbl_gen_bp_spec_repr_area")
        self.mba_lbl_gen_bp_spec_repr_widget = QtWidgets.QWidget()
        self.mba_lbl_gen_bp_spec_repr_widget.setGeometry(QtCore.QRect(0, 0, 280, 45))
        self.mba_lbl_gen_bp_spec_repr_widget.setObjectName("mba_lbl_gen_bp_spec_repr_widget")
        self.mba_lbl_gen_bp_spec_repr_layout = QtWidgets.QVBoxLayout(self.mba_lbl_gen_bp_spec_repr_widget)
        self.mba_lbl_gen_bp_spec_repr_layout.setContentsMargins(0, 3, 10, 0)
        self.mba_lbl_gen_bp_spec_repr_layout.setObjectName("mba_lbl_gen_bp_spec_repr_layout")
        self.mba_lbl_gen_bp_spec_repr_value = QtWidgets.QLabel(self.mba_lbl_gen_bp_spec_repr_widget)
        self.mba_lbl_gen_bp_spec_repr_value.setText("")
        self.mba_lbl_gen_bp_spec_repr_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_bp_spec_repr_value.setWordWrap(True)
        self.mba_lbl_gen_bp_spec_repr_value.setObjectName("mba_lbl_gen_bp_spec_repr_value")
        self.mba_lbl_gen_bp_spec_repr_layout.addWidget(self.mba_lbl_gen_bp_spec_repr_value)
        self.mba_lbl_gen_bp_spec_repr_area.setWidget(self.mba_lbl_gen_bp_spec_repr_widget)
        self.mba_lbl_gen_bp_spec_fit_hist_area = QtWidgets.QScrollArea(self.widget_mod_bp_analysis)
        self.mba_lbl_gen_bp_spec_fit_hist_area.setGeometry(QtCore.QRect(170, 600, 280, 45))
        self.mba_lbl_gen_bp_spec_fit_hist_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mba_lbl_gen_bp_spec_fit_hist_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mba_lbl_gen_bp_spec_fit_hist_area.setWidgetResizable(True)
        self.mba_lbl_gen_bp_spec_fit_hist_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_bp_spec_fit_hist_area.setObjectName("mba_lbl_gen_bp_spec_fit_hist_area")
        self.mba_lbl_gen_bp_spec_fit_hist_widget = QtWidgets.QWidget()
        self.mba_lbl_gen_bp_spec_fit_hist_widget.setGeometry(QtCore.QRect(0, 0, 280, 45))
        self.mba_lbl_gen_bp_spec_fit_hist_widget.setObjectName("mba_lbl_gen_bp_spec_fit_hist_widget")
        self.mba_lbl_gen_bp_spec_fit_hist_layout = QtWidgets.QVBoxLayout(self.mba_lbl_gen_bp_spec_fit_hist_widget)
        self.mba_lbl_gen_bp_spec_fit_hist_layout.setContentsMargins(0, 3, 10, 0)
        self.mba_lbl_gen_bp_spec_fit_hist_layout.setObjectName("mba_lbl_gen_bp_spec_fit_hist_layout")
        self.mba_lbl_gen_bp_spec_fit_hist_value = QtWidgets.QLabel(self.mba_lbl_gen_bp_spec_fit_hist_widget)
        self.mba_lbl_gen_bp_spec_fit_hist_value.setText("")
        self.mba_lbl_gen_bp_spec_fit_hist_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mba_lbl_gen_bp_spec_fit_hist_value.setWordWrap(True)
        self.mba_lbl_gen_bp_spec_fit_hist_value.setObjectName("mba_lbl_gen_bp_spec_fit_hist_value")
        self.mba_lbl_gen_bp_spec_fit_hist_layout.addWidget(self.mba_lbl_gen_bp_spec_fit_hist_value)
        self.mba_lbl_gen_bp_spec_fit_hist_area.setWidget(self.mba_lbl_gen_bp_spec_fit_hist_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.action_documentation = QtWidgets.QAction(MainWindow)
        self.action_documentation.setObjectName("action_documentation")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menu_help.addAction(self.action_documentation)
        self.menu_file.addAction(self.action_close)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tensorflow-Neuroevolution Visualizer"))
        self.ga_lbl_list_heading.setText(_translate("MainWindow", "List of generations and their best genome"))
        self.ga_lbl_genome_id.setText(_translate("MainWindow", "Genome ID "))
        self.ga_lbl_genome_fitness.setText(_translate("MainWindow", "Genome fitness: "))
        self.ga_lbl_genome_bp_id.setText(_translate("MainWindow", "Genome blueprint ID:"))
        self.ga_lbl_genome_assign_mod.setText(_translate("MainWindow", "Genome assigned modules:"))
        self.ga_lbl_genome_out_layers.setText(_translate("MainWindow", "Genome output layers:"))
        self.ga_lbl_genome_input_shape.setText(_translate("MainWindow", "Genome input shape:"))
        self.ga_lbl_genome_dtype.setText(_translate("MainWindow", "Genome dtype:"))
        self.ga_lbl_genome_orig_gen.setText(_translate("MainWindow", "Genome origin generation:"))
        self.mba_lbl_heading_generations.setText(_translate("MainWindow", "Select Generation:"))
        self.mba_lbl_heading_members.setText(_translate("MainWindow", "Select Member:"))
        self.mba_lbl_gen_summary_heading.setText(_translate("MainWindow", "Summary of Generation "))
        self.mba_lbl_gen_mod_spec.setText(_translate("MainWindow", "Mod Species:"))
        self.mba_lbl_gen_mod_spec_repr.setText(_translate("MainWindow", "Mod Species Repr:"))
        self.mba_lbl_gen_mod_spec_fit_hist.setText(_translate("MainWindow", "Mod Species Fitness Hist:"))
        self.mba_lbl_gen_bp_spec_fit_hist.setText(_translate("MainWindow", "BP Species Fitness Hist:"))
        self.mba_lbl_gen_bp_spec_repr.setText(_translate("MainWindow", "BP Species Repr:"))
        self.mba_lbl_gen_bp_spec.setText(_translate("MainWindow", "BP Species:"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.action_documentation.setText(_translate("MainWindow", "Documentation"))
        self.action_close.setText(_translate("MainWindow", "Close TFNE Backup"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
