import socket
from PIL import Image, ImageDraw, ImageFont
import os

def get_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def create_wallpaper():
    dir = os.getcwd()
    img = Image.open(dir + '/wallpaper_origin.png')
    text = get_hostname() + "\n" + get_ip()
    font = ImageFont.truetype(dir + '/BebasNeue-Regular.ttf', 65) 
    d1 = ImageDraw.Draw(img)
    d1.text((1250, 550), text,font = font, fill=(214, 38, 79))
    #img.show()
    img.save("wallpaper.png")
    pass

def set_wallpaper():
    dir = os.getcwd()
    file = dir + '/wallpaper.png'
    command = "gsettings set org.gnome.desktop.background picture-uri '" + file + "'" 
    os.system(command)

def main():
    create_wallpaper()
    set_wallpaper()

if __name__ == '__main__':
        main()
        