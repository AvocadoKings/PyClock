Hey guys gals and nb pals!

I have a problem...
My clock, you see. It's old. And not beautiful at all.
That's why i'm making my very own using my 3d printer, a wemos d1 mini (esp8266) and microPython.
Why not just use c?
Cuz c sucks and i don't like it + Python is just better (i'm better at it).

In this repository is the source code, micropython intallation guide and 3d files

MicroPyhon:

MicroPython is  a lightweight version of python that can be installed and used on an ESP and pyboard.
There are already some libraries pre-installed but it's not enough for me so there will be some py files with the libraries i need.

Links:

    binairy installs: https://micropython.org/download/
    documentation: https://docs.micropython.org/en/latest/index.html
    
Guide:
    In this repository you'll find a folder called `microPython`.
    Inside is `.exe` file and a `.bin` file.
    Download and open the `.exe` file.
    Download the `.bin` file.
    In the esp flasher tool navigate to `Config`.
    On the first line cloick on the `cog icon`.
    Navigate to your `.bin` file.
    In the esp flasher tool navigate to `Advanced`.
    Change the `SPI mode` to `DOUT`.
    Navigate back to `Operation`.
    Choose the right `COM` and press `Flash`.