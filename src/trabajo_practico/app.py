import tkinter
import os
from tkinter import ttk


def OnDoubleClick(event):
    print(event)
    item = treeview.identify('item', event.x, event.y)
    print("you clicked on", treeview.item(item, "values"))
    # subdir_entries = os.listdir(item)


app = tkinter.Tk()
app.title("GUI Application of Python")

ttk.Label(app, text="Treeview(hierarchical)").pack()
treeview = ttk.Treeview(app, show="tree")
treeview.bind("<Double-1>", OnDoubleClick)
treeview.pack(fill="both", expand=True)


def new_folder(parent_path, directory_entries, parent_iid, f_image, d_image):
    """Creates a graphical representation of the structure
    of subdirectories and files in the specified parent_path.

    Recursive tree building for large directories can take some time.

    :param parent_path: directory path, string
    :param directory_entries: List[str]
           a list containing the names of the entries in the parent_path
           obtained using os.listdir()
    :param parent_iid: unique identifier for a treeview item, string
    :param f_image: file icon, tkinter.PhotoImage
    :param d_image: directory icon, tkinter.PhotoImage
    :return: None
    """
    for name in directory_entries:
        item_path = parent_path + os.sep + name
        # optional: file does not exist or broken symbolic link
        # if not os.path.exists(item_path):
        # print("Skipped:", item_path)
        # continue
        if os.path.isdir(item_path):
            # set subdirectory node
            subdir_iid = treeview.insert(
                parent=parent_iid, index="end", text=name, image=d_image
            )
            print(subdir_iid)
            try:
                # pass the iid of the subdirectory as parent iid
                # all files/folders found in this subdirectory
                # will be attached to this subdirectory node
                subdir_entries = os.listdir(item_path)
                print(subdir_entries)
                """
                new_folder(
                    parent_path=item_path,
                    directory_entries=subdir_entries,
                    parent_iid=subdir_iid,
                    f_image=f_image,
                    d_image=d_image,
                )
                """
            except PermissionError:
                pass
        else:
            treeview.insert(
                parent=parent_iid, index="end", text=name, image=f_image
            )  # noqa
        print(item_path)


# png 16x16 -> base64 strings for tkinter.PhotoImage
file_img = """
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAABGdB
TUEAALGPC/xhBQAAAAlwSFlzAAAScwAAEnMBjCK5BwAAAalJREFU
OE99kUtLAmEUhg38Af6a6he06SJIF8FFREVtqkVEkBB2IcJIRDAk
80KrNq3CWihuuuh4GVIwM9BSa0bHUXGc8X7p1Bc6jtLLxzAwz3Pm
nPMNcaWySCR6CYVoOgMvzWaz3W63Wq1GowFPsVg8PDIqkUjg019A
gEOSJHAowEHAhDidzmAwGI3FEPZTXSDwafiJ3W5nWRbH8TSVGSAI
aBDi8TiGYT6fz2QyCwU+Dc0ADanX67XfWK3W/4QOjYRqtWqxWIQC
mhKh/NpAVyoVs/GcclwzabI7NF/odILocrnsPFwvGRcS6uUeob8T
RDOxMGuYz2vkfsdtVxhIg1AqMqnTRUYrD+iU2Vy+R+jvBMpTN+aC
Zi6umo2+RXouDmgkFJ4fyLNNNvUFdJFM0kfTuQOpfk9ZZLmuQBBE
Z4Np/VrtapVSKwqf7wmlLLc/iR9vGAyGnrWCgC4ImmZpKqVbKeoV
xK4sq5pI7kgjAfzCZBIK/PWX8jRxspRVjVPbY8FLLcdxfQKZ8vlx
j9eLebxuzOPGMO/j/YdyJro1dWezPblc4defieF8A+ZBma193+p6
AAAAAElFTkSuQmCC
"""
dir_img = """
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAABGdB
TUEAALGPC/xhBQAAAAlwSFlzAAAScgAAEnIBXmVb4wAAAihJREFU
OE990vtv0kAcAPDh4wd/8w/yp5n4i4kkmizoBMKcRIfG7YepWSSZ
MSTGSXQao8wtjIw5ZkJEJ4+O0CGvoWhSCmw0sFJaHoU+GEJbyDax
EwMjQS+Xy30v97m7791JOF4Y+FMOBEJsj508PXD8lERyoj3Yp4ig
XclNRSlyg0F0TFxLRbXFyAMqaarkQrXabmfO4eqdoBRWtgQnujGM
+DRVbIYnTU3Wvrf7hcubGRToTOsFvK3V/JZyy6KeCXL7CZc3CEVj
k7bTO85/A+FDgwr6rKNIQEtu6XnC0Ch/+j+wCSXXulke994vxh/X
sNkGaaXTfXfYVLbEIwk2gbQBpstxz0QOmq6mdXxxmUr1A8Wg4i8o
rLoWh2C3hvhxr5KcqhMLVMrRJ4eCX97irL/qFh6fdxkvQoAaj4yz
iTv17KsyYu8D8t7hg+q7fXahjr50GaWQawT7OkbDN3/u6JIflQxb
qXN8zzsQniv7tGGv9Czx/tz64gXIqcTCagoaqWxpcO/dKBzL4oTI
uu+QBYaaBX2DeBgyDoJmKQzIMyEVE5Wz8HXMO7W29tnnD8TiiS5A
HbIGPi1kJn3zZzdWLh2CoIKGZHRUlXJPzs29XVoy40SuC6p0lgyo
+PS4e/aM8835GHALDWvY2LVybAxcVs881XtAUEyjC8SEGPx7bfu2
4/mgzfwiEgSz4dcJixRxjq5YVtEM1r6oHiDGuP9RwHS1TOaP/tCj
/d+VL1STn8NNZQAAAABJRU5ErkJggg==
"""
file_image = tkinter.PhotoImage(data=file_img)
dir_image = tkinter.PhotoImage(data=dir_img)

# adds a parent item to the tree
# and returns the item's iid value (generated automatically)
parent_iid = treeview.insert(
    parent="", index="0", text="Documents", open=True, image=dir_image
)

start_path = os.path.expanduser(r"C:\\")
start_dir_entries = os.listdir(start_path)

# inserting items to the treeview
new_folder(
    parent_path=start_path,
    directory_entries=start_dir_entries,
    parent_iid=parent_iid,
    f_image=file_image,
    d_image=dir_image,
)

app.mainloop()
