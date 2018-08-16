import tkinter


class ConvertDiscordEmojiGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Discord Emoji Text")

        # top frame contains input label
        self.top_frame = tkinter.Frame(self.main_window)
        # middle first frame contains input entry
        self.middle_first_frame = tkinter.Frame(self.main_window)
        # middle second frame contains output label
        self.middle_second_frame = tkinter.Frame(self.main_window)
        # middle third frame contains output entry
        self.middle_third_frame = tkinter.Frame(self.main_window)
        # bottom frame contains both buttons
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.input_label = tkinter.Label(self.top_frame,
                                         text="Input")

        self.input_entry = tkinter.Entry(self.middle_first_frame,
                                         width=50)

        self.output_label = tkinter.Label(self.middle_second_frame,
                                          text="Output")

        self.output_text = tkinter.Text(self.middle_third_frame,
                                        width=50,
                                        height=20,
                                        state="disabled")

        self.copy_button = tkinter.Button(self.bottom_frame,
                                          text="Copy",
                                          command=self.copy)

        self.convert_button = tkinter.Button(self.bottom_frame,
                                             text="Convert",
                                             command=self.convert_string)

        self.char_label = tkinter.Label(self.bottom_frame,
                                        text="Total Characters: ")

        self.char_counter_var = tkinter.StringVar()
        self.char_counter_label = tkinter.Label(self.bottom_frame,
                                                textvariable=self.char_counter_var)

        self.top_frame.pack()
        self.middle_first_frame.pack()
        self.middle_second_frame.pack()
        self.middle_third_frame.pack()
        self.bottom_frame.pack()

        self.input_label.pack(side="top")
        self.input_entry.pack(side="top",
                              expand=True,)
        self.output_label.pack(side="top")
        self.output_text.pack(side="top",
                              expand=True)
        self.convert_button.pack(side="left")
        self.copy_button.pack(side="left")
        self.char_label.pack(side="left")
        self.char_counter_label.pack(side="right")

        tkinter.mainloop()

    def copy(self):
        text = str(self.output_text.get("1.0", "end"))
        self.output_text.clipboard_clear()
        self.output_text.clipboard_append(text)

    @staticmethod
    def num_switch(number):

        num_switch_dict = {
            "0": ":zero: ",
            "1": ":one: ",
            "2": ":two: ",
            "3": ":three: ",
            "4": ":four: ",
            "5": ":five: ",
            "6": ":six: ",
            "7": ":seven: ",
            "8": ":eight: ",
            "9": ":nine: "
        }
        discord_number = num_switch_dict.get(number)

        return discord_number

    @staticmethod
    def char_switch(char):

        char_switch_dict = {
            "!": ":exclamation: ",
            "?": ":question: ",
            "#": ":hash: ",
            "*": ":asterisk: ",
            "+": ":heavy_plus_sign: ",
            "-": ":heavy_minus_sign: ",
            "$": ":heavy_dollar_sign: ",
            "©": ":copyright: ",
            "®": ":registered: ",
            "™": ":tm: "
        }
        discord_char = char_switch_dict.get(char, char)

        return discord_char

    def convert_string(self):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        in_string = str(self.input_entry.get()).lower()
        out_string = ""
        list_in_string = list(in_string)
        i = 0

        while i < len(list_in_string):
            if list_in_string[i] == " ":
                out_string += "  "
            elif list_in_string[i].isdigit():
                out_string += self.num_switch(list_in_string[i])
            elif not list_in_string[i].isdigit() and not list_in_string[i].isalpha():
                out_string += self.char_switch(list_in_string[i])
            else:
                out_string += ":regional_indicator_" + list_in_string[i] + ": "
            i += 1

        out_string = out_string[:-1]
        self.char_counter_var.set(len(out_string))
        self.output_text.insert('end', out_string)
        self.output_text.configure(state="disabled")


GUI = ConvertDiscordEmojiGUI()
