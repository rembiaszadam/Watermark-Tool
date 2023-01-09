from PIL import Image, ImageDraw, ImageFont


class ImageEdit:

    def __init__(self):
        self.watermark_text = "WATERMARK TOOL"
        self.transparency_percentage = 50
        self.font_size = 100
        self.position_x = 100
        self.position_y = 100
        self.watermark_color = (237, 230, 211)
        self.img_width = 100
        self.img_height = 100
        self.img_directory = ""

    def img_dims(self, img_dir):
        # Get image dimensions.
        with Image.open(img_dir) as sample_image:
            self.img_width, self.img_height = sample_image.size
        self.img_directory = img_dir

    def build_image(self):
        # Take set values from set values and build image with watermark.
        watermark_position = (self.position_x, (self.img_height - self.position_y))
        watermark_transparency = int(255 - (self.transparency_percentage * 2.55))
        font_fill = (self.watermark_color[0], self.watermark_color[1], self.watermark_color[2], watermark_transparency)

        draw_image = Image.open(self.img_directory).convert("RGBA")

        text_img = Image.new("RGBA", draw_image.size, (255, 255, 255, 0))
        text_font = ImageFont.truetype(font="arial.ttf", size=self.font_size)
        text_draw = ImageDraw.Draw(text_img, "RGBA")
        text_draw.text(watermark_position, self.watermark_text, fill=font_fill, font=text_font, anchor="mm")

        combined = Image.alpha_composite(draw_image, text_img)
        return combined

    def preview_img(self):
        # Use system default to preview image.
        combined_image = self.build_image()
        combined_image.show()

    def export_img(self, save_dir):
        combined_image = self.build_image()
        export_img = combined_image.convert('RGB')
        export_img.save(save_dir)
