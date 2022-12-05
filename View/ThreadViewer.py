from tkinter import Canvas
from models.Thread import Thread


class ThreadViewer:
    def __init__(self, view_manager):
        self.view_manager = view_manager
        self.thread_width = 250
        self.thread_height = 250

    def draw_threads(self):
        canvas = self.view_manager.canvas
        threads = self.view_manager.thread_manager.threads
        offset_y = 0
        offset_x = 0
        for thread, x in zip(threads, range(len(threads))):
            if x % 4 == 0 and x != 0:
                offset_y += self.thread_height
                offset_x = 0
            self.__draw_thread(canvas, offset_x * self.thread_width, 10 + offset_y, thread)
            offset_x += 1

    def __draw_thread(self, canvas: Canvas, x: int, y: int, thread: Thread):
        if thread.current_file_transferred is None:
            canvas.create_rectangle(x, y, x + self.thread_width, y + self.thread_width, outline='#FF0010')
        else:
            canvas.create_rectangle(x, y, x+self.thread_width, y + self.thread_width, outline='#00FF10')
        canvas.create_text(x + (self.thread_width / 2), y, text=thread.name, fill='#FFFFFF', font='Helvetica 12 bold')
        canvas.create_text(x + 80, y + 42, text=f'Loaded:\n'
                                           f'{thread.get_thread_history_as_string()}',
                           fill='#FFFFFF', font='Helvetica 8 bold')
        canvas.create_text((self.thread_width / 2) + x + 50, y + 42, text="Loading: \n"
                                                                 f"{thread.get_working_package_as_string()}",
                           fill='#FFFFFF', font='Helvetica 8 bold')
