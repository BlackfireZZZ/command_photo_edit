from PIL import Image



class Fillter:
    def apply_to_pixel(self, pixel:(int, int, int)) -> (int, int ,int):
        """
        Применяет фильтр к одному пикселю
        :param pixel :цвет пикселя
        :return: новый цвет пикселя
        """
        raise NotImplementedError()
    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img: исходное изображение
        :return: новое изображение
        """
        for y in range(img.height):
            for x in range(img.width):

                global r,g,b
                pixel = img.getpixel((x, y))
                r, g, b = img.getpixel((x, y)) # Нужен для объявления переменных R G B

                new_r, new_g, new_b = self.apply_to_pixel(pixel)
                
                img.putpixel((x, y), (new_r, new_g, new_b)) # Изменяем изображение
        return img

class InverseFillter(Fillter):
    def apply_to_pixel(self, pixel:(int, int, int)) -> (int, int ,int):

        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b
        return new_r, new_g, new_b


class InverseRedFillter(Fillter):
    def apply_to_pixel(self, pixel:(int, int, int)) -> (int, int ,int):

        new_r = 255 - r
        new_g = g
        new_b = b
        return new_r, new_g, new_b


class InverseGreenFillter(Fillter):
    def apply_to_pixel(self, pixel:(int, int, int)) -> (int, int ,int):

        new_r = r
        new_g = 255 - g
        new_b = b
        return new_r, new_g, new_b


class InverseBlueFillter(Fillter):
    def apply_to_pixel(self, pixel:(int, int, int)) -> (int, int ,int):

        new_r = r
        new_g = g
        new_b = 255 - b
        return new_r, new_g, new_b

class ExitFillter(Fillter):
    def apply_to_pixel(self, pixel:(int, int, int)) -> (int, int ,int):

        new_r = r
        new_g = g
        new_b = b
        return new_r, new_g, new_b
