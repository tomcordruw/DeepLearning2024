# Imports
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from keras import layers
import tkinter

# Step 1: Save model in Jupyter-notebook
# e.g. mobilephoneprice.keras
# We'll use the lecture4 / ann_classification_example1.ipynb


# Step 2: Load the model and do some quick testing

# loading the model from file
model = keras.saving.load_model("lecture5/mobilephoneprice.keras")

print("----Welcome to the CyberAI Interface----")

# Test the model with code from ann_classification_example1
# Make a new test prediction

tester_row = {
    'battery_power': 1000, 
    'dual_sim': 0 ,
    'fc': 4, 
    'int_memory': 4, 
    'n_cores': 1, 
    'pc': 4,
    'px_height': 900,
    'px_width': 1200, 
    'ram': 1024, 
    'sc_h': 7, 
    'sc_w': 4, 
    'talk_time': 12
}

# convert to pandas-format
tester_row = pd.DataFrame([tester_row])
result = model.predict(tester_row)[0]
result_index = np.argmax(result)

categories = ['1: Cheap', '2: Avg-', '3: Avg+', '4: Expensive']

# print the actual name with this index
result_text = categories[result_index]

# print the result
print(f"Predicted price range: {result_text}")

# Step 3: Create an application interface with tkinter
# - Make buttons, textboxes, etc.
# - Make buttons function when clicked
# - Connect textboxes to the Keras model

# Using this example as a template:
# https://www.geeksforgeeks.org/how-to-set-text-of-tkinter-text-widget-with-a-button/

window = tkinter.Tk()
window.title("CyberAI")
window.geometry("400x900")
window.option_add("*font", "lucida 10 bold")

# Make a text label for the first entry
label1 = tkinter.Label(window, text="Battery power (mAh): ")
label1.pack(pady=10)

# Creating the first Entry for the first label
entry_battery = tkinter.Entry(window, text="Set")
entry_battery.pack()


label2 = tkinter.Label(window, text="Dual SIM (0/1): ")
label2.pack(pady=10)
entry_dualsim = tkinter.Entry(window)
entry_dualsim.pack()


label3 = tkinter.Label(window, text="Front camera (Mpx): ")
label3.pack(pady=10)
entry_frontcamera = tkinter.Entry(window)
entry_frontcamera.pack()
 
label4 = tkinter.Label(window, text="Internal storage (Gb): ")
label4.pack(pady=10)
entry_intmemory = tkinter.Entry(window)
entry_intmemory.pack()

label5 = tkinter.Label(window, text="Number of cores: ")
label5.pack(pady=10)
entry_numcores = tkinter.Entry(window)
entry_numcores.pack()

label6 = tkinter.Label(window, text="Main camera (Mpx): ")
label6.pack(pady=10)
entry_primarycam = tkinter.Entry(window)
entry_primarycam.pack()

label7 = tkinter.Label(window, text="Screen pixel height: ")
label7.pack(pady=10)
entry_pixelh = tkinter.Entry(window)
entry_pixelh.pack()

label8 = tkinter.Label(window, text="Screen pixel width: ")
label8.pack(pady=10)
entry_pixelw = tkinter.Entry(window)
entry_pixelw.pack()

label9 = tkinter.Label(window, text="RAM (MB): ")
label9.pack(pady=10)
entry_ram = tkinter.Entry(window)
entry_ram.pack()

label10 = tkinter.Label(window, text="Screen height (cm): ")
label10.pack(pady=10)
entry_screenh = tkinter.Entry(window)
entry_screenh.pack()

label11 = tkinter.Label(window, text="Screen width (cm): ")
label11.pack(pady=10)
entry_screenw = tkinter.Entry(window)
entry_screenw.pack()

label12 = tkinter.Label(window, text="Talk time (hours): ")
label12.pack(pady=10)
entry_talktime = tkinter.Entry(window)
entry_talktime.pack()
 
entry_list = [entry_battery, entry_dualsim, entry_frontcamera, entry_intmemory, entry_numcores, entry_primarycam, entry_pixelh, entry_pixelw,
              entry_ram, entry_screenh, entry_screenw, entry_talktime]

default_row = [1500, 0, 4, 4, 1, 4, 900, 1200, 1024, 7, 4, 12]


for i, element in enumerate(entry_list):
    element.insert(0, default_row[i])


# Creating the function to set the text 
# with the help of button
def set_text_by_button():
    tester_row = {
    'battery_power': int(entry_battery.get()), 
    'dual_sim': int(entry_dualsim.get()),
    'fc': int(entry_frontcamera.get()), 
    'int_memory': int(entry_intmemory.get()), 
    'n_cores': int(entry_numcores.get()), 
    'pc': int(entry_primarycam.get()),
    'px_height': int(entry_pixelh.get()),
    'px_width': int(entry_pixelw.get()), 
    'ram': int(entry_ram.get()), 
    'sc_h': int(entry_screenh.get()), 
    'sc_w': int(entry_screenw.get()), 
    'talk_time': int(entry_talktime.get())
    }
    
    # convert to pandas-format
    tester_row = pd.DataFrame([tester_row])
    result = model.predict(tester_row)[0]
    result_index = np.argmax(result)

    categories = ['1: Cheap', '2: Avg-', '3: Avg+', '4: Expensive']

    # print the actual name with this index
    result_text = categories[result_index]
    result_string.set(f"Predicted price range: {result_text}")
 
# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Set", 
                    command=set_text_by_button)

set_up_button.pack(pady=10)

# The result text will be changed by pressing the button
result_string = tkinter.StringVar()
result_string.set("Waiting for user input...")

label_result = tkinter.Label(window, textvariable=result_string, fg="red")
label_result.pack(pady=10)
 
window.mainloop()
