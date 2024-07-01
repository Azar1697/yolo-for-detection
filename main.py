from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.video import Video
from ultralytics import YOLO


Builder.load_string('''
<MyLabel>:
    text_size: self.size
    valign: 'middle'
    halign: 'center'
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1  # Цвет рамки (красный)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [10, 10, 10, 10]  # Закругление углов (всех углов)
''')


class MyLabel(Label):
    pass


class MainScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


class DataCollection(Screen):
    pass


class StatusLearning(Screen):
    pass



class StatsScreen(Screen):
    pass


class TrainingParameters(Screen):
    pass


class LoadDatasets(Screen):
    pass


class Camera(Screen):
    pass


class Folder(Screen):
    pass


class MainApp(App):
    def build(self):
        # Создаем экземпляр ScreenManager
        self.sm = ScreenManager()

        # Создаем экземпляр каждого экрана и добавляем содержимое
        main_screen = MainScreen(name='main')
        main_layout = FloatLayout()

        settings_screen = SettingsScreen(name='settings')
        settings_layout = FloatLayout()

        data_collection = DataCollection(name='data_collection')
        data_collection_layout = FloatLayout()

        status_learning = StatusLearning(name='status_learning')
        status_learning_layout = FloatLayout()

        stats_screen = StatsScreen(name='stats')
        stats_layout = FloatLayout()

        training_parameters = TrainingParameters(name='training_parameters')
        training_parameters_layout = FloatLayout()

        load_datasets = LoadDatasets(name='load_datasets')
        load_datasets_layout = FloatLayout()

        camera = Camera(name='camera')
        camera_layout = FloatLayout()

        folder = Folder(name='folder')
        folder_layout = FloatLayout()

        # ЭКРАН Выбор модели

        # Добавляем кнопку "Параметры обучения" на экран настроек
        btn_params = Button(text='Таблетки', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        #btn_params.bind(on_press=self.on_training_parameters_pressed)
        settings_layout.add_widget(btn_params)

        # Добавляем кнопку "Загрузить датасет" на экран настроек
        btn_load_dataset = Button(text='Капсулы', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #btn_load_dataset.bind(on_press=self.on_load_datasets_pressed)
        settings_layout.add_widget(btn_load_dataset)

        # Добавляем кнопку "назад" на экран настроек
        btn_back = Button(text='назад', size_hint=(0.3, 0.1),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_back.bind(on_press=self.on_back_pressed)
        settings_layout.add_widget(btn_back)

        settings_screen.add_widget(settings_layout)

        # ЭКРАН СБОР ДАННЫХ
        # Добавляем кнопку "камера" на экран настроек
        btn_camera = Button(text='Подключить по ip', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        btn_camera.bind(on_press=self.on_camera_pressed)
        data_collection_layout.add_widget(btn_camera)

        # Добавляем кнопку "Папка с данными" на экран настроек
        btn_folder_with_data = Button(text='подключить с помощью аналогового провода', size_hint=(0.3, 0.1),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn_folder_with_data.bind(on_press=self.on_folder_pressed)
        data_collection.add_widget(btn_folder_with_data)

        # Добавляем кнопку "назад" на экран сбор данных
        btn_back_1 = Button(text='назад', size_hint=(0.3, 0.1),
                          pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_back_1.bind(on_press=self.on_back_pressed)
        data_collection_layout.add_widget(btn_back_1)

        data_collection.add_widget(data_collection_layout)


        # ЭКРАН СТАТУС ОБУЧЕНИЯ
        # Добавляем кнопку "камера" на экран настроек
        label_camera = Label(text='счетчики сброшены', size_hint=(0.3, 0.1),
                            pos_hint={'center_x': 0.5, 'center_y': 0.7})
        status_learning_layout.add_widget(label_camera)

        # Добавляем кнопку "назад" на экран сбор данных
        btn_back_2 = Button(text='назад', size_hint=(0.3, 0.1),
                            pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_back_2.bind(on_press=self.on_back_pressed)
        status_learning_layout.add_widget(btn_back_2)

        status_learning.add_widget(status_learning_layout)

        # ЭКРАН СТАТИСТИКА
        # Добавляем кнопку "камера" на экран настроек
        label_all = Label(text='Общее колличество объектов', size_hint=(0.3, 0.1),
                             pos_hint={'center_x': 0.5, 'center_y': 0.8})
        stats_layout.add_widget(label_all)

        label_norm = Label(text='Общее колличество объектов', size_hint=(0.3, 0.1),
                          pos_hint={'center_x': 0.5, 'center_y': 0.6})
        stats_layout.add_widget(label_norm)

        label_defect = Label(text='Колличество дефектных объектов', size_hint=(0.3, 0.1),
                           pos_hint={'center_x': 0.5, 'center_y': 0.4})
        stats_layout.add_widget(label_defect)

        # Добавляем кнопку "назад" на экран статистика
        btn_back_3 = Button(text='назад', size_hint=(0.3, 0.1),
                            pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn_back_3.bind(on_press=self.on_back_pressed)
        stats_layout.add_widget(btn_back_3)

        stats_screen.add_widget(stats_layout)

        # ЭКРАН параметры обучения
        # Добавляем текст "эпохи" на экран параметры обучения
        label_epoch = Label(text=' Epoch:   20', size_hint=(0.3, 0.1),
                          pos_hint={'center_x': 0.5, 'center_y': 0.8})
        training_parameters_layout.add_widget(label_epoch)
        # Добавляем текст "эпохи" на экран параметры обучения
        label_Batch_size = Label(text='Batch_size', size_hint=(0.3, 0.1),
                           pos_hint={'center_x': 0.5, 'center_y': 0.6})
        training_parameters_layout.add_widget(label_Batch_size)

        # Добавляем кнопку "назад" на экран параметры обучения
        btn_back_4 = Button(text='назад', size_hint=(0.3, 0.1),
                            pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn_back_4.bind(on_press=self.on_back_pressed_parameters_dataset)
        training_parameters_layout.add_widget(btn_back_4)

        training_parameters.add_widget(training_parameters_layout)

        # ЭКРАН загрузить датасет
        # Добавляем текст "эпохи" на экран параметры обучения
        label_for_internet = Label(text=' Введите ссылку на dataset:   20', size_hint=(0.3, 0.1),
                            pos_hint={'center_x': 0.5, 'center_y': 0.7})
        load_datasets_layout.add_widget(label_for_internet)
        # Добавляем текст "эпохи" на экран параметры обучения
        button_for_device = Button(text='загрузить с устройства', size_hint=(0.3, 0.1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.5})
        load_datasets_layout.add_widget(button_for_device)

        # Добавляем кнопку "назад" на экран параметры обучения
        btn_back_5 = Button(text='назад', size_hint=(0.3, 0.1),
                            pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_back_5.bind(on_press=self.on_back_pressed_parameters_dataset)
        load_datasets_layout.add_widget(btn_back_5)

        load_datasets.add_widget(load_datasets_layout)

        # ЭКРАН камеры
        # Добавляем текст "Ip-адресс" на экран параметры обучения
        label_ip = Label(text='ip адресс', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        camera_layout.add_widget(label_ip)

        label_status = Label(text='статус подлючения:', size_hint=(.3, .1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        camera_layout.add_widget(label_status)

        label_frequency = MyLabel(text='частота:', size_hint=(.3, .1), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        camera_layout.add_widget(label_frequency)

        btn_back_6 = Button(text='назад', size_hint=(0.3, 0.1),pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn_back_6.bind(on_press=self.on_back_pressed_camera_folder)
        camera_layout.add_widget(btn_back_6)

        camera.add_widget(camera_layout)

        # Экран папка с данными
        label_frequency_1 = Label(text='частота:', size_hint=(.3, .1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        folder_layout.add_widget(label_frequency_1)

        btn_back_7 = Button(text='назад', size_hint=(0.3, 0.1),pos_hint={'center_x': 0.5, 'center_y': 0.4})
        btn_back_7.bind(on_press=self.on_back_pressed_camera_folder)
        folder_layout.add_widget(btn_back_7)

        folder.add_widget(folder_layout)

        video = Video(source='C:/Users/Frol97/yolo12/Short2.mp4', state='pause', size_hint=(0.5, 0.5), pos=(900, 400))
        main_layout.add_widget(video)

        # Создаем кнопку
        btn_play_video = Button(text='Включить RunTime', size_hint=(.22, .15), pos=(1190, 170))
        btn_play_video.bind(on_press=lambda instance: self.play_video(video))
        main_layout.add_widget(btn_play_video)

        # Добавляем макет на главный экран
        main_screen.add_widget(main_layout)

        self.model = YOLO('yolov8m.pt')



        # Добавляем экраны в ScreenManager
        self.sm.add_widget(main_screen)
        self.sm.add_widget(settings_screen)
        self.sm.add_widget(data_collection)
        self.sm.add_widget(status_learning)
        self.sm.add_widget(stats_screen)
        self.sm.add_widget(training_parameters)
        self.sm.add_widget(load_datasets)
        self.sm.add_widget(camera)
        self.sm.add_widget(folder)

        # Создаем макет и добавляем в него ScreenManager
        self.layout = FloatLayout()
        self.layout.add_widget(self.sm)

        self.buttons = []  # Список для хранения ссылок на кнопки

        buttons_data = [
            {'text': 'Выбор модели', 'size_hint': (0.1, .15), 'pos': (90, 700)},
            {'text': 'подключить камеру', 'size_hint': (0.1, .15), 'pos': (90, 500)},
            {'text': 'сброс счетчиков', 'size_hint': (0.1, .15), 'pos': (400, 700)},
            {'text': 'статистика', 'size_hint': (0.1, .15), 'pos': (400, 500)},
        ]

        for button_data in buttons_data:
            button = Button(**button_data, background_color='gray')
            self.layout.add_widget(button)
            self.buttons.append(button)  # Добавляем кнопку в список

            # Добавляем обработчик события для кнопки "настройки обучения"
            if button_data['text'] == 'Выбор модели':
                button.bind(on_press=self.on_settings_pressed)
            # Добавляем обработчик события для кнопки "подключить камеру"
            if button_data['text'] == 'подключить камеру':
                button.bind(on_press=self.on_data_collection_pressed)
            if button_data['text'] == 'сброс счетчиков':
                button.bind(on_press=self.on_status_learning_pressed)
            if button_data['text'] == 'статистика':
                button.bind(on_press=self.on_stats_pressed)
            if button_data['text'] == 'Параметры обучения':
                button.bind(on_press=self.on_training_parameters_pressed)
            if button_data['text'] == 'Загрузить датасет':
                button.bind(on_press=self.on_training_parameters_pressed)
            if button_data['text'] == 'камера':
                button.bind(on_press=self.on_camera_pressed)
            if button_data['text'] == 'папка с данными':
                button.bind(on_press=self.on_camera_pressed)
        # Возвращаем созданный макет
        return self.layout

    def play_video(self, video):
        video.state = 'play'

    # def load_video(self):
    #     self.video.source = 'Short.mp4'  # Замените 'Short.mp4' на путь к вашему видео

    def on_settings_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "settings"
        self.sm.current = 'settings'

        # Удаляем кнопки из макета
        for button in self.buttons:
            self.layout.remove_widget(button)

    def on_data_collection_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "settings"
        self.sm.current = 'data_collection'

        # Удаляем кнопки из макета
        for button in self.buttons:
            self.layout.remove_widget(button)

    def on_status_learning_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "settings"
        self.sm.current = 'status_learning'

        # Удаляем кнопки из макета
        for button in self.buttons:
            self.layout.remove_widget(button)

    def on_stats_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "settings"
        self.sm.current = 'stats'

        # Удаляем кнопки из макета
        for button in self.buttons:
            self.layout.remove_widget(button)

    def on_training_parameters_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "training_parameters"
        self.sm.current = 'training_parameters'

        # Удаляем кнопки из макета
        for button in self.buttons:
            self.layout.remove_widget(button)

    def on_load_datasets_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "training_parameters"
        self.sm.current = 'load_datasets'

        # Удаляем кнопки из макета
        for button in self.buttons:
            self.layout.remove_widget(button)

    def on_camera_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "training_parameters"
        self.sm.current = 'camera'

        # Удаляем кнопки из макета
        for button in self.buttons:
            self.layout.remove_widget(button)

    def on_folder_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "training_parameters"
        self.sm.current = 'folder'

        # Удаляем кнопки из макета
        for button in self.buttons:
            self.layout.remove_widget(button)


    def on_back_pressed(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "main"
        self.sm.current = 'main'

        # Восстанавливаем кнопки на главном экране
        for button in self.buttons:
            self.layout.add_widget(button)

    def on_back_pressed_parameters_dataset(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "settings"
        self.sm.current = 'settings'

        for button in self.buttons:
            self.layout.remove_widget(button)

    def on_back_pressed_camera_folder(self, instance):
        # Получаем сохраненный экземпляр ScreenManager и переключаемся на экран "settings"
        self.sm.current = 'data_collection'

        for button in self.buttons:
            self.layout.remove_widget(button)




if __name__ == '__main__':
    MainApp().run()

