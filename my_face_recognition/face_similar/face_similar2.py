
import face_recognition

def compare_face(self):
    if self.imgA_path == "":
        QMessageBox.information(self, "提示", self.tr("请先导入照片一"))
    elif self.imgB_path == "":
        QMessageBox.information(self, "提示", self.tr("请先导入照片二"))
    else:
        imgA = face_recognition.load_image_file(self.imgA_path)
        imgB = face_recognition.load_image_file(self.imgB_path)
        try:
            A_face_encoding = face_recognition.face_encodings(imgA)[0]
            B_face_encoding = face_recognition.face_encodings(imgB)[0]
            known_faces = [A_face_encoding]
            results = face_recognition.compare_faces(known_faces, B_face_encoding)[0]
            if results:
                QMessageBox.information(self, "提示", self.tr("两张图片为同一个人"))
            else:
                QMessageBox.information(self, "提示", self.tr("两张图片为两个不同的人"))
        except IndexError:
            QMessageBox.information(self, "提示", self.tr("图片导入失败，请重新导入图片!"))
            quit()


# 人脸比对界面
class FaceCompareWindow(QMainWindow, FaceCompareUi):
    def __init__(self):
        super(FaceCompareWindow, self).__init__()
        self.setupUi(self)

        self.imgA_path = ""
        self.imgB_path = ""
        self.imgB = None
        self.imgA = None

        self.img_a_button.clicked.connect(self.open_imgA)
        self.img_b_button.clicked.connect(self.open_imgB)
        self.compare_button.clicked.connect(self.compare_face)
        self.close_button.clicked.connect(self.close_window)

    def open_imgA(self):
        imgA_path, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                    "All Files(*);;Text Files(*.txt)")
        if not imgA_path.endswith('jpg') | imgA_path.endswith('png'):
            QMessageBox.about(self, '提示', '请选择jpg或者png类型图片')
        else:
            # 如果使用 cv2.imread 不能导入中文路径
            imgA = cv2.imdecode(np.fromfile(imgA_path, dtype=np.uint8), -1)
            frame_location = face_recognition.face_locations(imgA)
            if len(frame_location) == 0:
                QMessageBox.information(self, "提示", self.tr("没有检测到人脸，请重新导入图片!"))
            else:
                QApplication.processEvents()
                self.imgA = imgA
                self.imgA_path = imgA_path
                show = cv2.resize(imgA, (221, 261))  # 截取图片
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 显示原图
                showImage = QImage(show.data, show.shape[1], show.shape[0], show.shape[1] * 3, QImage.Format_RGB888)
                self.img_a_show.setPixmap(QPixmap.fromImage(showImage))
                self.img_a_path.setText(imgA_path)

    def open_imgB(self):
        imgB_path, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                    "All Files(*);;Text Files(*.txt)")
        if not imgB_path.endswith('jpg') | imgB_path.endswith('png'):
            QMessageBox.about(self, '提示', '请选择jpg或者png类型图片')
        else:
            imgB = cv2.imdecode(np.fromfile(imgB_path, dtype=np.uint8), -1)
            frame_location = face_recognition.face_locations(imgB)
            if len(frame_location) == 0:
                QMessageBox.information(self, "提示", self.tr("没有检测到人脸，请重新导入图片!"))
            else:
                QApplication.processEvents()
                self.imgB = imgB
                self.imgB_path = imgB_path
                show = cv2.resize(imgB, (221, 261))
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], show.shape[1] * 3, QImage.Format_RGB888)
                self.img_b_show.setPixmap(QPixmap.fromImage(showImage))
                self.img_b_path.setText(imgB_path)

    def compare_face(self):
        if self.imgA_path == "":
            QMessageBox.information(self, "提示", self.tr("请先导入照片一"))
        elif self.imgB_path == "":
            QMessageBox.information(self, "提示", self.tr("请先导入照片二"))
        else:
            imgA = face_recognition.load_image_file(self.imgA_path)
            imgB = face_recognition.load_image_file(self.imgB_path)
            try:
                A_face_encoding = face_recognition.face_encodings(imgA)[0]
                B_face_encoding = face_recognition.face_encodings(imgB)[0]
                known_faces = [A_face_encoding]
                results = face_recognition.compare_faces(known_faces, B_face_encoding)[0]
                if results:
                    QMessageBox.information(self, "提示", self.tr("两张图片为同一个人"))
                else:
                    QMessageBox.information(self, "提示", self.tr("两张图片为两个不同的人"))
            except IndexError:
                QMessageBox.information(self, "提示", self.tr("图片导入失败，请重新导入图片!"))
                quit()

    def close_window(self):
        self.img_a_show.setText("照片一")
        self.img_b_show.setText("照片二")
        self.img_a_path.setText("")
        self.img_b_path.setText("")
        self.imgA_path = ""
        self.imgB_path = ""
        self.imgB = None
        self.imgA = None
        self.close()