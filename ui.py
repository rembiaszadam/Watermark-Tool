from tkinter import *
from tkinter import messagebox, Tk, filedialog
from tkinter.colorchooser import askcolor
import customtkinter
from image_edit import ImageEdit


class AppInterface:

    def __init__(self, image_edit: ImageEdit):
        self.img = image_edit
        # Set app window
        self.window = Tk()
        self.window.geometry(f'670x620')
        self.window.title("")
        self.window.config(bg="black")

        # Set top and bottom frames
        self.frame_top = Frame(master=self.window, bg="grey20")
        self.frame_top.grid(row=0, column=0, padx=10, pady=10, sticky=N+E+W)

        self.frame_bottom = Frame(master=self.window, bg="grey20")

        # Top frame objects
        self.label_title = Label(master=self.frame_top, text="Watermark Tool", bg="grey20", fg="white")
        self.label_title.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=W)

        self.button_import = customtkinter.CTkButton(master=self.frame_top,
                                                     text="Import",
                                                     width=120,
                                                     command=self.select_file)
        self.button_import.grid(row=1, column=0, padx=5, pady=5)

        self.button_export = customtkinter.CTkButton(master=self.frame_top,
                                                     text="Export",
                                                     width=120,
                                                     command=self.export)
        self.button_export.grid(row=2, column=0, padx=5, pady=5)

        # Frame inside top frame to display image info.
        self.frame_info = Frame(master=self.frame_top, bg="grey30")
        self.frame_info.grid(row=1, column=1, rowspan=3, padx=5, pady=5, sticky=N+E+S+W)

        # Info frame objects
        self.label_dir = Label(master=self.frame_info, text="", bg="grey30", fg="white")
        self.label_dir.grid(row=0, column=0, padx=5, pady=5, sticky=E+W)

        self.label_img_dims = Label(master=self.frame_info, text="", bg="grey30", fg="white")
        self.label_img_dims.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        # Set top frame and info frame to expand with window.
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)

        self.frame_top.columnconfigure(1, weight=2)
        self.frame_top.rowconfigure(1, weight=3)

        # Bottom frame objects
        # Frame title
        self.label_watermark_tool = Label(master=self.frame_bottom,
                                          text="Watermark Details",
                                          bg="grey20",
                                          fg="white",)
        self.label_watermark_tool.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=W)

        # Default config for label objects
        self.label_details = {"master": self.frame_bottom,
                              "bg": "grey20",
                              "fg": "white",
                              "width": 12,
                              "anchor": "e"}

        # Label objects
        self.label_text = Label(**self.label_details, text="Text:")
        self.label_text.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        self.label_color = Label(**self.label_details, text="Color:")
        self.label_color.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        self.label_transparency = Label(**self.label_details, text="Transparency:")
        self.label_transparency.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        self.label_font_size = Label(**self.label_details, text="Font Size:")
        self.label_font_size.grid(row=4, column=0, padx=5, pady=5, sticky=E)

        self.label_position = Label(**self.label_details, text="Position:\n(Width x Height)", justify="right")
        self.label_position.grid(row=5, column=0, padx=5, pady=5, sticky=E)

        # User entry objects
        self.entry_text = Entry(master=self.frame_bottom)
        self.entry_text.insert(0, f"{self.img.watermark_text}")
        self.entry_text.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=E+W)

        self.button_color = customtkinter.CTkButton(master=self.frame_bottom,
                                                    text="Change Color",
                                                    command=self.change_color)
        self.button_color.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=W)

        self.entry_transparency = Entry(master=self.frame_bottom, width=4, justify="center", bg="grey20", fg="white")
        self.entry_transparency.insert(0, self.img.transparency_percentage)
        self.entry_transparency.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        self.slider_transparency = customtkinter.CTkSlider(master=self.frame_bottom,
                                                           from_=0,
                                                           to=100,
                                                           number_of_steps=100,
                                                           width=400,
                                                           command=self.set_transparency)
        self.slider_transparency.set(self.img.transparency_percentage)
        self.slider_transparency.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        self.entry_font_size = Entry(master=self.frame_bottom, width=4, justify="center", bg="grey20", fg="white")
        self.entry_font_size.insert(0, self.img.font_size)
        self.entry_font_size.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        self.slider_font_size = customtkinter.CTkSlider(master=self.frame_bottom,
                                                        from_=4,
                                                        to=400,
                                                        number_of_steps=396,
                                                        width=400,
                                                        command=self.set_font_size)
        self.slider_font_size.set(self.img.font_size)
        self.slider_font_size.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        # Position tool frame
        self.frame_position = Frame(master=self.frame_bottom, bg="black")
        self.frame_position.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky=W)

        # Position tool objects
        self.entry_position_x = Entry(master=self.frame_position, width=5, justify="center", bg="grey20", fg="white")
        self.entry_position_x.insert(0, f"{self.img.position_x}")
        self.entry_position_x.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky=E)

        self.entry_position_y = Entry(master=self.frame_position, width=5, justify="center", bg="grey20", fg="white")
        self.entry_position_y.insert(0, f"{self.img.position_y}")
        self.entry_position_y.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky=W)

        # Position tool width and height sliders
        self.slider_position_x = customtkinter.CTkSlider(master=self.frame_position,
                                                         from_=0,
                                                         to=self.img.img_width,
                                                         number_of_steps=self.img.img_width,
                                                         width=420,
                                                         command=self.set_position_x)
        self.slider_position_x.set(self.img.position_x)
        self.slider_position_x.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=S)

        self.slider_position_y = customtkinter.CTkSlider(master=self.frame_position,
                                                         from_=0,
                                                         to=self.img.img_height,
                                                         number_of_steps=self.img.img_height,
                                                         orient="vertical",
                                                         height=200,
                                                         command=self.set_position_y)
        self.slider_position_y.set(self.img.position_y)
        self.slider_position_y.grid(row=0, column=0, rowspan=2, padx=5, pady=5, sticky=W)

        # Preview button
        self.button_preview = customtkinter.CTkButton(master=self.frame_bottom,
                                                      text="Preview",
                                                      command=self.preview)
        self.button_preview.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def on_closing(self):
        self.window.destroy()

    def select_file(self):
        filename = filedialog.askopenfilename(title="Load Image")
        if not filename:
            return
        image_location = f"{filename}"

        # When first image is selected show edit tools.
        self.label_dir.config(text=image_location)
        self.img.img_dims(img_dir=image_location)
        self.label_img_dims.config(text=f"Image Width x Height: {self.img.img_width} x {self.img.img_height}")
        self.slider_position_x.configure(to=self.img.img_width, number_of_steps=self.img.img_width)
        self.slider_position_y.configure(to=self.img.img_height, number_of_steps=self.img.img_height)
        if self.frame_bottom.grid_info() == {}:
            self.frame_bottom.grid(row=1, column=0, padx=10, pady=10, sticky=N+E+W)
            self.slider_position_x.set(self.img.img_width/2)
            self.slider_position_y.set(self.img.img_height/2)
            self.set_position_x(self.img.img_width/2)
            self.set_position_y(self.img.img_height/2)

    def change_color(self):
        color = askcolor(title="Choose Watermark Text Color")[0]
        self.img.watermark_color = color

    def set_transparency(self, transparency):
        self.entry_transparency.delete(0, "end")
        self.entry_transparency.insert(0, f"{int(transparency)}")

    def set_font_size(self, size):
        self.entry_font_size.delete(0, "end")
        self.entry_font_size.insert(0, f"{int(size)}")

    def set_position_x(self, set_x):
        self.entry_position_x.delete(0, "end")
        self.entry_position_x.insert(0, f"{int(set_x)}")

    def set_position_y(self, set_y):
        self.entry_position_y.delete(0, "end")
        self.entry_position_y.insert(0, f"{int(set_y)}")

    def watermark_setup(self):
        self.img.watermark_text = self.entry_text.get()
        self.img.transparency_percentage = int(self.entry_transparency.get())
        self.img.font_size = int(self.entry_font_size.get())
        self.img.position_x = int(self.entry_position_x.get())
        self.img.position_y = int(self.entry_position_y.get())

    def preview(self):
        self.watermark_setup()
        self.img.preview_img()

    def export(self):
        self.watermark_setup()
        save_file = filedialog.asksaveasfile(mode="w", defaultextension=".jpg")
        if not save_file:
            return
        self.img.export_img(save_file)
        messagebox.showinfo(title="Image Saved", message=f"File saved.")
