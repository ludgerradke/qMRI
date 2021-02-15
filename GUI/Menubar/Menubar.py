from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MenuBar(QMenuBar):

    def __init__(self, mainWindow: QMainWindow):
        super(MenuBar, self).__init__()

        self.mainWindow = mainWindow
        self.setStyleSheet("background: rgb(100, 100, 100);")

        #################################################################################
        # File Menu
        actionFile = self.addMenu("&File")
        #################################################################################

        load_dicom = QAction(QIcon(r'.\GUI\Icons\loadDicomIcon.png'), 'Load Dicom', self)
        load_dicom.setShortcut('Ctrl+L')
        load_dicom.triggered.connect(self.load_dicom)
        actionFile.addAction(load_dicom)

        translate = QAction(QIcon(r'.\GUI\Icons\TranslatorIcon.png'), 'Translate Dicom', self)
        translate.triggered.connect(self.translate)
        actionFile.addAction(translate)

        export_dicom = QAction(QIcon(r'.\GUI\Icons\exportIcon.png'),
                               'Export Dicom', self)
        export_dicom.triggered.connect(self.export_dicom)
        actionFile.addAction(export_dicom)

        actionFile.addSeparator()
        unload = QAction(QIcon(r'.\GUI\Icons\unloadIcon.png'),
                         'Unload', self)
        unload.triggered.connect(self.unload)
        actionFile.addAction(unload)

        #################################################################################
        # Segmentation Menu
        actionSegmentation = self.addMenu("&Segmentation")
        #################################################################################
        load_vec_points = QAction(QIcon(r'.\GUI\Icons\VecPointsIcon.png'),
                                  'Load vector polygons', self)
        load_vec_points.triggered.connect(self.load_vec)
        actionSegmentation.addAction(load_vec_points)

        nifti = QAction(QIcon(r'.\GUI\Icons\NiftiIcon.png'),
                        'Load NIFTI mask', self)
        nifti.triggered.connect(self.load_nifti)
        actionSegmentation.addAction(nifti)

        vec2nifti = QAction(QIcon(r'.\GUI\Icons\Vec2Nifti.png'),
                            'Vector Polygon to Nifti', self)
        vec2nifti.triggered.connect(self.vec2nifti)
        actionSegmentation.addAction(vec2nifti)

        importOldVec = QAction(QIcon(r'.\GUI\Icons\Old2New.png'),
                               'Import old Vector Polygon', self)
        importOldVec.triggered.connect(self.importOldVec)
        actionSegmentation.addAction(importOldVec)

        actionSegmentation.addSeparator()
        actionSegmentation.addAction("Unload")

        #################################################################################
        # Edit Menu
        actionEdit = self.addMenu("Edit")
        #################################################################################
        addStudy = QAction(QIcon(r'.\GUI\Icons\addIcon.png'),
                           'add Study', self)
        addStudy.triggered.connect(self.add_study)
        actionEdit.addAction(addStudy)

        editStudy = QAction(QIcon(r'.\GUI\Icons\editIcon.png'),
                            'edit Study', self)
        editStudy.triggered.connect(self.edit_study)
        actionEdit.addAction(editStudy)
        actionEdit.addAction("delete Study")

        #################################################################################
        # Help Menu
        actionHelp = self.addMenu("Help")
        #################################################################################
        actionHelp.addAction("Help")
        actionHelp.addAction("Check for Updates..")
        actionHelp.addAction("User Manual")
        actionHelp.addSeparator()
        actionHelp.addAction("About")

    def load_dicom(self):
        pass

    def unload(self):
        pass

    def load_vec(self):
        pass

    def translate(self):
        pass

    def load_nifti(self):
        pass

    def export_dicom(self):
        pass

    def add_study(self):
        pass

    def edit_study(self):
        pass

    def vec2nifti(self):
        pass

    def importOldVec(self):
        pass
