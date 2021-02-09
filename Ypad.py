import tkinter as tk       
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk() 
main_application.geometry('1200x800')
main_application.title('Ypad text editor')
main_application.wm_iconbitmap('icon.ico')

######################################## Main Menu ############################################################
main_menu = tk.Menu()

############ file:
# file icons:
new_icon = tk.PhotoImage(file='ICONS/new.png')
open_icon = tk.PhotoImage(file='ICONS/open.png')
save_icon = tk.PhotoImage(file='ICONS/save.png')
save_as_icon = tk.PhotoImage(file='ICONS/save_as.png')
exit_icon = tk.PhotoImage(file='ICONS/exit.png')

file = tk.Menu(main_menu, tearoff=False)


######### edit:
# edit icons:
copy_icon = tk.PhotoImage(file='ICONS/copy.png')
paste_icon = tk.PhotoImage(file='ICONS/paste.png')
cut_icon = tk.PhotoImage(file='ICONS/cut.png')
clear_all_icon = tk.PhotoImage(file='ICONS/clear_all.png')
find_icon = tk.PhotoImage(file='ICONS/find.png')

edit = tk.Menu(main_menu, tearoff=False)


########## view:
# view icons:
status_bar_icon = tk.PhotoImage(file='ICONS/status_bar.png')
tool_bar_icon = tk.PhotoImage(file='ICONS/tool_bar.png')

view = tk.Menu(main_menu, tearoff=False)


######## color_theme:
# color_theme icon:
light_default_icon = tk.PhotoImage(file='ICONS/light_default.png')
light_plus_icon = tk.PhotoImage(file='ICONS/light_plus.png')
dark_icon = tk.PhotoImage(file='ICONS/dark.png')
red_icon = tk.PhotoImage(file='ICONS/red.png')
monokai_icon = tk.PhotoImage(file='ICONS/monokai.png')
night_blue_icon = tk.PhotoImage(file='ICONS/night_blue.png')

color_theme= tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus': ('#474747','#e0e0e0'),
    'Dark': ('#c4c4c4','#2d2d2d'),
    'Red': ('#2d2d2d','#ffe8e8'),
    'Monokai': ('#d3b774','#474747'),
    'Night Blue': ('#ededed','#6b9dc2')
}

##cascade:
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

# ------------------------&&&&&&&&&&& End Main Menu &&&&&&&&&&&&&&&&&&-----------------------------------------



######################################## Tool Bar ############################################################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)


## font box:
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0, padx=5)

## size box:
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['value'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1, padx=5)

## bold button:
bold_icon = tk.PhotoImage(file='ICONS/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

## italic button:
italic_icon = tk.PhotoImage(file='ICONS/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

## underline button:
underline_icon = tk.PhotoImage(file='ICONS/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

## font color button:
font_color_icon = tk.PhotoImage(file='ICONS/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

## align left button:
align_left_icon = tk.PhotoImage(file='ICONS/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

## align center button:
align_center_icon = tk.PhotoImage(file='ICONS/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

## align right button:
align_right_icon = tk.PhotoImage(file='ICONS/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)


# ------------------------&&&&&&&&&&& End Tool Bar &&&&&&&&&&&&&&&&&&-----------------------------------------


######################################## Text Editor ############################################################

text_editor = tk.Text(main_application)
text_editor.configure(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()       # setting the focus of cursor at the beginning
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)  # here seting scroll bar at right side
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.configure(command=text_editor.yview)
text_editor.configure(yscrollcommand=scroll_bar.set)


##########font family and font size functionalit:
current_font_family = 'Arial'
current_font_size = 12

# def change_font(main_application):  it doesent matter what you pass in the function
def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

# def change_fontsize(main_application):
def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)     # here we bind the functionality of the font and the size
font_size.bind("<<ComboboxSelected>>", change_fontsize)

########### buttons functionalit:

## bold button functionalit:
# ==========================

# print(tk.font.Font(font=text_editor['font']).actual())   #: {'family': 'Courier New', 'size': 10, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
# the above function gives us dictionary in the we get info about our font like default values as shown above

# default values from dictionary
# here we have to change the 'weight' default_value from 'normal' to 'bold' as shown bellow 
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

## italic button functionalit:
# ==========================

# default values from dictionary
# here we have to change the 'slant' default_value from 'roman' to 'italic' as shown bellow 

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

italic_btn.configure(command=change_italic)

## underline button functionalit:
# ===============================

# default values from dictionary
# here we have to change the 'underline' default_value from '0' to 'underline' as shown bellow 

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)


## font color button functionalit:
# ===============================
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    # print(color_var)   # ---->((255.99609375, 128.5, 64.25), '#ff8040')  ==> here we get the selected color tuple and inside that tuple one more tuple that inside tuple gives us(red,green,blue) values, and 
    # and after that we have the # value of color , we need that # value at index no.1 because it's easy to use
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)


########align functionalit:
# ==========================

# 1] align left button functionalit:
# ==================================
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)


# 2] align center button functionalit:
# ==================================
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)


# 3] align right button functionalit:
# ==================================
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)


text_editor.config(font=('Arial',12))   # here we set bydefault values of text ,like fint and size

#--------------------------&&&&&&&&&&& End Text Editor &&&&&&&&&&&&&&&&&&-----------------------------------------


######################################## Status Bar ############################################################

status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        charecters = len(text_editor.get(1.0, 'end-1c'))   # .replace(' ', '') :=>here we add the command like relpace, because of this our text_editor can't count the spaces in status bar
        status_bar.config(text=f'Charecters : {charecters} Worads : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)    # bind text_editor with status bar func


# ------------------------&&&&&&&&&&& End Status Bar &&&&&&&&&&&&&&&&&&-----------------------------------------



######################################## Main Menu Functionality ############################################################

# variable:
url = ''

######################################## file ******************************
#### new file functionality:
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)
## new file command:
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='ctrl+N', command=new_file)


#### open file functionality:
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
## open file command:
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='ctrl+O',  command=open_file)


#### save file functionality:
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return
## save file commands:
file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='ctrl+S',command=save_file)



#### save_as file functionality:
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return
## save_as file command:
file.add_command(label='Save_As', image=save_as_icon, compound=tk.LEFT, accelerator='ctrl+Alt+S',command=save_as)

#### exit file functionality:
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file ?')
            if mbox is True:      # int means 'Yes'
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:           # int means 'Yes'
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
             
## exit file command:
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='ctrl+Q',command=exit_func)


################################ edit *************************************

######## find functionality:
def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame:
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels:
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame,  text='Replace')

    ## entry:
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button:
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    # label grid:
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    # entry grid:
    find_input.grid(row=0 ,column=1, padx=4, pady=4)
    replace_input.grid(row=1 ,column=1, padx=4, pady=4)

    # button grid:
    find_button.grid(row=2 ,column=0 ,padx=8 ,pady=4)
    replace_button.grid(row=2 ,column=1 ,padx=8 ,pady=4)

    find_dialogue.mainloop()




## edit commands:
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='ctrl+Alt+X', command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='ctrl+Q', command=find_func)


############################# view ***************************************
## view check buttons:

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True



view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0,variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False,variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)


########################### color theme ************************************
## color theme:
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count+= 1

# ------------------------&&&&&&&&&&& End Main Menu Functionality &&&&&&&&&&&&&&&&&&-----------------------------------------

main_application.config(menu=main_menu)

###################### bind shortcut keys ############################################################
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)

main_application.mainloop()
