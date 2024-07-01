from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import cv2
from ultralytics import YOLO
import random
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
import mysql.connector


class VideoProcessingApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.video_widget = Image()
        layout.add_widget(self.video_widget)

        play_button = Button(text='Process Video', size_hint=(1, 0.1))
        play_button.bind(on_press=self.process_video)
        layout.add_widget(play_button)

        return layout

    def process_video(self, instance):
        model = YOLO('C:/Users/Frol97/yolo12/runs/detect/train/weights/best.pt')
        model.fuse()
        input_video_path = 'C:/Users/Frol97/yolo12/Short2.mp4'
        cap = cv2.VideoCapture(input_video_path)

        if not cap.isOpened():
            raise Exception("Error: Could not open video file.")

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = model.track(frame, iou=0.4, conf=0.5, persist=True, imgsz=640, verbose=False,
                                  tracker="botsort.yaml")

            if results[0].boxes.id is not None:
                boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
                ids = results[0].boxes.id.cpu().numpy().astype(int)

                for box, id in zip(boxes, ids):
                    random.seed(int(id))
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                    cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), color, 2)
                    cv2.putText(
                        frame,
                        f'id {id}',
                        (box[0], box[1]),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 255),
                        2,
                    )

                    # Отправка данных в базу данных
                    self.insert_into_db(id, box)

                texture = Texture.create(size=(frame.shape[1], frame.shape[0]))
                texture.blit_buffer(frame.tobytes(), colorfmt='bgr', bufferfmt='ubyte')
                self.video_widget.texture = texture
                Clock.tick()

        cap.release()

    def insert_into_db(self, id, box):
        conn = mysql.connector.connect(
            host="Frol97",
            user="Fro.love",
            password="Zt,ecj,fr12!",
            database="neironka"
        )
        cursor = conn.cursor()

        # Проверка на существование таблицы и создание, если она не существует
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS СТАТИСТИКА (
                id INT PRIMARY KEY,
                найдено_типов_аномалий INT,
                название_задетектированных_аномалий VARCHAR(255),
                количество_дефектных_объектов INT
            )
        ''')

        # Вставка данных в таблицу
        cursor.execute('''
            INSERT INTO СТАТИСТИКА (id, найдено_типов_аномалий, название_задетектированных_аномалий, количество_дефектных_объектов)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                найдено_типов_аномалий = VALUES(найдено_типов_аномалий),
                название_задетектированных_аномалий = VALUES(название_задетектированных_аномалий),
                количество_дефектных_объектов = VALUES(количество_дефектных_объектов)
        ''', (id, 1, 'Задетектированная_аномалия', 1))  # Пример значений, подставьте реальные данные

        conn.commit()
        conn.close()


if __name__ == '__main__':
    VideoProcessingApp().run()
